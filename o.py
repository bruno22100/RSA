from random import randint
import math #vai ficar nas funções uteis

def inteiro(a):
	if a == " ":
		return 32
	else:
		return ord(a) - 65

def expmod(a, b, n):	
	if b == 0:
		return 1;
	else:
		res = expmod(a, b/2, n);
		res = (res*res) % n;
		if b%2 == 1:
			res = (res*a) % n;
		return res;


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

	@staticmethod
	def encrypt(mensagem,chave_publica):
		mensagem_nova = ""
		for i in mensagem:
			mensagem_nova += str((inteiro(i)**chave_publica[0])%chave_publica[1]) + ' '
		f = open("NewMensage.txt", 'w')
		f.write(mensagem_nova)
		f.close()


linha = [];
a = RSA()
a.encrypt("teste",a.setup(linha))