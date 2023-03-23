texto = "Exemplo de string a ser invertida"

caracteres = list(texto)

inicio = 0
fim = len(caracteres) - 1

while fim > inicio:
    caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
    inicio += 1
    fim -= 1

texto_invertido = "".join(caracteres)

print(texto_invertido)