import nltk

x = int(input('Song Length (number of notes): '))

song = []

def fib(n):
    """Function that generates notes based off the Fibonnachi Series"""
    a=0
    b=1
    print('Song goes like this: ',end='')
    for i in range (1,n+1):
        fib=a+b
        if fib%12==1:
            song.append('C')
        elif fib%12==2:
            song.append('C#')
        elif fib%12==3:
            song.append('D')
        elif fib%12==4:
            song.append('D#')
        elif fib%12==5:
            song.append('E')
        elif fib%12==6:
            song.append( 'F')
        elif fib%12==7:
            song.append('F#')
        elif fib%12==8:
            song.append('G')
        elif fib%12==9:
            song.append('G#')
        elif fib%12==10:
            song.append( 'A')
        elif fib%12==11:
            song.append('A#')
        elif fib%12==0:
            song.append('B')
        a=b
        b=fib

    #this code will print song in reverse
    #for i in reversed(song):
    #    print (i + ' ,', end='')
    
    for i in song:
        print (i + ', ', end='')

    #uses matplotlib to graph the frequency of note appearance
    word_frequency = nltk.FreqDist(song)
    word_frequency.plot(12)

    #uses matplotlib to graph the frequency of note appearance in line with when they appear
    pattern = nltk.Text(song)
    pattern.dispersion_plot(["C", "C#", "D","D#","E","F","F#","G","G#","A","A#","B"])
    
while x != '':
    fib(x)
    print()
    x = int(input('Song Length (number of notes): '))
