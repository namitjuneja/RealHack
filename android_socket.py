import socket, traceback
from pymouse import PyMouse
m = PyMouse()
host = '192.168.1.14'
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
while 1:
	try:
		message, address = s.recvfrom(8192)
		m.move(abs(float("".join  (message.split(" "))  .split(",")[2])),abs(float("".join  (message.split(" "))  .split(",")[3])))
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
		traceback.print_exc()