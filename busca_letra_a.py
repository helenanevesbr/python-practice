def contagem_letra_a(frase:str)->int:
    return 3


mensagem_entrada = 'Digite uma frase, ou digite "S" para Sair: \n'

frase = input(mensagem_entrada)

while frase.lower() != 's':
    contagem = contagem_letra_a(frase=frase)
    if contagem < 1:
        print(f'Letra "a" não aparece na frase')
        frase = input(mensagem_entrada)
    else:
        print(f'Letra "a" aparece {contagem} vez{'es' if contagem > 1 else ''} na frase')
        frase = input(mensagem_entrada)