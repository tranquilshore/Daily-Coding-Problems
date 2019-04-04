import heapq

maxh = []
minh = []

heapq.heapify(minh)

def add(num):
    if len(maxh) == 0 or num < maxh[0]:
        maxh.append(num) # coz there is no heappush for max heap in heapq 
        heapq._heapify_max(maxh)
    else:
        heapq.heappush(minh,num)
    
    #restoring the varient that difference of the size of two heaps should be <= 1
    if len(maxh) == len(minh) + 2:
        heapq.heappush(minh,maxh[0])
        heapq._heapify_max(maxh)
    elif len(maxh)+2 == len(minh):
        maxh.append(heapq.heappop(minh))
        heapq._heapify_max(maxh)

def find_median():
    if len(maxh) == len(minh):
        if len(maxh) == 0:
            return 0
        else:
            return (maxh[0]+minh[0])/2.0 
    elif len(maxh) == len(minh)+1:
        return maxh[0]
    else:
        return minh[0]

add(1)
add(2)
add(3)
add(4)
add(5)
add(6)
print find_median()
    
    
