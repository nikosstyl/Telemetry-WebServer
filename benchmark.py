from sre_parse import expand_template
from tracemalloc import start
from blinker import receiver_connected
import requests
import time
import os
from multiprocessing import Process, Value

received = Value('i', 0, lock=False)
IP = 'http://localhost'
PORT = '9000'

def print_received():
	global receive
	while True:
		time.sleep(1)
		print('Received %d data in one second' % received.value)
		received.value = 0

def update_received():
	global received
	received.value = 0
	while True:
		r = requests.get(IP + ':' + PORT)
		if r.status_code == 200:
			received.value += 1

def main():
	p1 = Process(target=print_received)
	p2 = Process(target=update_received)
	p1.start()
	p2.start()

if __name__ == '__main__':
	main()