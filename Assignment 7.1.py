def chop(lst):
    if len(lst) >= 2:
        lst.pop(0)  
        lst.pop(-1) 
def middle(lst):
    lst=lst[1:-1]
    print(lst)

if __name__ == "__main__":
    my_list = [1, 2, 3, 4]
    
    print("my_list before call chop function", my_list)
    
    chop(my_list)
    print("my_List after call chop function: ", my_list)
    
    my_list = [1, 2, 3, 4]
    print("\n\nmy_list before call middle finction:", my_list)
    print("new_list after call middle finction:") 
    middle(my_list)
    print("my_list after call middle finction:", my_list)
