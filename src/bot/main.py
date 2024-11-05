from telegram.ext import ApplicationBuilder, Application

from src.settings import bot_settings
from src.bot.handlers import load_handlers


def pre_configure_bot(app: Application):
    pass


def post_configure_bot(app: Application):
    load_handlers(app)


def init_bot() -> Application:
    return ApplicationBuilder().token(bot_settings.token).build()


def start_bot():
    app = init_bot()
    post_configure_bot(app)
    app.run_polling()
