"""
Created on 6/9/22

@author: qinyuzhu
"""
import flirt
import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv("test_conversion.csv")
print(df)

lst = []
for date in df:
    new = datetime.strptime(date, '')
df["new_date"] = datetime.strftime()

ini_time =  "Jul 17 2019 11:49AM"

"""
the functions below can be used to do data conversion of different types followed the comments
"""
x= ""
base=""

#Converts x to an integer. base specifies the base if x is a string.
int(x [,base])
#Converts x to a long integer. base specifies the base if x is a string.
long(x[, base] )
#Converts x to a floating-point number.
float(x)
# Creates a complex number.
complex(real[, imag])
# Converts object x to a string representation.
str(x)
# Converts object x to an expression string.
repr(x)
# Evaluates a string and returns an object.
eval(str)
# Converts random varaible s to a tuple.
tuple(s)
# Converts random variable s to a list.
list(s)
# Converts random varaiable s to a set.
set(s)
# Creates a dictionary. d must be a sequence of (key,value) tuples.
dict(d)
# Converts s to a frozen set.
frozenset(s)
# Converts an integer to a character.
chr(x)
# Converts an integer to a Unicode character.
unichr(x)
# Converts a single character to its integer value.
ord(x)
# Converts an integer to a hexadecimal string.
hex(x)
# Converts an integer to an octal string.
oct(x)







if __name__ == '__main__':
    print(df)
