class Mensagens:
    def __init__(self, conteudo):
        self._conteudo = conteudo
        self._disponivel = True
    
    def visualizar(self):
        print(f'Visualização não definida.')

    def status(self):
        return "Disponível" if self._disponivel else "Indísponivel"
    
    def tipo(self):
        return "Mensagem"

# ===== Mensagem Comum =====
class MensagemComum(Mensagens):
    def visualizar(self):
        if self._disponivel:
            print(self._conteudo)
        else:
            print("Mensagem indisponível")
        
    def tipo(self):
            return "Comum"
    
# ===== Mensagem Protegida ===== 
class MensagemProtegida(Mensagens):
    def __init__(self, conteudo, chave):
        super().__init__(conteudo)
        self._chave = chave #encapsulamento

    def visualizar(self):
        if not self._disponivel:
            print("❌ Mensagem Indisponível.")
            return
    
        tentativa = input('Digite a chave: ')
        if tentativa == self._chave:
            print(self._conteudo)
        else:
            print("❌ Chave Incorreta.")

    def tipo(self):
        return "Protegida"

# ===== Mensagem de Visualização Única =====
class MensagemUnica(Mensagens):
    def visualizar(self):
        if self._disponivel:
            print(self._conteudo)
            self._disponivel = False
        else: 
            print("❌ Mensagem indisponível.")

    def tipo(self):
        return "Única"

# ===== Sistema Principal =====
mensagens = []

def criar_mensagem():
    print("\n Tipo de mensagem:")
    print("1 - Comum")
    print("2 - Protegida")
    print("3 - Única")
    
    tipo = input("Opção: ")
    conteudo = input("Digite o conteúdo: ")
    
    if tipo == "1":
      mensagens.append(MensagemComum(conteudo))

    elif tipo == "2":
        chave = input("Digite  a chave:")
        mensagens.append(MensagemProtegida(conteudo, chave))

    elif tipo == "3":
        mensagens.append(MensagemUnica(conteudo))

    else:
         print("Opção inválida")
         return
         
    print("Mensagem criada com sucesso!")

def listar_mensagens():
    print('\n===== Mensagens Cadastradas =====')
    
    if not mensagens:
        print("Nenhuma mensagem cadastrada.")
        return
    
    for i, msg in enumerate(mensagens):
        print(f'{i} - [{msg.tipo()}] {msg.status()}')

def visualizar_mensagem():
    if not mensagens:
        print('Nenhuma mensagem cadastrada!')
        return
    
    try:
        indice = int(input('Digite o índice da mensagem: '))
        mensagens[indice].visualizar() #polimorfismo
    except (IndexError, ValueError):
        print(f'❌ Índice inválido.')

def remover_mensagem():
    if not mensagens:
        print('Nenhuma mensagem cadastrada!')
        return
    
    try:
        indice = int(input('Digite o índice da mensagem: '))
        mensagens.pop(indice)
        print('✅ Mensagem removida com sucesso!')
    except (IndexError, ValueError):
        print('❌ Índice inválido.')

def sair():
    print("Encerrando sistema...")
    exit()

# ===== Menu Principal =====
def menu():
    while True:
        print("\n===== MURAL DE MENSAGENS =====")
        print("1 - Criar mensagem")
        print("2 - Listar mensagens")
        print("3 - Visualizar mensagem")
        print("4 - Remover mensagem")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == 0: sair()
        elif opcao == 1: criar_mensagem()
        elif opcao == 2: listar_mensagens()
        elif opcao == 3: visualizar_mensagem()
        elif opcao == 4: remover_mensagem()
        else:
            print('❌ Opção inválida! Tente novamente.')

menu()
