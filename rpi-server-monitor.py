#!/usr/bin/env python

import RPi.GPIO as GPIO 
import time, sys, signal, requests 
from lxml import html


GPIO.setmode(GPIO.BOARD) # Use board pin numbering
GPIO.setup(7, GPIO.OUT) # Setup GPIO Pin 7 to OUT
GPIO.setup(11, GPIO.OUT) # Setup GPIO Pin 11 to OUT


# Catch SIGTERM signals and exit gracefully
def signal_term_handler(signal, frame):
    #print 'got SIGTERM'
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_term_handler)


def coduo():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    page = requests.get('https://www.gametracker.com/server_info/IP-ADDRESS', headers=headers)
    tree = html.fromstring(page.content)

    # Get the element from it's XPath
    numPlayers = tree.xpath('//span[@id="HTML_num_players"]/text()')

    current = [int(i) for i in numPlayers]

    if current[0] > 0:
        #print('Players online!')
        GPIO.output(7,True) # Turn ON GPIO pin 7
    else:
        #print('No one playing')
        GPIO.output(7,False) # Turn OFF GPIO pin 7


def cod2():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    page = requests.get('https://www.gametracker.com/server_info/IP-ADDRESS', headers=headers)
    tree = html.fromstring(page.content)

    # Get the element from it's XPath
    numPlayers = tree.xpath('//span[@id="HTML_num_players"]/text()')

    current = [int(i) for i in numPlayers]

    if current[0] > 0:
        #print('Players online!')
        GPIO.output(11,True) # Turn ON GPIO Pin 11
    else:
        #print('No one playing')
        GPIO.output(11,False) # Turn OFF GPIO Pin 11


if __name__ == '__main__':

    try:
        while True:
            coduo()
            cod2()
            time.sleep(302)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
