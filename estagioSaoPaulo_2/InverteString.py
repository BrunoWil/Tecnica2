class StringInverter:
    def __init__(self, texto):
        self.texto = texto

    #-> Inverter a string
    def inverteString(self):
        invertidaString = ""
        for i in range(len(self.texto) - 1, -1, -1):
            invertidaString += self.texto[i]
        return invertidaString

    #-> Exibir a string invertida
    def exibirInvertidaString(self):
        invertidaString = self.inverteString()
        print(f"Invertida String: {invertidaString}")

#-> Uso
entradaTexto = input("Entrada de texto para Inverter: ")
inverter = StringInverter(entradaTexto)
inverter.exibirInvertidaString()
