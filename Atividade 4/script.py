class Playlist(list):
    def __init__(self, nome, programas):
        super().__init__(programas)
        self.nome = nome
        self._programas = programas

    def __getitem__(self, s):
        return self._programas[s]
        

class Programa():
    def __init__(self, nome, ano):
        self._nome = str(nome).title()
        self.ano = ano
        self._likes = 0

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}'

    def incrementarLike(self):
        self._likes += 1
        return 0

    @property
    def likes(self):
        return self._likes
    @property
    def nome(self):
        return self._nome
    @nome.setter 
    def nome(self, novo_nome):
        self._nome = novo_nome

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes: {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._likes}'

vingadores = Filme("vingadores - guerra infinita", 2019, 1.5)
Atlantis = Serie("Atlantis", 2019, 3)

programas = [vingadores, Atlantis]
playlistPraNoite = Playlist('Playlist para noite', programas)

for programa in playlistPraNoite:
    print(programa)