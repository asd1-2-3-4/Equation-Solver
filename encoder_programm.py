def check_last(input):
	if out_list[-1] == "1." or out_list[-1] == "2." or out_list[-1] == "3." or out_list[-1] == "4." or out_list[-1] == "5." or out_list[-1] == "6." or out_list[-1] == "7." or out_list[-1] == "8." or out_list[-1] == "9." or out_list[-1] == "0." or out_list[-1] == "x." or out_list[-1] == "y." or out_list[-1] == "z." or out_list[-1] == "a." or out_list[-1] == "b." or out_list[-1] == "c.":
		out_list.append("**"+input)
		
	else:
		out_list.append(input)
	

def encode_programm(equation):
	global out_list
	equation = list(equation)
	out_list = []
	for i in range(0, len(equation)):
		if equation[i] == "¹":
			check_last("1")
		else:
			if equation[i] == "²":
				check_last("2")
			else:
				if equation[i] == "³":
					check_last("3")
				else:
					if equation[i] == "⁴":
						check_last("4")
					else:
						if equation[i] == "⁵":
							check_last("5")
						else:
							if equation[i] == "⁶":
								check_last("6")
							else:
								if equation[i] == "⁷":
									check_last("7")
								else:
									if equation[i] == "⁸":
										check_last("8")
									else:
										if equation[i] == "⁹":
											check_last("9")
										else:
											if equation[i] == "⁰":
												check_last("0")
											else:
												out_list.append(equation[i] + ".")
	for i in range(0, len(out_list)):
		if len(out_list[i]) == 2:
			out_list[i] = list(out_list[i]).pop(0)
	out_list1 = out_list
	out_list = ""
	for i in range(0, len(out_list1)):
		out_list += out_list1[i]
	
	return out_list


