from data import DICTIONARY, LETTER_SCORES

def load_words():
	l=[]
	f = open(DICTIONARY,'r')
	for x in f:
		l.append(x[:len(x)-2].upper())
	return l

def calc_word_value(l):
	p = []
	#print(l)
	for x in l:
		value = 0
		for i in x:
			try:
				value+=LETTER_SCORES[i]
			except KeyError:
				continue
		p.append([x,value])
	return p

def max_word_value(p):
	index = 0
	maxi = 0
	for i in range(len(p)):
		if maxi < p[i][1]:
			maxi = p[i][1]
			index = i
	print(p[index][0])		

if __name__ == "__main__":
	max_word_value(calc_word_value(load_words()));
	# run unittests to validate
