def Traceback_print(file, line, module, lineread, Error, Errorread, other):
    print('Traceback (most recent call last):')
    print("  File '{0}', line {1}, in {2}".format(file,line,module))
    print("    {0}".format(lineread))
    print("{0}: {1}".format(Error,Errorread))
    if (other == ''):
        pass
    else:
        print(other)

def Error_print(Error):
    '''
    TypeError
    SyntaxError*
    NameError
    IndexError
    ImportError
    OSError
    ValueError
    TabError
    ZeroDivisionError
    UnicodeError
    '''

    Error_line = {"TypeError": "must be ***， not ***",
                  "SyntaxError": "invalid syntax",
                  }

    if (Error == ""):
        print("TypeError")
        print("    a = '4'")
        print("    print(a + 4)")
        print("    TypeError: must be str, not int")
        print("    TypeError: must be ***， not ***\n")

        print("SyntaxError")
        print("    if 6 == 6")
        print("            ^")
        print("        pass")
        print("    SyntaxError: invalid syntax\n")

        print("SyntaxError")
        print("    True = 1")
        print("    ^")
        print("    SyntaxError: can't assign to keyword\n")

Error_print("")