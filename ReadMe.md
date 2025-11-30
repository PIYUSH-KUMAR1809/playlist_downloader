# Video Downloader

> [!IMPORTANT]
> **Disclaimer**: This tool is developed for **educational purposes only**. The developer does not condone the use of this tool for downloading copyrighted content without permission. Users are responsible for complying with YouTube's Terms of Service and applicable copyright laws. Please use this tool only for content you own or have permission to download (e.g., your own videos, public domain content, or Creative Commons).

A simple, free tool to download videos without any ads, interruptions, or hindrances.

## 🚀 Features

- **Ad-free Experience**: Download videos directly without navigating through ad-heavy websites.
- **High Quality**: Downloads the best available quality (MP4 video + M4A audio).
- **Playlist Support**: Currently supports downloading entire playlists.

## 🔮 Future Plans

- **Single Video Download**: Option to download individual videos.
- **Web Interface**: A dedicated website for easier access.
- **GUI Application**: A smooth user interface to replace the command line.

## 📋 Requirements

- **Python 3.10** or higher.
- `ffmpeg` (usually installed automatically or available in your system).

## 🛠️ Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

To download a playlist, run the following command in your terminal:

```bash
python download_playlist.py "PLAYLIST_URL"
```

**Note:** Make sure to wrap the URL in quotes to avoid issues with special characters.
