import sys
import math


def parse_coef(text, nonzero=False):
    
    try:
        value = float(text)
    except (ValueError, TypeError):
        return None
    match (math.isfinite(value), value):
        case (False, _):
            return None
        case (True, 0.0) if nonzero:
            return None
        case _:
            return value


def ask_coef(prompt, nonzero):
    
    print(prompt)
    value = parse_coef(input(), nonzero)
    if value is None:
        print('Некорректное значение, повторите ввод.')
        return ask_coef(prompt, nonzero)
    return value


def get_coef(index, prompt, nonzero=False):
    arg = sys.argv[index] if len(sys.argv) > index else None
    value = parse_coef(arg, nonzero)
    return value if value is not None else ask_coef(prompt, nonzero)


def y_roots(a, b, c):
    
    D = b*b - 4*a*c
    match D:
        case _ if D < 0.0:
            return ()
        case 0.0:
            return (-b / (2.0*a),)
        case _:
            sqD = math.sqrt(D)
            return ((-b + sqD) / (2.0*a), (-b - sqD) / (2.0*a))


def x_roots(y):
    
    match y:
        case 0.0:
            return (0.0,)
        case _ if y > 0.0:
            return (math.sqrt(y), -math.sqrt(y))
        case _:
            return ()


def get_roots(a, b, c):
    
    return tuple(sorted({x for y in set(y_roots(a, b, c)) for x in x_roots(y)}))


def format_roots(roots):
    
    match roots:
        case ():
            return 'Нет действительных корней'
        case (x1,):
            return 'Один корень: {}'.format(x1)
        case (x1, x2):
            return 'Два корня: {} и {}'.format(x1, x2)
        case (x1, x2, x3):
            return 'Три корня: {}, {} и {}'.format(x1, x2, x3)
        case (x1, x2, x3, x4):
            return 'Четыре корня: {}, {}, {} и {}'.format(x1, x2, x3, x4)


def main():
    a = get_coef(1, 'Введите коэффициент А:', nonzero=True)
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    print(format_roots(get_roots(a, b, c)))


if __name__ == "__main__":
    main()

