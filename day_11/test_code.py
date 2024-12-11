from day_11.code import advent_1, advent_2

def test_advent_1_6():
    assert advent_1("""125 17
""", 6) == 22
    
def test_advent_1_25():
    assert advent_1("""125 17
""", 25) == 55312

def test_advent_2():
    assert advent_2("""125 17
""", 25) == 55312