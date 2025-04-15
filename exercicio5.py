resp="s"
while resp== "s":
a1=float(input("Digite a nota da primeira avaliação:"))
while a1 <0 or a1 >10:
    a1= float(input("Valor da primeira avaliação inválido, digite um número maior que 0:"))
while a2<0 or a2 >10:
    a2= float(input("Valor da primeira avaliação inválido, digite um número maior que 0:"))
media = (a1+a2)/2
print(media)