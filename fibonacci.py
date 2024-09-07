def e_fibonacci(numero_buscado: int) -> bool:
    ''' Calcula os números de Fibonacci e verifica se o número está na sequência '''

    if numero_buscado < 0:
        return False
    
    # Inicializa os dois primeiros números da sequência
    numero_antecessor, numero_atual = 0, 1
    
    if numero_buscado == 0:
        return True
    
    while numero_atual <= numero_buscado:
        if numero_atual == numero_buscado:
            return True
        numero_antecessor, numero_atual = numero_atual, numero_antecessor + numero_atual
    
    return False


mensagem_entrada = 'Digite um número para verificar se está na sequência de Fibonacci, ou digite "S" para Sair: \n'

numero = input(mensagem_entrada)

while numero.lower() != 's':
    try:
        if e_fibonacci(numero_buscado=int(numero)):
            print(f'O número {numero} pertence à sequência de Fibonacci.')
            numero = input(mensagem_entrada)
        else:
            print(f'O número {numero} não pertence à sequência de Fibonacci.')
            numero = input(mensagem_entrada)
    except:
        print(f'A entrada precisa ser um número inteiro')
        numero = input(mensagem_entrada)