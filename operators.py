x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print(len(x_list))
print(len(y_list))
print(len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")

if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
