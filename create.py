import random
import sys
import string

length=0

if len(sys.argv) > 1:
	if int(sys.argv[1]) > 3:
		length = int(sys.argv[1])
	else:
		print("Your password needs to be at least 4 characters long!")
		sys.exit()
else:
	length = 12
password = []
digit = False
string_char = False
punctuation = False

while (not(digit and string_char and punctuation)):
	password = []
	digit = False
	string_char = False
	punctuation = False
	for i in range(length):
		character = random.choice(string.ascii_letters + string.digits + "!?-;:")
		password.append(character)
		if character in string.ascii_letters:
			string_char = True
		elif character in string.digits:
			digit = True
		elif character in ["!", "?", "-", ";", ":"]:
			punctuation = True

password = "".join(password)

print(password)

