def inverter_string(texto) -> str:
    nova_string = ""
    for i in range(len(texto)):
        index = len(texto) - i - 1
        nova_string += texto[index]
    return nova_string


if __name__ == '__main__':
    texto = "Eu quero inverter isso!"
    print(f"String original: {texto}")
    print(f"String invertida: {inverter_string(texto)}")