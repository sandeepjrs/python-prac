def bubble_short(my_list):

    def swap(list_to_swap, index1, index2):
        list_to_swap[index1], list_to_swap[index2] = \
            list_to_swap[index2], list_to_swap[index1]
        return list_to_swap

    j= 0

    while j < len(my_list)-1:
        print("outer...iteration .............................." + str(j))
        i = 0
        while i < len(my_list)-1:
            print("iteration ...." + str(i))
            if my_list[i] < my_list[i + 1]:
                print(my_list)
            else:
                swap(my_list, i, i + 1)
                print(my_list)
            i +=1
        j += 1

    print(my_list)



l = [56,25,89,35,78,62,12]

print(l)

bubble_short(l)

