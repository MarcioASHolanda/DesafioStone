import pandas as pd
import requests 

array = []

request = requests.get('https://www.receitaws.com.br/v1/cnpj/13966572000171')

print(request)

data = request.json()

cnpj = data ['cnpj']

for acionistas in data ['qsa']:
    array.append({
        'cnpj': cnpj,
        'qual': acionistas['qual'],
        'nome': acionistas['nome']
    })

request = requests.get('https://www.receitaws.com.br/v1/cnpj/12839955000116')

print(request)

data = request.json()

cnpj = data ['cnpj']

for acionistas in data ['qsa']:
    array.append({
        'cnpj': cnpj,
        'qual': acionistas['qual'],
        'nome': acionistas['nome']
    })

request = requests.get('https://www.receitaws.com.br/v1/cnpj/16569357000125')

print(request)

data = request.json()

cnpj = data ['cnpj']

for acionistas in data ['qsa']:
    array.append({
        'cnpj': cnpj,
        'qual': acionistas['qual'],
        'nome': acionistas['nome']
    })


df = pd.DataFrame(array)
df.to_csv('Acionista_CNPJ_2.csv', sep=';', encoding='utf-8')


# ##SALVAR DADOS NO XLSX
# # Create a Pandas dataframe from some data.
# df = pd.DataFrame(array)

# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('Acionista_CNPJ_2.xlsx', engine='xlsxwriter')

# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1')

# # Close the Pandas Excel writer and output the Excel file.
# writer.save()