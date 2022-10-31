def scaleSpecificNoteNames(pitch,noteNumber):
    notes='C C# D D# E F F# G G# A A# B'.split()
    ind=notes.index(pitch)
    second=notes[ind:]
    first=notes[:ind]
    op=second+first
    print(op[noteNumber-1])