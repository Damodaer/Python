#Print hello world
i = 'Hello World'
print(i)

# define main function to print out something
def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1

main()

# Find reserv keywords 1st
import keyword

print(keyword.kwlist)


# Find reserv keywords 2nd

help('keywords')


#String literals the (' ', " ". '''  ''') diffrenc

S = 'This is a single quotes string'
print(S)

s = "This is double quotes string"
print(s)

String = '''This is Trible quotes string 
            and
                its can span
                    multiple line'''
print(String)
