import requests
import telebot
from telebot.types import InlineKeyboardButton as Btn , InlineKeyboardMarkup as Mak

headers = {
    'authority': 'api.pikwy.com',
    'accept': '*/*',
    'accept-language': 'bn-BD,bn;q=0.9,en-US;q=0.8,en;q=0.7',
    'dnt': '1',
    'origin': 'https://pikwy.com',
    'referer': 'https://pikwy.com/',
    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
}

token = "000"  # এখানে তোমার Bot Token বসাও
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def web(message):
    name = f"[{message.from_user.first_name}](tg://settings)"
    txt = '''হ্যালো {}, আমি একটি বট 📸  
যে যেকোনো ওয়েবসাইটের স্ক্রিনশট নিতে পারে।
তোমার ওয়েবসাইটের লিংক পাঠাও, আমি স্ক্রিনশট পাঠাবো।'''.format(name)

    if message.text == "/start":
        bot.reply_to(message, txt, parse_mode="markdown",
                     reply_markup=Mak().add(Btn('ডেভেলপার', url='tg://user?id=6829790680')))
    else:
        link = message.text
        params = {
            'tkn': '125',
            'd': '3000',
            'u': link,
            'fs': '0',
            'w': '1280',
            'h': '1200',
            's': '100',
            'z': '100',
            'f': 'jpg',
            'rt': 'jweb',
        }
        response = requests.get('https://api.pikwy.com/', params=params, headers=headers).json()
        try:
            img = response['iurl']
            date = response['date']
            dat = f'সময়: {date}'
            chat_id = message.chat.id

            bot.send_photo(chat_id, img, reply_to_message_id=message.message_id,
                           reply_markup=Mak().add(Btn(dat, url='https://t.me/YOUV1')))
        except:
            bot.reply_to(message, 'একটি সঠিক URL দিন (URL encode করা থাকা উচিত)')
        
bot.infinity_polling()
