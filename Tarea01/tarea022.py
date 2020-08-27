
def leernum():
    num  = int (input("Digite un numero "))
    boole = numprimo(num)
    if boole==True:
         print(f"El numero {num} es primo!")
    else:
        print(f"El numero {num} no es primo!")

def numprimo(num):
    b=0
    for i in range(1,num+1):
        if num%i==0:
            b=b+1      
    if b==2:
        boole=True       
    else:
        boole=False
    return(boole)


def main():
    leernum()

if __name__ == "__main__":
    main()
            

