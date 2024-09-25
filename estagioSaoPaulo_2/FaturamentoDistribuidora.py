

################METODO PANDAS################
import pandas as pd


class FaturamentoMensal:
    def __init__(self, arquivo_json):

        self.df = pd.read_json(arquivo_json)  #-> JSON em um DataFrame;
        self.dfValidos = self.df[self.df['valor'] > 0] #-> Filtra apenas os dias sem faturamento;

    def menorFaturamento(self):

        valorMinimo = self.dfValidos['valor'].min()
        return valorMinimo  #-> Retorna o menor valor de faturamento ocorrido em um dia do mês;

    def maiorFaturamento(self):

        valorMaximo = self.dfValidos['valor'].max()
        return valorMaximo  #-> Retorna o maior valor de faturamento ocorrido em um dia do mês;

    def mediaFaturamento(self):

        valorMedio = self.dfValidos['valor'].mean()
        return valorMedio  #-> Retorna a média mensal de faturamento;

    def diasAcimaDaMedia(self):

        valorMedio = self.mediaFaturamento()
        valorAcimaDaMedia = self.dfValidos[self.dfValidos['valor']
                                           > valorMedio].shape[0]
        return valorAcimaDaMedia  #-> Retorna o número de dias com faturamento superior à média;


#-> Instaciamento de classe;
faturamentoMensal = FaturamentoMensal(r'dados.json')

#-> Resultados obtidos
print(f"Menor valor de faturamento: {faturamentoMensal.menorFaturamento()}")
print(f"Maior valor de faturamento: {faturamentoMensal.maiorFaturamento()}")
print(f"Número de dias com faturamento superior à média: {faturamentoMensal.diasAcimaDaMedia()}")




################METODO CALCULO################ 
import json

class FaturamentoMensals:
    def __init__(self, arquivo_json):
        
        with open(arquivo_json, 'r') as f: #-> JSON ao instanciar a classe
            self.faturamento = json.load(f)
        self.faturamentoValidos = [dia['valor'] for dia in self.faturamento if dia['valor'] > 0] #-> Filtra os dias com faturamento maior que zero 

    def menorFaturamento(self):
        valorMin = min(self.faturamentoValidos)
        return valorMin #-> Retorna o menor valor de faturamento

    def maiorFaturamento(self):
        valorMax = max(self.faturamentoValidos)
        return valorMax #-> Retorna o maior valor de faturamento

    def mediaFaturamento(self):
        valorMedio = sum(self.faturamentoValidos) / len(self.faturamentoValidos)
        return valorMedio #-> Calcula e retorna a média dos valores de faturamento

    def faturamentoDiasAcimaDaMedia(self):
        
        media = self.mediaFaturamento() 
        valorAcima = sum(1 for valor in self.faturamentoValidos if valor > media)
        return valorAcima #-> Conta o número de dias com faturamento superior à média

#-> Uso da classe
faturamentoMensals = FaturamentoMensals('dados.json')

#-> Resultados
print(f"\t")
print(f"Menor valor de faturamento: {faturamentoMensals.menorFaturamento()}")
print(f"Maior valor de faturamento: {faturamentoMensals.maiorFaturamento()}")
print(f"Número de dias com faturamento superior à média: {faturamentoMensals.faturamentoDiasAcimaDaMedia()}")
