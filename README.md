# Voice-Enabled Knowledge Assistant

A Python command-line assistant that accepts typed or spoken questions, retrieves context from Wikipedia, generates a concise response with TinyLlama, and can read the response aloud.

## What it does

- Accepts a question through the terminal or microphone.
- Cleans common phrases from a query to identify the topic.
- Retrieves a short Wikipedia summary to provide context.
- Uses the `TinyLlama/TinyLlama-1.1B-Chat-v1.0` text-generation model through Hugging Face Transformers.
- Prints the generated response and can speak it using text-to-speech.
- Handles common speech-recognition failures, such as unclear speech or unavailable recognition service.

## How it works

```text
Text or microphone input
        ↓
Query cleanup / topic extraction
        ↓
Wikipedia context retrieval
        ↓
Prompt construction
        ↓
TinyLlama text generation
        ↓
Terminal output + optional spoken output
```

## Technology

- Python
- Hugging Face Transformers and TinyLlama 1.1B
- PyTorch
- SpeechRecognition (voice input)
- pyttsx3 (text-to-speech)
- Wikipedia retrieval

## Requirements

- Python installed
- Internet access for Wikipedia retrieval and model download/use
- A working microphone for voice input
- Audio support compatible with `SpeechRecognition` and its microphone dependency
- Enough memory for the model. CPU execution may be slower than GPU execution.

## Setup and run

1. Clone this repository and open its directory.
2. Create and activate a virtual environment.
3. Install the Python packages imported by the application. If a `requirements.txt` is added to this repository, use it with `python -m pip install -r requirements.txt`.
4. Run the application entry point from the repository root:

   ```bash
   python -m app.main
   ```

   If the project is not configured as a Python package in your checkout, run the entry point using the path supported by its import structure (for example, `python app/main.py`).

The first run may need to download TinyLlama model files. Microphone support can require additional OS-specific audio packages.

## Hardware behaviour

The application checks whether CUDA is available and selects CPU or GPU execution accordingly. CPU inference can take longer, especially on machines with limited memory.

## Limitations

- The Wikipedia summary is used as context; the assistant's output is not guaranteed to be complete or correct.
- Voice recognition uses an online recognition service in the configured implementation, so it may require internet access.
- This is a command-line application, not a web application.
- It is intended as a learning project, not a production conversational assistant.

## Suggested next improvements

- Add a `requirements.txt` with tested dependency versions.
- Improve handling for ambiguous or missing Wikipedia topics.
- Add automated tests for topic extraction and response formatting.
- Allow users to choose typed input or voice input more explicitly.
