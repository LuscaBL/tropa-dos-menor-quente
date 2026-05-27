class Mensagens:
    def __init__(self, conteudo):
        self._conteudo = conteudo
        self._disponivel = True
    
    def visualizar(self):
        print("Não dá pra visualizar")

    def status(self):
        if self._disponivel:
            return "Disponível"
        else:
            return "Indisponível"
    
    def editar(self, novo_conteudo):
        print("Não pode editar essa mensagem")
    
    def __str__(self):
        return f'[MENSAGEM] - {self.status()}'


class MensagemComum(Mensagens):
    def visualizar(self):
        if self._disponivel:
            print(self._conteudo)
        else:
            print("Mensagem indisponível")
    
    def editar(self, novo_conteudo):
        if self._disponivel:
            self._conteudo = novo_conteudo
            print("Mensagem editada")
        else:
            print("Não dá pra editar")

    def __str__(self):
        return f'[COMUM] - {self.status()}' 


class MensagemProtegida(Mensagens):
    def __init__(self, conteudo, chave):
        super().__init__(conteudo)
        self._chave = chave
        self._trancada = True

def visualizar(self):
    if not self._visualizada:
        print(self._conteudo)
        self._visualizada = True
        self._disponivel = False
    else:
        print("*" * len(self._conteudo))

    def alternar_trava(self):
        tentativa = input("Chave: ")
        if tentativa == self._chave:
            self._trancada = not self._trancada
            print("Mudou estado")
        else:
            print("Chave errada")

    def editar(self, novo_conteudo):
        if not self._disponivel:
            print("Indisponível")
        elif self._trancada:
            print("Tá trancada")
        else:
            self._conteudo = novo_conteudo
            print("Editada")

    def __str__(self):
        if self._trancada:
            estado = "Trancada"
        else:
            estado = "Destrancada"

        return f'[PROTEGIDA] - {self.status()} ({estado})'


class MensagemUnica(Mensagens):
    def __init__(self, conteudo):
        super().__init__(conteudo)
        self._visualizada = False

    def visualizar(self):
        if not self._visualizada:
            print(self._conteudo)
            self._visualizada = True
            self._disponivel = False
        else:
            print("*" * len(self._conteudo))

    def editar(self, novo_conteudo):
        if self._visualizada:
            print("Já foi vista")
        else:
            self._conteudo = novo_conteudo
            print("Editada")

    def __str__(self):
        return f'[ÚNICA] - {self.status()}' 


class SistemaMensagens:
    def __init__(self):
        self.mensagens = []

    def criar_mensagem(self):
        print("\n1 - Comum")
        print("2 - Protegida")
        print("3 - Única")
    
        tipo = input("Opção: ")
        conteudo = input("Conteúdo: ")
    
        if tipo == "1":
            self.mensagens.append(MensagemComum(conteudo))

        elif tipo == "2":
            chave = input("Chave: ")
            self.mensagens.append(MensagemProtegida(conteudo, chave))

        elif tipo == "3":
            self.mensagens.append(MensagemUnica(conteudo))

        else:
            print("Opção inválida")
            return
         
        print("Criada")

    def listar_mensagens(self):
        if not self.mensagens:
            print("Nada cadastrado")
            return
    
        for i in range(len(self.mensagens)):
            print(i, "-", self.mensagens[i])

    def visualizar_mensagem(self):
        if not self.mensagens:
            print("Nada cadastrado")
            return
    
        try:
            i = int(input("Índice: "))
            self.mensagens[i].visualizar()
        except:
            print("Erro")

    def editar_mensagem(self):
        if not self.mensagens:
            print("Nada cadastrado")
            return
    
        try:
            i = int(input("Índice: "))
            novo = input("Novo conteúdo: ")
            self.mensagens[i].editar(novo)
        except:
            print("Erro")

    def alternar_mensagem_protegida(self):
        if not self.mensagens:
            print("Nada cadastrado")
            return
    
        try:
            i = int(input("Índice: "))
            msg = self.mensagens[i]

            if isinstance(msg, MensagemProtegida):
                msg.alternar_trava()
            else:
                print("Não é protegida")
        except:
            print("Erro")

    def remover_mensagem(self):
        if not self.mensagens:
            print("Nada cadastrado")
            return
    
        try:
            i = int(input("Índice: "))
            self.mensagens.pop(i)
            print("Removida")
        except:
            print("Erro")


class InterfaceTexto:
    def __init__(self, sistema):
        self.sistema = sistema

    def menu(self):
        while True:   
            print("\n1 - Criar")
            print("2 - Listar")
            print("3 - Ver")
            print("4 - Editar mensagem")
            print("5 - Remover")
            print("6 - Trancar/destrancar")
            print("0 - Sair")

            try:
                op = int(input("Opção: "))
            except:
                print("Erro")
                continue

            if op == 0:
                break
            elif op == 1:
                self.sistema.criar_mensagem()
            elif op == 2:
                self.sistema.listar_mensagens()
            elif op == 3:
                self.sistema.visualizar_mensagem()
            elif op == 4:
                self.sistema.editar_mensagem()
            elif op == 5:
                self.sistema.remover_mensagem()
            elif op == 6:
                self.sistema.alternar_mensagem_protegida()
            else:
                print("Inválido")


sistema = SistemaMensagens()
interface = InterfaceTexto(sistema)
interface.menu()