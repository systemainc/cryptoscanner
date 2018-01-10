# bollinger_bot2


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