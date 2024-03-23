secret = input()
decode = input()

secret_list = []
decode_list = []
count_x = 0
count_y = 0

for x in secret:
    secret_list.append(x)
for x in decode:
    decode_list.append(x)
for x in decode_list:
    for y in secret_list:
        if x.lower() == y.lower() and x.isupper():
            decode_list[count_x] = (secret_list[count_y-1]).upper()
        elif x.lower() == y.lower():
            decode_list[count_x] = (secret_list[count_y-1])
        count_y += 1
    count_y = 0
    count_x += 1

print(''.join(decode_list))