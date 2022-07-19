from aiogram import Bot, Dispatcher, types
from app_config import TelegramDeliveriesBotConfig as TGConf
from aiogram.utils import executor
from apps.deliveries.models import Delivery
import asyncio


app = None
bot = Bot(token=TGConf.BOT_TOKEN)
disp = Dispatcher(bot, loop=asyncio.get_event_loop())

overdue_limit = 10


@disp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await msg.answer(f"Привет, {msg.from_user.first_name}!")


def overdue_list(overdue: Delivery):
    s = ""

    for id, delivery in enumerate(overdue):
       s += f"{id+1}) {delivery.number}, term: {delivery.term};\n"

    return s


@disp.message_handler(commands=['overdue'])
async def send_overdue(msg: types.Message):
    with app.app_context():
        overdue = Delivery.get_overdue()
    await msg.answer(f"""The number of overdue deliveries: {len(overdue)}.\n
                    There are {overdue_limit} overdue deliveries:\n""")

    for id, over in enumerate(overdue[:overdue_limit]):
        await msg.answer(f"{id+1}.) {over.term}, {over.number};")


def run_bot(flask_app):
    global app
    app = flask_app
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    executor.start_polling(disp)
