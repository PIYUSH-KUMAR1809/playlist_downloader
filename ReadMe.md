# Video Downloader

> [!IMPORTANT]
> **Disclaimer**: This tool is developed for **educational purposes only**. The developer does not condone the use of this tool for downloading copyrighted content without permission. Users are responsible for complying with YouTube's Terms of Service and applicable copyright laws. Please use this tool only for content you own or have permission to download (e.g., your own videos, public domain content, or Creative Commons).

A simple, free tool to download videos without any ads, interruptions, or hindrances.

## 🚀 Features

- **Ad-free Experience**: Download videos directly without navigating through ad-heavy websites.
- **High Quality**: Downloads the best available quality (MP4 video + M4A audio).
- **Playlist & Single Video Support**: Automatically detects and downloads entire playlists or individual videos.

## 🔮 Future Plans

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

To download a video or playlist, simply provide the URL:

```bash
python download_playlist.py "YOUR_URL_HERE"
```

**Note:** Always wrap the URL in quotes (`""`) to ensure special characters like `&` are processed correctly.

### Download Single Video from Playlist
If you have a playlist URL but only want to download the specific video being played, use the `--single-video` flag:

```bash
python download_playlist.py "YOUR_PLAYLIST_URL_HERE" --single-video
```

### Download Audio Only (mp3, m4a, wav)
You can specify the format using the `--format` (or `-f`) flag.
Supported formats: `mp4` (default), `mp3`, `m4a`, `wav`.

Example (Download as MP3):
```bash
python download_playlist.py "YOUR_URL_HERE" --format mp3 --single-video
```

### Options
- `-o`, `--output-dir`: Specify download directory (default: `downloads`)
- `-s`, `--single-video`: Force download as a single video, ignoring playlist context
- `-f`, `--format`: Specify format (mp4, mp3, m4a, wav)
- `-b`, `--browser`: Load cookies from browser (useful for age-gated content)