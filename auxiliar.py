def inteiro(a):
	if a == " ":
		return 32
	else:
		return ord(a) - 65

"""verifica se o numero é primo"""
def primo(a):
	tam = int(a ** (1/2));
	#print(a,tam);
	while tam > 1:
		if a % tam == 0:
			return 0
		tam -= 1
	return 1

#print(primo(randint(0,100)))
def mdc(a,b):
	if a%b == 0:
		return b;
	return mdc(b,a%b)