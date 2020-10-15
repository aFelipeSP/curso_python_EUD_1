import main

def test_entero():
    assert main.entero == 1
    
def test_decimal():
    assert main.decimal == 3.14
    
def test_texto():
    assert 'hola mundo' in main.texto.lower().strip()
    
def test_booleano():
    assert main.booleano == True
    
def test_lista():
    assert main.lista == [main.entero, main.decimal, main.texto, main.booleano]
    
def test_dict():
    assert main.dict == {'entero': main.entero, 'decimal': main.decimal, 'texto': main.texto, 'booleano': main.booleano, 'lista': main.lista}
