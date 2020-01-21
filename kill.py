import pexpect
from pexpect import pxssh
import sys

def main(ip):
	s = pxssh.pxssh()
	try :
		s.login(ip,'iiserb','iiserb')
		s.sendline (' rm')
	except Exception :
		pass


def get_ip():
	st = '172.28.154.'
	re = [st+str(2*i) for i in range(30)]
	return re

for i in get_ip():
	print(i)
	main(i)

