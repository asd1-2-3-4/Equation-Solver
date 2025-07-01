def root_sort(root_list):
    Compl_root = []
    Normal = []
    
    for el in root_list:
        img = "I" in el  # Проверяем, есть ли "I" в строке
        if img:
            Compl_root.append(el)
        else:
            Normal.append(el)
    
    return Normal, Compl_root

#l = ["2", "1", "4I", "12*21*I", "5"]
#print(root_sort(l))