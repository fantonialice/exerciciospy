
# Exercício: Faça um programa onde o usuário possa entrar com uma lista de modelos e suas respectivas alturas. O programa deve imprimir as primeiras 2 modelos de maior altura.

n = int(input("entre com a quantidade de modelos: "))

modelos = [0] * n
alturas = [0] * n

for i in range(0, n):
    modelos[i] = input("nome: ")
    alturas[i] = float(input("altura: "))

m1 = 0 # primeira maior altura
m2 = 0 # segunda maior altura    

nomem1 = "" #nome da modelo de maior altura
nomem2 = "" #nome da modelo de segunda maior altura

#pode tirar esses prints, foi só pra verificar mesmo
print(modelos)
print(alturas)

for i in range(0, n):
    if alturas[i] > m1:
        m2 = m1
        nomem2 = nomem1
        m1 = alturas[i]
        nomem1 = modelos[i]
    elif alturas[i] > m2:
        m2 = alturas[i]
        nomem2 = modelos[i]

print("modelo com maior altura: ", nomem1)
print("modelo com segunda maior altura: ", nomem2)

