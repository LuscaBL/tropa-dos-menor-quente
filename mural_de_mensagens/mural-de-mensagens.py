# =========================
# EXCEÇÕES
# =========================

class MensagemError(Exception):
    """Exceção base para erros relacionados a mensagens."""
    pass

class MensagemIndisponivelError(MensagemError):
    """Erro lançado quando a mensagem não está disponível."""
    pass

class MensagemTrancadaError(MensagemError):
    """Erro lançado ao tentar editar uma mensagem trancada."""
    pass

class ChaveIncorretaError(MensagemError):
    """Erro lançado quando a chave informada está incorreta."""
    pass

# =========================
# CLASSE BASE
# =========================

class Mensagens:
    """
    Classe base que representa uma mensagem genérica no sistema.
    
    Define atributos e operações comuns a todos os tipos de mensagens.
    """

    def __init__(self, conteudo: str) -> None:
        """
        Inicializa uma mensagem.

        :param conteudo: Texto da mensagem
        """
        self._conteudo: str = conteudo
        self._disponivel: bool = True
    
    def visualizar(self) -> None:
        """
        Método abstrato para visualizar a mensagem.

        Raises:
            MensagemError: Caso o método não seja implementado na subclasse.
        """
        raise MensagemError("Não dá pra visualizar")

    def status(self) -> str:
        """
        Retorna o status da mensagem.

        :return: "Disponível" ou "Indisponível"
        """
        return "Disponível" if self._disponivel else "Indisponível"
    
    def editar(self, novo_conteudo: str) -> None:
        """
        Método abstrato para edição da mensagem.

        :param novo_conteudo: Novo conteúdo da mensagem

        Raises:
            MensagemError: Caso a mensagem não possa ser editada.
        """
        raise MensagemError("Não pode editar essa mensagem")
    
    def __str__(self) -> str:
        """
        Retorna representação textual da mensagem.

        :return: String formatada com status
        """
        return f'[MENSAGEM] - {self.status()}'

# =========================
# MENSAGEM COMUM
# =========================

class MensagemComum(Mensagens):
    """
    Representa uma mensagem comum, que pode ser visualizada e editada livremente.
    """

    def visualizar(self) -> None:
        """
        Exibe o conteúdo da mensagem.

        Raises:
            MensagemIndisponivelError: Caso a mensagem não esteja disponível.
        """
        if self._disponivel:
            print(self._conteudo)
        else:
            raise MensagemIndisponivelError("Mensagem indisponível")
    
    def editar(self, novo_conteudo: str) -> None:
        """
        Atualiza o conteúdo da mensagem.

        :param novo_conteudo: Novo texto da mensagem

        Raises:
            MensagemIndisponivelError: Caso a mensagem não esteja disponível.
        """
        if self._disponivel:
            self._conteudo = novo_conteudo
            print("Mensagem editada")
        else:
            raise MensagemIndisponivelError("Não dá pra editar")

    def __str__(self) -> str:
        """
        Retorna representação textual da mensagem comum.
        """
        return f'[COMUM] - {self.status()}' 

# =========================
# MENSAGEM PROTEGIDA
# =========================

class MensagemProtegida(Mensagens):
    """
    Representa uma mensagem protegida por chave, que pode ser trancada ou destrancada.
    """

    def __init__(self, conteudo: str, chave: str) -> None:
        """
        Inicializa a mensagem protegida.

        :param conteudo: Texto da mensagem
        :param chave: Chave de acesso
        """
        super().__init__(conteudo)
        self._chave: str = chave
        self._trancada: bool = True

    def visualizar(self) -> None:
        """
        Exibe o conteúdo da mensagem.

        Raises:
            MensagemIndisponivelError: Caso a mensagem não esteja disponível.
        """
        if self._disponivel:
            print(self._conteudo)
        else:
            raise MensagemIndisponivelError("Mensagem indisponível")

    def alternar_trava(self) -> None:
        """
        Alterna o estado de trava da mensagem mediante verificação de chave.

        Raises:
            ChaveIncorretaError: Caso a chave informada seja inválida.
        """
        tentativa: str = input("Chave: ")
        if tentativa == self._chave:
            self._trancada = not self._trancada
            print("Mudou estado")
        else:
            raise ChaveIncorretaError("Chave errada")

    def editar(self, novo_conteudo: str) -> None:
        """
        Edita o conteúdo da mensagem protegida.

        :param novo_conteudo: Novo texto da mensagem

        Raises:
            MensagemIndisponivelError: Caso a mensagem esteja indisponível
            MensagemTrancadaError: Caso a mensagem esteja trancada
        """
        if not self._disponivel:
            raise MensagemIndisponivelError("Indisponível")
        elif self._trancada:
            raise MensagemTrancadaError("Tá trancada")
        else:
            self._conteudo = novo_conteudo
            print("Editada")

    def __str__(self) -> str:
        """
        Retorna representação textual da mensagem protegida.
        """
        estado: str = "Trancada" if self._trancada else "Destrancada"
        return f'[PROTEGIDA] - {self.status()} ({estado})'

# =========================
# MENSAGEM ÚNICA
# =========================

class MensagemUnica(Mensagens):
    """
    Representa uma mensagem que pode ser visualizada apenas uma vez.
    """

    def __init__(self, conteudo: str) -> None:
        """
        Inicializa a mensagem única.

        :param conteudo: Texto da mensagem
        """
        super().__init__(conteudo)
        self._visualizada: bool = False

    def visualizar(self) -> None:
        """
        Exibe o conteúdo apenas na primeira visualização.

        Após isso, a mensagem se torna indisponível.
        """
        if not self._visualizada:
            print(self._conteudo)
            self._visualizada = True
            self._disponivel = False
        else:
            print("*" * len(self._conteudo))

    def editar(self, novo_conteudo: str) -> None:
        """
        Edita o conteúdo da mensagem.

        :param novo_conteudo: Novo texto da mensagem

        Raises:
            MensagemIndisponivelError: Caso a mensagem já tenha sido visualizada
        """
        if self._visualizada:
            raise MensagemIndisponivelError("Já foi vista")
        else:
            self._conteudo = novo_conteudo
            print("Editada")

    def __str__(self) -> str:
        """
        Retorna representação textual da mensagem única.
        """
        return f'[ÚNICA] - {self.status()}' 

# =========================
# SISTEMA
# =========================

class SistemaMensagens:
    """
    Gerencia o conjunto de mensagens do sistema.
    """

    def __init__(self) -> None:
        """Inicializa o sistema com uma lista vazia de mensagens."""
        self.mensagens: list[Mensagens] = []

    def criar_mensagem(self) -> None:
        """Cria uma nova mensagem com base na escolha do usuário."""
        print("\n1 - Comum")
        print("2 - Protegida")
        print("3 - Única")
    
        tipo: str = input("Opção: ")
        conteudo: str = input("Conteúdo: ")
    
        if tipo == "1":
            self.mensagens.append(MensagemComum(conteudo))

        elif tipo == "2":
            chave: str = input("Chave: ")
            self.mensagens.append(MensagemProtegida(conteudo, chave))

        elif tipo == "3":
            self.mensagens.append(MensagemUnica(conteudo))

        else:
            print("Opção inválida")
            return
         
        print("Criada")

    def listar_mensagens(self) -> None:
        """Lista todas as mensagens cadastradas."""
        if not self.mensagens:
            print("Nada cadastrado")
            return
    
        for i, msg in enumerate(self.mensagens):
            print(i, "-", msg)

    def visualizar_mensagem(self) -> None:
        """Permite visualizar uma mensagem pelo índice."""
        if not self.mensagens:
            print("Nada cadastrado")
            return
    
        try:
            i: int = int(input("Índice: "))
            self.mensagens[i].visualizar()
        except (ValueError, IndexError, MensagemError) as e:
            print("Erro:", e)

    def editar_mensagem(self) -> None:
        """Permite editar uma mensagem pelo índice."""
        if not self.mensagens:
            print("Nada cadastrado")
            return
    
        try:
            i: int = int(input("Índice: "))
            novo: str = input("Novo conteúdo: ")
            self.mensagens[i].editar(novo)
        except (ValueError, IndexError, MensagemError) as e:
            print("Erro:", e)

    def alternar_mensagem_protegida(self) -> None:
        """Alterna o estado de trava de uma mensagem protegida."""
        if not self.mensagens:
            print("Nada cadastrado")
            return
    
        try:
            i: int = int(input("Índice: "))
            msg: Mensagens = self.mensagens[i]

            if isinstance(msg, MensagemProtegida):
                msg.alternar_trava()
            else:
                print("Não é protegida")
        except (ValueError, IndexError, MensagemError) as e:
            print("Erro:", e)

    def remover_mensagem(self) -> None:
        """Remove uma mensagem pelo índice."""
        if not self.mensagens:
            print("Nada cadastrado")
            return
    
        try:
            i: int = int(input("Índice: "))
            self.mensagens.pop(i)
            print("Removida")
        except (ValueError, IndexError) as e:
            print("Erro:", e)

# =========================
# INTERFACE
# =========================

class InterfaceTexto:
    """
    Interface de interação via terminal com o sistema de mensagens.
    """

    def __init__(self, sistema: SistemaMensagens) -> None:
        """
        Inicializa a interface.

        :param sistema: Instância do sistema de mensagens
        """
        self.sistema: SistemaMensagens = sistema

    def menu(self) -> None:
        """Exibe o menu principal e processa as ações do usuário."""
        while True:   
            print("\n1 - Criar")
            print("2 - Listar")
            print("3 - Ver")
            print("4 - Editar mensagem")
            print("5 - Remover")
            print("6 - Trancar/destrancar")
            print("0 - Sair")

            try:
                op: int = int(input("Opção: "))
            except ValueError:
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

# =========================
# EXECUÇÃO
# =========================

sistema = SistemaMensagens()
interface = InterfaceTexto(sistema)
interface.menu()