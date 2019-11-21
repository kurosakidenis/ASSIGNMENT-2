"""
Pig latin is a language game where English words are altered by moving some letters to the
end of the word and/or by adding a suffix.

Task Write a program that will take a word and output the pig latin version of the
word by following the following rules:
1. If the word starts with a consonant or group of consonants, move all letters before the first vowel
to the end of the word then add "ay".

Example : will -> illway
dog -> ogday
category -> ategorycay
chatter -> atterchay
trash -> ashtray

2. If the word starts with a vowel, simply add "way" to the end of the word.
Example : electrician - electricianway

"""

"""course = "python"
print(course[0])"""

word = str(input('Enter the word: '))

# i created a list containing all the vowels
word_list = ['a', 'e', 'i', 'o', 'u']
if word[0] in word_list:
    print(word + 'way')
else:
    # removing the first character from the word
    new_word = word
    new_word = new_word[0:] + new_word[:-2]
    new_word = new_word[1 : : ]
    print(new_word +'ay')
