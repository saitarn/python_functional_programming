from functools import reduce

# Map function (change item value)
def multiply_by2(item):
    return item*2

# FILTER function (return only True condition in item)
def my_odd(item):
    return item % 2 != 0

# REDUCE
def accumulator(acc, item):
    return acc + item



def main():
    my_list = [1,2,3,4]
    my_list2 = [10,20,30,40,50]
    my_list3 = [100,200,300]
    print(reduce(accumulator, my_list, 0))

if __name__ == "__main__":
    main()
    