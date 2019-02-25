array = [ ]
import requests
import pandas as pd
import csv
import re

request = requests.get('https://www.receitaws.com.br/v1/cnpj/16501555000157')

print(request)
data = request.json()
del data ['qsa']
del data ['atividade_principal']
del data ['atividades_secundarias']
del data ['billing']
del data ['data_situacao']
del data ['complemento']
del data ['uf']
del data ['telefone']
del data ['email']
del data ['situacao']
del data ['bairro']
del data ['logradouro']
del data ['numero']
del data ['cep']
del data ['municipio']
del data ['porte']
# del data ['abertura']
del data ['natureza_juridica']
del data ['ultima_atualizacao']
del data ['status']
del data ['tipo']
del data ['fantasia']
del data ['efr']
del data ['motivo_situacao']
del data ['situacao_especial']
del data ['data_situacao_especial']
del data ['extra']




array.append(data)

# array.append({
#         'DATA_ABERTURA': re.sub(r'[^\w]', ' ',data ['abertura']),
#         'CAPITAL_SOCIAL': re.sub(r'[^\w]', ' ',data ['capital_social']),
#         'CNPJ': re.sub(r'[^\w]', ' ',data ['cnpj']),
#         'NOME': re.sub(r'[^\w]', ' ',data ['nome'])

#     })
################################################################
request = requests.get('https://www.receitaws.com.br/v1/cnpj/14994237000140')
print(request)
data = request.json()
del data ['qsa']
del data ['atividade_principal']
del data ['atividades_secundarias']
del data ['billing']
del data ['data_situacao']
del data ['complemento']
del data ['uf']
del data ['telefone']
del data ['email']
del data ['situacao']
del data ['bairro']
del data ['logradouro']
del data ['numero']
del data ['cep']
del data ['municipio']
del data ['porte']
# del data ['abertura']
del data ['natureza_juridica']
del data ['ultima_atualizacao']
del data ['status']
del data ['tipo']
del data ['fantasia']
del data ['efr']
del data ['motivo_situacao']
del data ['situacao_especial']
del data ['data_situacao_especial']
del data ['extra']


array.append(data)

# array.append({
#         'DATA_ABERTURA': re.sub(r'[^\w]', ' ',data ['abertura']),
#         'CAPITAL_SOCIAL': re.sub(r'[^\w]', ' ',data ['capital_social']),
#         'CNPJ': re.sub(r'[^\w]', ' ',data ['cnpj']),
#         'NOME': re.sub(r'[^\w]', ' ',data ['nome'])

#     })

####################################################################
request = requests.get('https://www.receitaws.com.br/v1/cnpj/18727053000174')
print(request)
data = request.json()
del data ['qsa']
del data ['atividade_principal']
del data ['atividades_secundarias']
del data ['billing']
del data ['data_situacao']
del data ['complemento']
del data ['uf']
del data ['telefone']
del data ['email']
del data ['situacao']
del data ['bairro']
del data ['logradouro']
del data ['numero']
del data ['cep']
del data ['municipio']
del data ['porte']
# del data ['abertura']
del data ['natureza_juridica']
del data ['ultima_atualizacao']
del data ['status']
del data ['tipo']
del data ['fantasia']
del data ['efr']
del data ['motivo_situacao']
del data ['situacao_especial']
del data ['data_situacao_especial']
del data ['extra']


array.append(data)

# array.append({
#         'DATA_ABERTURA': re.sub(r'[^\w]', ' ',data ['abertura']),
#         'CAPITAL_SOCIAL': re.sub(r'[^\w]', ' ',data ['capital_social']),
#         'CNPJ': re.sub(r'[^\w]', ' ',data ['cnpj']),
#         'NOME': re.sub(r'[^\w]', ' ',data ['nome'])

#     })


##SALVAR DADOS NO CSV
# Create a Pandas dataframe from some data.
df = pd.DataFrame(array)
df.to_csv('Desafio_1.csv', sep=';', encoding='utf-8')

########################SALVAR DADOS NO XLSX
# Create a Pandas dataframe from some data.
#df = pd.DataFrame(array)

# Create a Pandas Excel writer using XlsxWriter as the engine.
#writer = pd.ExcelWriter('Desafio_1.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
#df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
#writer.save()







