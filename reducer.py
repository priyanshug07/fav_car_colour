grey = "('gray/siver', (127, 127, 127))"
black = "('black/carbon grey', (0, 0, 0))"
magenta = "('maroon/red', (150, 50, 60))"
white = "('white/cream', (255, 255, 255))"

f_read = open("fav_colour.txt", "r") 
li = [[0,"Grey/Silver"],[0,"Black/Carbon grey"],[0,"Maroon/Red"],[0,"White/Cream"]]
f1 = f_read.readlines()
for x in f1:
    if (x[2] == 'g'):
        li[0][0] += 1
    elif (x[2] == 'b'):
        li[1][0] += 1
    elif (x[2] == 'm'):
        li[2][0] += 1
    else:
        li[3][0] += 1
# print(li)

'''

grey -> 0
black -> 1
magenta -> 2
white -> 3

'''
print(li)
max_index1 = li.index(max(li,key = lambda x: x[0]))
print(li[max_index1][1]," is the favourite colour of Bangalore with the choice percentage of ",(li[max_index1][0]/541)*100,"%")
# li[max_index] = 0
# print(max_index1)
li.remove(li[max_index1])
max_index2 = li.index(max(li, key = lambda x: x[0]))
print(li[max_index2][1]," is the second favourite colour of Bangalore with the choice percentage of ",(li[max_index2][0]/541)*100,"%")