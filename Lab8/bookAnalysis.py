# Sibtain Ahmed
# Oct 25, 2025
from removeNonASCII import removeNonASCII

def outputAnalysis(file_name, count):
    keys = list(count.keys())
    keys.sort()
    # save the word count analysis to a file
    out = open(file_name + '_analysis.txt', 'w')
    for word in keys:
        out.write(word + " " + str(count[word]))
        out.write('\n')

def analyzeBook(file_name):
    with open(file_name + '.txt', 'r', encoding='utf-8') as f:
        count = {}
        for line in f:
            line = removeNonASCII(line)
            for word in line.split():
                # remove punctuation
                word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                word = word.replace(']', '').replace(';', '')
                # ignore case
                word = word.lower()
                # ignore numbers
                if word.isalpha():
                    if word in count:
                        count[word] = count[word] + 1
                    else:
                        count[word] = 1
    return count

def main():
    file_name = 'mother_book'
    count = analyzeBook(file_name)

    outputAnalysis(file_name, count)

if __name__ == "__main__":
    main()