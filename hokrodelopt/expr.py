import sympy as sm


class HOBOExpr:
    """
    It construct expressions using sympy.

    please refer to the sympy core:
        https://docs.sympy.org/latest/modules/core.html

    and to sympy logic:
        https://docs.sympy.org/dev/modules/logic.html

    """

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


class HOBOVar(HOBOExpr):
    """
    Examples
    --------
    >>> HOBOVar('x', lb=-10, ub=10)
    '-10 <= x <= 10'
    """

    @staticmethod
    def __is_valid_var_name(name):
        if len(name) < 1:
            raise ValueError("a varible name shouldn't be empty.")

        for char in name:
            if char.isspace():
                raise ValueError("a variable name shouldn't contain any spaces in it.")

    @staticmethod
    def __is_valid_var_lim(val):
        if not (val is None or isinstance(val, (int, float))):
            raise ValueError("variable limits must be numerical or None.")

    def __init__(self, name, lb, ub):
        HOBOExpr.__init__(self)
        self.name = name
        self.lb = lb
        self.ub = ub

    @property
    def name(self):
        """
        The variable name.
        """
        return self.name

    @name.setter
    def name(self, name):
        self.__is_valid_var_name(name)
        self.name = name

    @property
    def lb(self):
        return self.lb

    @lb.setter
    def lb(self, val):
        self.__is_valid_var_lim(val)
        self.lb = val

    @property
    def ub(self):
        return self.ub

    @ub.setter
    def ub(self, val):
        self.__is_valid_var_lim(val)
        self.ub = val

    def set_lims(self, lb, ub):
        if lb is not None and ub is not None and lb > ub:
            raise ValueError(
                "The given lower bound {} shouldn't be greater than the given ubber bound {}.".format(
                    lb, ub
                )
            )

        self.lb = lb
        self.ub = ub

    def __str__(self):
        if self.lb is not None:
            lb_str = str(self.lb) + " <= "
        else:
            lb_str = ""
        if self.ub is not None:
            ub_str = " <= " + str(self.ub)
        else:
            ub_str = ""
        return "".join((lb_str, super(HOBOVar, self).__str__(), ub_str))


class BinVar(HOBOVar):
    def __init__(self, name, lb=None, ub=None):
        HOBOVar.__init__(self, name=name, lb=lb, ub=ub)
        HOBOVar.set_lims(self, 0, 1)


class SpinVar(HOBOVar):
    def __init__(self, name, lb=None, ub=None):
        HOBOVar.__init__(self, name=name, lb=lb, ub=ub)
        HOBOVar.set_lims(self, -1, 1)


class IntVar(HOBOVar):
    def __init__(self, name, ub, lb=None):
        HOBOVar.__init__(self, name=name, lb=lb, ub=ub)
        HOBOVar.set_lims(self, 0, self.ub)
