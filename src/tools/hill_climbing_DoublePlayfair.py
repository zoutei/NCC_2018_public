from src.tools.hill_climbing import *

def random_change_keyword_length1(key):
    def add():
        i = random.randint(1, 25 - len(key))
        part = generate_random_keyword(1, i, get_existing_letter(key))
        l1 = list(set(list(part)))
        l = list(set(list(key)))
        for i in l1:
            for j in l:
                if i == j:
                    i = random.choice(get_existing_letter(key))
        return ''.join(l1)
    def minus():
        i = random.randint(4, len(key)-3)
        return i

    meth = ['add', 'minus']
    if len(key) < 9:
        return add() + key
    if len(key) > 22:
        return key[:minus()]
    else:
        method = random.choice(meth)
        if method == 'add':
            return add() + key
        else:
            j = minus()
            return key[:j]

def random_minor_change1(type):
    if type == 'grid':
        methods = [random_reverse_row_5x5, random_reverse_column_5x5, random_5x5grid]
        meth = random.choices(methods, [0.25, 0.25, 0.5], k=1)
        return meth[0]
    else:
        methods = [reverse, random_substitution, random_change_keyword_length1, random_substitution_n, random_swapping]
        meth = random.choices(methods, [0.2, 0.62, 0.7, 0.8, 0.2], k=1)
    # methods = [random_swapping, reverse, random_substitution]
    # meth = random.choices(methods, [0.20, 0.20, 0.60], k=1)
        return meth[0]

def random_split_keyword(keyword):
    i = random.randint(3, len(keyword) - 1)
    l = []
    l.append(keyword[:i])
    l.append(keyword[i:len(keyword)])
    key1 = random.choice(l)
    l.remove(key1)
    key2 = l[0]
    display_keyword = key1 + ' ' + key2
    return display_keyword

def hill_climbing_DoublePlayfair(text, config_dict):

    T = config_dict['T0']
    T_lowest = config_dict['T_lowest']
    NumberOfIterationPerT = config_dict['NumberOfIterationPerT']
    FunctionT = config_dict['FunctionT']
    CipherType = config_dict['CipherType']
    KeywordorGrid = config_dict['Keyword/Grid']
    LengthOfKey_lower = config_dict['LengthOfKey_lower']
    LengthOfKey_upper = config_dict['LengthOfKey_upper']
    Probability_threshold = config_dict['Probability_threshold']
    count = 1
    e = 2.71828182846

    PlainText = re.sub(r'\W', '', text)
    if KeywordorGrid == 'grid':
        parent_keyword = generate_random_5x5grid(deleted_letter = 'J')
    else:
        parent_keyword = generate_random_keyword(LengthOfKey_lower, LengthOfKey_upper, alphabets())
        parent_keyword = random_split_keyword(parent_keyword)
    parent_score = get_english_score(CipherType(PlainText, parent_keyword))
    #print(parent_score)
    highest_score = parent_score
    all_keys = []

    while T > T_lowest:
        print(count)
        countOfinter = 0

        while countOfinter <= NumberOfIterationPerT:
            meth = random_minor_change1(KeywordorGrid)
            child_keyword = meth(parent_keyword.replace(' ', ''))
            child_keyword = random_split_keyword(child_keyword)
            #print(child_keyword)
            if child_keyword not in all_keys:
                all_keys.append(table2str(child_keyword))
                resultText = CipherType(PlainText, child_keyword)
                child_score = get_english_score(resultText)
                dF = child_score - parent_score
                #print(child_score)
                if dF >= 0:
                    displayscore = parent_score
                    parent_keyword = child_keyword.replace(' ', '')
                    parent_score = child_score
                    if child_score > highest_score:
                        highest_score = child_score
                    print('#Iteration: ' + str(count) + '  Keyword: ' + table2str(parent_keyword) + '  Score: ' + str(child_score) + ' Highest score: ' + str(highest_score) + '  Parent score:  ' + str(displayscore))
                else:
                    prob = e**(dF/T)
                    if prob > Probability_threshold:
                        parent_keyword = child_keyword
                        parent_score = child_score
                        print('#Iteration: ' + str(count) + '  Keyword: ' + table2str(parent_keyword) + '  Score: ' + str(parent_score) + '  Highest score: ' + str(highest_score) + '  Probability: ' + str(prob))
                    # else:
                    #     print('#Iteration: ' + str(count) + '  Unsuccessful' + '  Probability: ' + str(prob) + ' ' + str(T) + ' ' + str(dF))

                countOfinter += 1
                count += 1

        T = FunctionT(T, count)

if __name__ == '__main__':
    print(random_split_keyword('CWGSZJVAPHB'))