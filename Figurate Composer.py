#Program that will take figurate number series and translate to music
#focused on pentagonal number which is 1/2n(3n-1)
#formulae sourced from: http://mathworld.wolfram.com/FigurateNumber.html accessed 02/01/17

print('Welcome to the Pentagonal Figurate Composer.')
x = int(input('Enter Song Length: '))

def figurate(input):
    """function takes max range as input and calculates figurate pentagonal numbers from the
         max range down to the bottom range value of 1
         using a while loop - could supplement for i in range also"""
    song = []
    i=0
    a=(1/2*input)
    b=(3*input-1)
    figurate=a*b
    
    print('Song goes like this: ',end='')
    print()
    while i < input:
        figurate=a*b
        
        if figurate%12==1:
            song.append('C')
        elif figurate%12==2:
            song.append('C#')
        elif figurate%12==3:
            song.append('D')
        elif figurate%12==4:
            song.append('D#')
        elif figurate%12==5:
            song.append('E')
        elif figurate%12==6:
            song.append('F')
        elif figurate%12==7:
            song.append('F#')
        elif figurate%12==8:
            song.append('G')
        elif figurate%12==9:
            song.append('G#')
        elif figurate%12==10:
            song.append( 'A')
        elif figurate%12==11:
            song.append('A#')
        elif figurate%12==0:
            song.append('B')
        
        input-=1
        a=(1/2*input)
        b=(3*input-1)

    #this prints song in reverse order - from first value in list to the last
    for i in reversed(song):
        print(i + ', ', end='')
        
    #this prints the song from last value in list to the first
    #for i in song:
    #    print(i + ', ', end='')

while x != '0':
    figurate(x)
    print()
    x = int(input('Enter Song Length (enter empty string to exit): '))
    
print('Empty String Detected - Program End')
