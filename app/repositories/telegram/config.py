import telebot
from app.config import config


TELEGRAM_API_KEY = config.get("TELEGRAM_API_KEY", "")
bot = telebot.TeleBot(TELEGRAM_API_KEY)