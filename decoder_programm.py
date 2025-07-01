degree_list = {
"0" : "⁰",
"1" : "¹",
"2" : "²",
"3" : "³",
"4" : "⁴",
"5" : "⁵",
"6" : "⁶",
"7" : "⁷",
"8" : "⁸",
"9" : "⁹",
}

def decode_programm(eq):
	new_eq = []
	helper_list = ""
	eq = list(eq)
	for i in range(0, len(eq)):
		if eq[i] == "*":
			if len(eq) > i+1:
				if eq[i+1] == "*":
					for n in range(i+2, len(eq)):
						if eq[n] != ' ' and eq[n] != '(' and eq[n] != '+' and eq[n] != '-' and eq[n] != '*':
							eq[n] = degree_list.get(eq[n])
						else:
							break
		else:
			new_eq.append(eq[i])
	for i in range(0, len(new_eq)):
		helper_list += new_eq[i]	
	new_eq = helper_list					
	return new_eq
						
						
#a = "x + x**2"						
#print(decode_programm(a))
					
	