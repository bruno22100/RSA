"""tranforma para inteiro um char"""
def inteiro(a):
	if a == " ":
		return 26
	return ord(a)

def convertToChar(a):
    if a==26:
    	return " "
    return  chr(a)

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

def inverseMod(a, b):
    a = a%b
    for i in range(1, b):
        if(i*a)%b == 1: return i
    return  1