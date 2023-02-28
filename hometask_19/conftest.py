import pytest
from triangle import Triangle


@pytest.fixture()
def triangle_declaration():
    tri = Triangle(9, 8, 7)
    yield tri
    del tri


@pytest.fixture()
def triangle_for_not_equal():
    sec_tri = Triangle(6, 8, 7)
    yield sec_tri
    del sec_tri


@pytest.fixture(scope='function')
def square_res(triangle_declaration):
    yield triangle_declaration.square()
    