"""
ASCII Ceasar Cipher
Range 32 -> 126
"""
def ceasar_cipher(s, shift, decrypt=False):
	shift = -shift if decrypt else shift
	ccipher = ""
	for ch in s:
		if(ch.isalpha()):
			if (ch.isupper()):
				ccipher += chr((ord(ch) + shift - 65) % 26 + 65)
			else:
				ccipher += chr((ord(ch) + shift - 97) % 26 + 97)
		elif(ch.isdigit()):
			ccipher += chr((ord(ch) + shift - 48) % 10 + 48)
		else:
			"""
			SPECIAL CHARS RANGE:
			32 - 47,
			58 - 64
			91 - 96
			123-126
			"""
			#Specal Characters
			SCR = [tuple(x) for x in [range(32,47+1), range(58,64+1), range(91,96+1), range(123,126+1)]]
			z = ord(ch)
			for T in SCR:
				if(z in T):
					ccipher += chr((z + shift - T[0]) % len(T) + T[0])
					break

	return ccipher