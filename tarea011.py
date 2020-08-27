


def leernum():
    num  = float (input("Digite un numero "))
    parimpar(num)


def parimpar(num):

    if num%2==0:
        print(f"El numero {num} es Par!")
    else:
        print(f"El numero {num} es Impar!")


def main():
    leernum()

if __name__ == "__main__":
    main()