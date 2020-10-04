from telegram.ext import CommandHandler

def start_command_handler(update, context):
    print("/start command handler runs...")
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def register_commands(dispatcher):
    print("Registering commands")
    dispatcher.add_handler(CommandHandler('start', start_command_handler))
