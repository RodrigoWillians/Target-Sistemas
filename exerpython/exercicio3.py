import json

path_dados = "./dados.json"

with open(path_dados) as fileOpen:
    file = json.load(fileOpen)
    
maiorValor = 0
diaMaior = 0
diaMenor=0
contador = 0
acumulador = 0
listaValores = []
for element in file:
    if element["valor"] !=0:
        acumulador+=element["valor"]
        contador +=1
    
    if element["valor"] > maiorValor:
        maiorValor=element["valor"]
        diaMaior=element["dia"]
        
print(f"Maior valor: {maiorValor:.2f}, Dia: {diaMaior}")  

print("---------------------------------------")

media = acumulador/contador
print(f"Media: {media:.2f}")

for element in file:
    if element["valor"]>media and element["valor"] != 0:
        print(f"dia: {element['dia']}, Valor acima da media: {element['valor']:.2f}")
        
        
print("---------------------------------------")
menorValor=maiorValor
for element in file:
    if element["valor"] <= menorValor and element["valor"]!=0:
        menorValor=element["valor"]
        diaMenor=element["dia"]

print(f"Menor valor: {menorValor:.2f}, Dia:{diaMenor}")
print("---------------------------------------")
    

fileOpen.close()

    