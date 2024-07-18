if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    coordinate_sorted = []
    coordinates = [[i, j , k ] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
   
    for coordinate in coordinates:
        sum = coordinate[0]+ coordinate[1] + coordinate[2]

        if (sum != n):
             coordinate_sorted.append(coordinate)
            
            
    coordinate_sorted.sort()
    
print(coordinate_sorted)
           
           
