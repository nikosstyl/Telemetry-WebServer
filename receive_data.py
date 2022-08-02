import json
import requests

def Receive_data():
	r = requests.get('http://localhost:9000')
	# sensors = json.loads(r.text)
	sensors = json.loads(r.json())
	# To parapanw einai ena python dictionary

	print_CAN_dict(sensors)

def print_CAN_dict(dict):
	for id, value in dict.items():
		print("ID:%s\tValue:%s" % (id, value))
	print("\n")

def main():
	while True:
		Receive_data()

if __name__ == '__main__':
	main()