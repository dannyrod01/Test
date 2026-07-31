#!/usr/bin/env python3
"""Transcribe an audio file to text using OpenAI's Whisper model."""

import argparse
import sys

import whisper


def transcribe(audio_path: str, model_name: str = "base") -> str:
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result["text"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio_path", help="Path to the audio file to transcribe")
    parser.add_argument(
        "--model",
        default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model size to use (default: base)",
    )
    args = parser.parse_args()

    text = transcribe(args.audio_path, args.model)
    print(text)


if __name__ == "__main__":
    sys.exit(main())
