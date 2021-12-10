def isValid(str):
    " check if string is valid bracked"
    stack = []
    countOpening = 0
    countClosing = 0
    for x in str:
        if x in ["{","[","("]:
            stack.append(x)
            countOpening += 1
        elif x in ["}","]",")"]:

            if len(stack) == 0:
                return False

            opening = stack.pop()
            countClosing +=1

            if not isValidBracket(opening, x):
                return False
        else:
            return False
    return (countOpening == countClosing) and True

def isValidBracket(opening,closing):
    return (opening == "{" and closing =="}") or \
        (opening == "(" and closing ==")") or \
        (opening == "[" and closing =="]")

def should_valid_bracket():
    print( "should true:",isValidBracket("{","}"))
    print( "should true:",isValidBracket("[","]"))
    print("should true:", isValid("{()}"))
    print("should false:",isValid("(}}"))
    print("should false:",isValid("{"))

def should_not_valid_bracket():
    print( isValidBracket("{",""))

if __name__=="__main__":
    should_valid_bracket()
    should_not_valid_bracket() 