def remove_spaces(removing):
	removing1 = list(removing)
	removing1 = list(removing)
	for i in range(0, len(removing)):
		if removing[i] == ' ':
			removing1.remove(removing[i])	
	removing = ""
	for i in range(0, len(removing1)):
		removing += removing1[i]
	return removing
	
#print(remove_spaces("3 = 32s d d"))