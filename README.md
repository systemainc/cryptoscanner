# This scanner/bot is designed to scan through the current crypto market using various public APIs. 
Config file allows various configurations, like the minimal market cap or trading volume (if you don't want to be spammed with signals for crappy cryptos). 

The current version implements bollinger bands, MACD and Money flow index signals to see of the current price/trand of a give crypto is at a good buying or selling point. There is also integration with Telegram channel to get signals.


#Dependencies:
sudo python -m pip install python-telegram-bot


#Setting up telegram channel.
1. use @botfather to create a bot. Make sure it ends with word 'bot'
2. Create a Telegram channel and add bot to it.
3. Go to your channel in the web interface. The URL will looks something like this:
https://web.telegram.org/#/im?p=c1110274154_3843246593751299742
the numbers after c and before _ is your c
hat ID. You should add it to config.yml users section and add -100 before the numbers
4. So, for the example above, the chat ID should be: -1001110274154


#Amazon AWS setup.
sudo apt-get install xvfb

#setup pacific timezone
sudo dpkg-reconfigure tzdata

#ToDo
- Explore the feasibility of using Fibonacci retracement for a reasonable buy zone indicator
- Implement config settings for better A/B testing, including using test Telegram channel
