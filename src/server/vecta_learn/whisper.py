# src/server/vecta_learn/transcribe.py

from transformers.pipelines.pt_utils import KeyDataset
from transformers import pipeline
from datasets import Dataset
from rich import print
from tqdm import tqdm
import pandas as pd
import ffmpeg
import torch

from datetime import datetime, timedelta
from typing import List, Optional, Tuple
from pathlib import Path

from ..schema.whisper import TimeStamp
from .. import settings


_SAMPLING_RATE = 16000

_DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
_TORCH_DTYPE = torch.float16 if torch.cuda.is_available() else torch.float32


def _str_to_path(path: str) -> Path:
    """Convert a string to a Path object."""

    if isinstance(path, str):
        return Path(path).resolve()
    return path.resolve()


def _is_video(file: Path | str) -> bool:
    """Check if the file is a video file."""

    file = _str_to_path(file)
    return file.suffix == ".mp4"


def _seconds_to_datetime(seconds: float) -> datetime:
    """Convert seconds to a datetime object."""

    # Round off the milliseconds before converting to datetime
    seconds = round(seconds)
    return (timedelta(seconds=seconds)).__str__()


def _to_timestamp(timestamp: Tuple[float, float]) -> TimeStamp:
    """Convert a tuple of seconds to a TimeStamp object."""

    return TimeStamp(
        start=_seconds_to_datetime(timestamp[0]), end=_seconds_to_datetime(timestamp[1])
    )


def video_to_wav(
    input_file: Path | str, output_file: Optional[Path | str] = None
) -> Path:
    """Convert a mp4 video file to a 16khz wav audio file.

    Args:
        input_file (Path): Path to the input file.
        output_file (Path): Path to the output file.

    Returns:
        Path: Path to the output file.
    """

    input_file = _str_to_path(input_file)

    if output_file is None:
        output_file = input_file.with_suffix(".wav").resolve()
    output_file = _str_to_path(output_file)

    assert input_file.suffix == ".mp4", "Input file must be a MP4 file"
    assert output_file.suffix == ".wav", "Output file must be a WAV file"

    try:
        _ = (
            ffmpeg.input(input_file)
            .output(
                f"{output_file}",
                format="wav",
                acodec="pcm_s16le",
                ac=1,
                ar=_SAMPLING_RATE,
            )
            .run(cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True)
        )
        return output_file
    except ffmpeg.Error as e:
        raise RuntimeError(
            f"Failed to convert video to audio: {e.stderr.decode('utf-8')}"
        ) from e


def transcribe(input_files: List[Path | str], show_progress: bool = True) -> None:
    """Transcribe audio data from a WAV file.

    Args:
        input_files (List[Path]): List of paths to the input files.

    Returns:
        None

    Raises:
        AssertionError: If the input file is not a WAV file.
        FileNotFoundError: If the input file does not exist.
    """

    if not isinstance(input_files, list):
        print("[bold yellow]Warning: [/bold yellow]input_files is not a list.")
        input_files = [input_files]

    # Validate and convert input files
    files = []
    for file in input_files:
        file = _str_to_path(file)

        if not file.exists():
            raise FileNotFoundError(f"Input file not found: {file}")

        if _is_video(file):
            file = video_to_wav(file)

        files.append(str(file))

    # Prepare dataset
    dataset = KeyDataset(
        Dataset.from_pandas(pd.DataFrame(files, columns=["path"])), "path"
    )

    # Prepare model
    _whisper = pipeline(
        task="automatic-speech-recognition",
        model=f"{settings.MODEL_PATH}/{settings.WHISPER_MODEL}",
        torch_dtype=_TORCH_DTYPE,
        device=_DEVICE,
    )
    _whisper.model = _whisper.model.to_bettertransformer()

    # Transcribe audio
    iter = _whisper(dataset, chunk_length_s=30, batch_size=36, return_timestamps=True)
    if show_progress:
        iter = tqdm(iter, total=len(dataset))

    results = []
    for out in iter:
        df = pd.DataFrame(out["chunks"])
        df["timestamp"] = df["timestamp"].apply(lambda x: _to_timestamp(x))

        # TODO: merge chunks to ~1 minute intervals
        print(out["text"])

        results.append(df)
        torch.cuda.empty_cache()

    torch.cuda.empty_cache()

    return results


def main(input_files: List[str]):
    """Main function to serve as the entrypoint for a Python Fire CLI.

    Args:
        input_files (List[str]): List of paths to the input files.
    """
    transcribe(input_files, show_progress=False)
    print("Done")


if __name__ == "__main__":
    import fire

    fire.Fire(main)
