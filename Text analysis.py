import re

def analyze_text():
    text = input("Введите текст: ")

    words = re.findall(r'\w+', text.lower())
    word_count = len(words)
    longest_word = max(words, key=len)

    vowels = 'аеёиоуыэюя'
    vowel_count = sum(char in vowels for char in text)

    word_frequency = {}
    for word in set(words):
        word_frequency[word] = words.count(word)

    print(f"Количество слов: {word_count}")
    print(f"Самое длинное слово: {longest_word}")
    print(f"Количество гласных букв: {vowel_count}")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency} раза")

analyze_text()