def array_sort():
    non_sorted_array = [1, 8, 9, 4, 16, 0, 4]
    y = len(non_sorted_array) - 1
    run = True
    while run:
        z = 0
        x = 0
        for i in range(len(non_sorted_array) - 1):
            a = non_sorted_array[x]
            b = non_sorted_array[x + 1]

            if a > b:
                non_sorted_array.remove(a)
                print(non_sorted_array)
                non_sorted_array.remove(b)
                non_sorted_array.insert(x, b)
                non_sorted_array.insert(x + 1, a)
            else:
                z = z + 1

        print("end of loop")

        if z == y:
            print(non_sorted_array)
        else:
            continue

array_sort()
