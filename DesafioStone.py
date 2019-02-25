import requests
import re




request = requests.get('https://www.receitaws.com.br/v1/cnpj/16501555000157')


data = request.json()

print('CNPJ: {}'.format(data['cnpj']))
# print('NOME: {}'.format(data['nome']))
# print('DATA DE ABERTURA: {}'.format(data['abertura']))
# # print('ATIVIDADE PRINCIPAL: {}'.format(data['atividade_principal']))
# print('CAPITAL SOCIAL: {}'.format(data['capital_social']))
# # print('ACIONISTAS: {}'.format(data['qsa']))


print(re.sub(r'[^\w]', ' ', ('CNPJ: {}'.format(data['cnpj']))))
