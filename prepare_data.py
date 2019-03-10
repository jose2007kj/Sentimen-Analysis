
import string
import re
from os import listdir
from collections import Counter
from nltk.corpus import stopwords



def load_doc(filename):

	file = open(filename, 'r')
	text = file.read()
	file.close()
	return text

def clean_doc(doc):
	
	tokens = doc.split()
	re_punc = re.compile('[%s]' % re.escape(string.punctuation))
	tokens = [re_punc.sub('', w) for w in tokens]
	tokens = [word for word in tokens if word.isalpha()]
	stop_words = set(stopwords.words('english'))
	tokens = [w for w in tokens if not w in stop_words]
	tokens = [word for word in tokens if len(word) > 1]
	return tokens


def add_doc_to_vocab(filename, vocab):
  
	doc = load_doc(filename)
	tokens = clean_doc(doc)
	vocab.update(tokens)


def process_docs(directory, vocab):

	
	for filename in listdir(directory):

		if not filename.endswith(".txt"):
	 		continue

		path = directory + '/' + filename 

		add_doc_to_vocab(path, vocab)

		


vocab = Counter()

process_docs('txt_sentoken/neg', vocab) 
process_docs('txt_sentoken/pos', vocab)





min_occurane = 5

# Removing 
to_remove=[]
for k,c in vocab.items():
	if c<=min_occurane:
		to_remove.append(k)

for k in to_remove:
	del vocab[k]

#n=len(vocab)
#print("Vocabulary",vocab.most_common()[:-n-1:-1]). reversing

tokens= [k for k,c in vocab.items()]



def save_list(lines, filename): 
	data = '\n'.join(lines)
	file = open(filename, 'w')
	file.write(data)
	file.close()

save_list(tokens, 'vocab.txt')	


vocab_filename = 'vocab.txt'
voc = load_doc(vocab_filename)
voc = voc.split()
voc = set(voc)


def doc_to_line(filename, vocab):
  
	doc = load_doc(filename)

	tokens = clean_doc(doc)

	tokens = [w for w in tokens if w in vocab] 

	return ' '.join(tokens)


def clean_review(directory, vocab):
	lines = list()

	for filename in listdir(directory):


		if not filename.endswith(".txt"):
			continue

		path = directory + '/' + filename
		
		line = doc_to_line(path, vocab)

		lines.append(line)

	return lines		

# prepare negative reviews
negative_lines = clean_review('txt_sentoken/neg', voc) 
save_list(negative_lines, 'negative.txt')
# prepare positive reviews
positive_lines = clean_review('txt_sentoken/pos', voc) 
save_list(positive_lines, 'positive.txt')