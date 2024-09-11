def unique_word_generator(words_list):
    seen = set()
    for word in words_list:
        if word.lower() not in seen:
            yield word
            seen.add(word.lower())

# Test unique word generator
words_list = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
for word in unique_word_generator(words_list):
    print(word)
