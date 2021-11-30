"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""


def remove_adjacent(nums):
    # +++ SUA SOLUÇÃO +++

    #Solução com otimização
    return [v for i, v in enumerate(nums) if nums[i] != nums[i - 1] or i == 0]


    #Minha solução sem otimização
    """"
    i = 0
    lista = []
    while i < len(nums):
        if not ((i != 0) and (nums[i] == nums[i - 1])): lista.append(nums[i])
        i += 1
    return lista
    """

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
    test(remove_adjacent, [2, 2, 3, 3, 4, 44, 3, 2, 2], [2, 3, 4, 44, 3, 2])
    test(remove_adjacent, [-1, -55, -6, -55, -55, -6], [-1, -55, -6, -55, -6])
