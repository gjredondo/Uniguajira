

def leernum():
    num  = int (input("Digite un numero "))
    boole = numper(num)
    if boole==True:
        print(f"El numero {num} es perfecto!")
    else:
        print(f"El numero {num} no es perfecto!")

def numper(num):
    acumu=0
    for i in range(1,num):
        if num%i==0:
            acumu=acumu+i   
    if acumu==num:
        boole=True
    else:
        boole=False
    return(boole)


def main():
    leernum()

if __name__ == "__main__":
    main()