'''
One of the substring search algorithm.
watch https://www.youtube.com/watch?v=qQ8vS2btsxI and https://www.youtube.com/watch?v=H4VrKHVG5qI&t=472s to understand.

average time complexity - O(n-m+1)
worst case time complexity - O(mn)
'''
prime = 101
def pattern_matching(text,pattern):
    m = len(pattern)
    n = len(text)

    pattern_hash = create_hash(pattern,m)
    text_hash = create_hash(text,m)

    for i in range(1,n-m+2):
        if pattern_hash == text_hash:
            if text[i-1:i+m-1] == pattern[0:]:
                return i-1
        if i < n-m+1:
            text_hash = recalculate_hash(text,i-1,i+m-1,text_hash,m)
    return -1

def recalculate_hash(input,old_index,new_index,old_hash,pattern_len):
    new_hash = old_hash-ord(input[old_index])
    new_hash = new_hash/prime 
    new_hash += ord(input[new_index])*pow(prime,pattern_len-1)
    return new_hash

def create_hash(input,end):
    hash = 0
    for i in range(end):
        hash = hash + ord(input[i])*pow(prime,i)
    return hash 

index = pattern_matching("abcdefghijklmijkl", "ijkl")
print "Index :", index
