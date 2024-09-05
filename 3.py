import json

def analise() -> list:
    with open('Target Systems/dados.json', 'r') as json_file:
        dados = json.load(json_file)
   
        
    valor_min = min(dado['valor'] for dado in dados if dado['valor'] != 0)
    valor_max = max(dado['valor'] for dado in dados)
    
    count = len([dado for dado in dados if dado['valor'] > 0])
    soma = sum(dado['valor'] for dado in dados)
    media = soma/count
    dias_maior_media = len([dado for dado in dados if dado['valor'] > media])
    
    return [valor_min, valor_max, dias_maior_media]

if __name__ == '__main__':
    min, max, dias = analise()
    print(f"O menor faturamento foi de {min}.\nO maior faturamento foi de {max}.\nO número de dias em que o faturamento foi maior que a média é {dias}.")