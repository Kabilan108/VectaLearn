# src/rag/llm.py

from langsmith.run_helpers import traceable
from llama_index.llms import OpenAI
from llama_index.llms.base import (
    ChatMessage,
    ChatResponse,
    CompletionResponse,
    ChatResponseGen,
    CompletionResponseGen,
)

from typing import List, Optional, Tuple, Union, Sequence, Any
from datetime import datetime


class SmithOpenAI(OpenAI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @traceable(run_type="chain", name="chat")
    def chat(self, messages: Sequence[ChatMessage], **kwargs: Any) -> ChatResponse:
        return super().chat(messages, **kwargs)

    @traceable(run_type="chain", name="stream_chat")
    def stream_chat(self, messages: Sequence[ChatMessage], **kwargs) -> ChatResponseGen:
        return super().stream_chat(messages, **kwargs)

    @traceable(run_type="chain", name="complete")
    def complete(self, prompt: str, **kwargs) -> CompletionResponse:
        return super().complete(prompt, **kwargs)

    @traceable(run_type="chain", name="stream_complete")
    def stream_complete(self, prompt: str, **kwargs: Any) -> CompletionResponseGen:
        return super().stream_complete(prompt, **kwargs)

    @traceable(run_type="chain", name="achat")
    async def achat(self, messages: Sequence[ChatMessage], **kwargs) -> ChatResponse:
        return await super().achat(messages, **kwargs)

    @traceable(run_type="chain", name="astream_chat")
    async def astream_chat(
        self, messages: Sequence[ChatMessage], **kwargs
    ) -> ChatResponseGen:
        return await super().astream_chat(messages, **kwargs)

    @traceable(run_type="chain", name="acomplete")
    async def acomplete(self, prompt: str, **kwargs) -> CompletionResponse:
        return await super().acomplete(prompt, **kwargs)

    @traceable(run_type="chain", name="astream_complete")
    async def astream_complete(self, prompt: str, **kwargs) -> CompletionResponseGen:
        return await super().astream_complete(prompt, **kwargs)
