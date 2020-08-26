def countLeftParen(myStr):
    x = 0
    count = 0
    tempStr = myStr
    while x == 0:
        if tempStr.find("(") != -1:
            tempStr = tempStr[tempStr.find("(")+1:]
            count += 1
        else:
            x = 1
    return count
    
def countRightParen(myStr):
    x = 0
    count = 0
    tempStr = myStr
    while x == 0:
        if tempStr.find(")") != -1:
            tempStr = tempStr[tempStr.find(")")+1:]
            count += 1
        else:
            x = 1
    return count
    
def countLeftBracket(myStr):
    x = 0
    count = 0
    tempStr = myStr
    while x == 0:
        if tempStr.find("[") != -1:
            tempStr = tempStr[tempStr.find("[")+1:]
            count += 1
        else:
            x = 1
    return count
    
def countRightBracket(myStr):
    x = 0
    count = 0
    tempStr = myStr
    while x == 0:
        if tempStr.find("]") != -1:
            tempStr = tempStr[tempStr.find("]")+1:]
            count += 1
        else:
            x = 1
    return count

def checkParen(myStr):
    for i in myStr:
       if i == ',':
          i = ''
    if countLeftParen(myStr) != countRightParen(myStr):
        return "Unbalanced"
    if countLeftBracket(myStr) != countRightBracket(myStr):
        return "Unbalanced"
    else:
        return "Balanced"