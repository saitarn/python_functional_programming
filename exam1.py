def multiply_by2(my_list):
    new_list = []
    for item in my_list:
        new_list.append(item*2)
    return new_list

def main():
    print(multiply_by2([1,2,3]))

if __name__ == "__main__":
    main()
    