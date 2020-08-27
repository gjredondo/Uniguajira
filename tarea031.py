

def leernum():
    num  = int (input("Digite un numero "))
    numper(num)

def numper(num):
    acumu=0
    for i in range(1,num):
        if num%i==0:
            acumu=acumu+i   
    if acumu==num:
        print(f"El numero {num} es perfecto ya que la suma de sus divisores es: {acumu}!")
    else:
        print(f"El numero {num} no es perfecto ya que la suma de sus divisores es: {acumu}!")


def main():
    leernum()

if __name__ == "__main__":
    main()
            