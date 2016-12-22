

def sel_sort(my_list):
    i = 0
    min_index = 0
    j=0
    while i < len(my_list)-1:
        min_index = i
        j=i+1
        print("I................" + str(i))
        while j < len(my_list):
            print("j...."+str(j))
            if my_list[min_index] < my_list[j]:
                pass
            else:
                temp = my_list[min_index]
                my_list[min_index] = my_list[j]
                my_list[j]=temp
            j+=1
        i+=1


    print(my_list)






l = [21,3,96,0,5,8,2]
print(l)
sel_sort(l)







