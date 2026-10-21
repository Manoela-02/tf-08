class Commit:
    """
    Representa um commit individual dentro do histórico de um repositório Git.
    Guarda as informações do commit e faz a referência para o commit anterior (pai).
    """
    def __init__(self, identificador, mensagem, autor, pai=None):
        self.identificador = identificador
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    def historico(self):
        """
        Método recursivo que imprime o commit atual no formato '#id mensagem (autor)'
        e delega para o commit pai fazer o mesmo, formando a cadeia do histórico.
        Caso base: se não houver pai, a recursão para (retorno antecipado).
        """
        print(f"#{self.identificador} {self.mensagem} ({self.autor})")
        
        if self.pai is None:
            return

        self.pai.historico()


class Repositorio:
    """
    Representa o Repositório Git, gerenciando o estado atual (head)
    e permitindo criar novos commits e inspecionar o histórico.
    """
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador_commits = 0

    def commitar(self, mensagem):
        """
        Cria um novo commit incrementando o identificador único, tendo o head atual
        como pai, e atualiza o head para apontar para este novo commit criado.
        """
        self.contador_commits += 1
        novo_commit = Commit(self.contador_commits, mensagem, self.autor, self.head)
        self.head = novo_commit

    def log(self):
        """
        Exibe todo o histórico de commits do repositório a partir do commit mais recente (head).
        Caso base: se o head for nulo, avisa que não há commits.
        """
        if self.head is None:
            print("Nenhum commit ainda")
            return

        self.head.historico()

    def total_de_commits(self):
        """
        Percorre a cadeia de commits partindo do head até a raiz utilizando um laço while,
        contando e devolvendo o número total de commits realizados.
        """
        quantidade = 0
        atual = self.head

        while atual is not None:
            quantidade += 1
            atual = atual.pai

        return quantidade


# Teste do repositório de commits conforme solicitado no roteiro
repositorio = Repositorio("meu-projeto", "Manoela Cordeiro da Silva - 6326244")
repositorio.log()
repositorio.commitar("Cria o projeto")
repositorio.commitar("Adiciona o README")
repositorio.commitar("Corrige o titulo do README")
repositorio.log()
print(repositorio.total_de_commits())
