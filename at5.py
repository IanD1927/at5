nome = input("nome do usuario: ")
valor = float(input("valor pago por horas trabalhadas: "))
horas = float(input("numero de horas trabalhadas: "))
dias = int(input("quantos dias trabalhados: "))

soma = valor * horas * dias

print("ola {} o valor a ser pago e de R${} ".format(nome, soma))
