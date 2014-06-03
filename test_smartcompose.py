from smartcompose import delegate


@delegate('_n', ('__add__', '__mul__'))
class NumberWrapper:
    """
    NumberWrapper
    """
    def __init__(self, n):
        self._n = n


def test_delegate():
    n = NumberWrapper(2)
    assert n + 1 == 3
    assert n * 3 == 6


def test_docstring():
    assert 'NumberWrapper' in NumberWrapper.__doc__


sequence_methods = [
    '__iter__',
    '__next__',
    '__getitem__',
    '__setitem__',
    '__delitem__',
    '__len__',
    '__bool__',
]


arithmetic_methods = [
    '__add__',
    '__mul__',
    '__sub__',
    '__truediv__',
    '__floordiv__',
    '__mod__',
    '__divmod__',
    '__pow__',
]
r_arithmetic_methods = ['__r' + method[2:] for method in arithmetic_methods]


@delegate('_contents', sequence_methods)
@delegate('_number', arithmetic_methods + r_arithmetic_methods)
class NumberedBag:
    def __init__(self, contents=None, number=1):
        self._contents = contents or []
        self._number = number


def test_double_delegation():
    bag = NumberedBag(['a', 'b', 'c'], 12)
    assert len(bag) == 3
    assert bag/2 == 6
    assert 2**bag == 4096
    assert bag[1] == 'b'
    del bag[1]
    assert bag[1] == 'c'
    bag[0] = 'A'
    assert bag[0] == 'A'
