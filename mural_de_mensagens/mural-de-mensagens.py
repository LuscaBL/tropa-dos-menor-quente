class Mensagens:
    def __init__(self, conteudo):
        self._conteudo = conteudo
        self._disponivel = True
    
    def visualizar(self):
        print(f'Visualização não definida.')

    def status(self):
        return "Disponível" if self._disponivel else "Indisponível"
    
    def tipo(self):
        return "Mensagem"

    def __str__(self):
        return f'[MENSAGEM] - {self.status()}'

# ===== Mensagem Comum =====
class MensagemComum(Mensagens):
    def visualizar(self):
        if self._disponivel:
            print(self._conteudo)
        else:
            print("❌ Mensagem indisponível")
        
    def tipo(self):
        return "Comum"
    
    def __str__(self):
        return f'[COMUM] - {self.status()}' 

# ===== Mensagem Protegida ===== 
class MensagemProtegida(Mensagens):
    def __init__(self, conteudo, chave):
        super().__init__(conteudo)
        self._chave = chave
        self._trancada = True

    def visualizar(self):
        if not self._disponivel:
            print("❌ Mensagem Indisponível.")
            return

        if self._trancada:
            print("*" * len(self._conteudo))
        else:
            print(self._conteudo)

    def alternar_trava(self):
        tentativa = input("Digite a chave: ")
        if tentativa == self._chave:
            self._trancada = not self._trancada
            estado = "destrancada" if not self._trancada else "trancada"
            print(f"🔒 Mensagem {estado} com sucesso!")
        else:
            print("❌ Chave incorreta.")

    def tipo(self):
        return "Protegida"
    
    def __str__(self):
        estado = "Trancada" if self._trancada else "Destrancada"
        return f'[PROTEGIDA] - {self.status()} ({estado})' 


class MensagemUnica(Mensagens):
    def __init__(self, conteudo):
        super().__init__(conteudo)
        self._visualizada = False

    def visualizar(self):
        if not self._visualizada:
            print(self._conteudo)
            self._visualizada = True
        else:
            print("*" * len(self._conteudo))

    def tipo(self):
        return "Única"

    def __str__(self):
        return f'[ÚNICA] - {self.status()}' 


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
        chave = input("Digite a chave: ")
        mensagens.append(MensagemProtegida(conteudo, chave))

    elif tipo == "3":
        mensagens.append(MensagemUnica(conteudo))

    else:
        print("❌ Opção inválida")
        return
         
    print("✅ Mensagem criada com sucesso!")


def listar_mensagens():
    print('\n===== Mensagens Cadastradas =====')
    
    if not mensagens:
        print("❌ Nenhuma mensagem cadastrada.")
        return
    
    for i, msg in enumerate(mensagens):
        print(f'{i} - {msg}')


def visualizar_mensagem():
    if not mensagens:
        print('❌ Nenhuma mensagem cadastrada!')
        return
    
    try:
        indice = int(input('Digite o índice da mensagem: '))
        mensagens[indice].visualizar()
    except (IndexError, ValueError):
        print(f'❌ Índice inválido.')


def alternar_mensagem_protegida():
    if not mensagens:
        print('❌ Nenhuma mensagem cadastrada!')
        return
    
    try:
        indice = int(input('Digite o índice da mensagem: '))
        msg = mensagens[indice]

        if isinstance(msg, MensagemProtegida):
            msg.alternar_trava()
        else:
            print("❌ Essa mensagem não é protegida.")
    except (IndexError, ValueError):
        print('❌ Índice inválido.')


def remover_mensagem():
    if not mensagens:
        print('❌ Nenhuma mensagem cadastrada!')
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


def menu():
    while True:
        print("\n===== MURAL DE MENSAGENS =====")
        print("1 - Criar mensagem")
        print("2 - Listar mensagens")
        print("3 - Visualizar mensagem")
        print("4 - Remover mensagem")
        print("5 - Trancar/Destrancar mensagem protegida")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print('❌ Opção inválida!')
            continue

        if opcao == 0: sair()
        elif opcao == 1: criar_mensagem()
        elif opcao == 2: listar_mensagens()
        elif opcao == 3: visualizar_mensagem()
        elif opcao == 4: remover_mensagem()
        elif opcao == 5: alternar_mensagem_protegida()
        else:
            print('❌ Opção inválida! Tente novamente.')


menu()