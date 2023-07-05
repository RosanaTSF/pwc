    # Anagrama de um Palindromo
def anagramaPalindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1] #inverte.

palavra = input ("Digite a palavra: ")

if anagramaPalindromo(palavra):
    print(f"{palavra} é um anagrama e também um palíndromo. True")
else:
    print(f"{palavra} não é um anagrama ou palíndromo. False")


