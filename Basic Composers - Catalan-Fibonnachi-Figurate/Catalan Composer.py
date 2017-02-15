#Gets catalan value based on user input and converts to music notation

print('Welcome to the Catalan Composer.')
y = int(input('Enter Song Length: '))

def catalan(n):
        song = []
        fact1=0 #this is n factorial
        fact2=0 #this is 2n factorial
        fact3=0 #this is n+1 factorial
        
        x = 0
        
        while(n > x):
            x += 0.0001 #exponential growth as loop runs - small decimal needed to account for this - help??
            
            fact1 = 1
            fact2 = 1
            fact3 = 1
            
            b = 2 * n
            a = n + 1
            
            fact1 = 1
            fact2 = 1
            fact3 = 1
                              
            for j in range(1,b+1): #2n factorial
                fact2 *= j
                    
            for k in range(1,a+1): #n+1 factorial
                fact3 *= k

            for i in range(1,n+1): #n factorial
                fact1 *= i
                
            result = fact2/(fact3*fact1)
            
            if result%12==1:
                song.append('C')
            elif result%12==2:
                song.append('C#')
            elif result%12==3:
                song.append('D')
            elif result%12==4:
                song.append('D#')
            elif result%12==5:
                song.append('E')
            elif result%12==6:
                song.append('F')
            elif result%12==7:
                song.append('F#')
            elif result%12==8:
                song.append('G')
            elif result%12==9:
                song.append('G#')
            elif result%12==10:
                song.append( 'A')
            elif result%12==11:
                song.append('A#')
            elif result%12==0:
                song.append('B')
            
            n -= 1
            
        #prints sequence in reverse order - easier to compare series of different lengths
        for i in reversed(song):
                print(i + ', ', end='')

        # for reverse of song:
        # for i in (song):
        #         print(i + ', ', end='')
        

while y  != '':
        
        catalan(y)
        print()
        y = int(input('Enter Song Length (enter empty string to exit):'))
