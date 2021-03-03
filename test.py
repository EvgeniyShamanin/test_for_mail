import pytest


def my_func(array):
    for item in array:
        if not isinstance(item, float):
            raise TypeError('Not_Float')
    return tuple(array)


def add(a, b):
    c = a + b
    return c


def even(a, b):
    if not all(map(lambda p: isinstance(p, (int, float)), (a, b),)):
        raise TypeError("Not_valid")
    try:
        c = a / b
    except ZeroDivisionError as error:
        print(error)
    else:
        return a, b, c


def test_tuple():
    res = my_func([1.3, 2.2, 3.4])
    assert isinstance(res, tuple)


def test_float():
    with pytest.raises(TypeError) as exc_info:
        my_func([1.3, '', 2.3])
    assert str(exc_info.value) == 'Not_Float'


@pytest.mark.parametrize("args, expected", [
    ((1, 2), 3),
    (("hello", " world"), "hello world"),
])
def test_add(args, expected):
    res = add(*args)
    assert res == expected


def test_even():
    with pytest.raises(TypeError) as exc_info:
        even(0, "dfs")
    assert str(exc_info.value) == 'Not_valid'


@pytest.mark.xfail()
def test_even_zero():
    even(1, 0)


def test_even_resolve():
    res = even(4, 2)
    assert res == (4, 2, 2)





