

# def multiply_by2(my_list):
#     new_list = []
#     for item in my_list:
#         new_list.append(item*2)
#     return new_list

# Map function (change item value)
def multiply_by2(item):
    return item*2

# FILTER function (return only True condition in item)
def my_odd(item):
    return item % 2 != 0



def main():
    # print(map(multiply_by2, [1,2,3]))
    my_list = [1,2,3,4,5,6,7]
    print(list(filter(my_odd, my_list)))

if __name__ == "__main__":
    main()
    