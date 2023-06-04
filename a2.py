import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

def questao_7(datapath):
    # recebendo database
    df = pd.read_csv(datapath)
    
    dicionario_municipios_estados = {'MG': 853, 'SP': 645, 'RS': 497, 'BA': 417, 'PR': 399, 'SC': 295, 'GO': 246, 'PI': 224, 'PB': 223, 'MA': 217, 'PE': 184, 'CE': 184, 'RN': 167, 'PA': 144, 'MT': 141, 'TO': 139, 'AL': 102, 'RJ': 92, 'MS': 79, 'ES': 78, 'SE': 75, 'AM': 62, 'RO': 52, 'AC': 22, 'AP': 16, 'RR': 15}

    # fazendo contagem de número de municipios com casos por estado e transformando em dataframe
    df_contagem_estados = pd.DataFrame(df.groupby(["SG_UF_NOT"])["ID_MUNICIP"].nunique())

    # decodficando os estados
    df_contagem_estados = decodifica_estados(df_contagem_estados)

    # retirando distrito federal, pois não é um estado
    df_contagem_estados.drop("DF", inplace = True)

    # compara o dataframe com o dicionário e adiciona os valores do dicionário em uma colun do dataframe fazendo a correpondência entre o index do dataframe e a chave do dicionário
    df_contagem_estados["n_municipios"] = [dicionario_municipios_estados.get(index) for index in df_contagem_estados.index]

    # adicionando coluna com  proporção de municipios
    df_contagem_estados["proporcao_municipios"] = round((df_contagem_estados["ID_MUNICIP"]/df_contagem_estados["n_municipios"] * 100))

    # criando e retornando dicionario
    return dict(zip(df_contagem_estados.index, df_contagem_estados["proporcao_municipios"]))

def questao_8(datapath):
    # recebendo database
    df = pd.read_csv(datapath)
    
    df["data_notificacao"] = pd.to_datetime(df["DT_NOTIFIC"])
    df["data_sintomas"] = pd.to_datetime(df["DT_SIN_PRI"])
    df["ATRASO_NOT"] = (df["data_notificacao"] - df["data_sintomas"]) / np.timedelta64(1, "D")

    return df

def questao_9(datapath):
    # recebendo database
    df = pd.read_csv(datapath)

    df["data_notificacao"] = pd.to_datetime(df["DT_NOTIFIC"])
    df["data_sintomas"] = pd.to_datetime(df["DT_SIN_PRI"])
    df["ATRASO_NOT"] = (df["data_notificacao"] - df["data_sintomas"]) / np.timedelta64(1, "D")

    df_media = df.groupby(["SG_UF_NOT"])["ATRASO_NOT"].mean()
    df_desvio = df.groupby(["SG_UF_NOT"])["ATRASO_NOT"].std()

    # decodificando nomes dos estados
    decodifica_estados(df_media)

    # salvando medias e desvios em listas para colocar em tuplas no dicionário final
    lista_medias = list(df_media)
    lista_desvios = list(df_desvio)
    tupla_medias_desvios = tuple(zip(lista_medias, lista_desvios))

    dicionario_medias_desvios = dict(zip(df_media.index, tupla_medias_desvios))

    return dicionario_medias_desvios

def questao_10(datapath):
    # recebendo database
    df = pd.read_csv(datapath)
    
    df["data_notificacao"] = pd.to_datetime(df["DT_NOTIFIC"])
    df["data_sintomas"] = pd.to_datetime(df["DT_SIN_PRI"])
    df["ATRASO_NOT"] = (df["data_notificacao"] - df["data_sintomas"]) / np.timedelta64(1, "D")
    
    # criando dataframe com municipios e a media para cada um
    df_atraso_municipio = pd.DataFrame(df.groupby(["ID_MUNICIP"])["ATRASO_NOT"].mean())

    # adicionando coluna com o numero de notificacoes no dataframe
    df_atraso_municipio["n_notificacoes"] = df.groupby(["ID_MUNICIP"])["ID_AGRAVO"].count()

    # fazendo gráfico
    fig, plot_municipios = plt.subplots()
    # plotando valores
    return plot_municipios.scatter(df_atraso_municipio["ATRASO_NOT"], df_atraso_municipio["n_notificacoes"])