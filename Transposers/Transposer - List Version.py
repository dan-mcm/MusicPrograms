# Tranposer program based on the use of lists
# Currently  only translates c to other keys
# Version 2  is working on translation of all keys to all other keys

input1 = input("Please insert your starting key: ")
input2 = input("Please insert key you wish to transpose to: ")
input3 = input("Please insert notes to translate: ")

cKey = ["C","D","E","F","G","A","B"]
gKey = ["G","A","B","C","D","E","F#"]
dKey = ["D","E","F#","G","A","B","C#"]
aKey = ["A","B","C#","D'","E'","F#","G#"]
eKey = ["E","F#","G#","A","B","C#'","D#'"]
bKey = ["B","C#'","D#'","E'","F#'","G#'","A#'","B'"]


def keyTransposer(selectedKey,translatedKey,song):
   """function tranposes key of C to other keys"""
   transposedSong = []
   output = ""

   # Currently only allowed to run from C as need to figure out how to account for # and b input...
   if selectedKey == 'c':
      startKey = cKey
      print("Selected start key notes: ", startKey) #test statement

   # Version 2 will explore how to optimise this long if statement....
   # Sticking to some basic keys for testing purposes
   if translatedKey == 'c':
      transposedKey = cKey
      print("Selected transposition key notes: ", transposedKey)
   elif translatedKey == 'g':
      transposedKey = gKey
      print("Selected transposition key notes: ", transposedKey)
   elif translatedKey == 'd':
      transposedKey = dKey
      print("Selected transposition key notes: ", transposedKey)
   elif translatedKey == 'a':
      transposedKey = aKey
      print("Selected transposition key notes: ", transposedKey)
   elif translatedKey == 'e':
      transposedKey = eKey
      print("Selected transposition key notes: ", transposedKey)
   elif translatedKey == 'b':
      transposedKey = bKey
      print("Selected transposition key notes: ", transposedKey)

   for note in song:
      notePosition = startKey.index(note) #seems an issue with selectedKey to startKey
      newNotePosition = transposedKey[notePosition]
      transposedSong.append(newNotePosition)

   print("Composing transposition...")

   for note in transposedSong:
      output += note + ", "

   return output



if __name__ == "__main__":
   print(keyTransposer(input1,input2,input3))
   
