import csv

dados = []

with open('eleicao.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    for row in readCSV:
        print row
	dados.append(row)

f = open('workfile.tsv', 'w')
f.write(dados)
