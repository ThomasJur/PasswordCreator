import random
import sys
import string

length=0
if len(sys.argv) > 1:
	length = int(sys.argv[1])
else:
	length = 12

password = []

for i in range(length):
	password.append(random.choice(string.ascii_letters + string.digits))

password = "".join(password)

print(password)

