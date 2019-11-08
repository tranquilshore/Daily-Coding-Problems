s = "hack"

def print_in_reverse(s,start):
    if start >= len(s):
        return
    print_in_reverse(s,start+1)
    print s[start],

print_in_reverse(s,0)
