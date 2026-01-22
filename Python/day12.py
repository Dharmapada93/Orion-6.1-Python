s = input("Enter a sentence: ").lower()
vowels = 'aeiou'
words = s.split()
print(len(words))

vowel_count = 0
consonant_count = 0

for i in s:
    if i.isalpha():
        if i in vowels:
           vowel_count += 1
        else:
            consonant_count += 1 

print("Vowels: ", vowel_count)
print("Consonants: ", consonant_count)