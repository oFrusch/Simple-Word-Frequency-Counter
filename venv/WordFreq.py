from collections import Counter

word_freq_counter = Counter()
with open("pride_and_prejudice.txt", "r") as book:
   for line in book:
        for word in line.split(" "):
            word_freq_counter[word] += 1


print(word_freq_counter)
