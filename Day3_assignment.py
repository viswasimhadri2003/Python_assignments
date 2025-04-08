#Question 1
def flatten_list(nested_list):
    flatted=[]
    for item in nested_list:
        if type(item) is list:
            flatted.extend(flatten_list(item))
        else:
            flatted.append(item)
    return flatted
    
list_input=[1,2,3,[1,2,3,[3,4],2]]
print(flatten_list(list_input))


#Question 2
def f_lst(data):
    if type(data) is str:
        return [int(num) for num in data.strip('()').split(',')]
    elif type(data) is list:
        return [f_lst(item) for item in data]
        
input_data=[[['(0,1,2)','(3,4,5)'],['(5,6,7)','(9,4,2)']]]
print(f_lst(input_data))