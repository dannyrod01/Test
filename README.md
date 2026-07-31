# Test

Editing test reame.md on 2025-10-31

## Whisper Transcription

This repo includes a minimal setup for transcribing audio using OpenAI's
[Whisper](https://github.com/openai/whisper) model.

### Install

Whisper also requires [ffmpeg](https://ffmpeg.org/) to be installed on your system
(e.g. `apt install ffmpeg`, `brew install ffmpeg`, or `choco install ffmpeg`).

```bash
pip install -r requirements.txt
```

### Usage

```bash
python transcribe.py path/to/audio.mp3
```

Optionally choose a model size (`tiny`, `base`, `small`, `medium`, `large`):

```bash
python transcribe.py path/to/audio.mp3 --model small
```

