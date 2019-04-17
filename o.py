from random import randint
import math #vai ficar nas funções uteis


"""verifica se o numero é primo"""
def primo(a):
	tam = int(math.sqrt(a));
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

class RSA():
	"""docstring for RSA"""
	"""def __init__(chave_publica,chave_privada):
		self.chave_publica = chave_publica;
		self.chave_privada = chave_privada;"""

	@staticmethod
	def setup(lista):
		while 1:
			p = randint(2,102);
			q = randint(2,102);
			if primo(p) and primo(q) and p != q:
				break
		n = p*q
		totiente = (p-1) * (q-1)
		print(p,q,n,totiente)
		while 1:
			e = randint(2,totiente);
			if mdc(e,totiente) == 1:
				break
		print(p,q,n,totiente,e)
		return (n,e)
		

linha = [];
a = RSA()
a.setup(linha);