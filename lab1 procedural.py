import sys
import math


def get_coef(index, prompt, nonzero=False):
    
    coef_str = sys.argv[index] if len(sys.argv) > index else None
    while True:
        if coef_str is None:
            print(prompt)
            coef_str = input()
        try:
            coef = float(coef_str)
            if math.isfinite(coef) and (not nonzero or coef != 0.0):
                return coef
        except ValueError:
            pass
        print('Некорректное значение, повторите ввод.')
        coef_str = None


def get_roots(a, b, c):
    
    result = []
    D = b*b - 4*a*c
    if D < 0.0:
        return result
    sqD = math.sqrt(D)
    
    ys = {(-b + sqD) / (2.0*a), (-b - sqD) / (2.0*a)}
    for y in ys:
        if y == 0.0:
            result.append(0.0)
        elif y > 0.0:
            sqY = math.sqrt(y)
            result.append(sqY)
            result.append(-sqY)
    return sorted(result)


def print_roots(roots):
    
    if len(roots) == 0:
        print('Нет действительных корней')
    else:
        print('Количество действительных корней: {}'.format(len(roots)))
        for i, root in enumerate(roots, 1):
            print('x{} = {}'.format(i, root))


def main():
    
    a = get_coef(1, 'Введите коэффициент А:', nonzero=True)
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a, b, c)
    print_roots(roots)



if __name__ == "__main__":
    main()

