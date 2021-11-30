import os
import sqlite3 as sql
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '1499712691:AAFRuln329buzav3EoVVomQb493BGWcOU3s'
bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

user_data = {}

class User_Data:
	def __init__(self, font):
		self.font = font
		self.text = ""

@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
	with sql.connect('profilbot.db') as con:
		cur = con.cursor()
		cur.execute('''CREATE TABLE IF NOT EXiSTS users(
                    user_name TEXT,
                    id INTEGER)''')
		con.commit()

		cur.execute("SELECT * FROM users WHERE id = ?", (message.from_user.id,))
		if not cur.fetchall():
			cur.execute("INSERT INTO users (user_name, id)VALUES(?, ?)",
				(message.from_user.first_name, message.from_user.id))
			con.commit()

	await bot.send_message(message.chat.id, """
/add_text - Videoga text yozish
/help - Bot haqida ma'lumot
""")


@dp.message_handler(commands = ['help'])
async def help(message: types.Message):
	await bot.send_message(message.chat.id, """
<i>Assalomu Aleykum!
Bu bot bilan siz profilingiz uchun sifatli va kreativ 
bo'lgan videolarga o'zingizni ismingizni yoki 
o'zingiz xohlagan biror bir textni turli xil 
shriftlarda videoga tushirishingiz mumkin!</i>
""", parse_mode = "html")

@dp.message_handler(commands = ['developer'])
async def developer(message: types.Message):
	await bot.send_message(message.chat.id, """
@murodillakarimov""")



@dp.message_handler(commands = ['add_text'])
async def add_text(message: types.Message):
	markup_inline = types.InlineKeyboardMarkup(row_width = 1)
	item_ok = types.InlineKeyboardButton(text = "☑️", callback_data = "yes")
	item_right = types.InlineKeyboardButton(text = " ➡️", callback_data = "right")

	markup_inline.add(item_ok, item_right)
	await bot.send_message(message.chat.id, "O'zingizga mos videoni tanlang ⬇️")
	await bot.send_video(message.chat.id, "BAACAgIAAxkBAAEJ6fZgoXtmI6r_NXM08-drMmuOrQfVAAOwDgACAp0JSSNyKDVEgxjvHwQ", reply_markup = markup_inline)


@dp.callback_query_handler(lambda call: call.data == True)
async def choose_video(call):
	markup_inline = types.InlineKeyboardMarkup(row_width = 1)
	item_ok = types.InlineKeyboardButton(text = "☑️", callback_data = "yes")
	item_right = types.InlineKeyboardButton(text = " ➡️", callback_data = "right")

	markup_inline.add(item_ok, item_right)

	markup_inline0 = types.InlineKeyboardMarkup(row_width = 3)
	item_left0 = types.InlineKeyboardButton(text = "⬅️", callback_data = "left0")
	item_ok0 = types.InlineKeyboardButton(text = "☑️", callback_data = "yes0")
	item_right0 = types.InlineKeyboardButton(text = " ➡️", callback_data = "right0")

	markup_inline0.add(item_left0, item_ok0, item_right0)

	markup_inline1 = types.InlineKeyboardMarkup(row_width = 3)
	item_left1 = types.InlineKeyboardButton(text = "⬅️", callback_data = "left1")
	item_ok1 = types.InlineKeyboardButton(text = "☑️", callback_data = "yes1")
	item_right1 = types.InlineKeyboardButton(text = " ➡️", callback_data = "right1")

	markup_inline1.add(item_left1, item_ok1, item_right1)

	markup_inline2 = types.InlineKeyboardMarkup(row_width = 3)
	item_left2 = types.InlineKeyboardButton(text = "⬅️", callback_data = "left2")
	item_ok2 = types.InlineKeyboardButton(text = "☑️", callback_data = "yes2")
	item_right2 = types.InlineKeyboardButton(text = " ➡️", callback_data = "right2")

	markup_inline2.add(item_left2, item_ok2, item_right2)

	markup_inline3 = types.InlineKeyboardMarkup(row_width = 3)
	item_left3 = types.InlineKeyboardButton(text = "⬅️", callback_data = "left3")
	item_ok3 = types.InlineKeyboardButton(text = "☑️", callback_data = "yes3")
	item_right3 = types.InlineKeyboardButton(text = " ➡️", callback_data = "right3")

	markup_inline3.add(item_left3, item_ok3, item_right3)

	markup_inline4 = types.InlineKeyboardMarkup(row_width = 3)
	item_left4 = types.InlineKeyboardButton(text = "⬅️", callback_data = "left4")
	item_ok4 = types.InlineKeyboardButton(text = "☑️", callback_data = "yes4")
	item_right4 = types.InlineKeyboardButton(text = " ➡️", callback_data = "right4")

	markup_inline4.add(item_left4, item_ok4, item_right4)

	markup_inline5 = types.InlineKeyboardMarkup(row_width = 3)
	item_left5 = types.InlineKeyboardButton(text = "⬅️", callback_data = "left5")
	item_ok5 = types.InlineKeyboardButton(text = "☑️", callback_data = "yes5")
	item_right5 = types.InlineKeyboardButton(text = " ➡️", callback_data = "right5")

	markup_inline5.add(item_left5, item_ok5, item_right5)

	markup_inline6 = types.InlineKeyboardMarkup(row_width = 3)
	item_left6 = types.InlineKeyboardButton(text = "⬅️", callback_data = "left6")
	item_ok6 = types.InlineKeyboardButton(text = "☑️", callback_data = "yes6")
	item_right6 = types.InlineKeyboardButton(text = " ➡️", callback_data = "right6")

	markup_inline6.add(item_left6, item_ok6, item_right6)

	markup_inline7 = types.InlineKeyboardMarkup(row_width = 3)
	item_left7 = types.InlineKeyboardButton(text = "⬅️", callback_data = "left7")
	item_ok7 = types.InlineKeyboardButton(text = "☑️", callback_data = "yes7")
	item_right7 = types.InlineKeyboardButton(text = " ➡️", callback_data = "right7")

	markup_inline7.add(item_left7, item_ok7, item_right7)

	markup_inline8 = types.InlineKeyboardMarkup(row_width = 1)
	item_ok8 = types.InlineKeyboardButton(text = "☑️", callback_data = "yes8")
	item_left8 = types.InlineKeyboardButton(text = "⬅️", callback_data = "left8")

	markup_inline8.add(item_ok8, item_left8)

	markup_inline9 = types.InlineKeyboardMarkup(row_width = 3)
	item_left9 = types.InlineKeyboardButton(text = "⬅️", callback_data = "left9")
	item_ok9 = types.InlineKeyboardButton(text = "☑️", callback_data = "yes9")
	item_right9 = types.InlineKeyboardButton(text = " ➡️", callback_data = "right9")

	markup_inline9.add(item_left9, item_ok9, item_right9)






	if call.message:
		if call.data == "right":
			await bot.edit_message_media(media = types.InputMedia(type = "video", media = "BAACAgIAAxkBAAEJ6fdgoXtmPoh7fPCHTGerEPcDE0qTmgACnA4AAre0CElC1sSIEKTcoR8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline0)
		elif call.data == "right0":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6fhgoXtm4mbaLWuWJKMFOB3vQfBQwAACnQ4AAre0CEnX4e7LyXBtnx8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline1)
		elif call.data == "right1":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6flgoXtmrDTCfZhN_G2V2NkUqvw8agACng4AAre0CEkJGWpJi-ujbB8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline2)
		elif call.data == "right2":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6fpgoXtm4jWTx8bqoH_pPxSjaKyvSAACnw4AAre0CEnbo2rsIOZ_pR8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline3)
		elif call.data == "right3":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6ftgoXtmyVDRVZo73sVp2GUUJDxm8QACoA4AAre0CEn7t-41H9hzix8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline4)
		elif call.data == "right4":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6fxgoXtmKqWt_vQv4WeN5EiLK93WmwACoQ4AAre0CEnfvl-uhAZf2R8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline5)
		elif call.data == "right5":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6f1goXtmH0VV0xJc1np-N-mOmSiM7QACog4AAre0CEmjjfH6DGcuLh8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline6)
		elif call.data == "right6":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6f5goXtmQRQ11FIIcYIU1ru8vgEChgACow4AAre0CEmMVYvVQEVkmh8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline7)
		elif call.data == "right7":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6f9goXtm_PpW46jT6pCCH5KYREeGSQACpA4AAre0CEmPX2_8mwABb04fBA"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline8)

		




		elif call.data == "left0":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6fZgoXtmI6r_NXM08-drMmuOrQfVAAOwDgACAp0JSSNyKDVEgxjvHwQ"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline)
		elif call.data == "left1":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6fdgoXtmPoh7fPCHTGerEPcDE0qTmgACnA4AAre0CElC1sSIEKTcoR8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline0)
		elif call.data == "left2":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6fhgoXtm4mbaLWuWJKMFOB3vQfBQwAACnQ4AAre0CEnX4e7LyXBtnx8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline1)
		elif call.data == "left3":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6flgoXtmrDTCfZhN_G2V2NkUqvw8agACng4AAre0CEkJGWpJi-ujbB8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline2)
		elif call.data == "left4":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6fpgoXtm4jWTx8bqoH_pPxSjaKyvSAACnw4AAre0CEnbo2rsIOZ_pR8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline3)
		elif call.data == "left5":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6ftgoXtmyVDRVZo73sVp2GUUJDxm8QACoA4AAre0CEn7t-41H9hzix8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline4)
		elif call.data == "left6":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6fxgoXtmKqWt_vQv4WeN5EiLK93WmwACoQ4AAre0CEnfvl-uhAZf2R8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline5)
		elif call.data == "left7":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6f1goXtmH0VV0xJc1np-N-mOmSiM7QACog4AAre0CEmjjfH6DGcuLh8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline6)
		elif call.data == "left8":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6f5goXtmQRQ11FIIcYIU1ru8vgEChgACow4AAre0CEmMVYvVQEVkmh8E"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline7)
		elif call.data == "left9":
			await bot.edit_message_media(media = types.InputMedia(type = 'video', media = "BAACAgIAAxkBAAEJ6f5goXtmQRQ11FIIcYIU1ru8vgEChgACow4AAre0CEmMVYvVQEVkmh8E`"),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline8)


		elif call.data == "yes":
			await bot.delete_message(call.message.chat.id, call.message.message_id)
			await bot.delete_message(call.message.chat.id, call.message.message_id-1)
			chat_id = call.message.chat.id
			user_data[chat_id] = User_Data(call.message.text)
			font = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
			f1 = types.KeyboardButton("1")
			f2 = types.KeyboardButton("2")
			f3 = types.KeyboardButton("3")
			f4 = types.KeyboardButton("4")
			f5 = types.KeyboardButton("5")
			f6 = types.KeyboardButton("6")
			font.add(f1, f2, f3, f4, f5, f6)

			await bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font)
		elif call.data == "yes0":
			await bot.delete_message(call.message.chat.id, call.message.message_id)
			await bot.delete_message(call.message.chat.id, call.message.message_id-1)
			chat_id = call.message.chat.id
			user_data[chat_id] = User_Data(call.message.text)
			font = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
			f1 = types.KeyboardButton("1")
			f2 = types.KeyboardButton("2")
			f3 = types.KeyboardButton("3")
			f4 = types.KeyboardButton("4")
			f5 = types.KeyboardButton("5")
			f6 = types.KeyboardButton("6")
			font.add(f1, f2, f3, f4, f5, f6)
			await bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			await bot.register_next_step_handler(call.message, input_font1)
		elif call.data == "yes1":
			await bot.delete_message(call.message.chat.id, call.message.message_id)
			await bot.delete_message(call.message.chat.id, call.message.message_id-1)
			chat_id = call.message.chat.id
			user_data[chat_id] = User_Data(call.message.text)
			font = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
			f1 = types.KeyboardButton("1")
			f2 = types.KeyboardButton("2")
			f3 = types.KeyboardButton("3")
			f4 = types.KeyboardButton("4")
			f5 = types.KeyboardButton("5")
			f6 = types.KeyboardButton("6")
			font.add(f1, f2, f3, f4, f5, f6)
			await bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font2)
		elif call.data == "yes2":
			await bot.delete_message(call.message.chat.id, call.message.message_id)
			await bot.delete_message(call.message.chat.id, call.message.message_id-1)
			chat_id = call.message.chat.id
			user_data[chat_id] = User_Data(call.message.text)
			font = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
			f1 = types.KeyboardButton("1")
			f2 = types.KeyboardButton("2")
			f3 = types.KeyboardButton("3")
			f4 = types.KeyboardButton("4")
			f5 = types.KeyboardButton("5")
			f6 = types.KeyboardButton("6")
			font.add(f1, f2, f3, f4, f5, f6)
			bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font3)
		elif call.data == "yes3":
			await bot.delete_message(call.message.chat.id, call.message.message_id)
			await bot.delete_message(call.message.chat.id, call.message.message_id-1)
			chat_id = call.message.chat.id
			user_data[chat_id] = User_Data(call.message.text)
			font = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
			f1 = types.KeyboardButton("1")
			f2 = types.KeyboardButton("2")
			f3 = types.KeyboardButton("3")
			f4 = types.KeyboardButton("4")
			f5 = types.KeyboardButton("5")
			f6 = types.KeyboardButton("6")
			font.add(f1, f2, f3, f4, f5, f6)
			await bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font4)
		elif call.data == "yes4":
			bot.delete_message(call.message.chat.id, call.message.message_id)
			bot.delete_message(call.message.chat.id, call.message.message_id-1)
			chat_id = call.message.chat.id
			user_data[chat_id] = User_Data(call.message.text)
			font = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
			f1 = types.KeyboardButton("1")
			f2 = types.KeyboardButton("2")
			f3 = types.KeyboardButton("3")
			f4 = types.KeyboardButton("4")
			f5 = types.KeyboardButton("5")
			f6 = types.KeyboardButton("6")
			font.add(f1, f2, f3, f4, f5, f6)
			await bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font5)
		elif call.data == "yes5":
			await bot.delete_message(call.message.chat.id, call.message.message_id)
			await bot.delete_message(call.message.chat.id, call.message.message_id-1)
			chat_id = call.message.chat.id
			user_data[chat_id] = User_Data(call.message.text)
			font = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
			f1 = types.KeyboardButton("1")
			f2 = types.KeyboardButton("2")
			f3 = types.KeyboardButton("3")
			f4 = types.KeyboardButton("4")
			f5 = types.KeyboardButton("5")
			f6 = types.KeyboardButton("6")
			font.add(f1, f2, f3, f4, f5, f6)
			bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font6)
		elif call.data == "yes6":
			await bot.delete_message(call.message.chat.id, call.message.message_id)
			await bot.delete_message(call.message.chat.id, call.message.message_id-1)
			chat_id = call.message.chat.id
			user_data[chat_id] = User_Data(call.message.text)
			font = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
			f1 = types.KeyboardButton("1")
			f2 = types.KeyboardButton("2")
			f3 = types.KeyboardButton("3")
			f4 = types.KeyboardButton("4")
			f5 = types.KeyboardButton("5")
			f6 = types.KeyboardButton("6")
			font.add(f1, f2, f3, f4, f5, f6)
			await bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font7)
		elif call.data == "yes7":
			await bot.delete_message(call.message.chat.id, call.message.message_id)
			await bot.delete_message(call.message.chat.id, call.message.message_id-1)
			chat_id = call.message.chat.id
			user_data[chat_id] = User_Data(call.message.text)
			font = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
			f1 = types.KeyboardButton("1")
			f2 = types.KeyboardButton("2")
			f3 = types.KeyboardButton("3")
			f4 = types.KeyboardButton("4")
			f5 = types.KeyboardButton("5")
			f6 = types.KeyboardButton("6")
			font.add(f1, f2, f3, f4, f5, f6)
			await bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font8)
		elif call.data == "yes8":
			await bot.delete_message(call.message.chat.id, call.message.message_id)
			bot.delete_message(call.message.chat.id, call.message.message_id-1)
			chat_id = call.message.chat.id
			user_data[chat_id] = User_Data(call.message.text)
			font = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
			f1 = types.KeyboardButton("1")
			f2 = types.KeyboardButton("2")
			f3 = types.KeyboardButton("3")
			f4 = types.KeyboardButton("4")
			f5 = types.KeyboardButton("5")
			f6 = types.KeyboardButton("6")
			font.add(f1, f2, f3, f4, f5, f6)
			await bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font9)



@dp.message_handler(content_types = ["text"])
async def input_font(message: types.Message):
	await bot.send_message(875587704, '👦🏻First_Name: ' + str(message.from_user.first_name) + '\n🌐Username: @' + str(message.from_user.username) + '\n👤User_id: ' + str(message.from_user.id) + '\n📩Message_text: ' + str(message.text))
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name)
	
	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name)
	
	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name)
	
	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name)
	
	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name)
	
	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name)



async def input_font1(message: types.Message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name1)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name1)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name1)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name1)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name1)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name1)


async def input_font2(message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name2)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name2)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name2)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name2)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name2)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name2)

async def input_font3(message: types.Message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name3)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name3)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name3)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name3)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name3)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name3)



async def input_font4(message: types.Message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name4)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await botbot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name4)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name4)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name4)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name4)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name4)


async def input_font5(message: types.Message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name5)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name5)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name5)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name5)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name5)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name5)


async def input_font6(message: types.Message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name6)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name6)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name6)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name6)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name6)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name6)


async def input_font7(message: types.Message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name7)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name7)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name7)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name7)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name7)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name7)


async def input_font8(message: types.Message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name8)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name8)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name8)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name8)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name8)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name8)

async def input_font9(message: types.Message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name9)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name9)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name9)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name9)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name9)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)

		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		await bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name9)


async def input_name(message: types.Message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	await bot.send_message(message.chat.id, "Iltimos biroz kuting")
	os.system(f"""ffmpeg -y -i v1.mp4 -vf drawtext="fontfile={user.font}.ttf: \
	text='{user.text}': fontcolor=white: fontsize=80:\
	x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output.mp4""")

	with open('output.mp4', 'rb') as vid:
		await bot.send_video(message.chat.id, vid)

async def input_name1(message: types.Message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	await bot.send_message(message.chat.id, "Iltimos biroz kuting")
	os.system(f"""ffmpeg -y -i v2.mp4 -vf drawtext="fontfile={user.font}.ttf: \
	text='{user.text}': fontcolor=white: fontsize=80:\
	x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output1.mp4""")

	with open('output1.mp4', 'rb') as vid:
		await bot.send_video(message.chat.id, vid)

async def input_name2(message: types.Message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	await bot.send_message(message.chat.id, "Iltimos biroz kuting")
	os.system(f"""ffmpeg -y -i v3.mp4 -vf drawtext="fontfile={user.font}.ttf: \
	text='{user.text}': fontcolor=white: fontsize=80:\
	x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output2.mp4""")

	with open('output2.mp4', 'rb') as vid:
		await bot.send_video(message.chat.id, vid)

async def input_name3(message: types.Message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	await bot.send_message(message.chat.id, "Iltimos biroz kuting")
	os.system(f"""ffmpeg -y -i v4.mp4 -vf drawtext="fontfile={user.font}.ttf: \
	text='{user.text}': fontcolor=white: fontsize=80:\
	x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output3.mp4""")

	with open('output3.mp4', 'rb') as vid:
		await bot.send_video(message.chat.id, vid)

async def input_name4(message: types.Message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	await bot.send_message(message.chat.id, "Iltimos biroz kuting")
	os.system(f"""ffmpeg -y -i v5.mp4 -vf drawtext="fontfile={user.font}.ttf: \
	text='{user.text}': fontcolor=white: fontsize=80:\
	x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output4.mp4""")

	with open('output4.mp4', 'rb') as vid:
		await bot.send_video(message.chat.id, vid)

async def input_name5(message: types.Message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	await bot.send_message(message.chat.id, "Iltimos biroz kuting")
	os.system(f"""ffmpeg -y -i v6.mp4 -vf drawtext="fontfile={user.font}.ttf: \
	text='{user.text}': fontcolor=white: fontsize=80:\
	x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output5.mp4""")

	with open('output5.mp4', 'rb') as vid:
		await bot.send_video(message.chat.id, vid)

async def input_name6(message: types.Message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	await bot.send_message(message.chat.id, "Iltimos biroz kuting")
	os.system(f"""ffmpeg -y -i v7.mp4 -vf drawtext="fontfile={user.font}.ttf: \
	text='{user.text}': fontcolor=white: fontsize=80: enable='between(t,8,10):'\
	x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output6.mp4""")

	with open('output6.mp4', 'rb') as vid:
		await bot.send_video(message.chat.id, vid)

async def input_name7(message: types.Message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	await bot.send_message(message.chat.id, "Iltimos biroz kuting")
	os.system(f"""ffmpeg -y -i v8.mp4 -vf drawtext="fontfile={user.font}.ttf: \
	text='{user.text}': fontcolor=white: fontsize=80: enable='between(t,4,10):'\
	x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output7.mp4""")

	with open('output7.mp4', 'rb') as vid:
		await bot.send_video(message.chat.id, vid)

async def input_name8(message: types.Message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	await bot.send_message(message.chat.id, "Iltimos biroz kuting")
	os.system(f"""ffmpeg -y -i v9.mp4 -vf drawtext="fontfile={user.font}.ttf: \
	text='{user.text}': fontcolor=white: fontsize=80:\
	x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output8.mp4""")

	with open('output8.mp4', 'rb') as vid:
		await bot.send_video(message.chat.id, vid)

async def input_name9(message: types.Message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	await bot.send_message(message.chat.id, "Iltimos biroz kuting")
	os.system(f"""ffmpeg -y -i v10.mp4 -vf drawtext="fontfile={user.font}.ttf: \
	text='{user.text}': fontcolor=white: fontsize=80:\
	x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output9.mp4""")

	with open('output9.mp4', 'rb') as vid:
		await bot.send_video(message.chat.id, vid)



if __name__ == '__main__':
	executor.start_polling(dp)