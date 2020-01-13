gap=-2
score_matrix={}
score_matrix["AA"]=2
score_matrix["AC"]=-1
score_matrix["AT"]=-1
score_matrix["AG"]=0
score_matrix["CC"]=2
score_matrix["CT"]=0
score_matrix["CG"]=-1
score_matrix["TT"]=2
score_matrix["TG"]=-1
score_matrix["GG"]=2
seq1=input("Sequenza 1=")
seq2=input("Sequenza 2=")
max=-1000000
gap2=len(seq2)
gap1=len(seq1)
best=[]
def allign(s1,s2):  #pair scoring function
	score=0
	for i in range(len(s1)):
		if s1[i]=="-" and s2[i]=="-":
			pass
		elif s1[i]=="-" or s2[i]=="-":
			score=score+gap
		else:
			pair=s1[i]+s2[i]
			if pair in score_matrix.keys():
				score=score + score_matrix[pair]
			else:
				score=score + score_matrix[pair[::-1]]
	return(score)
seq1="-" * gap2 + "-" * (gap1-1)+ seq1 
seq2="-" * (gap1-1) + seq2 + "-" * gap1
for i in range(gap2+gap1):
	x=allign(seq1,seq2)
	if x>max:
		best=[]
		max=x
		best.append(seq1)
	elif x==max:
		best.append(seq1)
	#print(seq1 + "\n" + seq2, x,  "\n")  #print all computed allignment
	t=seq1[0]
	seq1=seq1[1:]+ t
for i in range(len(best)):
	print( "".join(best[i]) + "\n" + seq2, max, "\n")