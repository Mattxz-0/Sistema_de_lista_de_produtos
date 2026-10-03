# 🛒 Gerenciador de Pedidos em Python (Lógica de Programação Pura)

Um sistema interativo de gerenciamento de produtos e pedidos desenvolvido em Python via linha de comando (CLI). 

Este projeto foi desenvolvido com foco estrito nos **fundamentos da lógica de programação**, manipulando estruturas de dados manualmente e sem o uso de métodos ou funções convenientes nativas da linguagem (como `.append()`, `.remove()`, `.pop()`, `sum()`, etc.).

---

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto é praticar e consolidar conceitos fundamentais de ciência da computação e lógica estruturada, tais como:

- **Estruturas de Decisão:** Controle de fluxo com `match/case` (Python 3.10+) e `if/elif/else`.
- **Laços de Repetição:** Controle de loops com `while` e tratamento de menus interativos.
- **Matrizes / Listas de Listas:** Agrupamento de dados compostos (`[[nome_produto, valor_produto]]`).
- **Manipulação Manual de Listas:** Inserção por concatenação e remoção por reconstrução de listas via algoritmo de filtragem manual.
- **Validação de Entradas:** Tratamento de strings vazias para prevenção de erros de execução.

---

## 📋 Funcionalidades

- [x] **Cadastrar Produto:** Permite inserir o nome e o valor do produto com validação contra campos em branco.
- [x] **Visualizar Pedido:** Exibe a lista numerada de itens cadastrados, formatando valores monetários (`R$`).
- [x] **Cálculo Automático:** Exibe o valor total acumulado do carrinho dinamicamente.
- [x] **Remover Produto:** Permite excluir um produto específico digitando seu número de índice.
- [x] **Recálculo do Total:** Ajusta o valor total do pedido automaticamente ao remover um produto.
- [x] **Menu Interativo:** Navegação contínua em loop até que o usuário opte por sair.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+** (necessário para o suporte ao `match/case`)

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
