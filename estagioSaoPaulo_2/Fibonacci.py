class Fibonacci:
    def __init__(self):
        self.sequencia = [0, 1]

    def gerar_sequencia(self, n):
        while self.sequencia[-1] < n:
            proximo_valor = self.sequencia[-1] + self.sequencia[-2]
            self.sequencia.append(proximo_valor)

    def pertence_a_sequencia(self, n):
        self.gerar_sequencia(n)
        if n in self.sequencia:
            return f"O número {n} pertence à sequência de Fibonacci."
        else:
            return f"O número {n} não pertence à sequência de Fibonacci."

# Número a verificar

def Numero_verifica():  
    numero = input("Informe um número: ")
    if numero.isnumeric():
        numero=int(numero)
        fibonacci = Fibonacci()
        print(fibonacci.pertence_a_sequencia(numero))
    else:
        print("Não é numero")
        Numero_verifica()

Numero_verifica()