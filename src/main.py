from bootstrap import bot, dispatcher
from commands import register_commands
from messages import register_messages

register_commands(dispatcher)
register_messages(dispatcher)

bot.start_polling()
