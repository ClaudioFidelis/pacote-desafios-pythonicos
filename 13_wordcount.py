"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys
from collections import Counter

# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).

# Minha solução
"""
def ler_arquivo(filename, sort_desc):
    with open(filename, "r") as arquivo:
        str = arquivo.read()
    lista = sorted(str.lower().split())
    tupla = [(v, lista.count(v)) for i, v in enumerate(lista) if lista[i] != lista[i - 1] or i == 0]
    if sort_desc: tupla.sort(key=lambda x: x[1], reverse=True)
    return tupla

def print_words(filename):
    tupla = ler_arquivo(filename, False)
    for i in tupla: print(i[0], i[1])
    return True

def print_top(filename):
    tupla = ler_arquivo(filename, True)
    i = 0
    while i < len(tupla) and i < 20:
        print(tupla[i][0], tupla[i][1])
        i += 1
    return True
"""


# Solução otimizada copiada dos colegas
def print_words(filename):
    for word, count in count_words(filename).items():
        print(f'{word} : {count}')


def print_top(filename):
    for word, count in sorted(count_words(filename, 20).items(), key=lambda wordc: wordc[1], reverse=True):
        print(f'{word} : {count}')


def count_words(filename, slice=-1):
    stopwords = [" ", "\n", "\t", ".", ",", ";"]
    with open(filename) as f:
        return Counter([word.lower() for word in f.read() if word not in stopwords][:slice])

# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.


def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
