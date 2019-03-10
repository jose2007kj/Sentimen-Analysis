import json,os

final = {'<pad>': 0, '<unk>': 1}
reverse={0:'<pad>',1:'<unk>'}
word_vocab_index = 2
for line in open('vocab.txt', 'r'):
	line = line.strip('\n')
	final[line]=word_vocab_index
	reverse[word_vocab_index]=line
	word_vocab_index += 1
with open('word2id.json','w') as json_data:     
	# json.dump(final, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4) ### this saves the array in .json format
	json.dump(final,json_data)
with open('id2word.json','w') as json_data:     
	# json.dump(final, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4) ### this saves the array in .json format
	json.dump(reverse,json_data)