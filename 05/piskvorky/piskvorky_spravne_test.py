from piskvorky import vyhodnot

def test_vyhodnot_vyhral_o():
    assert vyhodnot('----oooxx--') == 'o'
