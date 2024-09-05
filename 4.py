def representacao() -> None:
    valores = [
        {'estado': 'SP', 'valor': 67836.43},
        {'estado': 'RJ', 'valor': 36678.66},
        {'estado': 'MG', 'valor': 29229.88},
        {'estado': 'ES', 'valor': 27165.48},
        {'estado': 'Outros', 'valor': 19849.53},
    ]
    
    total = sum(dado['valor'] for dado in valores)

    for dado in valores:
        print(f"Estado: {dado['estado']} - Porcentagem do valor total: {dado['valor']*100/total:.2f}%")

if __name__ == '__main__':
    representacao()