import colors
import os
# This is where any implementations of algorithms will take place for testing purposes/Project demonstraition for the Video.

# Compresses the string
def burrows_wheeler_transform(S):
    # L is the resulting output string
    L = ""
    M = []
    # Form all cyclic rotations of S
    for i in range(0, len(S)):
        M.append(S[i:]+S[:i])
        print_M(M)
        step()
        
        
    # Sort the rotations Lexicographically
    M.sort()
    
    # Output last column.
    print_M(M)
    for i in range(0, len(M)):
        L += M[i][-1]
        
    return L

# Decompresses the string
def inverse_burrows_wheeler_transform(L):
    # This initializes the rows for the table as empty strings
    M = [""] * len(L)
    for i in range(0, len(L)):
        # Insert L as the first column of the table
        for j in range(len(L)):
            M[j] = L[j] + M[j]
        print_M(M)
        step()
        
        # Alphabetically sort the rows of the table
        M.sort()
    print_M(M)
    
    # Return the last row as the result
    return M[0]

def print_colored_string(string):
    text_color = 30 # Black
    bg_color = 41 # up to 47
    
    colored_string = ""
    for char in string:
        format = ';'.join(["2", "30", str(bg_color)])
        colored_string += '\x1b[%sm %s \x1b[0m' % (format, char)
        
        # Increment the color & check it is still within bounds
        bg_color += 1
        if bg_color > 47:
            bg_color = 41
    
    # Enables the VT100 Escape Sequence for windows 10 ver. 1607
    # Credit to Guestreader for the windows 10 fix @: https://stackoverflow.com/questions/16755142/how-to-make-win32-console-recognize-ansi-vt100-escape-sequences
    os.system('')
    print(colored_string)
    
# Prints out the matrix
def print_M(M):
    for row in M:
        print_colored_string(row)

# Prints text in the specified color
def print_color(text, color):
    # Enables the VT100 Escape Sequence for windows 10 ver. 1607
    # Credit to Guestreader for the windows 10 fix @: https://stackoverflow.com/questions/16755142/how-to-make-win32-console-recognize-ansi-vt100-escape-sequences
    os.system('')
    print(color + text + colors.CEND)
    
def step():
    try:
        input("Press a key to continue")
    except SyntaxError:
        pass
# "^BANANA"
result = burrows_wheeler_transform(chr(0)+input("Enter String to Encode: "))


print_color("\nEncoding Result:" + result, colors.CGREEN)

step()

print_color("\nDecoded Result:" + inverse_burrows_wheeler_transform(result), colors.CGREEN)