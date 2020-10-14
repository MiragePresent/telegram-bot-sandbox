from telegram.ext import CommandHandler

def start_command_handler(update, context):
    print("/start command handler runs...")
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def help_command_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я не буду з тобою говорити")

def register_commands(dispatcher):
    print("Registering commands")
    dispatcher.add_handler(CommandHandler('start', start_command_handler))
    dispatcher.add_handler(CommandHandler('help', help_command_handler))

    # Lambda functions test
    # More about lambda functions
    dispatcher.add_handler(CommandHandler(
        'test',
        lambda update, context: \
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="hello from lambda"
            )
    ))
