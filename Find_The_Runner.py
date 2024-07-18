if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maximum = max(arr)
    
    new_list = []
    for i in arr:
        if i != maximum:
            new_list.append(i)
    second_max = max(new_list)
    print(second_max)
    
   
        
