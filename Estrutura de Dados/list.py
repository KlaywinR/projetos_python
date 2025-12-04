list = [52, 56, -2, 223, 6367, 992, -88, 752, 992, 453, 3234]
pairs_list = []

item_one_occurences = 0
greater_value  = list[0]
lowest_value = list[0]
elements_everage = 0
negative_sum = 0

for index in range (0,len(list)):
    if (greater_value < list[index]):
        greater_value = list[index]

for idex in range (0, len(list)):
    if lowest_value > list[index]:
        lowest_value = list[index]
 
for index in range(0, len(list)):
    if (list[index] % 2 == 0):
        pairs_list.append(list[index])
    
for index in range(0, len(list)):
    if (list[index] ==  list[0]):
        item_one_occurences =  item_one_occurences + 1

for index in range(0,len(list)):
    elements_everage =+ elements_everage +list[index]
elements_everage = elements_everage / len(list)

for index in range(0, len(list)):
    if(list[index]< 0):
        negative_sum = negative_sum + list[index] 
        

print("\n------------------------------------------------")
print("\t------------ Results ------------ ")  

print("  Printing the list to track the results")   
print(list) 
print("\n")

print("Greater value found in the list:",greater_value)
print("Lowest value found in the list:",lowest_value)
print("List of numbers pairs: ",pairs_list)
print("Occurances of item 1: ", item_one_occurences)
print("Everage of elements list: ", f"{elements_everage:.4f}")
print("Negative Sum of numbers: ", negative_sum)
print("------------------------------------------------")
