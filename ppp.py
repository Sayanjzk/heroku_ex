from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
bot=Bot(token='5572335077:AAFcuWYUYXGbrD66s2cgRv9k1GgZ0D945Bo')
dp = Dispatcher(bot)
#                START MENU with knopki

menu=KeyboardButton('Меню')
dost=KeyboardButton('Доставка')
knopki=ReplyKeyboardMarkup(resize_keyboard=True)
knopki.add(menu,dost)
@dp.message_handler(commands=['start'])
async def start(message=types.Message):
	await message.answer("Сәлеметсіз бе! “ZamZam”-ға жазғаныңыз үшін рақмет ❤️\nЗдравствуйте! Спасибо, что обратились в «ZamZam» ❤️\n\nТапсырыс жасау үшін +7 778 200 6065 нөмірге хабараласыңыз 🙌🏻\nЧтобы сделать заказ позвоните по номеру +7 778 200 6065 🙌🏻\n",reply_markup=knopki)
	

@dp.message_handler()
async def prod(message=types.Message):
	chatID=message.from_user.id
	photoID='AgACAgIAAxkBAAMzYzXL6JNGphygRme2xTeHDi08I_MAAiS_MRswf6hJQWeeMVD88qoBAAMCAAN5AAMqBA'
	if message.text=='Меню':
		await bot.send_photo(chat_id=chatID,photo=photoID)
	elif message.text=='Доставка' : 
		await message.answer("Сәлеметсіз бе! Өкінішке орай, қазіргі кезде жеткізу қызметіміз жоқ. 😅\nТапсырысты такси арқылы немесе өзіңіз “ZamZam”-нан алып кетсеңіз болады. 😊\nОл үшін бізге хабарласыңыз: +7 778 200 6065\nТүсінушілігіңізге рақмет! ❤️\n\nЗдравствуйте! К сожалению, в данный момент у нас отсутсвует услуга доставки на дом. 😅\nВы можете забрать свой заказ при помощи такси или из “ZamZam” самовывозом. 😊\nДля этого позвоните нам: +7 778 200 6065\nСпасибо за Ваше понимание! ❤️\n")

executor.start_polling(dp,skip_updates=True)
