from random import randint
import math

def primo(a):
	tam = int(math.sqrt(a));
	#print(a,tam);
	while tam > 1:
		if a % tam == 0:
			return 0
		tam -= 1
	return 1

print(primo(randint(0,100)))