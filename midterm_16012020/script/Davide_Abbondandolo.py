PAM=open("./PAM250.txt","r")
BLOSUM=open("./BLOSUM62.txt","r")
FASTA=open("./alignments.fasta","r")
def sub_mat(input_matrix):
	pair_value={}
	flag=False
	a=0
	for line in input_matrix:
		if flag==False:
			AA=line.split()
			AA=AA[6]
		else:
			values=line.split()
			for i in range(len(values)):
				pair=AA[i]+AA[a]
				value=values[i]
				pair_value[pair]= int(value[:-1])
			a=a+1
		flag=True
	return pair_value

def scoring(matrix, gap, seq1, seq2):
	total=0
	for i in range(len(seq1)):
		pair=seq1[i]+seq2[i]
		if pair in matrix:
			score=matrix[pair]
		elif pair[::-1] in matrix:
			score=matrix[pair[::-1]]
		elif "-" in pair:
			if gap_mode==1:
				score=gap
			else:
				if i==0:
					pass
				else:
					ex_gap=-0.5
					prev_pair=seq1[i-1]+seq2[i-1]
					if "-" in prev_pair and "-" in pair:
						score=ex_gap
					else :
						score=gap
		total=total + score
	return total

def sequence(input):
	seq_name=[]
	seq=[]
	for line in input:
		line.rstrip()
		if line[0]==">":
			seq_name.append(line[:-1])
		else:
			seq.append(line[:-1])
	return (seq_name,seq)
gap_mode=int(input("Select gap type mode: 1 for simple gap, 0 for extension gap= "))

matrix=[]
seq_file=sequence(FASTA)
seq_name=seq_file[0]
seq=seq_file[1]
matrix.append(sub_mat(PAM))
matrix.append(sub_mat(BLOSUM))
gap=-2
for i in range(0,(len(seq_name)),2):
	mat="PAM250"
	for j in range(len(matrix)):
		score=scoring(matrix[j], gap, seq[i], seq[i+1])
		print(seq_name[i] +"\n" + seq_name[i+1] , score, mat, "\n")
		mat="BLOSUM62"

