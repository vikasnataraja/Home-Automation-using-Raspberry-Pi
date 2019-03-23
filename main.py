import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#LED
def Onl(pin):
        GPIO.output(pin3,GPIO.HIGH)
        return
def Offl(pin):
        GPIO.output(pin3,GPIO.LOW)
        return
#FAN
def Onfan(pin):
        GPIO.output(pin1,GPIO.HIGH) #in2
        GPIO.output(pin2,GPIO.LOW)   #IN1
        return
def Offfan(pin):
        GPIO.output(pin1,GPIO.LOW)
        return

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
pin1 = 11
pin2 = 13
pin3 = 15
pin4 = 29
pin5 = 33
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.IN)
GPIO.setup(pin5, GPIO.OUT)



def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == 'Onl':
       bot.sendMessage(chat_id, Onl(pin3),'')
    elif command == 'Offl':
       bot.sendMessage(chat_id, Offl(pin3),'')
    elif command == 'Onfan':
       bot.sendMessage(chat_id, Onfan(pin1),'')
       bot.sendMessage(chat_id, Onfan(pin2),'')
    elif command == 'Offfan':
       bot.sendMessage(chat_id, Offfan(pin1),'')
       bot.sendMessage(chat_id, Offfan(pin2),'')
    elif command == 'checkmoist':
       bot.sendMessage(chat_id, checkmoist(pin4),'')
    else:
        bot.sendMessage(chat_id,'busy! check later')
        print 'Enter valid command'

def checkmoist(pin):
  while (True):
    if GPIO.input(pin4):
       print("need to Water The Garden")
       GPIO.output(pin5, GPIO.HIGH)
       return
    else:
       print("no need to  water the garden")
       GPIO.output(pin5, GPIO.LOW)
       return



bot = telepot.Bot('332595434:AAFo5VxjrKs_uXYwQjcbWyBjEPS4m1YYuDw')
bot.message_loop(handle)
print 'I am listening...'
while 1:
     time.sleep(1)
