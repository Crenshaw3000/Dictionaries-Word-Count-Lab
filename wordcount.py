"""Count words in file."""
import sys

#def get_word_count(file):

file_name =  open(sys.argv[1])
word_counts = {}

for line in file_name: #strings in a list
    line =  line.rstrip()
    words = line.split()
 
    for word in words: #iterate thorugh each word
        word_counts[word] = word_counts.get(word,0) + 1
    
for word, count in word_counts.items(): #put in tuple after iterating; unpackes tuple
     print(f"{word}: {count}")  #prints the tuples
   # return word_counts


#get_word_count("test.txt")



