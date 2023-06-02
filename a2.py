import pandas as pd


AUTORES = ['Daniel de Miranda Almeida', 'Luís Felipe de Abreu Marciano']

def decodifica_estados(df):
    
    # dicionario com as siglas dos estados para decodificação
    dicionario_estados = {12: 'AC', 27: 'AL', 16: 'AP', 13: 'AM', 29: 'BA', 23: 'CE', 53: 'DF', 32: 'ES', 52: 'GO', 21: 'MA', 51: 'MT', 50: 'MS', 31: 'MG', 15: 'PA', 25: 'PB', 41: 'PR', 26: 'PE', 22: 'PI', 24: 'RN', 43: 'RS', 33: 'RJ', 11: 'RO', 14: 'RR', 42: 'SC', 35: 'SP', 28: 'SE', 17: 'TO'}
    # mudando os indices da series para as siglas dos estados
    df.rename(index = dicionario_estados, inplace = True)

    print(df)

    return df

def questao_1(datapath):
    # recebendo database
    df = pd.read_csv(datapath)
    # retornando quantidade de linhas
    return len(df.index)

def questao_2(datapath):
    # recebendo database
    df = pd.read_csv(datapath)
    # agrupando por muncipio e retornando a coluna ID_AGRAVO, que
    # como é sempre não nula, pode ser usada para contar o número
    # de casos por município
    return df.groupby(["ID_MUNICIP"])["ID_AGRAVO"].count()

def questao_3(datapath):
    # recebendo database
    df = pd.read_csv(datapath)
    
    # retorna uma series que é transformada em dicionario
    dicionario_sexo = dict(df.groupby(["CS_SEXO"])["ID_AGRAVO"].count())
    # pega a chave que tem o maior valor em todo o dicionário
    sexo_mais_frequente = max(dicionario_sexo, key=dicionario_sexo.get)
    # retornando tupla    
    return (sexo_mais_frequente, dicionario_sexo)


def questao_4(datapath):
    # recebendo database
    df = pd.read_csv(datapath)
    
    # pegando a média da coluna idade_anos
    return df["idade_anos"].mean()

def questao_5(datapath):
    # recebendo database
    df = pd.read_csv(datapath)
    
    # agrupando quantidade de casos por estado
    series_estados = df.groupby(["SG_UF_NOT"])["ID_AGRAVO"].count()
    
    # decodificando estados
    series_estados = decodifica_estados(series_estados)

    # transformando em dicionario a series
    return dict(series_estados)

def questao_6(datapath):
    # recebendo database
    df = pd.read_csv(datapath)
    
    # retirando qualquer sexo diferente de M do dataframe
    series_estados = df[df.CS_SEXO == "M"]

    # agrupando quantidade de casos por estado
    series_estados = series_estados.groupby(["SG_UF_NOT"])["ID_AGRAVO"].count()

    series_estados = decodifica_estados(series_estados)

    return dict(series_estados)

def questao_7():
    pass

def questao_8():
    pass

def questao_9():
    pass

def questao_10():
    pass

print(questao_6("Raiva_Humana_2021.csv"))