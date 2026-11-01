#Create a TCP server bound to 127.0.0.1 and the provided PORT variable.
#  Accept one client, receive and decode one message, 
# validate it with re.fullmatch(),
#  print parsed fields or Fail, then close.

import socket, re

#provided
pattern = r'username\s*:\s*(?P<user>\w+)\s*,\s*password\s*:\s*(?P<pw>\S+)'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', PORT))

s.listen()
con, addr = s.accept()

reply = con.recv(1024).decode()
match = re.fullmatch(pattern, reply)

if match:
    print('Username:', match.group('user'))
    print('Password:', match.group('pw'))
else:
    print('Fail')
con.close()
s.close()