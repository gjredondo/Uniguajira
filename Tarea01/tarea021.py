


def leernum():
    num  = int (input("Digite un numero "))
    numprimo(num)

def numprimo(num):
    b=0
    for i in range(1,num+1):
        if num%i==0:
            b=b+1      
    if b==2:
        print(f"El numero {num} es primo!")
    else:
        print(f"El numero {num} no es primo!")


def main():
    leernum()

if __name__ == "__main__":
    main()
            

