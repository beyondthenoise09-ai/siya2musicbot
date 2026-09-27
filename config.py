# Authored By Saya Musics © 2025
import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()


def _required(name: str) -> str:
    value = getenv(name)
    if not value:
        raise SystemExit(f"[ERROR] - Missing required environment variable: {name}")
    return value


def _required_int(name: str) -> int:
    value = _required(name)
    try:
        return int(value)
    except ValueError as exc:
        raise SystemExit(f"[ERROR] - {name} must be a valid integer.") from exc


# ── Core bot config ────────────────────────────────────────────────────────────
API_ID = _required_int("API_ID")
API_HASH = _required("API_HASH")
BOT_TOKEN = _required("BOT_TOKEN")

OWNER_ID = _required_int("OWNER_ID")
OWNER_USERNAME = getenv("OWNER_USERNAME", "kidzmc")
BOT_USERNAME = getenv("BOT_USERNAME", "SexySayaBot")
BOT_NAME = getenv("BOT_NAME", "Saya Music")
ASSUSERNAME = getenv("ASSUSERNAME", "musicxsaya")

# ── Database & logging ─────────────────────────────────────────────────────────
MONGO_DB_URI = _required("MONGO_DB_URI")
LOGGER_ID = _required_int("LOGGER_ID")

# ── Limits (durations in min/sec; sizes in bytes) ──────────────────────────────
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "1200"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1800"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "157286400"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1288490189"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "30"))

# ── External APIs ──────────────────────────────────────────────────────────────
COOKIE_URL = getenv("COOKIE_URL", "https://pastebin.com/YfK14h8y")  # paste link (raw URL is auto-resolved)
API_URL = getenv("API_URL", "https://pvtz.nexgenbots.xyz")
VIDEO_API_URL = getenv("VIDEO_API_URL", "https://api.video.nexgenbots.xyz")
API_KEY = getenv("API_KEY", "")
DEEP_API = getenv("DEEP_API", "")

# ── Git / updates ──────────────────────────────────────────────────────────────
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/shnwazdeveloper/saya-music")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN")  # needed if repo is private

# ── Support links ──────────────────────────────────────────────────────────────
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://github.com/shnwazdeveloper/saya-music")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://github.com/shnwazdeveloper/saya-music/issues")

# ── Assistant auto-leave ───────────────────────────────────────────────────────
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3600"))

# ── Debug ──────────────────────────────────────────────────────────────────────
DEBUG_IGNORE_LOG = True

# ── Spotify (optional) ─────────────────────────────────────────────────────────
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")

# ── Session strings (optional) ─────────────────────────────────────────────────
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ── Media assets ───────────────────────────────────────────────────────────────
START_VIDS = [
    "https://litter.catbox.moe/ge4ds72i538f45q2.mp4",
]
STICKERS = [
    "CAACAgUAAxkBAAEDt9Np-fu9lBKL7octL4Pd5XkcyCj-qQACzhsAAuwSIFQNutRA9ZkJSjsE",
    "CAACAgUAAxkBAAEDt9dp-fv1sv9-j3okIltpNFS9tzZgRAACJhcAAtU0IFSHj_3D1IPNozsE",
]
HELP_IMG_URL = "https://litter.catbox.moe/ejtf4k5gi1nav49v.jpg"
PING_VID_URL = "https://litter.catbox.moe/ge4ds72i538f45q2.mp4"
PLAYLIST_IMG_URL = "https://litter.catbox.moe/ejtf4k5gi1nav49v.jpg"
STATS_VID_URL = "https://litter.catbox.moe/ge4ds72i538f45q2.mp4"
TELEGRAM_AUDIO_URL = "https://litter.catbox.moe/ejtf4k5gi1nav49v.jpg"
TELEGRAM_VIDEO_URL = "https://litter.catbox.moe/ejtf4k5gi1nav49v.jpg"
STREAM_IMG_URL = "https://litter.catbox.moe/ejtf4k5gi1nav49v.jpg"
SOUNCLOUD_IMG_URL = "https://litter.catbox.moe/ejtf4k5gi1nav49v.jpg"
YOUTUBE_IMG_URL = "https://litter.catbox.moe/ejtf4k5gi1nav49v.jpg"
SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ── Helpers ────────────────────────────────────────────────────────────────────
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))


DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ───── Bot Introduction Messages ───── #
AYU = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

AYUV = [
    """
‹ 𝐖 𝐀 𝐈 𝐅 𝐔 ✗ 𝐒 𝐋 𝐀 𝐘 𝐄 𝐑 ›
━━━━━━━━━━━━━━━━━━━━━
↬ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆, {0} 🍷
I am {1}.

🎧 𝗘𝘅𝗽𝗲𝗿𝗶𝗲𝗻𝗰𝗲 𝗟𝗮𝗴-𝗙𝗿𝗲𝗲 𝗠𝘂𝘀𝗶𝗰 𝗦𝘁𝗿𝗲𝗮𝗺𝗶𝗻𝗴.
I am a high-performance bot designed to play High-Fidelity Audio in your Telegram Voice Chats.

┌ ⚙️ 𝗦𝘆𝘀𝘁𝗲𝗺 𝗦𝗽𝗲𝗰𝘀:
├ ‣ 𝗨𝗽𝘁𝗶𝗺𝗲: {2}
├ ‣ 𝗦𝘁𝗼𝗿𝗮𝗴𝗲: {3}
├ ‣ 𝗖𝗣𝗨 𝗟𝗼𝗮𝗱: {4}
└ ‣ 𝗥𝗔𝗠 𝗨𝘀𝗮𝗴𝗲: {5}

📊 𝗡𝗲𝘁𝘄𝗼𝗿𝗸:
‣ 𝗨𝘀𝗲𝗿𝘀: {6} | 𝗖𝗵𝗮𝘁𝘀: {7}

✨ 𝘑𝘶𝘴𝘵 𝘢𝘥𝘥 𝘮𝘦 𝘵𝘰 𝘺𝘰𝘶𝘳 𝘨𝘳𝘰𝘶𝘱 𝘢𝘯𝘥 𝘭𝘦𝘵 𝘵𝘩𝘦 𝘣𝘦𝘢𝘵𝘴 𝘵𝘢𝘬𝘦 𝘰𝘷𝘦𝘳.

🛠 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 & 𝗠𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝗲𝗱 𝗕𝘆:
└ 『 D E V E L O P E R 乂 C H A N D A N 』
"""
]

# ── Runtime structures ─────────────────────────────────────────────────────────
BANNED_USERS = filters.user()
adminlist, lyrical, autoclean, confirmer = {}, {}, [], {}

# ── Minimal validation ─────────────────────────────────────────────────────────
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")
