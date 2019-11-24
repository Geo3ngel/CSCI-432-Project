# This is where any implementations of algorithms will take place for testing purposes/Project demonstraition for the Video.

# TODO: Verbos Implentation w/ stepping

# Compresses the string
def burrows_wheeler_transform(S):
    L = []
    M = []
    # Form all cyclic rotations of S
    for i in range(0, len(S)):
        M.append(S[i:]+S[:i])
        
    # Sort the rotations Lexicographically
    M.sort()
    
    # Output last column.
    print_M(M)
    output = ""
    for i in range(0, len(M)):
        output += M[i][-1]
        
    return output

# Decompresses the string
def inverse_burrows_wheeler_transform(L):
    pass
    return S
# TODO: Manual Walkthrough (Task to Tommy?) 

# Prints out the matrix
def print_M(M):
    for row in M:
        print(row)

print("\nResult:", burrows_wheeler_transform("^BANANA"))