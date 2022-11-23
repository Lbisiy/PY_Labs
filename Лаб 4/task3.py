def delete(list_, index=None):
    if index is not None:
        new_list1 = list_[:index]
        new_list2 = list_[index + 1:]
        new_list = new_list1 + new_list2
    else:
        new_list = list_[:-1]
    return new_list

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
