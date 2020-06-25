import sys, getopt

input='''test-asdf-gfsa
1234-333-999
test,asdf,adfs
1234,333,999'''

def printHelp():
    print('''SYNOPSIS:
    extractinator.py [OPTION] [OPTION] ...

DESCRIPTION:
    -h
        prints overview over synopsis and flags
    -p
        extracts substring at the given position. Each data record is divided into substrings with the specified 
        delimiter (specifiy with -d. If none is specified, "/" will be used). 
    -d 
        set custom delimiter  
    -f
        use file as input
    -s
        use stdin as input

EXAMPLES
    extractinator.py -f input.txt -e 2 -d '.'
        -> divides each data record by the delimiter '.' and extracts the 2nd substring. The content of the file 
           "input.txt" is used.
            ''')

def extract(data, position, delimiter):
    skip = False
    for item in data:
        try:
            print(item.split(delimiter)[int(position)])
        except IndexError:
            skip = True

    if skip == True:
        print(' -> some entries were skipped')

if __name__ == "__main__":
    delimiter='/'
    action=''
    actions = ['ex', 'alias', 'abotype']

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:d:f:", actions)
    except getopt.GetoptError:
        printHelp()
        sys.exit()

    for opt, arg in opts:
        if opt.replace('-', '') in actions:
            action = opt
        if opt == '-p':
            pos = int(arg)
        if opt == '-d':
            delimiter = arg
        if opt == '-h':
            printHelp()
            sys.exit()
    
    if action == '--ex':
        extract(input.splitlines(), pos, delimiter)
        sys.exit()
    else:
        print('no action supplied, exiting ...')
        sys.exit()
    
    