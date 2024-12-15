from day_12.code import advent_1, advent_2

def test_advent_1_1():
    assert advent_1("""AAAA
BBCD
BBCC
EEEC
""") == 140
    
def test_advent_1_2():
    assert advent_1("""OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
""") == 772
    
def test_advent_1_3():
    assert advent_1("""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""") == 1930


def test_advent_2():
    assert advent_2("""AAAA
BBCD
BBCC
EEEC
""") == 80
    
def test_advent_2_2():
    assert advent_2("""OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
""") == 436
    
def test_advent_2_3():
    assert advent_2("""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""") == 1206
    
def test_advent_2_4():
    assert advent_2("""AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
""") == 368
    
def test_advent_2_5():
    assert advent_2("""EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
""") == 236
