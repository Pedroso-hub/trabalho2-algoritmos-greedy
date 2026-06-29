from rally import escolher_paradas
import random
import time
import pandas as pd

def valida(pontos, d):
    for i in range(len(pontos)-1):
        curr = pontos[i]
        next = pontos[i+1]
        if next-curr > d:
            return False
        
    return True


totais = []
quant_pontos = []
for i in range(1000, 10000, 100):
    

    L =i-1

    d = random.randint(1, L)
    # print(d)
    pontos = []
    prox_parada = 1
    for j in range(random.randint(1, L)):
        prox_parada = random.randint(prox_parada+1, prox_parada+d-1)
        pontos.append(prox_parada)

    if not valida(pontos, d):
        print("deu ruim")

    start_time = time.perf_counter()
    escolher_paradas(L, d, pontos)
    end_time = time.perf_counter()
    total = end_time - start_time
    totais.append(total)
    quant_pontos.append(len(pontos))
    
print(quant_pontos)
df = pd.DataFrame({"Tempo": totais, "n": quant_pontos})
df_sorted = df.sort_values(by='Tempo')
df_sorted.to_csv("resultados.csv", index=False)
    

    





