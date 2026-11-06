# ch = "z"
# value = ord(ch) - ord("a") + 1
# print(value)

# ch = "A"
# value = ord(ch) - ord("A") + 27
# print(value)

def solve(message , key , result):
    r1 = 0
    r2 = 0
    for ch in message:
        if 'a' <= ch <= 'z':
         r1 += ord(ch) - ord('a') + 1

        elif 'A' <= ch <= 'Z':
         r1 += ord(ch) - ord('A') + 27
    for ch in key:
        if 'a' <= ch <= 'z':
          r2 += ord(ch) - ord('a') + 1
    
        elif 'A' <= ch <= 'Z':
          r2 += ord(ch) - ord('A') + 27   
    r3 = r1 + r2  
    # if r3 == result:
    #    print("True")  
    # else:
    #    print("False")   
    return r3 == result

    

message = "freeCodeCamp"
key = "Rocks"
result = 238
print(solve(message , key , result))