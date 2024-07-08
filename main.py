import argparse
import sys
import io
parser = argparse.ArgumentParser(description="Count number of bytes or lines in a file")


parser.add_argument('-c', dest='count_bytes', help='Count number of bytes in a file', action='store_true')
parser.add_argument('-l', dest='count_lines', help='Count the number of lines in a file', action='store_true')
parser.add_argument('-w',dest='count_words', help='Count words in a file', action='store_true')
parser.add_argument('-m',dest='count_chars', help='Count caracters in a file', action='store_true')

parser.add_argument('filename', nargs='?', type=argparse.FileType('rb'), default=sys.stdin, help="File to read from (default: standard input)")

args = parser.parse_args()

input = args.filename.read()

filename = args.filename
#print(type(filename))
results = []
line_count = 0

def count_bytes():
     if type(filename)== io.TextIOWrapper:
         results.append(len(input.encode('utf-8')))
         return
     with open(filename, 'rb') as file:
        file.seek(0, 2)
        byte_count = file.tell()
        results.append(byte_count)

def count_lines():
    if type(filename)== io.TextIOWrapper:
         results.append(input.count('\n') + (1 if input and input[-1] != '\n' else 0))
         return
    
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
        results.append(line_count)


def count_words():

    if type(filename)== io.TextIOWrapper:
        results.append(len(input.split()))
        return
    
    with open(filename, 'r') as file:
        word_count = sum(len(line.split()) for line in file)
        results.append(word_count)

def count_chars():

    if type(filename)== io.TextIOWrapper:
        results.append(len(input))
        return
    
    with open(filename, 'r') as file:
        char_count = sum(len(line)+1 for line in file)
        results.append(char_count)

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


results =map( lambda x: str(x), sorted(results))
if type(filename)!= io.TextIOWrapper:
    results.append(filename)
print( ' '.join(results) )

#TODO: Ordorner les count par ordre croissant.
# TODO: Pipe