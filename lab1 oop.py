import sys
import math


class Coefficient:
    
    def __init__(self, index, prompt, nonzero=False):
        self.index = index
        self.prompt = prompt
        self.nonzero = nonzero
        self.value = self._read()

    def _is_correct(self, text):
        try:
            value = float(text)
        except ValueError:
            return False
        return math.isfinite(value) and not (self.nonzero and value == 0.0)

    def _read(self):
        text = sys.argv[self.index] if len(sys.argv) > self.index else None
        while text is None or not self._is_correct(text):
            if text is not None:
                print('Некорректное значение, повторите ввод.')
            print(self.prompt)
            text = input()
        return float(text)


class BiquadraticEquation:
   
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def discriminant(self):
        
        return self.b**2 - 4*self.a*self.c

    def _y_roots(self):
        D = self.discriminant
        if D < 0.0:
            return set()
        sqD = math.sqrt(D)
        return {(-self.b + sqD) / (2.0*self.a), (-self.b - sqD) / (2.0*self.a)}

    def get_roots(self):
        
        roots = []
        for y in self._y_roots():
            if y == 0.0:
                roots.append(0.0)
            elif y > 0.0:
                roots.extend([math.sqrt(y), -math.sqrt(y)])
        return sorted(roots)

    def print_roots(self):
        roots = self.get_roots()
        if not roots:
            print('Нет действительных корней')
            return
        print('Количество действительных корней: {}'.format(len(roots)))
        for i, root in enumerate(roots, 1):
            print('x{} = {}'.format(i, root))


def main():
    a = Coefficient(1, 'Введите коэффициент А:', nonzero=True).value
    b = Coefficient(2, 'Введите коэффициент B:').value
    c = Coefficient(3, 'Введите коэффициент C:').value
    BiquadraticEquation(a, b, c).print_roots()


if __name__ == "__main__":
    main()

