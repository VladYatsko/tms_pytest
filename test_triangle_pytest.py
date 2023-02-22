from triangle import Triangle


def test_triangle_eq(triangle_declaration):
    third = Triangle(9, 8, 7)
    assert triangle_declaration.__eq__(third)


def test_triangle_nq(triangle_declaration, triangle_for_not_equal):
    assert triangle_declaration.__ne__(triangle_for_not_equal)


def test_triangle_perimetr(triangle_declaration):
    assert triangle_declaration.perimetr() ==\
           triangle_declaration.a + triangle_declaration.b + triangle_declaration.c
    

def test_less_than(triangle_declaration, triangle_for_not_equal):
    assert triangle_for_not_equal.__le__(triangle_declaration)


def test_greater_than(triangle_declaration, triangle_for_not_equal):
    assert triangle_declaration.__ge__(triangle_for_not_equal)


def test_square(triangle_declaration, square_res):
    assert triangle_declaration.square() == square_res


def test_del(triangle_declaration):
    assert triangle_declaration.__del__() is None
    
