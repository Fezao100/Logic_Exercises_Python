#Função para inverter string
def inverter_string(s):
    string_invertida = ""
    
    #Loop para inverter a string passando pelos caracteres do fim ao começo
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

entrada = input("Digite uma palavra para ser invertida: ")
print("Palavra invertida:", inverter_string(entrada))
