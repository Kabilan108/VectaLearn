# src/server/models/whisper.py

from pydantic import BaseModel, field_validator
import re


class TimeStamp(BaseModel):
    start: str
    end: str

    @field_validator("start", "end")
    def validate_time_format(cls, v):
        if not re.match(r"^(?:[01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", v):
            raise ValueError("Time must be in the H:MM:SS or HH:MM:SS format")
        return v
