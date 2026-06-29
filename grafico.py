import matplotlib.pyplot as plt
import pandas as pd
# Como 'n' varia de forma aleatória, o gráfico de dispersão (scatter) é o ideal
# Usamos plt.subplots() para evitar o uso de .figure() conforme boas práticas
fig, ax = plt.subplots(figsize=(10, 6))
df_sorted = pd.read_csv("resultados.csv")
# Criando o gráfico de dispersão
ax.scatter(
    df_sorted['n'], 
    df_sorted['Tempo'], 
    color='royalblue', 
    alpha=0.6, 
    edgecolors='none', 
    s=35
)

# Configurando os títulos e identificações dos eixos
ax.set_title('Análise de Complexidade: Tempo de Execução vs. Quantidade de Pontos', fontsize=14, fontweight='bold')
ax.set_xlabel('Quantidade de Pontos (n)', fontsize=12)
ax.set_ylabel('Tempo (segundos)', fontsize=12)

# Adicionando linhas de grade para facilitar a leitura do gráfico
ax.grid(True, linestyle='--', alpha=0.6)

# Garante que nenhum rótulo ou título seja cortado nas bordas
plt.tight_layout()

# Salva o gráfico em um arquivo de imagem de alta resolução
plt.savefig('grafico_resultados.png', dpi=300)