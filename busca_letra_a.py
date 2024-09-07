def contagem_letra_a(texto:str)->int:
    return sum(1 for letra in texto if letra.lower() == 'a')


mensagem_entrada = 'Digite uma texto, ou digite "S" para Sair: \n'

texto = input(mensagem_entrada)

while texto.lower() != 's':
    contagem = contagem_letra_a(texto=texto)
    if contagem < 1:
        print(f'Letra "a" não aparece na frase')
        texto = input(mensagem_entrada)
    else:
        print(f'Letra "a" aparece {contagem} vez{'es' if contagem > 1 else ''} na frase')
        texto = input(mensagem_entrada)