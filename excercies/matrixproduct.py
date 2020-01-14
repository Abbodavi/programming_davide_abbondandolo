A=[[2,4],
   [3,1]]
B=[[2,1],
   [1,3]]
C=[]
for i in range(len(A)):
	row=[]
	for j in range(len(A)):
		prod=0
		for k in range(len(A)):
			prod=prod+A[i][k]*B[j][k]
		row.append(prod)
	C.append(row)	
print(C)