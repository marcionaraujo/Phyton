"""
Programa velocidade
Descrição: Fa¸ca um programa que pergunte a velocidade do carro do usu´arios. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usu´ario foi multado. Nesse caso, exiba o valor da multa, cobrando R $ 5,00 por km acima de 80km/h.
Autor: Márcio Nunes Araújo
Versão: 1
Data: 18/08/2022
"""

# Entrada de dados
velocidade = int(input('Qual a valocidade do carro (em Km/h)?'))

# Processamento de dados
mensagem = ''
multa = float(5 * (velocidade - 80))

if velocidade > 80:
    mensagem = f'Você foi multado em R$ {multa}) por trafegar a {velocidade}Km/h.'

# Saida de dados
print(mensagem)
