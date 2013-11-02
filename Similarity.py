from nltk.corpus import wordnet as wn
word1 = wn.synsets('children')
word2 = wn.synsets('babies')
max_sim = 0
max_sim_w1=""
max_sim_w2=""
for w1 in word1:
	for w2 in word2:
		sim = w1.path_similarity(w2)
		#sim = w1.lch_similarity(w2)
		#sim = w1.wup_similarity(w2)
		#sim = w1.res_similarity(w2,corpus)
		#sim = w1.jcn_similarity(w2,corpus)
		#sim = w1.lin_similarity(w2,corpus)
		
		if max_sim < sim:
			max_sim = sim
			max_sim_w1=w1
			max_sim_w2=w2

print max_sim
print max_sim_w1
print max_sim_w2

