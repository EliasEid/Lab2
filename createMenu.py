def createMenu(listOfOptions):
    '''Description: returns a string of numbered menu options
       Preconditions: listOfOptions is a list of strings that indicate menu options
    '''
    ct=1
    result=[]
    for option in listOfOptions:
        result.append(str(ct) + "-" + option)
        ct+=1
    return "\n".join(result)
