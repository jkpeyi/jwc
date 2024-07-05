import argparse

parser = argparse.ArgumentParser(description="Count number of bytes or lines in a file")


parser.add_argument('-c', dest='count_bytes', help='Count number of bytes in a file', action='store_true')
parser.add_argument('-l', dest='count_lines', help='Count the number of lines in a file', action='store_true')
parser.add_argument('-w',dest='count_words', help='Count words in a file', action='store_true')
parser.add_argument('-m',dest='count_chars', help='Count caracters in a file', action='store_true')

parser.add_argument('filename', help='The file to be processed')

args = parser.parse_args()

filename = args.filename
results = []
line_count = 0

def count_bytes():
     with open(filename, 'rb') as file:
        file.seek(0, 2)
        byte_count = file.tell()
        results.append(str(byte_count))

def count_lines():
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
        results.append(str(line_count))


def count_words():
    with open(filename, 'r') as file:
        word_count = sum(len(line.split()) for line in file)
        results.append(str(word_count))

def count_chars():
    with open(filename, 'r') as file:
        char_count = sum(len(line)+1 for line in file)
        results.append(str(char_count))

if args.count_bytes:
    count_bytes()
       

if args.count_lines:
    count_lines()
   
        
if args.count_words:
   count_words()
  

if args.count_chars:
    count_chars()


if args.count_bytes==args.count_lines == args.count_words == args.count_chars==False:
    count_bytes()
    count_lines()
    count_words()
    count_chars()

results.append(filename)

print( ' '.join(results) )

#TODO: Ordorner les count par ordre croissant.
# TODO: Pipe