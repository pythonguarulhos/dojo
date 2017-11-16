
# Versao inicial apenas com uso de funcao

def jokenpo(player1, player2):
    input_validos = ('pedra', 'tesoura', 'papel')
    player1 = player1.lower()
    player2 = player2.lower()
    if (player1 not in input_validos) or (player2 not in input_validos):
        return 'jogada inválida!'

    if player1 == player2:
        return 'empate'

    tabela_resultado = {
        'pedra': 'tesoura',
        'papel': 'pedra',
        'tesoura': 'papel'
    }

    if tabela_resultado[player1] == player2:
        ganhador = player1
    elif tabela_resultado[player2] == player1:
        ganhador = player2

    return f'ganhador: {ganhador}'


# Versao 2 com Orientacao a objetos

class Base:
    def __eq__(self, other):
        if not isinstance(other, Base):
            raise JokenpoError('Entrada Invalida')
        return isinstance(self, other.__class__)

    tabela_resultado = {
        'pedra': 'tesoura',
        'papel': 'pedra',
        'tesoura': 'papel'
    }

    def __gt__(self, other):
        if not isinstance(other, Base):
            raise JokenpoError('Entrada Invalida')
        type_self = self.__class__.__name__.lower()
        type_other = other.__class__.__name__.lower()
        return self.tabela_resultado[type_self] == type_other


class JokenpoError(Exception):
    """Erro customizado do jokenpo"""
    def __str__(self):
        return 'Entrada Invalida'


class Tesoura(Base):
    pass


class Papel(Base):
    pass


class Pedra(Base):
    pass
