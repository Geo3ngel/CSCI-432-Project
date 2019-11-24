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

result = burrows_wheeler_transform("^BANANA")

print("\nEncoded Result:", result)

print("Decoded Result:", inverse_burrows_wheeler_transform(result))