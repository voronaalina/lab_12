x='C://lab12//the_little_prince.txt'

def vowels_count_line(line):
    vowels = "aeiouAEIOU"
    count= sum(1 for char in line if char in vowels)
    return count

def count_vowels_file(x):
    total_vowels = 0
    with open(x, 'rt') as file:
        for line in file:
            total_vowels += vowels_count_line(line)
    return total_vowels

vowel_count=count_vowels_file(x)
print("Голосних літер у файлі: ", vowel_count)