l = list(range(1,31))
print l
print len(l)



def binarySearch(target, myList):
    left = 0
    right= len(myList)-1

    while left<=right:
        mid = (left + right)/2

        print '''left : {0}  right : {1}  mid : {2}'''.format(left, right, mid)


        if myList[mid] == target:
            return mid
        else:
            if myList[mid] < target:
                left = mid +1
            else:
                right = mid -1


    return -1

x=binarySearch(25,l)

print "the value : "+str(x)
