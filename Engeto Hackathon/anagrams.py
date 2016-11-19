with open('anagrams_words.txt', encoding = 'utf-8') as content:
    anagrams_words = content.read()

anagrams_words_array = anagrams_words.split('\n')

input_word = input('Zadej slovo, najdu ti anagram. ')
input_word_array = list(sorted(input_word))

print(input_word_array)

for word in anagrams_words_array:
    sorted_word = list(sorted(word))
    anagram = []
    if sorted_word == input_word_array:
        anagram.append(word)
        print(anagram)
    else:
        pass
