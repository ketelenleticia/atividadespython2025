def soma():
    n1= int(input("me diga um número: "))
    n2= int(input("me diga outro número: "))
    print(n1+n2)

soma()

def subtracao():
    n1= int(input("me diga um número: "))
    n2= int(input("me diga outro número: "))
    print(n1-n2)

subtracao()


def multiplicacao():
    n1= int(input("me diga um número: "))
    n2= int(input("me diga outro número: "))
    print(n1*n2)

multiplicacao()


def divisao():
    n1= int(input("me diga um número: "))
    n2= int(input("me diga outro número: "))
    if n2 == 0:
        return("não pode dividir.")
    else:
        return(n1/n2)
    
    
print(divisao())
        
