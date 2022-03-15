import sympy


class HOBOExpr:
    "for general expressions"

    def __new__(cls, name):
        if isinstance(name, str):
            expr = sympy.Symbol(name)
        else:
            expr = sympy.Symbol(str(name))

        return expr

    def __init__(self, name):
        super(HOBOExpr, self).__init__()

    def __add__(self, other):
        """for expressions of the form (var1 + var2)"""
        return sympy.Add(self, other)

    def __radd__(self, other):
        """for expressions of the form (var1 + var2) from right"""
        return self.__add__(other)

    def __mul__(self, other):
        """for expressions of the form (var1 * var2)"""
        return sympy.Mul(self, other)

    def __rmul__(self, other):
        """for expressions of the form (var1 * var2) from right"""
        return self.__mul__(other)

    def __sub__(self, other):
        """for expressions of the form (var1 - var2)"""
        return self.__add__(-other)

    def __pow__(self, order):
        """for expressions of the form (base ** exponent)"""
        return sympy.Pow(self, order)


class BinVar(HOBOExpr):
    pass


class SpinVar(HOBOExpr):
    pass


class IntVar(HOBOExpr):
    pass
