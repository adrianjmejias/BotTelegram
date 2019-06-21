
# https://github.com/eternnoir/pyTelegramBotAPI

import telebot
import unirest

import serial
from serial.tools import list_ports
import serial.rfc2217


token = "630476434:AAHiDmdHiUdfg7Q2bG283S6LcA-_TDwK4cM"

bot = telebot.TeleBot(token)


ports = list(list_ports.comports())

# return the port if 'USB' is in the description 
for port_no, description, address in ports:
    
    print("---------------------------")
    print(port_no)
    print(description)
    print(address)
    print("------------------------------")

ser = serial.Serial('/dev/ttyACM1', baudrate=9600)  # open serial port



print(ser.name)         # check which port was really used

@bot.message_handler(commands=['on'])
def send_welcome(message):
    bot.reply_to(message, "Prendiendo")
    print(message)

    ser.write("1")

#     ...     x = ser.read()          # read one byte
# ...     s = ser.read(10)        # read up to ten bytes (timeout)
# ...     line = ser.readline()   # read a '\n' terminated line







    # response = unirest.get('https://jsonplaceholder.typicode.com/todos/1',
    #     headers={
    #         "X-RapidAPI-Host": "copa-america.p.rapidapi.com",
    #         "X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
    #     })

    # # contents = urllib.request.urlopen("http://examp).read()
    # bot.reply_to(message, "88888")


@bot.message_handler(commands=['off'])
def send_welcome(message):
    bot.reply_to(message, "Apagando")

    print(message)
    ser.write('0')






    # response = unirest.get('https://jsonplaceholder.typicode.com/todos/1',
    #     headers={
    #         "X-RapidAPI-Host": "copa-america.p.rapidapi.com",
    #         "X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
    #     })

    # # contents = urllib.request.urlopen("http://examp).read()
    # bot.reply_to(message, "88888")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)



bot.polling()