#MinimoChallenge
#Luigi Corradi

import pandas as pd

#Lendo os csv
cod_cep = pd.read_csv('codigo-por-cep.csv', sep =';')
p_cod_w = pd.read_csv('preco-por-codigo-e-peso.csv', sep =';')
p_cod_w['codigo-regiao'] = p_cod_w['codigo-regiao'].str.strip()
p_cod_w['peso-maximo'] = p_cod_w['peso-maximo'].str.replace(',', '.')

#Custo do Frete
def PrecoFrete(CEP,peso):
	CEP = int(CEP)
	peso = peso.replace(',', '.')
	df = cod_cep[cod_cep["CEP Inicial"]<=CEP]
	df2 = df[df['CEP Final']>=CEP]
	cod = df2['Geografia Comercial'].iloc[0]
	df3 = p_cod_w[p_cod_w['codigo-regiao'] == cod]
	lista_peso = df3['peso-maximo'].tolist()

	if peso in lista_peso:
		df4 = df3[df3['peso-maximo'] == peso]
		preco = df4['preco'].iloc[0]
		return preco
	else:
		for i in lista_peso:
			p = float(i)
			Peso = float(peso)/1000
			if Peso<p:
				linha  = i
				break
			else:
				continue
		df4 = df3[df3['peso-maximo'] == linha]
		preco = float(df4['preco'].iloc[0].replace(',', '.'))
		return preco


#Custo de Logistica
#parametros simulação
#preços
#packing
p_pa = 5.72 #[R$/pedido]
#picking
p_pi = 0.28 #[R$/produto]
#volume
p_v = 49.98 #[R$/m3]
#peso(weight)
p_w = 0.91 #[R$/Kg]

def PrecoLogistica(larg,prof,alt,peso,qtd):
	larg = larg.replace(',', '.')
	larg = float(larg)
	prof = prof.replace(',', '.')
	prof = float(prof)
	alt = alt.replace(',', '.')
	alt = float(alt)
	peso = peso.replace(',', '.')
	peso = float(peso)/1000
	qtd = qtd.replace(',', '.')
	qtd = float(qtd)
	vol = larg*prof*alt
	preco = p_pa + p_pi*qtd + p_v*vol +p_w*peso
	return preco

#pedindo input pro usuario
print('informe os valores [somente numeros]')
largura = input("informe a largura [m]: ")
profundidade = input("informe a profundidade [m]: ")
altura = input("informe a altura [m]: ")
peso = input("informe o peso [g]: ")
qtd = input("informe a quantidade [un]: ")
CEP = input("informe o CEP: ")

#caso 1
# largura = '0,2'
# profundidade = '0,2'
# altura = '0,3'
# peso = '250'
# qtd = '2'
# CEP = '05612050'

#caso 2
# largura = '0,4'
# profundidade = '0,2'
# altura = '0,5'
# peso = '1200'
# qtd = '3'
# CEP = '04520010'

#caso 3
# largura = '1'
# profundidade = '1'
# altura = '0,5'
# peso = '2000'
# qtd = '1'
# CEP = '07115000'


preco = PrecoFrete(CEP,peso) + PrecoLogistica(largura,profundidade,altura,peso,qtd)
print(f'O preço do pedido é de R$ {preco}')