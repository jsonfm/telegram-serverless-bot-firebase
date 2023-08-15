import logging
import telebot
from app.config import config
telebot.logger.setLevel(logging.DEBUG)

TELEGRAM_API_KEY = config.get("TELEGRAM_API_KEY", "")
bot = telebot.TeleBot(TELEGRAM_API_KEY, threaded=False)
