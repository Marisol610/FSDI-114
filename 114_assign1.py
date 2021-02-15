

def anagramSolution (stringA, stringB):

    
    listB = list(stringB)

    same=True
    char1= 0

    if len(stringA) != len(stringB):
        same= False

    while char1 < len(stringA) and same:
        char2=0
        found =False
        
        while char2 <len(listB) and not found:
            if stringA[char1] == listB[char2]:
                found =True

            else:
                char2= char2 + 1

        if found:
            listB[char2] = None
        else:
            same=False
        char1 = char1 + 1
    return same

print(anagramSolution('pear', 'reap'))
















