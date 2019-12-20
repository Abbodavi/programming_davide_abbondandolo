table=open("./../data/blosum.txt","r")
pair_value={}

v=False
for line in table:
	if v==False:
		AA=line.split()
	else:
		value=line.split()
		aa2=value[0]
		score=value[1:]
		for i in range(len(score)):
			pair=AA[i]+aa2
			pair_value[pair]= score[i]
	v=True
print(pair_value)

seq1="ALASVLIRLITRLYP"
seq2="ASAVHLNRLITRLYP"
total=0
for i in range(len(seq1)):
	pair=seq1[i]+seq2[i]
	value=int(pair_value[pair])
	total=total+value
print(total)