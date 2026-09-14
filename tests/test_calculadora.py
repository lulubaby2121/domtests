from app.calculadora import(
    somar,
    subtrair,
    calcular_desconto
)

def test_somar():
    resultado = somar(2,3)
    assert resultado == 5

def test_subtrair():
    resultado = subtrair(5,3)
    assert resultado == 2

def test_calcular_desconto():
    resultado = calcular_desconto(100, 10)
    assert resultado == 90