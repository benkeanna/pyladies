from piskvorky import tah_pocitace

def test_tah_pocitace_pocet_o():
    pole = tah_pocitace('--------------------')
    assert pole.count('o') == 1

def test_tah_pocitace_pocet_nic():
    pole = tah_pocitace('--------------------')
    assert pole.count('-') == 19

def test_tah_pocitace_delka():
    pole = tah_pocitace('--------------------')
    assert len(pole) == 20
