# 8rainhas ♟️
Projeto feito para obtenção de nota para a disciplina de Inteligência Artificial.

### Problema 🧩
O problema das 8 rainhas é um famoso problema que envolve peças e tabuleiro de xadrez. A questão é posicionar 8 rainhas em um tabuleiro 8x8 de forma que nenhuma rainha se ataque. Ou seja, nenhuma rainha pode
estar na mesma linha, coluna ou diagonal de outra rainha.

Trata-se de um problema de busca, isto é, um problema computacional onde o objetivo é encontrar uma solução que preenche certo requisito dentro de um conjunto de estados possíveis. O objetivo é encontrar um
caminho do estado inicial até um estado final. 

### Solução Proposta 💡
Neste algoritmo, utilizamos dois métodos para encontrar a solução do problema das 8 rainhas: Subida na Encosta e Algoritmo Genético

#### Subida na Encosta ⛰️
Método simples onde sempre nos movemos em busca da possível solução, o algoritmo termina quando encontra um pico onde o nó atual tem um valor melhor que todos os seus vizinhos. É como tentar alcançar o pico
de uma montanha no meio de um nevoeiro. Infelizmente, podemos encontrar mínimos/máximos locais.

#### Algoritmo Genético 🧬
Pode ser visto como uma variante de busca em feixe estocástico onde os estados sucessores são gerados a partir de dois pais. Iniciamos o algoritmo com uma população gerada aleatoriamente, a partir daí selecionamos
os possíveis pais de uma nova população a partir de uma função fitness. Após a seleção dos pais, realizamos a operação de crossover para a produção de filhos. 

Diferente da Subida na Encosta, conseguem fugir de mínimos e máximos locais porque conseguem explorar uma ampla variedade de soluções possíveis. 

### O que aprendi? 🤓 
Pude colocar em prática conhecimos que estava vendo em sala e observar como as técnicas aprendidas funcionam, ajudando na fixação dos conteúdos. Também comecei a me interessar pelo assunto, me atraiu e quem sabe
posso ampliar meus conhecimentos futuramente!
