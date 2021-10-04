class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    josmar = Pessoa(nome='Josmar')
    vinicius = Pessoa(josmar, nome='Vinicius')
    print(Pessoa.cumprimentar(vinicius))
    print(id(vinicius))
    print(vinicius.cumprimentar())
    print(vinicius.nome)
    print(vinicius.idade)
    for filho in vinicius.filhos:
        print(filho.nome)
    vinicius.sobrenome = 'Valerio'
    del vinicius.filhos
    print(vinicius.__dict__)
    print(josmar.__dict__)