from program import jokenpo
from program import Pedra, Papel, Tesoura, JokenpoError
import pytest


# Versao 1 com funcao
def test_pedra_tesoura():
    assert jokenpo('pedra', 'tesoura') == 'ganhador: pedra'
    assert jokenpo('tesoura', 'pedra') == 'ganhador: pedra'


def test_pedra_papel():
    assert jokenpo('pedra', 'papel') == 'ganhador: papel'
    assert jokenpo('papel', 'pedra') == 'ganhador: papel'


def test_papel_tesoura():
    assert jokenpo('papel', 'tesoura') == 'ganhador: tesoura'
    assert jokenpo('tesoura', 'papel') == 'ganhador: tesoura'


def test_pedra_pedra():
    assert jokenpo('pedra', 'pedra') == 'empate'


def test_papel_papel():
    assert jokenpo('papel', 'papel') == 'empate'


def test_tesoura_tesoura():
    assert jokenpo('tesoura', 'tesoura') == 'empate'


def test_input_invalido():
    assert jokenpo('tesoura', 'martelo') == 'jogada inválida!'
    assert jokenpo('martelo', 'tesoura') == 'jogada inválida!'


def test_input_maius():
    assert jokenpo('Tesoura', 'PAPEL') == 'ganhador: tesoura'


# Versao 2 com Orientacao a objetos

def test_pedra_tesoura_new():
    assert Pedra() > Tesoura()
    assert Tesoura() < Pedra()


def test_pedra_papel_new():
    assert Pedra() < Papel()
    assert Papel() > Pedra()


def test_papel_pedra_new():
    assert Papel() > Pedra()
    assert Pedra() < Papel()


def test_papel_tesoura_new():
    assert Papel() < Tesoura()
    assert Tesoura() > Papel()


def test_tesoura_papel_new():
    assert Tesoura() > Papel()
    assert Papel() < Tesoura()


def test_tesoura_pedra_new():
    assert Tesoura() < Pedra()
    assert Pedra() > Tesoura()


def test_tesoura_tesoura_new():
    assert Tesoura() == Tesoura()


def test_papel_papel_new():
    assert Papel() == Papel()


def test_pedra_pedra_new():
    assert Pedra() == Pedra()


def test_input_invalido_maior_new():
    with pytest.raises(JokenpoError):
        assert Pedra() > 'Invalido'


def test_input_invalido_igual_new():
    with pytest.raises(JokenpoError) as err:
        assert Pedra() == 'Invalido'
    assert str(err.value) == 'Entrada Invalida'
