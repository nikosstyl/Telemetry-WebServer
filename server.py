from http.server import HTTPServer, BaseHTTPRequestHandler
import json

received = {}

class requestHandler(BaseHTTPRequestHandler):
	def do_GET (self):
		global received

		if received:
			self.send_status_code(200)
			# Return ok if data already exists and then send data
			self.wfile.write(received)
		else:
			self.send_status_code(400)
			# Return not ok if data are not available yet
	
	def do_POST(self):
		global received
		
		content_length = int(self.headers.get('content-length', 0))
		# Get the length of the contents
		received = self.rfile.read(content_length)
		self.send_status_code(200)

	def send_status_code(self, status_code):
		self.send_response(status_code)
		self.send_header('content-type', 'application/json')
		self.end_headers()

def main():
	PORT = 9000
	server_address = ('localhost', PORT)
	server = HTTPServer(server_address, requestHandler)
	print('Server running on port %s' % PORT)
	server.serve_forever()

if __name__ == '__main__':
	main()