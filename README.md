# 🛒 Gerenciador de Pedidos em Python (Lógica Pura)

Sistema interativo via terminal (CLI) para cadastro, visualização e remoção de produtos, com cálculo automático do valor total.

Projetado exclusivamente com **lógica de programação pura**, sem o uso de métodos nativos da linguagem (como `.append()`, `.remove()` ou `.pop()`).

---

## ⚡ Funcionalidades

- **Cadastrar Produto:** Nome e valor com validação de entrada.
- **Visualizar Pedido:** Lista numerada de produtos com formatação em `R$`.
- **Remover Produto:** Exclusão por índice com atualização automática do valor total.
- **Menu Interativo:** Navegação via `match/case` em laço contínuo.

---

## 🧠 Destaques de Algoritmo

### Inserção sem `.append()`
```python
produtos = produtos + [[produto, valor]]
