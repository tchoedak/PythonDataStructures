"""Strings"""

def isPalindromic(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


def stringToInt(val):
    if type(val) == str:
        r = 0
        for i in range(len(val)):
            if i == 0:
                r = int(val[i])
            else:
                r = (r * 10) + int(val[i])
            i += 1
        return r

def intToString(val):
    if type(val) == int:
        c = ""
        if val < 0:
            c += "-"
        while val != 0:
            digit = val % 10
            c += str(digit)
            val /= 10
        return c[::-1]

def convertToDeci(string, input_base):
    #base1 > 2
    #base2 <= 16
                           
    exp = len(string)- 1
    ind = 0
    deci_total = 0
    while True:
        deci_total += int(string[ind]) * (input_base ** exp)
        exp -= 1
        ind += 1
        if exp < 0:
            break
    return deci_total
    
def baseConvert(string, base, new_base):
    #base1 > 2
    #base2 <= 16
    base_representation = {
                           10: "A",
                           11: "B",
                           12: "C",
                           13: "D",
                           14: "E",
                           15: "F",
                           16: "G"}
                           
    deci_input = convertToDeci(string, base)
    
    new_base_string = ""
    while True:
        new_base_rep = deci_input % new_base
        if new_base_rep > 9:
            new_base_rep = base_representation[new_base_rep]
        new_base_string += str(new_base_rep)
        deci_input /= new_base
        if deci_input == 0:
            break
    return new_base_string[::-1]