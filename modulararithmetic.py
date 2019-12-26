import numbers
from functools import total_ordering
import operator

@total_ordering
class Mod:
    def __init__(self, value, modulus):
        self.modulus = modulus
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, numbers.Integral):
            raise TypeError('The value must be an integer.')
        self._value = value % self.modulus

    @property
    def modulus(self):
        return self._modulus

    @modulus.setter
    def modulus(self, value):
        if not isinstance(value, numbers.Integral):
            raise TypeError('The modulus must be an integer.')
        if value < 0:
            raise ValueError('The modulus must be a positive number.')
        self._modulus = value

    def _get_other_value(self, other):
        if isinstance(other, numbers.Integral):
            return other % self.modulus
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return other.value
        return TypeError('Incompatible Types')

    def _perform_operation(self, other, op, *, in_place=False):
        other_value = self._get_other_value(other)
        new_value = op(self.value, other_value)
        if in_place:
            self.value = new_value % self.modulus
        else:
            return Mod(new_value, self.modulus)

    def __eq__(self, other):
        other_value = self._get_other_value(other)
        return self.value == other_value

    def __hash__(self):
        return hash((self.value, self.modulus))

    def __int__(self):
        return self.value

    def __repr__(self):
        return 'Mod(value={}, modulus={})'.format(self.value, self.modulus)

    def __add__(self, other):
        other_value = self._get_other_value(other)
        return self._perform_operation(other, operator.add, in_place=False)

    def __iadd__(self, other):
        other_value = self._get_other_value(other)
        return self._perform_operation(other, operator.add, in_place=True)

    def __sub__(self, other):
        other_value = self._get_other_value(other)
        return self._perform_operation(other, operator.sub, in_place=False)

    def __isub__(self, other):
        other_value = self._get_other_value(other)
        return self._perform_operation(other, operator.sub, in_place=True)

    def __mul__(self, other):
        other_value = self._get_other_value(other)
        return self._perform_operation(other, operator.mul, in_place=False)

    def __imul__(self, other):
        other_value = self._get_other_value(other)
        return self._perform_operation(other, operator.mul, in_place=True)

    def __pow__(self, other):
        other_value = self._get_other_value(other)
        return self._perform_operation(other, operator.pow, in_place=False)

    def __ipow__(self, other):
        other_value = self._get_other_value(other)
        return self._perform_operation(other, operator.add, in_place=True)

    def __neg__(self):
        self.value = -self.value
        return self

    def __lt__(self, other):
        other_value = self._get_other_value(other)
        return self.value < other_value
