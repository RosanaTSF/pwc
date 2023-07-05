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