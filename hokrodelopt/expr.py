import sympy


class HOBOExpr:
    "for general expressions"

    def __init__(self, expr):
        self.expr = expr

    def __add__(self, other):
        """for expressions of the form (var1 + var2)"""
        return HOBOExpr(self.expr + other.expr)

    def __radd__(self, other):
        """for expressions of the form (var1 + var2) from right"""
        return self.__add__(other)

    def __mul__(self, other):
        """for expressions of the form (var1 * var2)"""
        return HOBOExpr(self.expr * other.expr)

    def __rmul__(self, other):
        """for expressions of the form (var1 * var2) from right"""
        return self.__mul__(other)

    def __sub__(self, other):
        """for expressions of the form (var1 - var2)"""
        return self.__add__(-other)

    def __pow__(self, order):
        """for expressions of the form (base ** exponent)"""
        if isinstance(order, int) and order >= 1:
            return HOBOExpr(self.expr ** order.expr)
        else:
            return sympy.Integer(1)

    def __div__(self, other):
        """for expressions of the form (var1 - var2)"""
        return HOBOExpr(self.expr / other.expr)

    def __neg__(self):
        """for expressions of the form (-var)"""
        return HOBOExpr(self.expr * sympy.Integer(-1))

    def __pos__(self):
        """for expressions of the form (+var)"""
        return HOBOExpr(self.expr)


class BinVar(HOBOExpr):
    pass


class SpinVar(HOBOExpr):
    pass


class IntVar(HOBOExpr):
    pass
