import pandas as pd
import requests 

array = []

request = requests.get('https://www.receitaws.com.br/v1/cnpj/16501555000157')

print(request)

data = request.json()

cnpj = data ['cnpj']

for atividade_principal in data ['atividade_principal']:
    array.append({
        'cnpj': cnpj,
        'code': atividade_principal['code'],
        'text': atividade_principal['text']
    })

request = requests.get('https://www.receitaws.com.br/v1/cnpj/14994237000140')

print(request)

data = request.json()

cnpj = data ['cnpj']

for atividade_principal in data ['atividade_principal']:
    array.append({
        'cnpj': cnpj,
        'code': atividade_principal['code'],
        'text': atividade_principal['text']
    })


request = requests.get('https://www.receitaws.com.br/v1/cnpj/18727053000174')

print(request)

data = request.json()

cnpj = data ['cnpj']

for atividade_principal in data ['atividade_principal']:
    array.append({
        'cnpj': cnpj,
        'code': atividade_principal['code'],
        'text': atividade_principal['text']
    })

df = pd.DataFrame(array)
df.to_csv('AtividadePrincipalComCNPJ_1.csv', sep=';', encoding='utf-8')

# ##SALVAR DADOS NO XLSX
# # Create a Pandas dataframe from some data.
# df = pd.DataFrame(array)

# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('AtividadePrincipalComCNPJ_1.xlsx', engine='xlsxwriter')

# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1')

# # Close the Pandas Excel writer and output the Excel file.
# writer.save()
