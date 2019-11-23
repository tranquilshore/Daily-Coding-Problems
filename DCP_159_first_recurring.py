s = "abbac"
n = len(s)

def first_recurring(s,n):
    ascii_arr = [0 for i in range(128)]
    for i in range(n):
        ascii_arr[ord(s[i])] += 1 
        if ascii_arr[ord(s[i])] > 1:
            return s[i]
    return "No recurring character found"

print first_recurring(s,n)
