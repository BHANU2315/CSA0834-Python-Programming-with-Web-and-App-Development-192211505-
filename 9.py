def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = 0
        for line in file:
            line_count += 1
    return line_count

filename = 'your_text_file.txt'  # Replace 'your_text_file.txt' with the path to your text file
line_count = count_lines(filename)
print("Number of lines in the file:", line_count)
