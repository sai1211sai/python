def transpose(M1):
    M2=[]  
    for i in range(len(M1[0])): 
        row =[] 
        for j in range (len(M1)):  
            row.append(M1[j][i]) 
        M2.append(row) 
    return M2 

M1 = [[4, 5, 3, 9], [7, 1, 8, 2], [5, 6, 4, 7]] 
print(transpose(M1))     
  