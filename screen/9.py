def longest_words(file):
    try:
        with open(file, encoding='utf-8') as f:
            content = f.read()
            words = content.split()
            
            if not words:
                return "Файл пустой или содержит только пробелы"
            
            max_length = len(max(words, key=len))
            sought_words = []
            
            for word in words:
                if len(word) == max_length:
                    sought_words.append(word)
            
            if len(sought_words) == 1:
                return sought_words[0]
            else:
                return sought_words
                
    except FileNotFoundError:
        return "Файл не найден"
    except Exception as e:
        return f"Произошла ошибка: {e}"

print(longest_words('input.txt'))