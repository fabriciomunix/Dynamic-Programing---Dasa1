# Explicação passo a passo do projeto_insumos.py

Este documento explica o funcionamento do arquivo `projeto_insumos.py`, que simula o consumo diário de insumos utilizando estruturas de dados e algoritmos clássicos.

## 1. Introdução
O script foi desenvolvido para demonstrar conceitos de Fila, Pilha, Busca Sequencial, Busca Binária, Merge Sort e Quick Sort, aplicados ao contexto de consumo de insumos laboratoriais.

## 2. Geração dos Dados
- **Função:** `gerar_dados_consumo(n)`
- **Descrição:** Gera uma lista de dicionários simulando o consumo de insumos, cada um com nome, quantidade e validade (dias até vencer).

## 3. Estruturas de Dados
### Fila
- **Função:** `registrar_fila(dados)`
- **Descrição:** Cria uma fila (FIFO) com os dados, simulando ordem cronológica de chegada dos insumos.

### Pilha
- **Função:** `registrar_pilha(dados)`
- **Descrição:** Cria uma pilha (LIFO) com os dados, simulando o último insumo a entrar sendo o primeiro a sair.

## 4. Buscas
### Busca Sequencial
- **Função:** `busca_sequencial(dados, alvo)`
- **Descrição:** Procura linearmente por um insumo pelo nome.

### Busca Binária
- **Função:** `busca_binaria(dados, alvo)`
- **Descrição:** Procura por um insumo pelo nome, mas exige que os dados estejam ordenados. Utiliza o método de busca binária.

## 5. Ordenação
### Merge Sort
- **Função:** `merge_sort(lista, chave)`
- **Descrição:** Ordena a lista de insumos pela chave informada usando o algoritmo Merge Sort.

### Quick Sort
- **Função:** `quick_sort(lista, chave)`
- **Descrição:** Ordena a lista de insumos pela chave informada usando o algoritmo Quick Sort.

## 6. Relatório
- **Função:** `gerar_relatorio_console(dados, titulo)`
- **Descrição:** Imprime no console um relatório dos insumos, mostrando nome, quantidade e validade.

## 7. Execução Principal (`__main__`)
1. Gera dados simulados.
2. Mostra os dados iniciais.
3. Demonstra uso de fila (mostra os 3 primeiros).
4. Demonstra uso de pilha (remove e mostra os 3 últimos).
5. Realiza buscas sequencial e binária por um insumo específico.
6. Ordena os dados por quantidade (Merge Sort) e validade (Quick Sort), mostrando os resultados.

---

Este passo a passo serve como guia para entender e modificar o código conforme necessário.