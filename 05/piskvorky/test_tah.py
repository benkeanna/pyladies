from piskvorky import tah

def test_tah_x_na_pozici():
    pole = '-----'
    pozice = 2
    symbol = 'x'
    assert tah(pole, pozice, symbol) == '--x--'

def test_tah_delka_pole():
    pole = '-----'
    assert len(pole) == 5
