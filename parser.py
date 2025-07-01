import sympy as sp


q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m= sp.symbols('q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m')

def parse(equation_string, variable):
    try:
        # Разделяем строку на левую и правую части
        left, right = equation_string.split("=")
        
        # Преобразуем строки в символьные выражения
        left_expr = sp.sympify(left.strip())
        right_expr = sp.sympify(right.strip())
        
        # Создаем уравнение
        equation = sp.Eq(left_expr, right_expr)
        
        # Решаем уравнение
        solution = sp.solve(equation, variable)
        return solution
    except Exception as e:
        print(f"Ошибка при решении уравнения: {e}")
        return None


#result = parse("40*t = 80", "t")
#print(result)

###