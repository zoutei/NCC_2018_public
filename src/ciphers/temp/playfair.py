import re
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from src.tools.checkenglishness import get_english_score
from src.tools.text_manipulation import text_split_in_order

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

'''NO I'''
def form_grid(keyword):
    table = []
    list_keyword = []
    for i in range(len(keyword)):
        if keyword[i].upper() not in list_keyword:
            list_keyword.append(keyword[i].upper())
    for each in alphabets:
        if each not in list_keyword:
            list_keyword.append(each)
    if list_keyword.index('I') > list_keyword.index('J'):
        list_keyword[list_keyword.index('I')] = 'J'
        list_keyword.remove(list_keyword[list_keyword.index('J')])
    else:
        list_keyword.remove(list_keyword[list_keyword.index('I')])
    # if list_keyword.index('J') > list_keyword.index('I'):
    #     list_keyword.remove(list_keyword[list_keyword.index('J')])
    # else:
    #     list_keyword.remove(list_keyword[list_keyword.index('I')])
    #     list_keyword[list_keyword.index('J')] = 'I'

    while len(list_keyword)>0:
        row = list_keyword[0:5]
        table.append(row)
        del list_keyword[:5]

    #print(table)
    return table

def get_coordinate(table, target):
    for y in range(0, len(table)):
        for x in range(0, len(table[y])):
            if table[y][x] == target:
                return (x, y)

def horizontal_shift(coordinate, direction_right = 1):
    new_x = (coordinate[0]+direction_right)%5
    return (new_x, coordinate[1])

def verticle_shift(coordinate, direction_down = 1):
    new_y = (coordinate[1]+direction_down)%5
    return (coordinate[0], new_y)

def rectangle_shift(coordinate_a, coordinate_b):
    delta_x = abs(coordinate_a[0] - coordinate_b[0])
    if coordinate_a[0] > coordinate_b[0]:
        coord_b = (coordinate_b[0] + delta_x, coordinate_b[1])
        coord_a = (coordinate_a[0] - delta_x, coordinate_a[1])
    else:
        coord_a = (coordinate_a[0] + delta_x, coordinate_a[1])
        coord_b = (coordinate_b[0] - delta_x, coordinate_b[1])
    return coord_a, coord_b

def playfair(text, table, direction_right = 1, direction_down = 1):
    plaintext = []
    text = re.sub('I','J', text)
    #text = re.sub('J', 'I', text)
    bigram_list = text_split_in_order(text, 2)
    for each in bigram_list:
        a = each[0]
        b = each[1]
        coord_a = get_coordinate(table, a)
        coord_b = get_coordinate(table, b)
        if coord_a[1] == coord_b[1]:  #On the same horizontal line
            coord_a = horizontal_shift(coord_a, direction_right)
            coord_b = horizontal_shift(coord_b, direction_right)
        if coord_a[0] == coord_b[0]:  #On the same verticle line
            coord_a = verticle_shift(coord_a, direction_down)
            coord_b = verticle_shift(coord_b, direction_down)
        if coord_a[0] != coord_b[0] and coord_a[1] != coord_b[1]:  #rectangle
            coord_a, coord_b = rectangle_shift(coord_a, coord_b)[0], rectangle_shift(coord_a, coord_b)[1]

        text_a, text_b = table[coord_a[1]][coord_a[0]], table[coord_b[1]][coord_b[0]]
        plaintext.append(text_a)
        plaintext.append(text_b)

    output = ''.join(plaintext)
    return output
    # output = ['NO I and some X needs to be removed: ', ''.join(plaintext)]
    # print(output)

def generate_random_keyword(lowerlimit, upperlimit):
    keyword = ''
    keyword_length = random.randint(lowerlimit, upperlimit)
    #print(keyword_length)
    while keyword_length > 0:
        char = random.choice(alphabets)
        keyword += char
        keyword_length -= 1
    return keyword

def random_swapping(key):
    l = list(key)
    i, j = random.randint(0, len(l)-1), random.randint(0, len(l)-1)
    if i != j:
        pass
    else:
        i = (i + 1)%(len(key))
    l[i], l[j] = l[j], l[i]
    new_key = ''.join(l)
    return new_key

def reverse(key):
    key = key[::-1]
    return key

def random_substitution(key):
    l = list(key)
    i = random.randint(0, len(key)-1)
    target = random.choice(alphabets)
    if l[i] != target:
        l[i] = target
    else:
        i  = (i + 1)%(len(key))
        l[i] = target
    new_key = ''.join(l)
    return new_key

def random_minor_change():
    methods = [random_swapping, reverse, random_substitution]
    meth = random.choices(methods, [0.25, 0.25, 0.7], k=1)
    return meth[0]

def check_negative_element(list):
    for each in list:
        if each < 0:
            return True
        else:
            return False

def display_data(x, y):
    # data = (successful, unsuccessful)
    # colours = ('green', 'red')
    # groups = ('successful child', 'unsuccessful child')
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
    # for data, color, group in zip(data, colours, groups):
    #     x, y = data
    #     ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
    # plt.title('Matplot scatter plot')
    # plt.legend(loc=2)
    # plt.show()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.ion()
    fig.suptitle('Hill Climbing')
    plt.xlabel('Count')
    plt.ylabel('Englishness score')
    plt.axis([0, 10**2, 0, 500])
    #plt.clf()
    ax1.scatter(x, y)
    plt.pause(0.001)
    plt.ioff()
    return ax1

def hill_climbing():
    highest_score = 0
    highest_likely_key = ''
    parent_keyword = generate_random_keyword(6, 6)
    parent_score = get_english_score(playfair(text, form_grid(parent_keyword), direction_right=-1, direction_down=-1))
    #start_score = get_english_score(playfair(text, form_grid(parent_keyword), direction_right=-1, direction_down=-1))
    count = 1
    while True:

        unsuccessful_threshold = 1000
        unsuccessful = 0
        count += 1

        dG_list = []
        meth = random_minor_change()
        child_keyword = meth(parent_keyword)
        output = playfair(text, form_grid(child_keyword), direction_right=-1, direction_down=-1)
        child_score = get_english_score(output)
        dF = child_score - highest_score
        dG = child_score - parent_score
        parent_score = child_score
        parent_keyword = child_keyword
        meth = str(meth).split(' ')[1]

        # fig = plt.figure()
        # ax1 = fig.add_subplot(111)
        # anim = animation.FuncAnimation(fig, display_data,
        #                                frames=100, interval=20, blit=True)
        display_data(count, child_score)

        if dF > 0:
            unsuccessful = 0
            highest_likely_key = child_keyword
            highest_score = child_score
            # parent_score = child_score
            # parent_keyword = child_keyword
            print('Iteration ' + str(count) + '   child keyword: ' + child_keyword + '  child score: ' + str(
                child_score) + '   Method: ' + meth + '  Highest score: ' + str(highest_score))
        elif dG < 0:
            unsuccessful += 1
            pass
        elif dG > 0 and dF < 0:
            print('Iteration ' + str(count) + '   child keyword: ' + child_keyword + '  child score: ' + str(
                child_score) + '   Method: ' + meth + '  Highest score: ' + str(highest_score))
            unsuccessful = 0
            pass


        #     dG_list.append(dG)
        #     unsuccessful += 1
        # count += 1
        # if len(dG_list) > unsuccessful_threshold :#and check_negative_element(dG_list):
        #     print('Reached maxima')
        #     print('NO I and some X needs to be removed : ', output)
        #     break
        # else:
        #     pass

        # else:
        #     e = 2.71828
        #     T = 9*3**(-count) + 2
        #     probability = (e**(dF/T))*100
        #     if 100 - probability < 10:
        #         # parent_score = child_score
        #         # parent_keyword = child_keyword
        #         print('Iteration ' + str(count) + '   child keyword: ' + child_keyword + '  child score: ' + str(
        #             child_score) + '   Method: ' + str(meth) + '  Probability: ' + str(probability))
        #     else:
        #         unsuccessful += 1
        #     #print('Iteration ' + str(count) + '  Unsuccessful ' + str(unsuccessful))
        #
        # #count += 1
        #
        if unsuccessful > unsuccessful_threshold:
            print('Reached maxima')
            print('NO I and some X needs to be removed : ', output)
            break

if __name__ == '__main__':
    file = open('../../../questions/example/playfair_1.txt')
    text = file.read()
    file.close()
    #form_grid('noodle')
    #print(get_english_score(playfair(text, form_grid('noodle'), direction_right = -1, direction_down = -1)))
    #print(get_coordinate(form_grid('noodle'), 'D'))
    #print(rectangle_shift((4,3), (3,0)))
    #generate_random_keyword(2, 18)
    hill_climbing()
    #display_data(1,1)