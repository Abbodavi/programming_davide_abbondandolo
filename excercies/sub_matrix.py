import math
sequence_in_allign=["ACAGGTGGACCT","ACTGGTCGACTT","CTATATGG","CCGGATCG"]
base=["A","C","G","T"]
total_sequence=""
for i in sequence_in_allign:
	total_sequence=total_sequence+i

freq_total={}
for i in base:
	count=0
	for j in range(len(total_sequence)):
		if i==total_sequence[j]:
			count+=1
	freq_total[i]=count/len(total_sequence)

num_pair={}
for i in range(0,len(sequence_in_allign),2):
	for j in range(len(sequence_in_allign[i])):
		pair=sequence_in_allign[i][j]+sequence_in_allign[i+1][j]
		if pair in num_pair.keys():
			num_pair[pair]+=1
		elif pair[::-1] in num_pair.keys():
			num_pair[pair[::-1]]+=1
		else:
			num_pair[pair]=1

for key in num_pair:
	num_pair[key]+=1
for i in base:
	for j in base:
		pair= i + j
		if pair in num_pair.keys():
			pass
		elif pair[::-1] in num_pair.keys():
			pass
		else:
			num_pair[pair]=1

pair_freq={}
for keys in num_pair:
	indipendent_pair_freq=1
	for i in range(len(keys)):
		indipendent_pair_freq= indipendent_pair_freq * freq_total[keys[i]]
	pair_freq[keys]= round(math.log((num_pair[keys]/(len(total_sequence)/2)) / indipendent_pair_freq),2)
pair=[]
for i in pair_freq.keys():
	pair.append(i)
pair.sort()
for i in pair:
	print(i, pair_freq[i])