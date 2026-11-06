# ch = "z"
# value = ord(ch) - ord("a") + 1
# print(value)

# ch = "A"
# value = ord(ch) - ord("A") + 27
# print(value)

def solve(message , key , result):
    total = 0
    for ch in message + key:
        if 'a' <= ch <= 'z':
         total += ord(ch) - ord('a') + 1

        elif 'A' <= ch <= 'Z':
         total += ord(ch) - ord('A') + 27
     
     
    # if r3 == result:
    #    print("True")  
    # else:
    #    print("False")   
    return total == result

    

message = "freeCodeCamp"
key = "Rocks"
result = 238
print(solve(message , key , result))