from operacoes import *

print(f"soma = {1}")
print(f"subtraçao = {2}")
print(f"multiplicaçao = {3}")
print(f"divisao = {4}")
print(F" finalizar = {0}")
opçao=int(input("digite o numero da operaçao: "))


if (opçao in [1,2,3,4]):
    n1=int(input("digite um numero: "))    
    n2=int(input("digite outro numero: "))
    
    if opçao ==1:
        print(soma(n1,n2))

    elif opçao==2:
        print(subtracao(n1,n2)) 
    elif opçao==3:
       print(multiplicacao(n1,n2))
    elif opçao==4:
        print(divisao(n1,n2))
else:
    import emoji
    print(emoji.emojize("finalizar:sparkles: :thumbs_up:",language="alias"))
