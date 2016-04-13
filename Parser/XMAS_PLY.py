""" This will parse the data from the unix command echo "Header1 is this~Header2 and that~~Data 1.0~Data 2.0" | tr "~" "\n"
which is:
Header1 is this
Header2 and that

Data 1.0
Data 2.0
"""

tokens = ('Day', 'Love', "Gift")
literals = ['.', ]

AdamList = {}
NumString = {"A" : 1, "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "Eleven" : 11, "Twelve" : 12, "and a" : 1}
GiftKs = []


# Tokens
t_Day = r'.*day.*'
t_Love = r'.*love.*'

#def t_Strint(t):
#    r'(A|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve|and\sa)'
#    if t.value == "A":
#        t.value = 1
#        AdamList.append(t.value)
#    if t.value == "and a":
#        t.value = 1
#        AdamList.append(t.value)
#    if t.value == "Two":
#        AdamList.append(len(t.value))
#        t.value = 2
#        AdamList.append(t.value)
#    if t.value == "Three":
#        t.value = 3
#        AdamList.append(t.value)
#    if t.value == "Four":
#        t.value = 4
#        AdamList.append(t.value)
#    if t.value == "Five":
#        t.value = 5
#        AdamList.append(t.value)
#    if t.value == "Six":
#        t.value = 6
#        AdamList.append(t.value)
#    return t

def t_Gift(t):
    r'(A|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve|and\sa) .*'
    lbrk = []
    wrd = ""
    for i in range(0, len(t.value)):
        if (t.value[i] != " "):
            wrd += t.value[i]
        else:
            lbrk.append(wrd)
            wrd = ""
    lbrk.append(wrd)
    wrd = ""
    #print (lbrk)
    if lbrk[0] == "and":
        lbrk[0] = "and a"
        lbrk.remove(lbrk[1])
    for i in range(1, len(lbrk)):
        wrd += lbrk[i] + " "
    lbrk[0] = NumString[lbrk[0]]
    if wrd in AdamList:
        AdamList[wrd] += lbrk[0]
    else:
        AdamList[wrd] = lbrk[0]
        GiftKs.append(wrd)
    return t

# Ignored characters
t_ignore = " \r"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex   # ply.lex comes from the ply folder in the PLY download.
lexer = lex.lex()

# Parsing rules

global time_step
time_step = 0

def p_start(t):
    '''start : Day
             | Love
             | Gift
    '''
    #print ("Saw ", t[1])
    #if len(t) > 2:
    #    print ("Saw a ", t[2])


def p_error(t):
    if t == None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc   # ply.yacc comes from the ply folder in the PLY download.
parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        #print(AdamList)
        #print(GiftKs)
        for i in GiftKs:
            print (AdamList[i], " ", i)
        break
    parser.parse(s)

# To run the parser do the following in a terminal window: echo "Header1 is this~Header2 and that~~Data 1.0~Data 2.0" | tr "~" "\n" | grep -v '^\s*$' | python PLYstarter.py | sed "s/_~_/ which is a float./"
