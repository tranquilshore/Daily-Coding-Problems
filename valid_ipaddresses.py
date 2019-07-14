
s = "25525511135"
s = "11111011111"
def valid(ip):
    ip = ip.split(".")

    for i in ip:
        if len(i) > 3 or int(i) < 0 or int(i) > 255:
            return False 
        if len(i) > 1 and int(i) == 0:
            return False 
        if len(i) > 1 and int(i) != 0 and i[0] == "0":
            return False 
    return True 


def convert(s):
    size = len(s)
    
    if size > 12:
        return []
    
    s_new = s 
    l = []

    #generate different combinations
    for i in range(1,size-2):
        for j in range(i+1,size-1):
            for k in range(j+1,size):
                s_new = s_new[:k]+"."+s_new[k:]
                s_new = s_new[:j]+"."+s_new[j:]
                s_new = s_new[:i]+"."+s_new[i:]
                
                if valid(s_new):
                    l.append(s_new)
                s_new = s 
    return l 

print convert(s)



