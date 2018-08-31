from io import open

total_cadeiras = 29
QE = 12684

class politico:
    def __init__(self,num, nom, par_col, vot):
        self.numero = num
        self.nome = nom
	self.part_colig = par_col
	self.votos = vot

dados = []

with open("eleicao.csv", encoding="utf-8") as f:
	f.readline()
	for line in f:
        	print(line.decode)
		dados.append(line)
	f.close()


		
		



f = open('workfile.tsv', 'w')
for i in dados:
	f.write(i)
	
