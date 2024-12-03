from day_03.code import advent_1, advent_2

def test_advent_1():
    assert advent_1("""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""") == 161

def test_advent_2():
    assert advent_2("""xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""") == 48