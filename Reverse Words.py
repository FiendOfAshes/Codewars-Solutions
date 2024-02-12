def reverse_words(text):
    result = [word[::-1] for word in text.split(' ')]
    return ' '.join(result)
