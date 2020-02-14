import input_data 										#input import
BLOSUM52=input_data.BLOSUM52
seq2=input_data.seq2
seq1=input_data.seq1

def NW_matrix(s1,s2,matrix,gap):
	score_m=[[0] * (len(s1)+1) for i in range(len(s2)+1)]			#create 2 equal matrix for score
	move_m=[[0] * (len(s1)+1) for i in range(len(s2)+1)]			#and movement of size(n+1)*(m+1)
	for i in range(1,len(s1)+1):			#initialize 1° row
		score_m[0][i]=i*gap 				#of score matrix
		move_m[0][i]="o"					#of move matrix
	for i in range(1,len(s2)+1):			#initialize 1° column
		score_m[i][0]=gap*i 				#of score matrix
		move_m[i][0]="v" 					#of move matrix
	for i in range(1,len(s2)+1): 								#for every row
		for j in range(1,len(s1)+1):							#for every colum in each row
			o=score_m[i][j-1]+gap								#compute score when adding a gap in s2
			v=score_m[i-1][j]+gap								#compute score when adding a gap in s1
			d=score_m[i-1][j-1]+matrix[s2[i-1]+s1[j-1]]			#compute score of alignign 2 AA
			best=max(o,v,d)										#select the highest
			score_m[i][j]=best									#put in in the cell
			if best==d:											#if best is equal to align
				move_m[i][j]="d"								#write letter corrisondig to align in move matrix
			elif best==v:										#if best is equal to gap in s2
				move_m[i][j]="v"								#write letter corrisondig to it in move matrix
			else:												#if best is equal to gap in s1
				move_m[i][j]="o"								#write letter corrisondig to it in move matrix
	return score_m, move_m				#return the 2 matrix

def allign(F,P,s1,s2):
	i=len(s2)		#start from bottom left corner (x and y coordinate given) X
	j=len(s1)		# Y
	score=F[i][j]	#which corrispond to the alignment score
	all1=""			#2 empty string for backtracking
	all2=""
	while i!=0 and j!=0:	#until we are on the 1° cell
		if P[i][j]=="d":	#if move matix has d we align the 2 residues
			all1=all1+s1[j-1]	#add the one we are considering for s1
			all2=all2+s2[i-1]	#add the one we are considering for s2
			i-=1	#move x and y pointer in the matrix
			j-=1
		elif P[i][j]=="v": #if move matix has v
			all1=all1+"-" #we add gap in s1 
			all2=all2+s2[i-1] # and align residues in s2 in the alignment
			i-=1		#move X pointer
		elif P[i][j]=="o": #if move matix has o
			all1=all1+s1[j-1] #we add residues in s1
			all2=all2+"-"	#and add gapp in s2 in the alignment
			j-=1	#move Y pointer
	all1=all1[::-1] #reverse the 2 string, because they are written backwards
	all2=all2[::-1]
	res=all1+"\n" + all2 #string with alignment
	return res,score #return aligment and score

matrix=NW_matrix(seq1,seq2,BLOSUM52,-2)  #compute 2 matrix, gap penality is set to -2
result=allign(matrix[0],matrix[1],seq1,seq2) #use matrix obtained before to get the alignment
print(result[0],result[1]) #and print it with it's score