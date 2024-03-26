

# Projeto de Linguagens Formais e Autômatos: Caça ao Tesouro Pirata

Este projeto foi desenvolvido por estudantes do curso de Ciência da Computação na disciplina de Linguagens Formais e Autômatos, ministrado pela professora Kadidja Valeria.

Alunos responsáveis: 
- Jenniffer Glenda
- Deborah Lohanne 
- Lucas Gonçalves

## Descrição
Este repositório contém um exemplo de implementação do problema do caixeiro viajante, relacionando-o com a busca por tesouros em um mapa fictício. O objetivo é encontrar o caminho mais curto que visite cada local uma vez, simbolizando a jornada de um pirata em busca de tesouros escondidos.

## Funcionamento do Código
### Definição do Grafo
O grafo representa as distâncias entre as localizações no mapa, onde cada vértice representa uma localização e cada aresta representa a distância entre duas localizações.

### Função para Calcular Distância
A função `calcula_distancia` recebe um caminho (uma lista de vértices) e o gráfico, e calcula a distância total percorrida ao seguir esse caminho.

### Função Recursiva para Encontrar o Melhor Caminho
A função `encontrar_melhor_caminho` utiliza uma abordagem de força bruta para percorrer todas as permutações possíveis dos vértices e encontrar o caminho que minimize a distância total.

### Exemplo de Uso
Um exemplo de uso é fornecido no código, onde o grafo representa as distâncias entre as localizações no mapa. O algoritmo é executado e o melhor caminho encontrado, juntamente com a menor distância, é impresso na saída.

## Executando o Código
Para executar o código, você pode copiar e colar o exemplo fornecido em um arquivo Python (.py) e executá-lo em um ambiente Python de sua escolha. Certifique-se de ter o módulo `itertools` disponível em seu ambiente.

## Personalização
Você pode personalizar o código para o seu próprio problema ajustando os gráficos para representar as distâncias entre suas próprias localizações. Certifique-se de que a matriz de adjacência (grafo) esteja corretamente definida de acordo com suas necessidades.

Lembre-se de que este é um algoritmo de força bruta e pode não ser eficiente para um grande número de localizações. Para conjuntos de dados maiores, seria aconselhável explorar algoritmos mais eficientes, como o algoritmo genético ou o algoritmo de vizinho mais próximo.

Este é um exemplo simples e educacional do problema do caixeiro viajante e pode ser expandido e otimizado conforme necessário para atender às suas próprias necessidades.

