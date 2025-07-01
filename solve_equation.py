from encoder_programm import check_last, encode_programm
from add_multiplication import add_multiplication
from remove_spaces import remove_spaces
from parser import parse
from factorization import factorize
from root_sort import root_sort
from display_roots import display_roots
from sympy import symbols, solve, sqrt

q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m= symbols('q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m')

def solve_equation(equation, show_imaginary_roots=False, presentable_mode=False):
	# Решение уравнения
	try:
		equation = equation.split(',', 1)
		equation[0] =factorize(add_multiplication(encode_programm(remove_spaces(equation[0]))))
		answer = parse(equation[0], equation[1])
	except Exception as e:
		return f"Ошибка решения: {e}"
		
	# Отображение ответа уравнения
	try:
		for i in range(0, len(answer)):
			answer[i] = str(answer[i])
		root1, root2 = root_sort(answer)
		if presentable_mode:
			return display_roots(root1, root2, show_imaginary_roots)
		else:
			if show_imaginary_roots:
				return root1, root2
			else:
				return root1
	except Exception as e:
		return f"Ошибка ввода. Уравнение введено в неправильном формате: {e}"
		
		
#Пример использования

#print(solve_equation(уравнение: x²=4, решить относительно: x))

#print(solve_equation("x² + 1 = 0, x", True, True))