# Algoritmo Genético — 1º Trabalho de Otimização e Combinatória

Equipe: Lucas Willian Mezzalira e Pedro Rockenbach

## Especificação (Função 10)

- Função: Z = 2x² − 13x + xy − 7y/3, com x, y ∈ [−15, 15] (maximização)
- Codificação binária com bit de sinal (5 bits por variável, sem complemento de dois)
- Seleção por ranking (linear de Baker, pressão seletiva 1.2)
- Cruzamento uniforme
- Mutação por inversão
- Elitismo de 1 indivíduo por geração
- Critério de parada: número de gerações

## Requisitos

- Python 3
- matplotlib e numpy

### Windows

    py -m pip install matplotlib numpy

### Linux

    sudo apt install python3-matplotlib python3-numpy

## Como executar

Na pasta do projeto:

### Windows

    py main.py

### Linux

    python3 main.py

- tamanho da população
- número de gerações
- taxa de cruzamento (entre 0 e 1, com ponto: 0.7)
- taxa de mutação (entre 0 e 1, com ponto: 0.01)

## Saídas

- `logs/log.csv`: geração, fitness médio, melhor fitness, melhor x e melhor y de cada geração
- `imagens/fitness_medio.png`: gráfico do fitness médio por geração
- `imagens/grafico_geracao.png`: população no espaço de busca
