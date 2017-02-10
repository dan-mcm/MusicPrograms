from mingus.containers import Bar
from mingus.containers import Composition
from mingus.containers import Track
from mingus.containers import NoteContainer
import mingus.extra.LilyPond as LilyPond

x = int(input('Song Length (number of notes): '))

song = []
b = Bar() # creates new bar element for Mingus = has limit of 4/4 timing by default
b.set_meter((4,4))

c = Composition()
c.set_author('Daniel McMahon', 'daniel40392@gmail.com')
c.set_title('Ode to Fibonnachi')
t = Track()
t.add_bar(b)
c.add_track(t)

def fib(n):
    """Function that generates notes based off the Fibonnachi Series"""
    a=0
    b=1
    print('Generating Music.... Please Wait....',end='')
    
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
        
    n = NoteContainer(song)
    
while x != '':
    fib(x)
    print()
    for note in song:
            b + note
            c.add_note(note)
    comp = LilyPond.from_Composition(c)
    LilyPond.to_pdf(comp, "Ode_to _Fibonnachi")
    print("Song completed - check desktop for exported PDF")
    x = int(input('Song Length (number of notes): '))
