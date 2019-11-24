import colors
import os
# This is where any implementations of algorithms will take place for testing purposes/Project demonstraition for the Video.

# TODO: Add Verbos Implentation
# TODO Add stepping

    
# Compresses the string
def burrows_wheeler_transform(S):
    # L is the resulting output string
    L = ""
    M = []
    # Form all cyclic rotations of S
    for i in range(0, len(S)):
        M.append(S[i:]+S[:i])
        
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
        # Alphabetically sort the rows of the table
        M.sort()
    print_M(M)
    
    # Return the last row as the result
    return M[-1]
# TODO: Manual Walkthrough (Task to Tommy?) 

# Prints out the matrix
def print_M(M):
    for row in M:
        print(row)

# Prints text in the specified color
def print_color(text, color):
    # Enables the VT100 Escape Sequence for windows 10 ver. 1607
    # Credit to Guestreader for the windows 10 fix @: https://stackoverflow.com/questions/16755142/how-to-make-win32-console-recognize-ansi-vt100-escape-sequences
    os.system('')
    print(color + text + colors.CEND)

result = burrows_wheeler_transform("^BANANA")

print("\nEncoded Result:", result)

print("\nDecoded Result:", inverse_burrows_wheeler_transform(result))

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            os.system('')
            print(s1)
        print('\n')
        
def print_colored_string(string):
    """
    prints table of formatted text format options
    """
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
        
    os.system('')
    print(colored_string)

        
#print_format_table()

print_color("VALIDATION: ", colors.CGREEN)

print_colored_string("Row Test")