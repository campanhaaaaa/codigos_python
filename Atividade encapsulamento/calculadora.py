class Calculadora:

    def __init__(self):

        self.__num1 = 0
        self.__num2 = 0
    
    def somar(self, valor1, valor2):

        self.__num1 = valor1
        self.__num2 = valor2

        print(f"A soma é {self.__num1 + self.__num2}\n")

    def subtrir(self, valor1, valor2):

        self.__num1 = valor1
        self.__num2 = valor2

        print(f"A subtração é {self.__num1 - self.__num2}\n")

    def multiplicar(self, valor1, valor2):

        self.__num1 = valor1
        self.__num2 = valor2

        print(f"A multiplicação é {self.__num1 * self.__num2}\n")

    def dividir(self, valor1, valor2):

        self.__num1 = valor1
        self.__num2 = valor2

        print(f"A divisão é {self.__num1 / self.__num2}\n")




    


        


