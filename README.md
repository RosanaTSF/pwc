Challenge 1
Manipulação de Strings.
Criei um input (tipo spring) para o usuário digitar uma verso. 
Separei as palavras da frase numa lista usando o comando split.
Usando a sintaxe de slicing ::-1, inverti a ordem dos elementos na lista de palavras.
Com o join() juntei as palavras revertidas em uma única string, com espaço " " como separador entre as palavras.

Challenge 2
Removendo Caracteres Duplicados.
O código implementa uma função chamada letrasDuplas.
Ele itera por cada caractere e cria uma nova string com caracteres únicos.
O for char in string, itera por cada caractere da string de entrada.
O if char not in letras, verifica se o caractere já existe.
letras += char, adiciona o caractere à string letras.

Challenge 3
Verificando Palíndromo
O código implementa uma função chamada palindromo que verifica se uma string é um palíndromo. 
Ele remove os espaços em branco e converte a string para letras minúsculas. 
Em seguida, compara se a string original é igual à sua versão invertida. 
Se forem iguais, a função retorna True, indicando que a string é um palíndromo. 
Caso contrário, retorna False.

Principais comandos utilizados:
string = string.replace(" ", "").lower(): Remove os espaços em branco e converte a string para letras minúsculas.
if string == string[::-1]: Compara se a string original é igual à sua versão invertida.
print(f"A ave '{ave}' é um palíndromo."): Imprime uma mensagem indicando que a string é um palíndromo.
print(f"A ave '{ave}' não é um palíndromo."): Imprime uma mensagem indicando que a string não é um palíndromo.
[::-1]: Utiliza a sintaxe [:: -1] para inverter a string. A primeira parte (:) indica o início, a segunda parte (:) indica o fim e a terceira parte (-1) percorre a string de trás para frente.

Challenge 4
O código frase como entrada do usuário, converte a primeira letra de cada palavra para maiúscula usando o método title(), e imprime a frase com as letras maiúsculas na tela.

Principais comandos Utilizados:

frase = input("Digite uma frase: "): Solicita ao usuário que digite uma frase e armazena o valor digitado na variável frase.
maiusculo = frase.title(): Converte a primeira letra de cada palavra na frase para maiúscula usando o método title() 
e armazena o resultado na variável maiusculo.

