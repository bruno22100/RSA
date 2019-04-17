from random import randint
from auxiliar import *

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
			mensagem_nova += str((inteiro(i) ** chave_publica[0]) % chave_publica[1]) + " "
		f = open("mensagem_criptografada.txt", 'w')
		f.write(mensagem_nova)
		f.close()


linha = [];
a = RSA()
a.encrypt("teste",a.setup(linha))