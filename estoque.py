estoque = []

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def adicionar(self, qtd):
        if qtd > 0:
            self.quantidade += qtd
        else:
            print("❌ Quantidade inválida!")

    def remover(self, qtd):
        if qtd > 0 and qtd <= self.quantidade:
            self.quantidade -= qtd
        else:
            print("❌ Quantidade inválida ou insuficiente!")

    def atualizar_preco(self, novo_preco):
        if novo_preco >= 0:
            self.preco = novo_preco
        else:
            print("❌ Preço inválido!")

    def __str__(self):
        return f"{self.nome} | Qtd: {self.quantidade} | Preço: R${self.preco:.2f}"

# ========== BUSCAR PRODUTO ==========
def buscar_produto(nome):
    for produto in estoque:
        if produto.nome.lower() == nome.lower():
            return produto
    return None

# ========== LISTAR PRODUTOS ==========
def listar():
    if not estoque:
        print('Estoque vazio.')
    else:
        print("\n=== ESTOQUE ===")
        for p in estoque:
            print(p)

# ========== ADICIONAR NOVO PRODUTO ==========
def novo_produto():
    nome = input('\nDigite o nome do produto: ')

    try:
        qtd = int(input('Digite a quantidade: '))
        preco = float(input('Informe o preço: '))
    except ValueError:
        print("❌ Entrada inválida!")
        return

    if qtd < 0 or preco < 0:
        print("❌ Valores não podem ser negativos!")
        return

    if buscar_produto(nome):
        print("❌ Produto já existe!")
        return

    novo = Produto(nome, qtd, preco)
    estoque.append(novo)
    print('✅ Produto adicionado com sucesso!')

# ========== ADICIONAR QUANTIDADE ==========
def adicionar_qtd():
    nome = input('\nInforme o produto: ')
    produto = buscar_produto(nome)

    if produto:
        try:
            qtd = int(input('Quantidade a adicionar: '))
            produto.adicionar(qtd)
        except ValueError:
            print("❌ Entrada inválida!")
    else:
        print('❌ Produto não encontrado!')

# ========== REMOVER QUANTIDADE ==========
def remover_qtd():
    nome = input('\nInforme o produto: ')
    produto = buscar_produto(nome)

    if produto:
        try:
            qtd = int(input('Quantidade a remover: '))
            produto.remover(qtd)
        except ValueError:
            print("❌ Entrada inválida!")
    else:
        print('❌ Produto não encontrado!')

# ========== MENU ==========
def menu():
    while True:
        try:
            return int(input(
                "\n=== GERENCIAMENTO DE ESTOQUE ===\n"
                "1 - Adicionar produto\n"
                "2 - Adicionar quantidade\n"
                "3 - Remover quantidade\n"
                "4 - Listar estoque\n"
                "0 - Sair\n"
                "Escolha: "
            ))
        except ValueError:
            print('❌ Opção inválida!')

# ========== EXECUÇÃO ==========
def main():
    while True:
        opcao = menu()

        if opcao == 0:
            print("Encerrando...")
            break
        elif opcao == 1:
            novo_produto()
        elif opcao == 2:
            adicionar_qtd()
        elif opcao == 3:
            remover_qtd()
        elif opcao == 4:
            listar()
        else:
            print('❌ Opção inválida!')

        print('-' * 40)

main()