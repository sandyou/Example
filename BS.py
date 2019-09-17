def bubble_sort_flag(list):
    for i in range(0,len(list)-1):
        flag = False
        for j in range(0,len(list)-1-i):
            if list[j] > list[j+1]:
                flag = True
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
        if flag == False:
            break
        print("pass",i+1,": ", list)
