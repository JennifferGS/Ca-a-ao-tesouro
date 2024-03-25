import itertools

# Função para calcular a distância entre dois pontos (ilhas)
def calcula_distancia(caminho, grafo):
    distancia_total = 0
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        distancia_total += grafo[origem][destino]
    distancia_total += grafo[caminho[-1]][caminho[0]]  # Volta ao ponto de partida
    return distancia_total

# Função recursiva para encontrar o melhor caminho 
def encontrar_melhor_caminho(grafo, vertices, caminho_atual=None):
    if caminho_atual is None:
        caminho_atual = [vertices[0]]  # Começa pelo primeiro vértice

    if len(caminho_atual) == len(vertices):
        distancia = calcula_distancia(caminho_atual, grafo)
        return caminho_atual, distancia

    melhor_caminho = None
    menor_distancia = float('inf')

    for proximo_vertice in vertices:
        if proximo_vertice not in caminho_atual:
            novo_caminho = caminho_atual + [proximo_vertice]
            caminho, distancia = encontrar_melhor_caminho(grafo, vertices, novo_caminho)
            if distancia < menor_distancia:
                menor_distancia = distancia
                melhor_caminho = caminho

    return melhor_caminho, menor_distancia

# Exemplo de uso
grafo = [
    [0, 29, 20, 21, 12], #0
    [29, 0, 15, 18, 1 ], #1
    [20, 15, 0, 27, 35], #2
    [21, 18, 27, 0, 40], #3
    [12, 1, 35, 40, 0]   #4
]
vertices = list(range(len(grafo)))  # Vértices numerados de 0 a 4

melhor_caminho, menor_distancia = encontrar_melhor_caminho(grafo, vertices)
print("Melhor caminho:", melhor_caminho)
print("Menor distância:", menor_distancia)
