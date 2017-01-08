from piskvorky import vyhodnot

def test_vyhodnot_vyhru_x():
    pole = '-xxx----------------'
    assert len(pole) == 20
    assert vyhodnot(pole) == 'x'

def test_vyhodnot_vyhru_o():
    pole = 'ooo-----------------'
    assert vyhodnot(pole) == 'o'

def test_vyhodnot_remizu():
    pole = 'xoxo'
    assert vyhodnot(pole) == '!'
