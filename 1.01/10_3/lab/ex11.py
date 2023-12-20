# Exercise 1.1. It is a good idea to read this book in front of a computer so
# you can try out the examples as you go.

# Whenever you are experimenting with a new feature, you should try to make
# mistakes. For example, in the “Hello, world!” program, what happens if you
# leave out one of the quotation marks? What if you leave out both? What if
# you spell print wrong?

# This kind of experiment helps you remember what you read; it also helps when
# you are programming, because you get to know what the error messages mean.
# It is better to make mistakes now and on purpose than later and accidentally.

# 1. In a print statement, what happens if you leave out one of the
# parentheses, or both?

#print('Hello worlds'
#when a parentheses is left out you get a syntax error saying "unexpected EOF while parsing"

# 2. If you are trying to print a string, what happens if you leave out one
# of the quotation marks, or both?

#print('Cheese)
# got EOL while scanning string literal, syntax error and name error

# 3. You can use a minus sign to make a negative number like -2.
# What happens if you put a plus sign before a number? What about 2++2?

# got SyntaxError: Missing parentheses in call to 'print'. Did you mean print(2++2)?
# got TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'int'

# 4. In math notation, leading zeros are ok, as in 09. What happens if you try
# this in Python?  What about 011?

#got SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
#what does octal mean?

# 5. What happens if you have two values with no operator between them? "22", "11"

#'22' = '11'
#you get the SyntaxError: cannot assign to literal