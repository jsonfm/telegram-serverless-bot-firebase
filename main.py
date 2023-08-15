from firebase_functions import https_fn
import telebot

# config
from app.config import config

# repositories
from app.repositories.firebase.config import app  # initializes firebase app
from app.repositories.telegram.config import bot

# utils
from app.utils import get_daily_horoscope


def fetch_horoscope(message, sign):
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\n*Sign:* {sign}\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, "Here's your horoscope!")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")


def day_handler(message):
    sign = message.text
    text = "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, fetch_horoscope, sign.capitalize())


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    text = """Hello, I'm PyroBot, I can say what is your horoscope. Please use `/horoscope` command."""
    bot.reply_to(message, text, parse_mode="Markdown")


@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text = "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)


@https_fn.on_request()
def webhook(request: https_fn.Request):
    if request.json:
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
    return https_fn.Response("", status=200)


WEBHOOK_URL = config.get("WEBHOOK_URL")
bot.set_webhook(
    url=WEBHOOK_URL,
)
