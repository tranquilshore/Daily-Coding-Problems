#O(n) approach
# Python program to remove all adjacent duplicates from a string 

# Recursively removes adjacent duplicates from str and returns 
# new string. las_removed is a pointer to last_removed character 
def removeUtil(string, last_removed): 

	# If length of string is 1 or 0 
	if len(string) == 0 or len(string) == 1: 
		return string 

	# Remove leftmost same characters and recur for remaining 
	# string 
	if string[0] == string[1]: 
		last_removed = ord(string[0]) 
		while len(string) > 1 and string[0] == string[1]: 
			string = string[1:] 
		string = string[1:] 

		return removeUtil(string, last_removed) 

	# At this point, the first character is definiotely different 
	# from its adjacent. Ignore first character and recursively 
	# remove characters from remaining string 
	rem_str = removeUtil(string[1:], last_removed) 

	# Check if the first character of the rem_string matches 
	# with the first character of the original string 
	if len(rem_str) != 0 and rem_str[0] == string[0]: 
		#last_removed = ord(string[0]) 
		return (rem_str[1:]) 

	# If remaining string becomes empty and last removed character 
	# is same as first character of original string. This is needed 
	# for a string like "acbbcddc" 
	if len(rem_str) == 0 and last_removed == ord(string[0]): 
		return rem_str 

	# If the two first characters of str and rem_str don't match, 
	# append first character of str before the first character of 
	# rem_str. 
	return ([string[0]] + rem_str) 

#O(n^2) approach
def rmv(st,i):
    if i==len(st)-1:
        return
    if not st:
        return 
    if st[i]==st[i+1]:
        tmp=st[i]
        while(i<len(st) and st[i]==tmp):
            st.pop(i)
        if not i-1:
            rmv(st,i-1)
        else:
            rmv(st,0)
    else:
        rmv(st,i+1)

# inp=list("acabbbac")
# rmv(inp,0)
# print ''.join(inp)

print removeUtil(list("qpaaaaadaaaaadprq"),0)
