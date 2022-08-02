import json
import requests
from random import seed, randint

IP = 'http://localhost'
PORT = '9000'

def Send_data():
	read_sensors = {}

	i=0
	can_id = 1000
	for i in range(10):
		can_compound_id = i
		id = str(can_id) + "," + str(can_compound_id)
		read_sensors[id] = str(randint(0,150))
	# print_CAN_dict(read_sensors)
	r = requests.post(IP + ':' + PORT, json=json.dumps(read_sensors))
	# print("Status code: %d" % r.status_code)


def print_CAN_dict(dict):
	for id, value in dict.items():
		print("ID:%s\tValue:%s" % (id, value))

def main():
	seed(10)
	while True:
		Send_data()

if __name__ == '__main__':
	main()