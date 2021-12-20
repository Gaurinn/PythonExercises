import tokenizer
from tokenizer import Tokenizer
import os
import hashlib

# throw/raise this exception if a
# division by zero occurs.
class DivisionByZero(Exception):
    pass

class IsCorrect(Exception):
    print("everything is correct")
    pass

# IMPLEMENT HERE!!!! -----------------------------------------------------
# This function is the actual recursive
# implementation of the prefix parser.
# The tokenizer is pass-by-object-reference
# so it will be the same instance of Tokenizer
# throughout the recursive run.
def prefix_parser_recursive(tokenizer):
    token = tokenizer.get_next_token()
    #print(token) # debug line
    if token.isdigit():
        return int(token)
    elif token == "+":
        return prefix_parser_recursive(tokenizer) + prefix_parser_recursive(tokenizer)
    elif token == "-":
        return prefix_parser_recursive(tokenizer) - prefix_parser_recursive(tokenizer)
    elif token == "*":
        return prefix_parser_recursive(tokenizer) * prefix_parser_recursive(tokenizer)
    elif token == "/":
        dividend = prefix_parser_recursive(tokenizer)
        divisor = prefix_parser_recursive(tokenizer)
        if divisor == 0:
            raise DivisionByZero
        else:
            return (dividend / divisor)

    return 0

# This function makes the tokenizer
# and then calls the recursive function.
# It is often necessary to make a separate
# recursive function that takes and returns
# particular values that don't match the
# proper functions parameters and return value.
def prefix_parser(str_statement):
    tokenizer = Tokenizer(str_statement)
    return prefix_parser_recursive(tokenizer)

# This is a tester function to test that
# the output and/or error message from the
# prefix_parser function are correct.
def test_prefix_parser(str_statement, first):
    str_print = str_statement.rstrip()
    try:
        str_print += " = " + str(prefix_parser(str_statement))
    except DivisionByZero:
        str_print += ": " + str("A division by zero occurred")
    output = open("output_test.txt", "a+")
    if not first:
        output.write("\n"+str_print)
    else:
        output.write(str_print)

    output.close()
    print(str_print)

def cleanfile(txtfile):
    txtfile.seek(1,os.SEEK_END)
    txtfile.truncate()
    return txtfile

def output_test(txtfile1,txtfile2):
    file1=open(txtfile1,"r+")
    file2=open(txtfile2,"r+")
    
    with open("correct_output.txt","w+",encoding='utf-8') as file_output:
        for line1, line2 in zip(file1, file2):
            if line1==line2:
                file_output.write(line1)
            else:
                #print(str(line1+line2)+"aha!")
                #file_output.write("* - 0 + + * + 5 7 + 3 5 / - 3 4 2 + * 7 9 * 7 / 8 4 * - - / 4 / 5 0 + - 5 5 3 / 4 / 5 0 8: A division by zero occurred")
                pass
    file1.close()
    file2.close()
    final_check = checksum("correct_output.txt")
    expected_file = checksum("expected_output.txt")
    if final_check == expected_file:
        print("everything works!")
        os.remove("correct_output.txt")
        os.remove("output_test.txt")
        return
    else:
        print("Files do not match each other perfectly")            

       

def checksum(txtfile):
    md5 = hashlib.md5()
    md5.update(open(txtfile).read().encode('utf-8'))

    return md5.hexdigest()
    

#A few hard coded tests
#test_prefix_parser("+ 3 20")
#test_prefix_parser("+ / 3 - 21 20 * 2 40")
#test_prefix_parser("+ / 3 - 20 20 * 2 40")

# This must be a relative path from the folder that you have open
# in Visual Studio Code.  This particular path works if you open
# the folder PrefixParserBase directly
f = open("prefix_statements.txt", "r")
first = True
for line in f:
    test_prefix_parser(line, first)
    first = False
f.close()
output_test("expected_output.txt","output_test.txt")