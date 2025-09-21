
"""
Projeto - Dimensionamento e Consumo de Insumos (DASA / Aurawave)
Integrantes:
- Fabrício Carlos : RM555017
- Erick Fujita    : RM556096
- Arnaldo Filho   : RM555780
- João Boht       : RM558690

Descrição:
Simulação de consumo diário de insumos e aplicação de estruturas de dados e algoritmos
clássicos: Fila, Pilha, Busca Sequencial, Busca Binária, Merge Sort e Quick Sort.
Inclui um pequeno "runner" no bloco __main__ para demonstração.

Como executar:
$ python projeto_insumos.py
"""

from collections import deque
import random
from typing import List, Dict, Optional


# -----------------------------
# Simulação de dados de consumo
# -----------------------------
def gerar_dados_consumo(n: int = 15) -> List[Dict]:
    """Gera n registros simulados de consumo de insumos."""
    insumos = [
        "Reagente A", "Reagente B", "Descartável X", "Descartável Y",
        "Corante Azul", "Corante Vermelho", "Lâmina", "Solução Salina"
    ]
    dados = []
    for _ in range(n):
        item = random.choice(insumos)
        qtd = random.randint(1, 10)
        validade = random.randint(1, 60)  # dias até vencer
        dados.append({"insumo": item, "quantidade": qtd, "validade": validade})
    return dados


# -----------------------------
# FILA e PILHA
# -----------------------------
def registrar_fila(dados: List[Dict]) -> deque:
    """Cria uma fila (ordem cronológica)."""
    fila = deque()
    for d in dados:
        fila.append(d)  # chegada -> fim; saída -> começo
    return fila


def registrar_pilha(dados: List[Dict]) -> List[Dict]:
    """Cria uma pilha (último a entrar, primeiro a sair)."""
    pilha = []
    for d in dados:
        pilha.append(d)
    return pilha


# -----------------------------
# BUSCAS
# -----------------------------
def busca_sequencial(dados: List[Dict], alvo: str) -> Optional[Dict]:
    """Busca linear por nome do insumo."""
    for d in dados:
        if d["insumo"] == alvo:
            return d
    return None


def busca_binaria(dados: List[Dict], alvo: str) -> Optional[Dict]:
    """Busca binária (exige dados ordenados por 'insumo')."""
    dados_ordenados = sorted(dados, key=lambda x: x["insumo"])
    esquerda, direita = 0, len(dados_ordenados) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if dados_ordenados[meio]["insumo"] == alvo:
            return dados_ordenados[meio]
        elif dados_ordenados[meio]["insumo"] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None


# -----------------------------
# ORDENAÇÃO (Merge Sort e Quick Sort)
# -----------------------------
def merge_sort(lista: List[Dict], chave: str) -> List[Dict]:
    """Ordena usando Merge Sort pela 'chave' informada."""
    if len(lista) <= 1:
        return lista[:]
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)
    return _merge(esquerda, direita, chave)


def _merge(esq: List[Dict], dir: List[Dict], chave: str) -> List[Dict]:
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i][chave] <= dir[j][chave]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado


def quick_sort(lista: List[Dict], chave: str) -> List[Dict]:
    """Ordena usando Quick Sort pela 'chave' informada."""
    if len(lista) <= 1:
        return lista[:]
    pivo = lista[0]
    menores = [x for x in lista[1:] if x[chave] <= pivo[chave]]
    maiores = [x for x in lista[1:] if x[chave] > pivo[chave]]
    return quick_sort(menores, chave) + [pivo] + quick_sort(maiores, chave)


# -----------------------------
# RELATÓRIO (console)
# -----------------------------
def gerar_relatorio_console(dados: List[Dict], titulo: str = "Relatório de Insumos") -> None:
    print(f"\\n--- {titulo} ---")
    for d in dados:
        print(f"Insumo: {d['insumo']} | Qtd: {d['quantidade']} | Validade: {d['validade']} dias")


# -----------------------------
# MAIN (demonstração)
# -----------------------------
if __name__ == "__main__":
    random.seed(42)  # reprodutibilidade

    # 1) Geração
    dados = gerar_dados_consumo(12)
    gerar_relatorio_console(dados, "Dados simulados (entrada)")

    # 2) Fila
    fila = registrar_fila(dados)
    print("\\n[FILA] Ordem cronológica (peek nos 3 primeiros):")
    for i, f in enumerate(list(fila)[:3], start=1):
        print(f"{i:02d} -> {f}")

    # 3) Pilha
    pilha = registrar_pilha(dados)
    print("\\n[PILHA] Pops nos 3 últimos registros:")
    for i in range(3):
        if pilha:
            print(f"POP {i+1}: {pilha.pop()}")

    # 4) Buscas
    alvo = "Reagente A"
    print("\\n[BUSCA SEQUENCIAL]", busca_sequencial(dados, alvo))
    print("[BUSCA BINÁRIA]", busca_binaria(dados, alvo))

    # 5) Ordenações
    ordenado_merge = merge_sort(dados, "quantidade")
    gerar_relatorio_console(ordenado_merge, "Ordenado por quantidade (Merge Sort)")

    ordenado_quick = quick_sort(dados, "validade")
    gerar_relatorio_console(ordenado_quick, "Ordenado por validade (Quick Sort)")
