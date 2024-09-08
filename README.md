# Code Test

Os scripts de python abaixo testam minha habilidade em python

## Executando os scripts

Este guia explica como executar os seguintes scripts:

- `busca_letra_a.py`, que conta as ocorrências da letra 'a' (incluindo variações como 'á', 'â', 'ã', etc.) em um texto fornecido pelo usuário.
- `fibonacci.py`, que verifica se um número inteiro qualquer faz parte da sequência Fibonacci.

### Pré-requisitos

Antes de executar os scripts, certifique-se de que você tem Python instalado em sua máquina. Você pode verificar isso executando `python --version` ou `python3 --version` no terminal. Os scripts foram testados com Python 3.12, mas devem funcionar com outras versões que suportam o módulo `re`.

### Como Executar

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde o arquivo `busca_letra_a.py` ou `fibonacci.py` está localizado.
3. Execute o script usando um dos dois comandos abaixo (dependendo da sua configuração do Python):

```bash
python nome_do_arquivo.py
```

ou

```bash
python3 nome_do_arquivo.py
```

4. Uma vez iniciado, o script irá solicitar que você digite uma entrada. Insira o texto ou número desejado e pressione Enter.

## Rodando os Testes com Pytest

Este documento fornece instruções sobre como executar os testes automatizados para este projeto usando `pytest`.

### Pré-requisitos

Antes de começar, você precisará ter o `pytest` instalado. Se ainda não o instalou, pode fazê-lo executando o seguinte comando:

```bash
pip install pytest
```

### Executando os Testes

Para rodar todos os testes localizados na pasta tests dentro do diretório raiz do projeto, siga os passos abaixo.

1. Abra um terminal.
2. Navegue até o diretório raiz do projeto.
3. Execute o seguinte comando:
```bash
pytest tests
```
4. Esse comando irá automaticamente encontrar e executar todos os arquivos de teste dentro da pasta tests.

