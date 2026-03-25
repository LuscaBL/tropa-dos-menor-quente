estoque = []
class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def adicionar(self, qtd):
        self.quantidade += qtd

    def remover(self, qtd):
        self.quantidade -= qtd

# ========== BUSCAR PRODUTO (FUNÇÃO AUXILIAR) ==========
def buscar_produto(nome):
    for produto in estoque:
        if produto.nome == nome:
            return produto
    return None

# ========== LISTAR PRODUTOS ==========
def listar():
    if not estoque:
        print('Estoque vazio.')
        return
    else:
        for p in estoque:
            print(f'Nome: {p.nome} | Quantidade: {p.quantidade} | Preço: R${p.preco}')

# ========== ADICIONAR PRODUTO ==========
def novo_produto():
    nome =  input('\nDigite o nome do produto que deseja adicionar: ')
    qtd = int(input('\nDigite a quantidade do produto: '))
    preco = float(input('\nInforme o preço do produto: '))

    novo = Produto(nome, qtd, preco)
    estoque.append(novo)
    print(f'✅ Produto adicionado com sucesso!')
    return

# ========== ADICIONAR QUANTIDADE ==========
def adicionar_qtd():
    nome = input('\nInforme o produto: ')
    produto = buscar_produto(nome)

    if produto:
        qtd = int(input('Quantidade a adicionar: '))
        produto.adicionar(qtd)
        print(f'✅ {qtd} {nome} adicionado com sucesso ao total!')
    else:
        print('❌ Produto não encontrado!')

# ========== REMOVER QUANTIDADE ==========
def remover_qtd():
    nome = input('\nInforme o produto: ')
    produto = buscar_produto(nome)

    if produto:
        qtd = int(input('Quantidade a remover: '))
        produto.remover(qtd)
        print(f'✅ {qtd} {nome} removido com sucesso!\n')
    else:
        print('❌ Produto não encontrado!')
        
# ========== MENU PRINCIPAL ==========
def menu():
    while True:
        try:
            return int(input("\n=== GERENCIAMENTO DE ESTOQUE ===\n\n1 - Adicionar produto\n2 - Adicionar quantidade a produto\n3 - Remover quantidade de produto\n4 - Listar estoque\n0 - Sair\n\nEscolha uma opção: "))
        except ValueError:
            print(f'❌OPÇÃO INCORRETA. TENTE NOVAMENTE!')

# ========== EXECUTOR ==========
def main():
    while True:
        opcao = menu()

        if opcao == 0: exit()
        elif opcao == 1: novo_produto()
        elif opcao == 2: adicionar_qtd()
        elif opcao == 3: remover_qtd()
        elif opcao == 4: listar()
        else: print(f'❌Opção incorreta. Tente novamente!')
    
        print('-' * 40)

main()