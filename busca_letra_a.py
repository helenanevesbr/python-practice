import re

def contagem_letra_a(texto:str)->int:
    return len(re.findall(r'[AaÁáÂâÃãÀà]', texto))

if __name__ == '__main__':
    mensagem_entrada = 'Digite um texto, ou digite "S" para Sair: \n'
    texto = input(mensagem_entrada)

    while texto.lower() != 's':
        contagem = contagem_letra_a(texto=texto)
        if contagem < 1:
            print(f'Letra "a" não aparece na frase')
            texto = input(mensagem_entrada)
        else:
            print(f'Letra "a" aparece {contagem} vez{'es' if contagem > 1 else ''} na frase')
            texto = input(mensagem_entrada)

