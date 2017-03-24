''' Study Guide: Glossary thus far
print           function, prints a string to standard out
+               addition and concatentation operator
+=              shorthand for thing = thing + something
-               subtraction operator
*               multiplication operator, can be used to repeat strings
/               division operator
=               assignment operator
==              equality operator
>               greater than operator
<               less than operator
>=              greater than or equal operator
<=              less than or equal operator
,               comma, used for seperating arguments / variables
" "             double quotes, string delimeter
""" """         3 double quotes, string block delimeter
' '             single quotes, alternate string delimeter
''' '''         3 single quotes, alternate string block delimeter
%               Modulo operator / string formatter symbol (eg. print 'my name is %s' % myname)
%d              number string formatter symbol
%s              string string formatter symbol
%r              raw-input string formatter symbol
True            Boolean true operator
False           Boolean false operator
(               Open parantheses
)               Close parantheses
\               escape symbol, used for including special characters in strings
\n              newline string symbol
\t              tab string symbol
\\              backslash string symbol
\'              single quotes string symbol
\"              double quotes string symbol
raw_input(<prompt>)     prompts standard in for an input and returns it
argv            argument vector, a list of input arguments from standard in
from            keyword for importing functions, eg from <module> import <function>
sys             module relating to interpreter functions
import          brings code from another module into the current module
os              module relating to operating system functions
os.path         module (part of the os module) relating to path functions
os.path.exists(path)            function that tests whether the path exists
open(filepath, mode)            factory function, opens the file at filepath in the specified mode (eg read or write) then returns it as a file object        
file.read()                     returns the contents of file
file.close()                    destructor mothod, closes the file and destroys the file object
file.seek(offset, <whence>)     moves offset lines from whence, default whence is 0 (the start of the file). 1 = the current line, 2 = the EOF
file.truncate()                 chops off everything after the current line in the file
file.readline()                 returns the current line in the file, then moves to the next one
len(object)                     function, returns the length of the object. Units depend on the object.
def                             used for defining functions
*args           the function version of argv
return          for returning a value from a function
function        a section of reusabe code that takes 0 or more inputs, does its thing, then returns an output 
method          a function that is part of a certain kind of object called a 'class'

'''