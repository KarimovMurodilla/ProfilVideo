import os
import re
import telebot
import sqlite3 as sql
from telebot import types

token = '1499712691:AAFRuln329buzav3EoVVomQb493BGWcOU3s'
bot = telebot.TeleBot(token)

user_data = {}

class User_Data:
	def __init__(self, font):
		self.font = font
		self.text = ""

@bot.message_handler(commands = ['start'])
def send_welcome(message):
	bot.send_message(875587704, '👦🏻First_Name: ' + str(message.from_user.first_name) + '\n🌐Username: @' + str(message.from_user.username) + '\n👤User_id: ' + str(message.from_user.id) + '\n📩Message_text: ' + str(message.text))
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

	bot.send_message(message.chat.id, """
/add_text - Videoga text yozish
/help - Bot haqida ma'lumot
""")


@bot.message_handler(commands = ['help'])
def send_welcome(message):
	bot.send_message(message.chat.id, """
<i>Assalomu Aleykum!
Bu bot bilan siz profilingiz uchun sifatli va kreativ 
bo'lgan videolarga o'zingizni ismingizni yoki 
o'zingiz xohlagan biror bir textni turli xil 
shriftlarda videoga tushirishingiz mumkin!</i>
""", parse_mode = "html")

@bot.message_handler(commands = ['developer'])
def send_welcome(message):
	bot.send_message(message.chat.id, """
@murodillakarimov""")



@bot.message_handler(commands = ['add_text'])
def send_welcome(message):
	markup_inline = types.InlineKeyboardMarkup(row_width = 1)
	item_ok = types.InlineKeyboardButton(text = "☑️", callback_data = "yes")
	item_right = types.InlineKeyboardButton(text = " ➡️", callback_data = "right")

	markup_inline.add(item_ok, item_right)
	v1 = 'BAACAgIAAxkBAAIRXWCqyT7ahgirNb_gwpdXB5_hbLuZAAKwDgACAp0JSX-UbL8F-aG8HwQ'
	bot.send_message(message.chat.id, "O'zingizga mos videoni tanlang ⬇️")
	bot.send_video(message.chat.id, v1, reply_markup = markup_inline)

@bot.callback_query_handler(func = lambda call: True)
def send_welcome(call):
	v1 = 'BAACAgIAAxkBAAIRXWCqyT7ahgirNb_gwpdXB5_hbLuZAAKwDgACAp0JSX-UbL8F-aG8HwQ'
	v2 = 'BAACAgIAAxkBAAIRXmCqyUkXFrcN-9ZkQrs6c4EQ4CFhAAKBCwACWX9ZSYWiH3WgeVnJHwQ'
	v3 = 'BAACAgIAAxkBAAIRX2CqyVOndl_YexNACcypwpHp6K-AAAKCCwACWX9ZSZNk30AeKIFjHwQ'
	v4 = 'BAACAgIAAxkBAAIRYGCqyVjIUv5qly_CVVFe7oNed2Q4AAKDCwACWX9ZSeUJyqH5V0uOHwQ'
	v5 = 'BAACAgIAAxkBAAIRYWCqyWJG-w2xXMNQolF6PXqD_gSBAAKECwACWX9ZScd43SUgXNvbHwQ'
	v6 = 'BAACAgIAAxkBAAIRYmCqyWdat2phI5di4iDwk-Cl2qS-AAKFCwACWX9ZSesQ6I2Bc9cWHwQ'
	v7 = 'BAACAgIAAxkBAAIRY2CqyYQUfNn0ddl9r9wfQSRMHKGaAAKGCwACWX9ZSQIAAUn_FpEfgB8E'
	v8 = 'BAACAgIAAxkBAAIRZGCqyYn7q6dbk-sXGJJ9vrU9nB8eAAKHCwACWX9ZSX6Pl8Qnh-YHHwQ'
	v9 = 'BAACAgIAAxkBAAIRZWCqyYyrTSZ_u8lxolrQO4UTFgJ_AAKjDgACt7QISWefWp23ZOPZHwQ'
	v10 = 'BAACAgIAAxkBAAIRZmCqyZNczq_6XMb3EGWVZ4F9XW3XAAKICwACWX9ZSUO7zhi0phcRHwQ'
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
			bot.edit_message_media(media = types.InputMedia(type = "video", media = v2),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline0)
		elif call.data == "right0":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v3),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline1)
		elif call.data == "right1":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v4),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline2)
		elif call.data == "right2":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v5),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline3)
		elif call.data == "right3":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v6),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline4)
		elif call.data == "right4":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v7),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline5)
		elif call.data == "right5":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v8),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline6)
		elif call.data == "right6":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v9),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline7)
		elif call.data == "right7":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v10),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline8)

		




		elif call.data == "left0":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v1),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline)
		elif call.data == "left1":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v2),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline0)
		elif call.data == "left2":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v3),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline1)
		elif call.data == "left3":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v4),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline2)
		elif call.data == "left4":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v5),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline3)
		elif call.data == "left5":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v6),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline4)
		elif call.data == "left6":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v7),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline5)
		elif call.data == "left7":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v8),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline6)
		elif call.data == "left8":
			bot.edit_message_media(media = types.InputMedia(type = 'video', media = v9),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline7)
		elif call.data == "left9":
			 bot.edit_message_media(media = types.InputMedia(type = 'video', media = v10),
			chat_id = call.message.chat.id,
			message_id = call.message.message_id,
			reply_markup = markup_inline8)


		elif call.data == "yes":
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

			bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font)
		elif call.data == "yes0":
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
			bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font1)
		elif call.data == "yes1":
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
			bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font2)
		elif call.data == "yes2":
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
			bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font3)
		elif call.data == "yes3":
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
			bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
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
			bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font5)
		elif call.data == "yes5":
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
			bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font6)
		elif call.data == "yes6":
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
			bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font7)
		elif call.data == "yes7":
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
			bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font8)
		elif call.data == "yes8":
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
			bot.send_photo(call.message.chat.id, photo = "https://imbt.ga/iZV3p4bGfF", caption = "Rasmdan shriftni tanlang!  ⬆️", reply_markup = font)
			bot.register_next_step_handler(call.message, input_font9)



@bot.message_handler(content_types = ["text"])
def input_font(message):
	bot.send_message(875587704, '👦🏻First_Name: ' + str(message.from_user.first_name) + '\n🌐Username: @' + str(message.from_user.username) + '\n👤User_id: ' + str(message.from_user.id) + '\n📩Message_text: ' + str(message.text))
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name)
	
	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name)
	
	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name)
	
	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name)
	
	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name)
	
	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name)



def input_font1(message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name1)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name1)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name1)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name1)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name1)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name1)


def input_font2(message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name2)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name2)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name2)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name2)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name2)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name2)

def input_font3(message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name3)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name3)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name3)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.chat.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name3)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name3)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name3)



def input_font4(message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name4)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name4)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name4)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name4)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name4)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name4)


def input_font5(message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name5)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name5)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name5)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name5)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name5)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name5)


def input_font6(message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name6)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name6)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name6)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name6)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name6)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name6)


def input_font7(message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name7)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name7)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name7)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name7)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name7)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name7)


def input_font8(message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name8)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name8)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name8)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name8)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name8)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name8)

def input_font9(message):
	if message.text == "1":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name9)

	elif message.text == "2":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name9)

	elif message.text == "3":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name9)

	elif message.text == "4":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name9)

	elif message.text == "5":
		markup_remove = types.ReplyKeyboardRemove(selective = False)
		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name9)

	elif message.text == "6":
		markup_remove = types.ReplyKeyboardRemove(selective = False)

		chat_id = message.chat.id
		user_data[chat_id] = User_Data(message.text)
		bot.send_message(message.from_user.id, "Ismingizni yoki biror bir text yozing: ", reply_markup = markup_remove)
		bot.register_next_step_handler(message, input_name9)


def input_name(message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	if re.search(r'[^a-zA-Za0123456789@|\'/?<>()~!#$%&*"":=+_, .-]',message.text):
		bot.send_message(message.chat.id, "Iltimos faqat lotin harfidan foydalaning va ortiqcha simvol ishlatmang!")
		bot.register_next_step_handler(message, input_name)
	else:
		bot.send_message(message.chat.id, "Iltimos biroz kuting...")
		os.system(f"""ffmpeg -y -i v1.mp4 -vf drawtext="fontfile={user.font}.ttf: \
		text='{user.text}': fontcolor=white: fontsize=80:\
		x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output.mp4""")

		with open('output.mp4', 'rb') as vid:
			bot.send_video(message.chat.id, vid)

def input_name1(message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	if re.search(r'[^a-zA-Za0123456789@|\'/?<>()~!#$%&*"":=+_, .-]',message.text):
		bot.send_message(message.chat.id, "Iltimos faqat lotin harfidan foydalaning va ortiqcha simvol ishlatmang!")
		bot.register_next_step_handler(message, input_name1)
	else:
		bot.send_message(message.chat.id, "Iltimos biroz kuting...")
		os.system(f"""ffmpeg -y -i v2.mp4 -vf drawtext="fontfile={user.font}.ttf: \
		text='{user.text}': fontcolor=white: fontsize=80:\
		x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output1.mp4""")

		with open('output1.mp4', 'rb') as vid:
			bot.send_video(message.chat.id, vid)

def input_name2(message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	if re.search(r'[^a-zA-Za0123456789@|\'/?<>()~!#$%&*"":=+_, .-]',message.text):
		bot.send_message(message.chat.id, "Iltimos faqat lotin harfidan foydalaning va ortiqcha simvol ishlatmang!")
		bot.register_next_step_handler(message, input_name2)
	else:
		bot.send_message(message.chat.id, "Iltimos biroz kuting...")
		os.system(f"""ffmpeg -y -i v3.mp4 -vf drawtext="fontfile={user.font}.ttf: \
		text='{user.text}': fontcolor=white: fontsize=80:\
		x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output2.mp4""")

		with open('output2.mp4', 'rb') as vid:
			bot.send_video(message.chat.id, vid)

def input_name3(message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	if re.search(r'[^a-zA-Za0123456789@|\'/?<>()~!#$%&*"":=+_, .-]',message.text):
		bot.send_message(message.chat.id, "Iltimos faqat lotin harfidan foydalaning va ortiqcha simvol ishlatmang!")
		bot.register_next_step_handler(message, input_name3)
	else:
		bot.send_message(message.chat.id, "Iltimos biroz kuting...")
		os.system(f"""ffmpeg -y -i v4.mp4 -vf drawtext="fontfile={user.font}.ttf: \
		text='{user.text}': fontcolor=white: fontsize=80:\
		x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output3.mp4""")

		with open('output3.mp4', 'rb') as vid:
			bot.send_video(message.chat.id, vid)

def input_name4(message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	if re.search(r'[^a-zA-Za0123456789@|\'/?<>()~!#$%&*"":=+_, .-]',message.text):
		bot.send_message(message.chat.id, "Iltimos faqat lotin harfidan foydalaning va ortiqcha simvol ishlatmang!")
		bot.register_next_step_handler(message, input_name4)
	else:
		bot.send_message(message.chat.id, "Iltimos biroz kuting...")
		os.system(f"""ffmpeg -y -i v5.mp4 -vf drawtext="fontfile={user.font}.ttf: \
		text='{user.text}': fontcolor=white: fontsize=80:\
		x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output4.mp4""")

		with open('output4.mp4', 'rb') as vid:
			bot.send_video(message.chat.id, vid)

def input_name5(message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	if re.search(r'[^a-zA-Za0123456789@|\'/?<>()~!#$%&*"":=+_, .-]',message.text):
		bot.send_message(message.chat.id, "Iltimos faqat lotin harfidan foydalaning va ortiqcha simvol ishlatmang!")
		bot.register_next_step_handler(message, input_name5)
	else:
		bot.send_message(message.chat.id, "Iltimos biroz kuting...")
		os.system(f"""ffmpeg -y -i v6.mp4 -vf drawtext="fontfile={user.font}.ttf: \
		text='{user.text}': fontcolor=white: fontsize=80:\
		x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output5.mp4""")

		with open('output5.mp4', 'rb') as vid:
			bot.send_video(message.chat.id, vid)

def input_name6(message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	if re.search(r'[^a-zA-Za0123456789@|\'/?<>()~!#$%&*"":=+_, .-]',message.text):
		bot.send_message(message.chat.id, "Iltimos faqat lotin harfidan foydalaning va ortiqcha simvol ishlatmang!")
		bot.register_next_step_handler(message, input_name6)
	else:
		bot.send_message(message.chat.id, "Iltimos biroz kuting...")
		os.system(f"""ffmpeg -y -i v7.mp4 -vf drawtext="fontfile={user.font}.ttf: \
		text='{user.text}': fontcolor=white: fontsize=80: enable='between(t,8,10):'\
		x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output6.mp4""")

		with open('output6.mp4', 'rb') as vid:
			bot.send_video(message.chat.id, vid)

def input_name7(message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	if re.search(r'[^a-zA-Za0123456789@|\'/?<>()~!#$%&*"":=+_, .-]',message.text):
		bot.send_message(message.chat.id, "Iltimos faqat lotin harfidan foydalaning va ortiqcha simvol ishlatmang!")
		bot.register_next_step_handler(message, input_name7)
	else:
		bot.send_message(message.chat.id, "Iltimos biroz kuting...")
		os.system(f"""ffmpeg -y -i v8.mp4 -vf drawtext="fontfile={user.font}.ttf: \
		text='{user.text}': fontcolor=white: fontsize=80: enable='between(t,4,10):'\
		x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output7.mp4""")

		with open('output7.mp4', 'rb') as vid:
			bot.send_video(message.chat.id, vid)

def input_name8(message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	if re.search(r'[^a-zA-Za0123456789@|\'/?<>()~!#$%&*"":=+_, .-]',message.text):
		bot.send_message(message.chat.id, "Iltimos faqat lotin harfidan foydalaning va ortiqcha simvol ishlatmang!")
		bot.register_next_step_handler(message, input_name8)
	else:
		bot.send_message(message.chat.id, "Iltimos biroz kuting...")
		os.system(f"""ffmpeg -y -i v9.mp4 -vf drawtext="fontfile={user.font}.ttf: \
		text='{user.text}': fontcolor=white: fontsize=80:\
		x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output8.mp4""")

		with open('output8.mp4', 'rb') as vid:
			bot.send_video(message.chat.id, vid)

def input_name9(message):
	chat_id = message.chat.id
	user = user_data[chat_id]
	user.text = message.text
	if re.search(r'[^a-zA-Za0123456789@|\'/?<>()~!#$%&*"":=+_, .-]',message.text):
		bot.send_message(message.chat.id, "Iltimos faqat lotin harfidan foydalaning va ortiqcha simvol ishlatmang!")
		bot.register_next_step_handler(message, input_name9)
	else:
		bot.send_message(message.chat.id, "Iltimos biroz kuting...")
		os.system(f"""ffmpeg -y -i v10.mp4 -vf drawtext="fontfile={user.font}.ttf: \
		text='{user.text}': fontcolor=white: fontsize=80:\
		x=(w-text_w)/2: y=(h-text_h)/2" -codec:a copy output9.mp4""")

		with open('output9.mp4', 'rb') as vid:
			bot.send_video(message.chat.id, vid)



if __name__ == '__main__':
	bot.polling(none_stop = True)