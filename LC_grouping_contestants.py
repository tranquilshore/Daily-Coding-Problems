n = 8 

def grouping_contestants(n):
    def pair_contestants(contestants):
        length = len(contestants)
        if length == 2:
            return tuple(contestants)
        return pair_contestants([(contestants[i],contestants[length-i-1]) for i in range(length//2)])
    return str(pair_contestants(range(1,n+1))).replace(' ','')

print grouping_contestants(n)