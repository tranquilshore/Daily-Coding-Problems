from math import *
points = [(0, 0), (5, 4), (3, 1)] 
source = (1, 2) 

k = 2 

def euclidean_distance(x1,y1,x2,y2):
    return sqrt(pow((x1-x2),2)+pow((y1-y2),2))

def nearest_neighbours(points,source,k):
    points_with_distance = []
    for p in points:
        d = euclidean_distance(p[0],p[1],source[0],source[1])
        points_with_distance.append((p,d))
    return points_with_distance

def build_min_heap(A):
    n = len(A)
    for i in range(n/2-1,-1,-1):
        min_heapify(A,i)

def min_heapify(A,i):
    l = 2*i + 1
    r = 2*i + 2
    n = len(A)
    if l<n and A[l][1]<A[i][1]:
        smallest = l 
    else:
        smallest = i 
    if r<n and A[r][1]<A[i][1]:
        smallest = r
    if smallest != i:
        A[smallest],A[i] = A[i],A[smallest]
        min_heapify(A,smallest)

def extract_min(A):
    n = len(A)
    if n < 1:
        return "heap underflow!"
    min_ = A[0][0]
    A[0] = A[-1]
    A.pop()
    min_heapify(A,0)
    return min_ 

def main(points,source,k):
    if k > len(points):
        return "Invalid k!"
    points_with_distance = nearest_neighbours(points,source,k)
    build_min_heap(points_with_distance)
    for i in range(k):
        print extract_min(points_with_distance)

main(points,source,k)