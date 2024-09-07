from fibonacci import e_fibonacci

def test_fibonacci_com_numero_negativo():
    assert not e_fibonacci(-1), "Números negativos não devem pertencer à sequência de Fibonacci"

def test_fibonacci_com_zero():
    assert e_fibonacci(0), "0 pertence à sequência de Fibonacci"

def test_fibonacci_com_um():
    assert e_fibonacci(1), "1 pertence à sequência de Fibonacci"

def test_fibonacci_com_numero_fibonacci():
    assert e_fibonacci(13), "13 pertence à sequência de Fibonacci"

def test_fibonacci_com_numero_nao_fibonacci():
    assert not e_fibonacci(4), "4 não pertence à sequência de Fibonacci"

