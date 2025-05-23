# 🎥 Video Transcript Summarizer

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Deepgram](https://img.shields.io/badge/API-Deepgram-purple.svg)](https://deepgram.com)
[![TogetherAI](https://img.shields.io/badge/API-TogetherAI-orange.svg)](https://together.ai)
[![Maintained](https://img.shields.io/badge/status-maintained-brightgreen.svg)]()

A powerful tool that:
- 🧠 Transcribes `.mp3` audio files using **Deepgram**
- ✨ Summarizes the transcript using **TogetherAI (LLaMA 3.1)**
- 📤 Saves everything neatly into an `exports.csv` file

---

## 📁 Project Structure

```

video-link-summarizer/
├── audiototext.py               # Transcribes .mp3 to plain text
├── summarizer.py                # AI summarization using TogetherAI
├── write\_exports\_csv.py         # (Legacy) Summarizes .vtt subtitle files
├── write\_exports\_from\_audio.py  # ✅ Processes audio files and exports summaries
├── vtt\_cleaner.py               # Optional cleaner for .vtt format
├── exports.csv                  # ✅ Final CSV output
├── requirements.txt             # Dependency list

````

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/video-link-summarizer.git
cd video-link-summarizer
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API keys

#### 🔑 Deepgram

```bash
export DEEPGRAM_API_KEY=your_key_here
```

#### 🔑 TogetherAI

Make sure you're authenticated via environment or `together` config.

---

## 🚀 Usage

### ▶️ Option A: Process `.mp3` Audio Files (Recommended)

```bash
python write_exports_from_audio.py path/to/mp3_directory/
```

✅ Transcribes + summarizes → Adds results to `exports.csv`

---

### 📝 Option B: Process `.vtt` Subtitle Files (Legacy)

```bash
python write_exports_csv.py path/to/vtt_directory/
```

🔁 Cleans subtitle → summarizes → Adds results to `exports.csv`

---

## 📄 Output Format

The exported CSV will contain:

| File Name     | Heading            | Content                                           |
| ------------- | ------------------ | ------------------------------------------------- |
| `demo.mp3`    | "Tool Walkthrough" | "The tool allows users to view, filter..."        |
| `example.vtt` | "Lease Insights"   | "This video explores how document abstraction..." |

---

## 🔧 Requirements

* Python 3.9+
* [Deepgram SDK](https://github.com/deepgram/deepgram-python-sdk)
* [TogetherAI SDK](https://github.com/togethercomputer/together-python)

---

## 🧠 Potential Extensions

* [ ] Auto-convert `.mp4` → `.mp3` using `ffmpeg`
* [ ] Upload results to Notion, Sheets, or a frontend viewer
* [ ] Build a minimal drag-n-drop UI for non-devs

---

## 🙌 Credits

* 🎙️ [Deepgram](https://deepgram.com) — Fast and accurate transcription
* 🧠 [TogetherAI](https://together.ai) — State-of-the-art summarization via LLaMA 3.1

---

## 📜 License

MIT License — free to use and adapt with attribution

---

> Give it a ⭐ if this helped you summarize your content better!
