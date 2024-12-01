from day_01.code import advent_1, advent_2

def test_advent_1():
    assert advent_1("""3   4
4   3
2   5
1   3
3   9
3   3
""") == 11

def test_advent_2():
    assert advent_2("""3   4
4   3
2   5
1   3
3   9
3   3
""") == 31