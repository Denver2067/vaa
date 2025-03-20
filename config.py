import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = "23894001"
API_HASH = "16b67a856fa4e07f3f78c43c82b1d1e4"
# ------------------------------------------------------
BOT_TOKEN = "8035210092:AAGoMmHEYHBKAkGF88TStvi4bloKl7PDxn4"
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","Theo_Godness")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","Fidha_X_Music_bot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = "mongodb+srv://cookies2002boy:cookies2002boy@cluster0.bc2ox.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", "-1002011723196"))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 7909700698))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = "sarwin04"
# ----------------------------------------------------------------
HEROKU_API_KEY = "HRKU-852706f4-8cba-4108-912f-e6b0f4a788a8"
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/cookies2002/Sam",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------


# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Fidha_X_Chennal")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Fidha_X_Chennal")
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = "BQC86fAAI_UPWl3aTyFTLvwzGHOIScz09YiikPlTf8FvEbNCFU0SPUdRp7OdC6TZMF_8XwrC9iAvErfb_H9SefA1b4JkiMUEbz8HsRq3lYIcojoNdJW5j-sSXHtYvfSRyh9hTjtT8Bge_M4pW8KKr9KAYbQHorCaGh5T0beyZ-YQarwSKX7ixII2vSKt0o_ikAuxSupmOLN6tDXaO1_2GNMz4KavCfwBs8AOXUnXPXhyi9UnfjyEXpso5mnd7Md4k5_9A5OwDadC5nWJt6jgiT5oNav9UST18BNJkwoCtuuUaYLCU4HiEujdSDo6SV2tDKjzFwskNExN3CwDbyCopf0DqlSbGQAAAAHSHhobAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/rEw.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/r2A.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/rw8.jpg"
STATS_IMG_URL = "https://envs.sh/r2j.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/8e3552aa743ffdb6f18c9.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/8e3552aa743ffdb6f18c9.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
