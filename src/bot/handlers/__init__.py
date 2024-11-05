from telegram import BotCommand, BotCommandScopeChat
from telegram.ext import Application, CommandHandler, ContextTypes

from src.bot.handlers.start import start


async def update_commands(context: ContextTypes.DEFAULT_TYPE, chat_id):
    base_commands = [
        BotCommand("start", "Начало работы"),
        BotCommand("help", "Запрос помощи"),
    ]

    commands = list()
    commands.extend(base_commands)

    private_scope = BotCommandScopeChat(chat_id)
    await context.bot.set_my_commands(commands, scope=private_scope)


def load_handlers(app: Application):
    app.add_handler(CommandHandler("start", start))
