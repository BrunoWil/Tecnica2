import pandas as pd

class FaturamentoDistribuidora:
    def __init__(self, dados):
        #-> DataFrame com os dados de faturamento
        self.Dados = pd.DataFrame(dados)
    
    def calcularPercentuais(self):
        #-> Calcular o faturamento total
        faturamentoTotal = self.Dados['Faturamento'].sum()
        
        #-> Calcular o percentual de representação de cada estado
        self.Dados['Percentual(%)'] = ((self.Dados['Faturamento'] / faturamentoTotal) * 100).round(2)
    
    def exibirResultados(self):
        #-> Exibir o DataFrame com os percentuais
        print(self.Dados)

#-> Dados de faturamento por estado
dadosFaturamento = {
    'Estado': ['SP', 'RJ', 'MG', 'ES', 'Outros'],
    'Faturamento': [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
}

#-> Criar uma instância da classe e calcular os percentuais
distribuidora = FaturamentoDistribuidora(dadosFaturamento)
distribuidora.calcularPercentuais()
distribuidora.exibirResultados()




class FaturamentoDistribuidora:
    def __init__(self, faturamentoEstados):
        self.faturamentoEstados = faturamentoEstados
        self.faturamentoTotal = self.calcularFaturamentoTotal()

    #-> Calcular o faturamento total
    def calcularFaturamentoTotal(self):
        return sum(self.faturamentoEstados.values())

    #-> Calcular o percentual de cada estado
    def calcularPercentualEstados(self):
        percentualEstados = {}
        for estado, valor in self.faturamentoEstados.items():
            percentual = (valor / self.faturamentoTotal) * 100
            percentualEstados[estado] = percentual
        return percentualEstados

    #-> Método para exibir o resultado
    def exibirPercentualEstados(self):
        percentualEstados = self.calcularPercentualEstados()
        print("Percentual de representação de cada estado:")
        for estado, percentual in percentualEstados.items():
            print(f"{estado}: {percentual:.2f}%")

#-> Exemplo de uso
faturamentoEstados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

#-> Instancia a classe e executa o cálculo
faturamento_distribuidora = FaturamentoDistribuidora(faturamentoEstados)
print("\t")
faturamento_distribuidora.exibirPercentualEstados()
