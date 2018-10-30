import crypt

def crackPassword(cryptPass):

	salt = cryptPass[0:2]

	passwords = open('dictionary.txt', 'r')
	for pwds in passwords.readlines():
		pwds = pwds.strip('\n')
		cryptPwds = crypt.crypt(pwds, salt)
		if (cryptPwds == cryptPass):
			print("Found Password: " + pwds)
	print("Password not Found")
	return


def main():
	passFile = open('') #Path of the file containing users and crypts
	for l in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print("Cracking password for: " + user)
			crackPassword(cryptPass)

if __name__ == "__main__":
	main()
