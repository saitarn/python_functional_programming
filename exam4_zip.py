
# FILTER function (return only True condition in item)
def my_odd(item):
    return item % 2 != 0

# ZIP (Operate with 2 lists or two iterable) combine 2 lists order by order to TUPLE


def main():
    # print(map(multiply_by2, [1,2,3]))
    my_list = [1,2,3,4,5,6,7]
    my_list2 = [10,20,30,40,50]
    print(list(zip(my_list, my_list2)))

if __name__ == "__main__":
    main()
    