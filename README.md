
## Caça ao Tesouro - Encontrando o Melhor Caminho

Este é um exemplo de implementação do problema do caixeiro viajante, onde o objetivo é encontrar o caminho que visita todas as cidades uma vez e retorna ao ponto de partida minimizando a distância total percorrida. O código utiliza uma abordagem de força bruta para encontrar o caminho mais curto através de todas as permutações possíveis dos vértices.

## Funcionamento do Código
Definição do Grafo : O grafo representa as distâncias entre as cidades, onde cada vértice representa uma cidade e cada aresta representa a distância entre duas cidades.

Função para Calcular Distância : A função calcula_distanciarecebe um caminho (uma lista de vértices) e o gráfico, e calcula a distância total percorrida ao seguir esse caminho.

Função Recursiva para Encontrar o Melhor Caminho : A função encontrar_melhor_caminhoutiliza a abordagem de força bruta para percorrer todas as permutações possíveis dos vértices e encontrar o caminho que minimize a distância total.

Exemplo de Uso : Um exemplo de uso é fornecido, onde o gráfico representa as distâncias entre cinco cidades. O algoritmo é executado e o melhor caminho encontrado juntamente com a menor distância é impresso na saída.

## Executando o Código
Para executar o código, você pode copiar e colar o exemplo fornecido em um arquivo Python (.py) e repeti-lo em um ambiente Python de sua escolha. Certifique-se de ter o módulo itertoolsdisponível no seu ambiente.

Personalização
Você pode personalizar o código para o seu próprio problema ajustando o gráfico para representar as distâncias entre suas próprias cidades. -se de que a matriz de adjacência ( grafo) esteja corretamente definida de acordo com suas necessidades.

Lembre-se de que este é um algoritmo de força bruta e pode não ser eficiente para um grande número de cidades. Para conjuntos de dados maiores, seria aconselhável explorar algoritmos mais eficientes, como o algoritmo genético ou o algoritmo de vizinho mais próximo.

Este é um exemplo simples e educacional do problema do caixeiro viajante e pode ser expandido e otimizado conforme necessário para atender às suas próprias necessidades.
