import os
import random
from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip, concatenate_videoclips, vfx
from gtts import gTTS
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# Only here: bot token
BOT_TOKEN = os.getenv("BOT_TOKEN")  # set in Cloud Run environment
PORT = int(os.getenv("PORT", "8080"))

VIDEO_TYPE, VIDEO_QUALITY, VIDEO_DURATION = range(3)

quality_map = {
    "144p": (256, 144),
    "240p": (426, 240),
    "360p": (640, 360),
    "480p": (854, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "1440p": (2560, 1440),
    "2160p": (3840, 2160)
}

user_data_store = {}
character_voice_map = {}  # voice effect per character

# --- all bot functions remain same as previous final version ---
# start, receive_text, receive_file, video_type, video_quality, video_duration
# generate_and_send, create_video_from_text, main()

# Full code is same as previous bot.py, only BOT_TOKEN comes from environment

# At the end, main() runs the webhook on PORT
