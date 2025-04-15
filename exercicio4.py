pin=1234
tentativas=1
msg= "Senha incorreta, usuario bloqueado"
while tentativas<=3:
    senha = int(input("Digite sua senha:"))
    if senha == pin:
        msg=("Senha correta")
        break
    tentativas+=1
print(msg)