<div align="center">

  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;size=30&amp;duration=2800&amp;pause=900&amp;color=FFB86B&amp;center=true&amp;vCenter=true&amp;width=980&amp;lines=Voice-Enabled+Knowledge+Assistant%3BPython+%7C+TinyLlama+%7C+Hugging+Face%3BSpeech+Recognition+%2B+Text-to-Speech" alt="Animated title: Voice-Enabled Knowledge Assistant" />

  <p><strong>A Python command-line assistant combining speech input, Wikipedia context, TinyLlama text generation, and spoken output.</strong></p>

  <p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&amp;logoColor=white&amp;style=for-the-badge" alt="Python" />
  <img src="https://img.shields.io/badge/TinyLlama-1.1B-FFB86B?logo=huggingface&amp;logoColor=black&amp;style=for-the-badge" alt="TinyLlama" />
  <img src="https://img.shields.io/badge/Hugging+Face-Transformers-FFD21E?logo=huggingface&amp;logoColor=black&amp;style=for-the-badge" alt="Transformers" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&amp;logoColor=white&amp;style=for-the-badge" alt="PyTorch" />
  <img src="https://img.shields.io/badge/SpeechRecognition-Voice+Input-7B68EE?style=for-the-badge" alt="SpeechRecognition" />
  </p>

  <p>
  <a href="https://github.com/yajneshx94/text-generation-content-tool/stargazers"><img src="https://img.shields.io/github/stars/yajneshx94/text-generation-content-tool?style=for-the-badge&amp;logo=github" alt="GitHub stars" /></a>
  <a href="https://github.com/yajneshx94/text-generation-content-tool/network/members"><img src="https://img.shields.io/github/forks/yajneshx94/text-generation-content-tool?style=for-the-badge&amp;logo=github" alt="GitHub forks" /></a>
  <a href="https://github.com/yajneshx94/text-generation-content-tool/commits/main/"><img src="https://img.shields.io/github/last-commit/yajneshx94/text-generation-content-tool?style=for-the-badge&amp;logo=git" alt="Last commit" /></a>
  </p>

  <a href="https://github.com/yajneshx94/text-generation-content-tool"><strong>View source repository →</strong></a>

</div>

<p align="center"><img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="Decorative rainbow divider" /></p>

---

A Python command-line assistant that accepts typed or spoken questions, retrieves context from Wikipedia, generates a concise response with TinyLlama, and can read the response aloud.

## 🧭 Contents

- [What it does](#what-it-does)
- [How it works](#how-it-works)
- [Technology](#technology)
- [Requirements](#requirements)
- [Setup and run](#setup-and-run)
- [Hardware behaviour](#hardware-behaviour)
- [Limitations](#limitations)
- [Suggested next improvements](#suggested-next-improvements)

<a id="what-it-does"></a>
## What it does
- Accepts a question through the terminal or microphone.
- Cleans common phrases from a query to identify the topic.
- Retrieves a short Wikipedia summary to provide context.
- Uses the `TinyLlama/TinyLlama-1.1B-Chat-v1.0` text-generation model through Hugging Face Transformers.
- Prints the generated response and can speak it using text-to-speech.
- Handles common speech-recognition failures, such as unclear speech or unavailable recognition service.

<a id="how-it-works"></a>
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

<a id="technology"></a>
## Technology
- Python
- Hugging Face Transformers and TinyLlama 1.1B
- PyTorch
- SpeechRecognition (voice input)
- pyttsx3 (text-to-speech)
- Wikipedia retrieval

<a id="requirements"></a>
## Requirements
- Python installed
- Internet access for Wikipedia retrieval and model download/use
- A working microphone for voice input
- Audio support compatible with `SpeechRecognition` and its microphone dependency
- Enough memory for the model. CPU execution may be slower than GPU execution.

<a id="setup-and-run"></a>
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

<a id="hardware-behaviour"></a>
## Hardware behaviour
The application checks whether CUDA is available and selects CPU or GPU execution accordingly. CPU inference can take longer, especially on machines with limited memory.

<a id="limitations"></a>
## Limitations
- The Wikipedia summary is used as context; the assistant's output is not guaranteed to be complete or correct.
- Voice recognition uses an online recognition service in the configured implementation, so it may require internet access.
- This is a command-line application, not a web application.
- It is intended as a learning project, not a production conversational assistant.

<a id="suggested-next-improvements"></a>
## Suggested next improvements
- Add a `requirements.txt` with tested dependency versions.
- Improve handling for ambiguous or missing Wikipedia topics.
- Add automated tests for topic extraction and response formatting.
- Allow users to choose typed input or voice input more explicitly.

---

<div align="center">

  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="Decorative rainbow divider" />

  <p><strong>Thanks for checking out this project!</strong></p>

  <p>
    <img src="https://visitor-badge.laobi.icu/badge?page_id=yajneshx94.text-generation-content-tool&amp;left_color=24292e&amp;right_color=FFB86B&amp;left_text=Repository%20visitors" alt="Repository visitor count" />
  </p>

</div>
