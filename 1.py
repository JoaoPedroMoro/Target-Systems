def funcao_soma() -> int:
    indice = 13
    soma, k = 0, 0
    for i in range(indice):
        k += 1
        soma += k
    return soma

if __name__ == '__main__':
    print(funcao_soma())