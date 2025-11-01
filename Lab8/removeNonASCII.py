# Sibtain Ahmed 
# Oct 25, 2025
# This script removes non-ASCII characters from a text file


def removeNonASCII(text):
    clean = ''
    for char in text:
        if ord(char) < 128:
            clean += char
    return clean

def storeCleanedFile(cleaned_text, original_file_name):
    output_file_name = 'cleaned_' + original_file_name
    with open(output_file_name, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)
    print(f"Cleaned content stored in: {output_file_name}")

def readFile(file_name):   
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def main():
    input_file_name = input("Enter the input file name: ")
    file_content = readFile(input_file_name)
    clean = removeNonASCII(file_content)
    print("Content with non-ASCII characters removed:")
    print(clean)
    storeCleanedFile(clean, input_file_name)


if __name__ == "__main__":
    main()