

# def multiply_by2(my_list):
#     new_list = []
#     for item in my_list:
#         new_list.append(item*2)
#     return new_list

def multiply_by2(item):
    return item*2

def main():
    # print(map(multiply_by2, [1,2,3]))

    print(list(map(multiply_by2, [1,2,3])))

if __name__ == "__main__":
    main()
    