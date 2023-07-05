# Removendo Caracteres Duplicados
def letrasDuplas(string):
    letras = '' # Espaço entre os caracteres.
    for char in string:
        if char not in letras:
            letras += char # Se o caractere não for repetido imprima.
    return letras

palavraDupla = "PricewaterhouseCoopers."  # Antigo nome da PWC.
letras = letrasDuplas(palavraDupla)
print(letras)
