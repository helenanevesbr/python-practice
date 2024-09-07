from busca_letra_a import contagem_letra_a

def test_contagem_letra_a_vazia():
    assert contagem_letra_a("") == 0, "Deve retornar 0 para string vazia"

def test_contagem_letra_a_sem_a():
    assert contagem_letra_a("bcd efg") == 0, "Deve retornar 0 se não há 'a' no texto"

def test_contagem_letra_a_com_varias_a():
    assert contagem_letra_a("Ana tem uma árvore à beira da estrada.") == 12, "Deve contar corretamente as variações de 'a'"

def test_contagem_letra_a_com_caracteres_especiais():
    assert contagem_letra_a("@b@c@d@ e#f$g% ^&*(") == 2, "Caracteres especiais não devem afetar a contagem de 'a'"
