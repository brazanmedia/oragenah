import Constants as keys
import requests
import telegram
import json
import os, sys, time, random
import Responses as R
import datetime
from urllib import request
from telegram.ext import *




#cek coin sekan koin gecko
def gecko(update, context):
    chat_id = update.effective_chat.id    
    pair = context.args[0]
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=idr&symbols="
    per = pair.upper()
    lope = pair.lower()
    #ope = pair.title()
    prentah = f"{url}{lope}"
    
    foo=['If you dont know how to take care of money, money will run away from you','Jangan menggoda istri orang,biarlah istri orang yang menngoda kita','hidup itu pasti banyak cobaan, kalau banyak saweran itu namanya dangdutan','Jangan semangat,ayo menyerah, aerdrop zonk masih ada ginjal']
    random_link=random.choice(foo)
    custom_keyboard = [['top-left', 'top-right'], ['bottom-left', 'bottom-right']]
    reply_markup = telegram.ReplyKeyboardRemove()


    res = request.urlopen(prentah)
    #data = json.loads(res.read())
    
    data = json.loads(res.read())
    
    x = datetime.datetime.now()
    
 #   dt = range(len(data))
   
    for i in range(len(data)):
    	name = data[0]['id']
    harga = data[0]['current_price']
    rank = data[0]['market_cap_rank']
    high = data[0]['high_24h']
    low = data[0]['low_24h']
    persen = data[0]['price_change_percentage_24h']
    ath = data[0]['ath']
    atl = data[0]['atl']
    lope = pair.lower()
    
    
    if bool(data) == []:
    	
    	text = f"Token {per} tidak di temukan! \n Tangan mu Ra suport..!! \n Stop calay...!!! \n\n {x}"
         #text = f"🧞‍♂ {per} *{name.title()}*\nCMC Rank  *# {rank}* \n\n`Harga   Rp {harga:0,} | {persen:,.2f}%\nHigh 24H : Rp{high:0,} \nLow  24H : Rp{low:0,}\nAth|Atl  {ath:0,} | {atl:0,} IDR`\n\n*Mileaaa make rook..\nGasss serookk..*\n\nRandom :\n_°{random_link}°_\n\n[mantap-mantap disini](https://t.me/CuanAirdropduit)\n\n{x}"
    else:
    	
    #	text = f"Token {per} tidak di temukan! \n Tangan mu Ra suport..!! \n Stop calay...!!! \n\n {x}"
        text = f"🧞‍♂ {per} *{name.title()}*\nCMC Rank  *# {rank}* \n\n`Harga   Rp {harga:0,} | {persen:,.2f}%\nHigh 24H : Rp{high:0,} \nLow  24H : Rp{low:0,}\nAth|Atl  {ath:0,} | {atl:0,} IDR`\n\n*Mileaaa make rook..\nGasss serookk..*\n\nRandom :\n_°{random_link}°_\n\n[mantap-mantap disini](https://t.me/CuanAirdropduit)\n\n{x}"
    context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup, parse_mode=telegram.ParseMode.MARKDOWN)

def bacot(update, context):
	text = str(update.message.text).lower()
	respon = R.sample_responses(text)
	
	update.message.reply_text(respon)
	


	#os.system('clear')
	
    
def main():
	updater = Updater(keys.API_KEY, use_context=True)
	dp = updater.dispatcher
	
	dp.add_handler(CommandHandler("p", gecko))
	
	dp.add_handler(MessageHandler(Filters.text, bacot))
	

	#dp.add_error_handler(error)
	
	updater.start_polling()
	updater.idle()
	
main()
