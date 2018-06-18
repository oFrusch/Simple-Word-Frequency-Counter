from collections import Counter

book = open("pride_and_prejudice.txt", "r")
word_freq_counter = Counter()

for line in book:
   words = line.split(" ")
   for word in words:
       word_freq_counter[word] += 1


print(word_freq_counter)
