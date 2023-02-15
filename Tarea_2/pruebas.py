#a = "\u0030" #unicode for 0
#b = "\u00B2" #unicode for ²

#print(a.isdigit())
#print(b.isdigit())

def countDis(str):
 
    # Stores all distinct characters
    s = set(str)
 
    # Return the size of the set
    return len(s)
 
 
# Driver Code
if __name__ == "__main__":
 
    # Given string S
    S = "mouij4"
 
    print(countDis(S))