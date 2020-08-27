


def funexpo(fbase,fexpo):
    res=fbase
    for i in range(1,fexpo):
        res=res*fbase
    return res


def leerdatos():
    numero  = int (input("Digite un numero para realizar la operacion: "))
    formula(numero)

def factorial (*n):
    for x in n:
        fac=1
        for y in range(1,x+1):
            fac=fac*y
    return fac

def formula(num):
    final=1+num
    for i in range(2,51):
        ne=funexpo(num,i)
        nf=factorial(i)
        final=final+(ne/nf)
    print (f"El resultado de la formula es: {final}")


def main():
    leerdatos()

if __name__ == "__main__":
    main()
            


