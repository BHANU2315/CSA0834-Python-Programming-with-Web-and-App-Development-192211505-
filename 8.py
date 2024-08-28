def count_spaces_lines_characters(filename):
    spaces = 0
    lines = 0
    characters = 0
    
    with open(filename, 'r') as file:
        for line in file:
            characters += len(line)
            spaces += line.count(' ')
            lines += 1
    
    return spaces, lines, characters

filename = 'your_text_file.txt'  # Replace 'your_text_file.txt' with the path to your text file
spaces, lines, characters = count_spaces_lines_characters(filename)

print("Spaces:", spaces)
print("Lines:", lines)
print("Characters:", characters)
 