# CaixeiroViajante

# Problema do Caixeiro Viajante
Este é um exemplo simples de resolução do problema do caixeiro viajante usando força bruta. O problema do caixeiro viajante envolve encontrar o caminho mais curto que visita todas as cidades exatamente uma vez e retorna à cidade de origem.

## Descrição

A biblioteca itertools é importante para gerar todas as permutações possíveis dos vértices do grafo. Isso é usado para testar todas as possíveis ordens de visita aos vértices.

## Como usar

Instância de uma classe Automato.
Chamo o método encontrar_caminho_para_tesouropassando o estado inicial como argumento.
O método retornará o caminho encontrado para a Ilha do Tesouro, se existir.
Pitão

# Exemplo de uso
 ```python
aut = Automato()
#Inicia a busca pelo caminho para o tesouro a partir do estado inicial (Piratas).
caminho_para_tesouro = aut.encontrar_caminho_para_tesouro("Piratas")
if caminho_para_tesouro:
    print("Caminho para o tesouro:", caminho_para_tesouro)
else:
    print("Não foi possível encontrar um caminho para o tesouro.")

    
## Licença
Este código é distribuído sob licença MIT. Consulte o arquivo LICENSE para obter detalhes.

