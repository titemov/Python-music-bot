# About
Multiserver python-based discord bot for YouTube videos. This bot have dynamic music queue and support playlists up to 250 tracks. Everything that yt-dlp can process this bot can too, but it is recommended to use YouTube videos ONLY.

__STILL WIP__
## Requirements
- [ffmpeg](https://www.ffmpeg.org/) binary to be in the same folder.
- `pip install -r requirements.txt`
- All Privileged Gateway Intents must be turned __ON__

## Commands
- **`-ping`** – current bot ping
- **`-hello`** – test command
- **`-play [link or title]`** – play single track
- **`-search [title]`** – precise search by name
- **`-loop`** – loop current track
- **`-unloop`** – unloop current track
- **`-np`** – show current playing track
- **`-pause`** – pause current track
- **`-resume`** – resume current paused track
- **`-skip`** – skip current track
- **`-queue`** – show tracks queue
- **`-clear`** – clear queue
  - _If bot exits the voice channel correctly, the queue is cleared automatically_
- **`-jump [№ in queue]`** – play track by its № in queue
- **`-leave`** – kick bot out of current voice channel (unprotected)
  - _If bot exits the voice channel correctly, the queue is cleared automatically_
