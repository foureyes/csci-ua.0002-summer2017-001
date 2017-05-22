animals = [
        ['hissy elliot', 'snake', 5], 
        ['jane clawstin', 'cat', 8], 
        ['paw newman', 'cat', 2], 
        ['bark twain', 'dog', 4],
]

def bubble_sort(my_list):
    URGENCY = 2
    count_swaps = 1
    while count_swaps > 0:
        count_swaps = 0
        for i in range(len(my_list) - 1):
            if my_list[i][URGENCY] > my_list[i + 1][URGENCY]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                count_swaps += 1


animals1 = animals[:]
bubble_sort(animals1)
print(animals1)

def selection_sort(my_list):
    URGENCY = 2
    for cur in range(len(my_list) - 1):
        min_index = cur
        for i in range(cur + 1, len(my_list)):
            if my_list[i][URGENCY] < my_list[min_index][URGENCY]:
                min_index = i

        if min_index != cur:
            my_list[cur], my_list[min_index] = my_list[min_index], my_list[cur]

animals2 = animals[:]
selection_sort(animals2)
print(animals2)


