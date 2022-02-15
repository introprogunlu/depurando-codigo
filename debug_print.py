def imprimir_cuadrados(n1,n2):
    print("el numero uno es",n1)
    print("el numero dos es",n2)
    for x in range(n1,n2):
        print(f"se imprime {x} * {x}") 
        print(x * x)

imprimir_cuadrados(2,5)

def imprimir_sumas_continuos(n1,n2):
    print("n1",n1)
    print("n2",n2)
    a = n1
    print ("a",a)
    for x in range(n1,n2):
        print("x1",x)
        print("a1",a)
        a +=x
        print("a2",a)
        print("x2",x)
    return a

resultado = imprimir_sumas_continuos(2,5)
print(resultado)