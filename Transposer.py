def basicComposer(string):
    """function that will translate numbers 1-9 into C scale e.g. 1=c 3=e 5=g"""
    result=''
    
    for i in range(0,len(string)):
        if string[i] == '1':
            result += 'C, '
        elif string[i] == '2':
            result += 'D, '
        elif string[i] == '3':
            result += 'E, '
        elif string[i] == '4':
            result += 'F, '
        elif string[i] == '5':
            result += 'G, '
        elif string[i] == '6':
            result += 'A, '
        elif string[i] == '7':
            result += 'B, '
        elif string[i] == '8':
            result += 'C\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == '9':
            result += 'D\', '
    
    print(result)

def basicTransposer(string):
    """function that will translate from key of C to scale degree - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += '1, '
        elif string[i] == 'D':
            result += '2, '
        elif string[i] == 'E':
            result += '3, '
        elif string[i] == 'F':
            result += '4, '
        elif string[i] == 'G':
            result += '5, '
        elif string[i] == 'A':
            result += '6, '
        elif string[i] == 'B':
            result += '7, '
        elif string[i] == 'C\'':
            result += '8, '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += '9, '

    print(result)

def c2csharpTransposer(string):
    """function that will translate from key of C to key of C# - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'C#, '
        elif string[i] == 'D':
            result += 'D#, '
        elif string[i] == 'E':
            result += 'F, '
        elif string[i] == 'F':
            result += 'F#, '
        elif string[i] == 'G':
            result += 'G#, '
        elif string[i] == 'A':
            result += 'A#, '
        elif string[i] == 'B':
            result += 'C, '
        elif string[i] == 'C\'':
            result += 'C#\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'D#\', '

    print(result)

def c2dflatTransposer(string):
    """function that will translate from key of C to key of Db - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'Db, '
        elif string[i] == 'D':
            result += 'Eb, '
        elif string[i] == 'E':
            result += 'F, '
        elif string[i] == 'F':
            result += 'Gb, '
        elif string[i] == 'G':
            result += 'Ab, '
        elif string[i] == 'A':
            result += 'Bb, '
        elif string[i] == 'B':
            result += 'C, '
        elif string[i] == 'C\'':
            result += 'Db\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'Eb\', '

    print(result)
    
def c2dTransposer(string):
    """function that will translate from key of C to key of D - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'D, '
        elif string[i] == 'D':
            result += 'E, '
        elif string[i] == 'E':
            result += 'F#, '
        elif string[i] == 'F':
            result += 'G, '
        elif string[i] == 'G':
            result += 'A, '
        elif string[i] == 'A':
            result += 'B, '
        elif string[i] == 'B':
            result += 'C#, '
        elif string[i] == 'C\'':
            result += 'D\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'E\', '

    print(result)

def c2dsharpTransposer(string):
    """function that will translate from key of C to key of D# - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'D#, '
        elif string[i] == 'D':
            result += 'F, '
        elif string[i] == 'E':
            result += 'G, '
        elif string[i] == 'F':
            result += 'G#, '
        elif string[i] == 'G':
            result += 'A#, '
        elif string[i] == 'A':
            result += 'C, '
        elif string[i] == 'B':
            result += 'D, '
        elif string[i] == 'C\'':
            result += 'D#\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'F\', '

    print(result)

def c2eflatTransposer(string):
    """function that will translate from key of C to key of Eb - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'Eb, '
        elif string[i] == 'D':
            result += 'F, '
        elif string[i] == 'E':
            result += 'G, '
        elif string[i] == 'F':
            result += 'Ab, '
        elif string[i] == 'G':
            result += 'Bb, '
        elif string[i] == 'A':
            result += 'C, '
        elif string[i] == 'B':
            result += 'D, '
        elif string[i] == 'C\'':
            result += 'Eb\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'F\', '

    print(result)
    
def c2eTransposer(string):
    """function that will translate from key of C to key of E - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'E, '
        elif string[i] == 'D':
            result += 'F#, '
        elif string[i] == 'E':
            result += 'G#, '
        elif string[i] == 'F':
            result += 'A, '
        elif string[i] == 'G':
            result += 'B, '
        elif string[i] == 'A':
            result += 'C#, '
        elif string[i] == 'B':
            result += 'D#, '
        elif string[i] == 'C\'':
            result += 'E\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\', ':
            result += 'F#\',  '

    print(result)

def c2fTransposer(string):
    """function that will translate from key of C to key of F - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'F, '
        elif string[i] == 'D':
            result += 'G, '
        elif string[i] == 'E':
            result += 'A, '
        elif string[i] == 'F':
            result += 'Bb, '
        elif string[i] == 'G':
            result += 'C\',  '
        elif string[i] == 'A':
            result += 'D\', '
        elif string[i] == 'B':
            result += 'E\', '
        elif string[i] == 'C\'':
            result += 'F\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'G\', '

    print(result)

def c2fsharpTransposer(string):
    """function that will translate from key of C to key of F# - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'F#, '
        elif string[i] == 'D':
            result += 'G#, '
        elif string[i] == 'E':
            result += 'A#, '
        elif string[i] == 'F':
            result += 'B, '
        elif string[i] == 'G':
            result += 'C#\',  '
        elif string[i] == 'A':
            result += 'D#\', '
        elif string[i] == 'B':
            result += 'F\', '
        elif string[i] == 'C\'':
            result += 'F#\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'G#\', '

    print(result)

def c2gflatTransposer(string):
    """function that will translate from key of C to key of Gb - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'Gb, '
        elif string[i] == 'D':
            result += 'Ab, '
        elif string[i] == 'E':
            result += 'Bb, '
        elif string[i] == 'F':
            result += 'B, '
        elif string[i] == 'G':
            result += 'Db\',  '
        elif string[i] == 'A':
            result += 'Eb\', '
        elif string[i] == 'B':
            result += 'F\', '
        elif string[i] == 'C\'':
            result += 'Gb\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'Ab\', '

    print(result)
    
def c2gTransposer(string):
    """function that will translate from key of C to key of G - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'G, '
        elif string[i] == 'D':
            result += 'A, '
        elif string[i] == 'E':
            result += 'B, '
        elif string[i] == 'F':
            result += 'C\', '
        elif string[i] == 'G':
            result += 'D\', '
        elif string[i] == 'A':
            result += 'E\', '
        elif string[i] == 'B':
            result += 'F#\', '
        elif string[i] == 'C\'':
            result += 'G\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'G#\', '

    print(result)

def c2gsharpTransposer(string):
    """function that will translate from key of C to key of G# - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'G#, '
        elif string[i] == 'D':
            result += 'A#, '
        elif string[i] == 'E':
            result += 'C\', '
        elif string[i] == 'F':
            result += 'C#\', '
        elif string[i] == 'G':
            result += 'D#\',  '
        elif string[i] == 'A':
            result += 'F\', '
        elif string[i] == 'B':
            result += 'G\', '
        elif string[i] == 'C\'':
            result += 'G#\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'A#\', '

    print(result)

def c2aflatTransposer(string):
    """function that will translate from key of C to key of Ab - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'Ab, '
        elif string[i] == 'D':
            result += 'Bb, '
        elif string[i] == 'E':
            result += 'C\', '
        elif string[i] == 'F':
            result += 'Db\', '
        elif string[i] == 'G':
            result += 'Eb\',  '
        elif string[i] == 'A':
            result += 'F\', '
        elif string[i] == 'B':
            result += 'G\', '
        elif string[i] == 'C\'':
            result += 'Ab\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'Bb\', '

    print(result)
    
def c2aTransposer(string):
    """function that will translate from key of C to key of A - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'A, '
        elif string[i] == 'D':
            result += 'B, '
        elif string[i] == 'E':
            result += 'C#\', '
        elif string[i] == 'F':
            result += 'D\', '
        elif string[i] == 'G':
            result += 'E\', '
        elif string[i] == 'A':
            result += 'F#\', '
        elif string[i] == 'B':
            result += 'G#\', '
        elif string[i] == 'C\'':
            result += 'A\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'B\', '

    print(result)
    
def c2asharpTransposer(string):
    """function that will translate from key of C to key of A#- accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'A#, '
        elif string[i] == 'D':
            result += 'C\', '
        elif string[i] == 'E':
            result += 'D\', '
        elif string[i] == 'F':
            result += 'D#\', '
        elif string[i] == 'G':
            result += 'F\',  '
        elif string[i] == 'A':
            result += 'G\', '
        elif string[i] == 'B':
            result += 'A\', '
        elif string[i] == 'C\'':
            result += 'A#\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'C\', '

    print(result)

def c2bflatTransposer(string):
    """function that will translate from key of C to key of Bb - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'Bb, '
        elif string[i] == 'D':
            result += 'C\', '
        elif string[i] == 'E':
            result += 'D\', '
        elif string[i] == 'F':
            result += 'Eb\', '
        elif string[i] == 'G':
            result += 'F\',  '
        elif string[i] == 'A':
            result += 'G\', '
        elif string[i] == 'B':
            result += 'A\', '
        elif string[i] == 'C\'':
            result += 'Bb\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'C\', '

    print(result)
    
def c2bTransposer(string):
    """function that will translate from key of C to key of B - accidentals excluded"""
    result=''
    for i in range(0,len(string)):
        if string[i] == 'C':
            result += 'B, '
        elif string[i] == 'D':
            result += 'C#\', '
        elif string[i] == 'E':
            result += 'D#\', '
        elif string[i] == 'F':
            result += 'E\', '
        elif string[i] == 'G':
            result += 'F#\', '
        elif string[i] == 'A':
            result += 'G#\', '
        elif string[i] == 'B':
            result += 'A#\', '
        elif string[i] == 'C':
            result += 'B\', '
        #9th element included to help prevent user error crashing the system
        elif string[i] == 'D\'':
            result += 'C#\', '

    print(result)

print('Welcome to the musical translator. I work primarily with the C major scale.')
print('If you would like to transfer a song in C to its note scale positions enter the number 1.')
print('If you would like to transfer a C scale to another key please insert the key you wish to translate to')
print('To exit program insert an empty string.')
x = str(input('Please insert your choice: '))

while x != '':
    
    if x == '1':
        print('Running 1')
        n = str(input('Please insert your melody: '))
        basicTransposer(n)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'C#' or x == 'c#':
        print('Running Csharp')
        csharp = str(input('Please insert your melody: '))
        c2csharpTransposer(csharp)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'Db' or x == 'db':
        print('Running Dflat')
        dflat = str(input('Please insert your melody: '))
        c2dflatTransposer(dflat)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'D' or x == 'd':
        print('Running D')
        d = str(input('Please insert your melody: '))
        c2dTransposer(d)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'D#' or x == 'd#':
        print('Running Dsharp')
        dsharp = str(input('Please insert your melody: '))
        c2dsharpTransposer(dsharp)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'Eb' or x == 'eb':
        print('Running Eflat')
        eflat = str(input('Please insert your melody: '))
        c2eflatTransposer(eflat)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'E' or x == 'e':
        print('Running E')
        e = str(input('Please insert your melody: '))
        c2eTransposer(e)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'F' or x == 'f':
        print('Running F')
        f = str(input('Please insert your melody: '))
        c2fTransposer(f)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'F#' or x == 'f#':
        print('Running Fsharp')
        fsharp = str(input('Please insert your melody: '))
        c2fsharpTransposer(fsharp)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'Gb' or x == 'gb':
        print('Running Gflat')
        gflat = str(input('Please insert your melody: '))
        c2dflatTransposer(gflat)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'G' or x == 'g':
        print('Running G')
        g = str(input('Please insert your melody: '))
        c2gTransposer(g)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'G#' or x == 'g#':
        print('Running Gsharp')
        gsharp = str(input('Please insert your melody: '))
        c2gsharpTransposer(gsharp)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'Ab' or x == 'ab':
        print('Running Aflat')
        aflat = str(input('Please insert your melody: '))
        c2aflatTransposer(aflat)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'A' or x == 'a':
        print('Running A')
        a = str(input('Please insert your melody: '))
        c2aTransposer(a)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'A#' or x == 'a#':
        print('Running Asharp')
        asharp = str(input('Please insert your melody: '))
        c2asharpTransposer(asharp)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'Bb' or x == 'bb':
        print('Running Bflat')
        bflat = str(input('Please insert your melody: '))
        c2bflatTransposer(bflat)
        x = str(input('Please insert your choice: '))
        
    elif  x == 'B' or x == 'b':
        print('Running B')
        b = str(input('Please insert your melody: '))
        c2bTransposer(b)
        x = str(input('Please insert your choice: '))
        
    else:
        print('Invalid input - please try again:')
        x = str(input('Please insert your choice: '))

print('Empty string detected - program end')
#basicComposer(x)
