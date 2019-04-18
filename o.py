from random import randint
from auxiliar import *

class RSA():
	"""docstring for RSA"""

	@staticmethod
	def setup():
		while 1:
			p = randint(2,50);
			q = randint(2,50);
			if primo(p) and primo(q) and p != q and p*q > 122:
				break
		n = p*q
		totiente = (p-1) * (q-1)
		f = open("formador_das_chaves.txt", 'w')
		linha = str(p) + "\n" + str(q)
		f.write(linha)
		f.close()
		#print(p,q,n,totiente)
		while 1:
			e = randint(2,totiente);
			if mdc(e,totiente) == 1:
				break
		#print(p,q,n,totiente,e)
		f = open("chavepublica.txt", 'w')
		linha = str(n) + "\n" + str(e)
		f.write(linha)
		f.close()
		return (n,e)

	@staticmethod
	def encrypt(mensagem,chave_publica):
		mensagem_nova = ""
		for i in mensagem:
			mensagem_nova += str((inteiro(i) ** chave_publica[1]) % chave_publica[0]) + " "
		f = open("mensagem_criptografada.txt", 'w')
		f.write(mensagem_nova)
		f.close()

	@staticmethod
	def decrypt(mensagem):
		f = open("formador_das_chaves.txt", "r")
		chave = list(map(int, f.read().split()))
		f.close()
		toti = (chave[0]) * (chave[1])

		f = open("chavepublica.txt", "r")
		chave = list(map(int, f.read().split()))
		f.close()

		e = int(chave[1])
		d = inverseMod(e,toti)

		mensagem_nova = ''
		print(mensagem)
		for i in mensagem:
			print((i**d) % chave[0])
			mensagem_nova += convertToChar((i**d) % chave[0])
		print(mensagem_nova)
		f = open("mensagem_Descriptografada.txt", 'w')
		f.write(mensagem_nova)
		f.close()
		
		
linha = [];
a = RSA()
a.encrypt("teste",a.setup())
f = open("mensagem_criptografada.txt", 'r')
mensagem = list(map(int, f.read().split()))
a.decrypt(mensagem)