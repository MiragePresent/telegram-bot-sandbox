from telegram.ext import MessageHandler, Filters

def echo(update, context):
    print("new message received")
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def register_messages(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
