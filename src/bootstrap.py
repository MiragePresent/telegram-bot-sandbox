import logging
from telegram.ext import Updater
from config import BOT_TOKEN, LOGS_DIR

# logs format
logging.basicConfig(
    filename=f"{LOGS_DIR}/bot.log",
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

bot = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = bot.dispatcher

dispatcher.add_error_handler(logging)
