sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
"""word_lengths = []"""



new_sentence =[len(word) for word in words if word != "the"]
print(new_sentence)





