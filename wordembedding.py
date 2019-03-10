import numpy as np
from keras.models import Sequential
from keras.layers import Embedding
import json,os
from numpy  import array
import codecs, json 

with open('word2id.json') as json_data:
    d = json.load(json_data)
    k= d.values()
with open('id2word.json') as json_data:
    id2word = json.load(json_data)
    # k= d.values()
    
a = array(k)
# print(a)
model = Sequential()
model.add(Embedding(13059, 5, input_length=1))

input_array = a
final = []
# print(type(input_array))
# print(len(input_array))
# print(input_array)
for word in input_array:
	print id2word[str(word)]
	
	tem = array([str(word)])
	print tem

	model.compile('rmsprop', 'mse')
	output_array = model.predict(tem)
	# with open('embedding.text','a') as f_handle:
	# 	np.savetxt(f_handle,id2word[word].encode('utf-8'), delimiter=" ", fmt="%s") 
 #    	np.savetxt(f_handle,output_array,newline=os.linesep)
	# print id2word[word],
	final.append({'word': id2word[str(word)].encode('utf-8'),
		'embedding': output_array.tolist() })
	with open('final.json','w') as json_data:     
	# json.dump(final, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4) ### this saves the array in .json format
		json.dump(final,json_data)
	# print(output_array)
	# print(type(output_array))
	# with open('vec5.txt', 'a') as the_file:
	#     the_file.write(word)
	#     the_file.write(":")
	#     the_file.write(output_array)
	#     the_file.write("\n")
with open('final.json','w') as json_data:     
	# json.dump(final, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4) ### this saves the array in .json format
	json.dump(final,json_data)