
# https://github.com/eternnoir/pyTelegramBotAPI

import telebot

token = "630476434:AAHiDmdHiUdfg7Q2bG283S6LcA-_TDwK4cM"

bot = telebot.TeleBot(token)


def FefiVocal(a):
    if(a == 'a'): 
        return 'i'
    if(a == 'e'): 
        return 'i'
    if(a == 'o'): 
        return 'i'
    if(a == 'u'): 
        return 'i'
    return a



@bot.message_handler(commands=['fefify'])
def route_fefify(message):
    print(message)
    # response = unirest.get('https://jsonplaceholder.typicode.com/todos/1',
    #     headers={
    #         "X-RapidAPI-Host": "copa-america.p.rapidapi.com",
    #         "X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
    #     })

    # # contents = urllib.request.urlopen("http://examp).read()
    fefiedMsg = message.text

    fefiedMsg = fefiedMsg.split(' ')

    fefiedMsg.pop(0)

    fefiedMsg = ' '.join(fefiedMsg)
    print(fefiedMsg)
    
    fefiedMsg = ''.join([FefiVocal(x) for x in fefiedMsg])
    print(fefiedMsg)
    bot.reply_to(message,fefiedMsg)
    pass

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

print("bot listening")
bot.polling()