def count_words(filename):
    with open(filename, 'r') as file:
        word_count = 0
        for line in file:
            words = line.split()
            word_count += len(words)
    return word_count

filename = 'your_text_file.txt'  # Replace 'your_text_file.txt' with the path to your text file
word_count = count_words(filename)
print("Number of words in the file:", word_