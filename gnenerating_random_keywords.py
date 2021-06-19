import random
import string

def randStr(chars = string.ascii_lowercase + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))


counter_limit = 8000000
#counter_limit = 8
word_counter = 0
list_containing_words = []

while word_counter < counter_limit:
    random_length = random.randint(3, 20)
    #print(random_length)
    word = randStr(N=random_length)
    list_containing_words.append(word)
    word_counter = word_counter + 1

print(list_containing_words)
with open('random_word_list.txt', 'w') as f:
    for item in list_containing_words:
        f.write("%s\n" % item)