with open('data.txt', 'w') as f:
    f.write("Hey Raj! This is a sample text file.")
with open('data.txt', 'a') as f:
    f.write("Adding another line for word count testing.")
with open('data.txt', 'r') as f:
    content = f.read()
    print("File Content:")
    print(content)

words = content.split()
print(f"Total number of words: {len(words)}")