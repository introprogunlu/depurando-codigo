def cuadrado(n1):

    return n1 *n1
def suma_tres_numeros(n1,n2,n3):
    return n1+n2+n3

def restar_dos_numeros(n1,n2):
    return n1-n2

def test_cuadrado():
    assert(cuadrado(2)== 4)
    assert(cuadrado(3) == 9)
    assert(cuadrado(5) == 25)
    print("EXITO!!! cuadrados")

def test_sumas():
    assert(suma_tres_numeros(1,2,3)== 6)
    assert(suma_tres_numeros(3,3,3)== 9)
    assert(suma_tres_numeros(10,2,3)== 15)
    print("EXITO sumas")

def test_restar_dos_numeros():
    assert(restar_dos_numeros(4,2)==2)
    assert(restar_dos_numeros(5,13)==-8)
    assert(restar_dos_numeros(14,2)==12)
    print("EXITO restas")


test_sumas()
test_cuadrado()
test_restar_dos_numeros()