import jieba

def train_model(filename, queryword):
    file = open("train_data_new.txt")
    line = file.readline()
    data_x = []
    data_y = []
    NOX_part = 0
    TOTAL  = 0
    index    = 1
    while line:
        seprated = line.split(' ')
        if seprated[0] == '#####':
            data_y.append(seprated[1])
            ## save the number of X
            if index != 1:
                data_x.append(NOX_part)
                NOX_part = 0
            ## print seprated[1]
        else:
            TOTAL  += int(seprated[1])
            ## number of query word
            if seprated[0] == queryword:
                NOX_part += int(seprated[1])
                
        line = file.readline()
        index += 1
    file.close()

    ## using dictionary to store result
    category = {}
    if TOTAL != 0:
        for index in range(0, len(data_x)):
            category[data_y[index]] = data_x[index]
    ## return the result
    return category

def GetCategories(querywords):
    Category_pre = train_model('train_data.txt', querywords[0])
    combine = Category_pre

    for i in range(1,len(querywords)):
        Category_cur = train_model('train_data.txt', querywords[i])
        tmp_combine = CombineQuery(Category_pre, Category_cur)
        if not IsAllZero(tmp_combine):
            combine = tmp_combine
            Category_pre = combine
    combine = sorted(combine.items(), lambda y,x:cmp(x[1],y[1]))
    
    categories = []
    for item in combine:
        if item[1] != 0:
            categories.append(item)
    return categories

def CutWords(sentence):
        sentence = sentence.replace(' ','')
        words_cut = jieba.cut(sentence, cut_all=True)
        words_cut = list(words_cut)
        ##
        if len(words_cut) == 0:
            words_cut = ' ';
        ## 
        if len(words_cut) > 1:
            coding_scheme = 'gbk'
        else:
            coding_scheme = 'utf-8'
        
        for item in words_cut:
            item = item.encode(coding_scheme)
        return words_cut
    
def CombineQuery(query0, query1):
    Combine = {}
    for item in query0:
        Combine[item] = query0[item] * query1[item]
    return Combine

def IsAllZero(arr):
    for item in arr.keys():
        if int(arr[item]) != 0:
            return False
    return True

        
