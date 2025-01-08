import yt_logger
BOT_TOKEN = 'YOUR TOKEN'
FFMPEG_PATH = "ffmpeg.exe"

YDL_OPTIONS = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': 'mp3',
    'simulate': True,
    'preferredquality': 0,
    'preferredcodec': 'mp3',
    'key': 'FFmpegExtractAudio',
    'quiet': True,
    'logger': yt_logger.MyLogger(),
    'player_client': 'web',
    'source_address': '0.0.0.0',
    'force-ipv4': True,
    'cachedir': False
}

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5' , 
    'options': '-vn'
}