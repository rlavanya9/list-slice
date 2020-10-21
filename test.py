#def custom_append(input_list,value):
#    input_list[-1:len(input_list)] = str(value)
#    return input_list


#input_list = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
#print(custom_append(input_list, 'Re'))

#def custom_extend(input_list, second_list):
#    input_list = input_list + second_list
#    return input_list


# months = ['Jan', 'Feb', 'Mar']
# print(custom_extend(months,['Apr', 'May']))
# def custom_remove(input_list, value):
#     seen = False
#     new_list = []
#     idx = 0
#     for i in range(len(input_list)):
#         if (input_list[i] == value) and (seen == False):
#             idx = i
#             seen = True
#             print(idx)
#             print(input_list[i])
#         if i != idx:
#             new_list += input_list[i]
#     input_list = new_list
#     return input_list
    
            

    
    


# notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
# print(custom_remove(notes, 'Do'))

# def equality(some_list, another_list):

#     idx = 0
#     for element in range(len(some_list)):
#  #       for item in another_list:
#             if some_list[element] == another_list[idx]:
#                 print(some_list[element])
#                 print(another_list[idx])
#                 print("inside equal")
#                 idx += 1
#   #              break
#             else:
#                 return False
#     return True

# print(equality(['Jan', 'Feb', 'Mar'], ['Jan', 'Mar', 'Feb']))        

# def custom_remove(input_list, value):
#     length = len(input_list)
#     for i in range(length):
#         print(id(input_list))
#         if (input_list[i] == value):
#             del input_list[i]
#             print(id(input_list))
#             break

# multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
# print(custom_remove(multiples, 9))

# input_list = ['Jan','Feb','Mar']
# print(id(input_list))
# new_list = input_list[0:-1]
# input_list = new_list
# print(id(input_list))
# print(new_list)

input_list = ['Jan','Feb','Mar']
second_list = ['Apr', 'May']

length = custom_len(second_list)
for i in second_list:
        input_list[length:length] = second_list[i] 
return input_list
# new_list = [i for i in range(len(input_list)-1,-1,-1)]
# print(id(new_list))
# input_list = new_list    
# print(id(input_list))


# input_list = ['Jan','Feb','Mar']

#     a = input_list[-1]
#     new_list = input_list[0:-1]
#     input_list = new_list
#     print(id())
#     return a
