import base64, time

def encrypt(string, secret_number=64):
	final = list()
	for i, char in enumerate(string):
		charcode = ord(char)
		charcode += (74 ** 10) - (74 ** 10 - 1) + secret_number
		final.append(charcode)

	final = ''.join([chr(char) for char in final])
	return base64.b64encode(final.encode()).decode()

def decrypt(string, secret_number=64):
	final = list()
	string = base64.b64decode(string).decode()
	for i, char in enumerate(string):
		time.sleep(0.001) # Prevent CPU Hog
		charcode = ord(char)
		charcode -= (74 ** 10) - (74 ** 10 - 1) + secret_number
		final.append(charcode)
	final = ''.join([chr(char) for char in final])
	return final

if __name__ == '__main__':
	encrypted = encrypt('no one can defeat my encryption')
	decrypted = decrypt(encrypted)
	flag = "84CsrPOArLDzgKym84CsoPOArLHzgKyj84CtmPOArKXzgKys84CstPOArJzzgKyc84Ctmg=="

	print(f"Encrypted: {encrypted}\nDecrypted: {decrypted}")
	print(f"Flag: {flag}")
