# Manipulação de Strings
string = input ("Digite um verso: ");
verso = string.split(); # Divide a string em uma lista de palavras.
inverso =  verso [::-1]; # Usando a sintaxe de slicing [::-1], inverte a ordem dos elementos na lista de palavras.
stringInversa = " ".join(inverso); # join() junta as palavras revertidas em uma única string, com espaço " " como separador entre as palavras.
print("String invertida:", stringInversa);
