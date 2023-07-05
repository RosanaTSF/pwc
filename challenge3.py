# Verificar Palíndromo
def palindromo(string):
    
    string = string.replace(" ", "").lower() #replace remove os espaços em branco e lower converte para minúsculas.

    if string == string[::-1]: 
        return True 
    else:
        return False 

ave = "arara"

resultado = palindromo(ave)

if resultado:
    print(f"A ave '{ave}' é um palíndromo.")
else:
    print(f"A ave '{ave}' não é um palíndromo.")


# Sintaxe [:: -1] possui três partes separadas pelo operador:
# A primeira(:): começa o primeiro elemento.
# A segunda(:): está indo até o último.
# A terceira parte (-1): percorre de trás para frente.