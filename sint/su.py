def remove_trailing_newline(line):
    line = line.rstrip('\n')
    return line

line = "Hello\n"
line, i = remove_trailing_newline(line)
print(line)  # Output: "Hello"
print(i)  # Output: 6
