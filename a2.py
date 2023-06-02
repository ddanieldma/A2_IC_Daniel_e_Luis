import pandas as pd


AUTORES = ['Daniel de Miranda Almeida', 'Luís Felipe de Abreu Marciano']

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

def questao_3():
    pass


def questao_4():
    pass

def questao_5():
    pass

def questao_6():
    pass

def questao_7():
    pass

def questao_8():
    pass

def questao_9():
    pass

def questao_10():
    pass
