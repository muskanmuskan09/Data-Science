def word_generator(s):
    words = s.split()
    for word in words:
        yield word

# Test word generator
text = "The quick brown fox jumps over the lazy dog."
for word in word_generator(text):
    print(word)
