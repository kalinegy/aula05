x=0
soma=0
alunos=int(input("Digite o número de alunos desta sala:"))
while x < alunos:
    nota = int(input("Digite a nota:"))
    soma += nota
    x += 1
media = soma / alunos
print(media)
