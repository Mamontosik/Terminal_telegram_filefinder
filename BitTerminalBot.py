from collections import defaultdict

# Чтение слов из файла
with open('[file address]/words.txt', 'r') as file:
    words = file.read().split()

# Функция для получения множества символов в слове
def get_char_set(word):
    return set(word)

# Словарь для хранения слов по их символам
char_to_words = defaultdict(list)

# Заполнение словаря
for word in words:
    char_set = get_char_set(word)
    for char in char_set:
        char_to_words[char].append(word)

# Поиск и вывод слов с общими символами
words_with_common_chars = defaultdict(set)

for char, word_list in char_to_words.items():
    if len(word_list) > 1:
        for i in range(len(word_list)):
            for j in range(i + 1, len(word_list)):
                words_with_common_chars[(word_list[i], word_list[j])].add(char)

# Вывод результатов
if words_with_common_chars:
    print("Слова с общими символами и повторяющиеся символы между ними:")
    for word_pair, common_chars in words_with_common_chars.items():
        print(f"{word_pair[0]} и {word_pair[1]}: {', '.join(common_chars)}")
else:
    print("Нет слов с общими символами.")

# Поиск пары слов с наибольшим количеством общих символов
max_common_chars = 0
max_common_pair = None

for word_pair, common_chars in words_with_common_chars.items():
    if len(common_chars) > max_common_chars:
        max_common_chars = len(common_chars)
        max_common_pair = word_pair

# Вывод пары слов с наибольшим количеством общих символов
if max_common_pair:
    print("\nПара слов с наибольшим количеством общих символов:")
    print(f"{max_common_pair[0]} и {max_common_pair[1]}: {', '.join(words_with_common_chars[max_common_pair])} ({max_common_chars} общих символов)")
else:
    print("\nНет пары слов с общими символами.")