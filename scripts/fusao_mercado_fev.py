import json
import csv

from processamento_dados import Dados

# def leitura_json(path_json):
#     dados_json = []
#     with open(path_json, 'r', encoding='utf-8') as file:
#         dados_json = json.load(file)
    
#     return dados_json

# def leitura_csv(path_csv):
#     dados_csv = []
#     with open(path_csv, 'r', encoding='utf-8') as file:
#         spamreader = csv.DictReader(file, delimiter=',')
#         for row in spamreader:
#             dados_csv.append(row)
    
#     return dados_csv

# def leitura_dados(path, tipo_arquivo):
#     dados = []

#     if tipo_arquivo == "csv":
#         dados = leitura_csv(path)
    
#     elif tipo_arquivo == "json":
#         dados = leitura_json(path)
    
#     return dados

# def get_columns(dados):
#     return list(dados[-1].keys())

# def rename_columns(dados, key_mapping):
#     new_dados_csv = []

#     for old_dict in dados_csv:
#         dict_temp = {}
#         for old_key, value in old_dict.items():
#             dict_temp[key_mapping[old_key]] = value
#         new_dados_csv.append(dict_temp)
    
#     return new_dados_csv

# def size_data(dados):
#     return len(dados)

# def join(dadosA, dadosB):
#     combined_list = []
#     combined_list.extend(dadosA)
#     combined_list.extend(dadosB)
    
#     return combined_list

def transformando_dados_tabelas(dados, nomes_colunas):
    dados_combinados_tabela = [nomes_colunas]

    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)
    
    return dados_combinados_tabela

def salvando_dados(dados, path):
    with open(path_dados_combinados, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

# Iniciando Leitura
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract

dados_empresaA = Dados(path_json, 'json')
print(f"Empresa A {dados_empresaA.nome_colunas}")
print(f"quantidade de linhas empresa A {dados_empresaA.qtde_linhas}")

dados_empresaB = Dados(path_csv, 'csv')
print(f"Empresa B {dados_empresaB.nome_colunas}")
print(f"quantidade de linhas empresa B {dados_empresaB.qtde_linhas}")

# Transformação

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(f"Novos nomes das colunas da Empresa B {dados_empresaB.nome_colunas}")

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"Dados após fusão das empresas {dados_fusao.nome_colunas}")
print(f"quantidade de linhas após fusão dos dados {dados_fusao.qtde_linhas}")

# Carregamento dos dados
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)


# dados_json = leitura_dados(path_json, 'json')
# print(f"Json: {dados_json[0]}")

# nome_colunas_json = get_columns(dados_json)
# print(f"colunas json: {nome_colunas_json}")

# dados_csv = leitura_dados(path_csv, 'csv')
# print(f"Csv: {dados_csv[0]}")

# tamanho_dados_json= size_data(dados_json)
# print(f"tamanho dos dados json: {tamanho_dados_json}")

# nome_colunas_csv = get_columns(dados_csv)
# print(f"colunas csv: {nome_colunas_csv}")

# tamanho_dados_csv = size_data(dados_csv)
# print(f"tamanho dos dados csv: {tamanho_dados_csv}")

# Transformação dos dados

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}


# dados_csv = rename_columns(dados_csv, key_mapping)
# nome_colunas_csv = get_columns(dados_csv)
# print(f"Novo nome das colunas csv: {nome_colunas_csv}")

# dados_fusao = join(dados_json, dados_csv)
# nome_colunas_fusao = get_columns(dados_fusao)
# tamanho_dados_fusao = size_data(dados_fusao)
# print(f"o nome das colunas dos dados combinados são: {nome_colunas_fusao}")
# print(f"o tamanho total dos dados combinados é: {tamanho_dados_fusao}")

# Salvando os dados
# dados_fusao_tabela = transformando_dados_tabelas(dados_fusao, nome_colunas_fusao)

# path_dados_combinados = 'data_processed/dados_combinados.csv'

# salvando_dados(dados_fusao_tabela, path_dados_combinados)
# print(path_dados_combinados)
