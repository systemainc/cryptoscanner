
from telegram.ext import Updater, CommandHandler, Job
import datetime
import logging
import yaml
import sys
import os
import time



class bb_telegram():

    def __init__(self, token, chat_id):
        self.chat_id = chat_id
        self.token = token
        self.updater = Updater(self.token)
        self.dp = self.updater.dispatcher
        self.dp.add_handler(CommandHandler("start", self.start))
        self.updater.start_polling()
        self.msg_body = None
        #self.updater.idle()


    def start(self):
        #bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
        #bot.send_message(chat_id=1116291223, text="I'm a bot, please talk to me!")
        #bot.send_message(chat_id=683976468, text="I'm a bot, please talk to me!")
        self.dp.bot.send_message(chat_id=self.chat_id, text="I'm starting now!")
        print("message was send")

    def create_msg(self, currency, last_price, rate, files):
        if (currency == 'BTC'):
            self.msg_body = "Price Alert (BTRX " + currency + "/USD @ " + str(last_price) + ")\n" \
                            "Price for " + currency + " currency is within a " + rate + " range.\n" \
                            "https://www.coinigy.com/main/markets/BTRX/" + currency + "/USD.\n" \
                            "Timestamp: " + datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p") + "\n"
        else:
            self.msg_body = "Price Alert (BTRX " + currency + "/BTC @ " + str(last_price) + ")\n" \
                            "Price for " + currency + " currency is within a " + rate + " range.\n" \
                            "https://www.coinigy.com/main/markets/BTRX/" + currency + "/BTC.\n" \
                            "Timestamp: " + datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p") + "\n"
        return self.msg_body


    def send_message(self, cryptocurrency, rate, vol_24h, upper_line, lower_line, price, MFI, MACD_delta):
        if (cryptocurrency == 'BTC'):
            self.msg_body = "Price for " + cryptocurrency + " currency is within a " + rate.upper() + " range.\n" \
            "Timestamp: " + datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p") + "\n" \
            "Price: " + str(price) + "\n" \
            "Upper: " + str(upper_line.values()[0]) + "\n" \
            "Lower: " + str(lower_line.values()[0]) + "\n" \
            "24hr Vol (USD): " + str(vol_24h) + "\n" \
            "MFI: " + str(MFI) + "\n" \
            "MACD_delta: " + str(MACD_delta) + "\n" \
            "https://www.coinigy.com/main/markets/BTRX/" + cryptocurrency + "/USD.\n"
        else:
            self.msg_body = "Price for " + cryptocurrency + " is " + format(price, '.8f') + " and is currency within a " + rate.upper() + " range.\n" \
            "Timestamp: " + datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p") + "\n" \
            "Price: " + str(price) + "\n" \
            "Upper: " + str(upper_line.values()[0]) + "\n" \
            "Lower: " + str(lower_line.values()[0]) + "\n" \
            "24hr Vol (BTC): " + str(vol_24h) + "\n" \
            "MFI: " + str(MFI) + "\n" \
            "MACD_delta: " + str(MACD_delta) + "\n" \
            "https://www.coinigy.com/main/markets/BTRX/" + cryptocurrency + "/BTC.\n"

        self.dp.bot.send_message(chat_id=self.chat_id, text=self.msg_body, disable_web_page_preview="true")
        print("message was send")



    def send_picture(self, cryptocurrency):
        if cryptocurrency is not 'BTC':
            filename = cryptocurrency + '_BTC.png'
        else:
            filename = 'BTC_USD.png'
        self.dp.bot.sendDocument(chat_id=self.chat_id, document=open(filename, 'rb'))
        print("picture was send")



def main():

    try:
        with open('config.yml', 'r') as ymlfile:
            config = yaml.load(ymlfile)
    except BaseException:
        #print(path_to_config + " file is not exists! Please create it first.")
        sys.exit()

    token = config['token']
    chat_id = config['users'][0]
    telegram = bb_telegram(token, chat_id)

    telegram.send_message('ETH', 'selling', '999', 2.4)
    telegram.send_picture('BTC')

    #telegram.dp.bot.send_message(chat_id, text="I'm a bot, please talk to me!")
    #telegram.dp.bot.sendDocument(chat_id, document=open('fig_1.png', 'rb'))



if __name__ == "__main__":
        main()