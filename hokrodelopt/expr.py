import sympy as sm


class HOBOExpr:
    """for general expressions"""

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
        if isinstance(self, int) and isinstance(order, int) and order >= 0:
            return sm.Integer(self) ** sm.Integer(order)
        elif isinstance(self, int) and isinstance(order, int) and order < 0:
            return sm.Integer(1) / (sm.Integer(self) ** sm.Integer(abs(order)))
        elif isinstance(order, int) and order >= 1:
            return HOBOExpr(self.expr ** sm.Integer(order))
        elif isinstance(order, int) and order == 0:
            return sm.Integer(1)
        else:
            raise TypeError("order cannot be negative.")

    def __div__(self, other):
        """for expressions of the form (var1 / var2)"""
        return HOBOExpr(self.expr / sm.Float(other))

    def __neg__(self):
        """for expressions of the form (-var)"""
        return HOBOExpr(self.expr * sm.Integer(-1))

    def __pos__(self):
        """for expressions of the form (+var)"""
        return HOBOExpr(self.expr)


class BinVar(HOBOExpr):
    pass


class SpinVar(HOBOExpr):
    pass


class IntVar(HOBOExpr):
    pass
