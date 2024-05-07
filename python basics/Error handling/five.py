'''
if you want execute program mandatory,irrespective of error,try,except block.
code should be in finally block
'''

print(10/5)

try:
    print(10/0)

except:
    print(10/1)

finally:
    print("finally block will execute always! irrespective of errors")        