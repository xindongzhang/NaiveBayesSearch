def unique(arr):
    new = [];
    for item in arr:
        if item not in new:
            new.append(item)
    return new

def NUM_X(arr_x, item):
    index = [i for i, a in enumerate(arr_x) if a == item]
    return len(index)

def NUM_XY(arr_x, arr_y, item_x, item_y):
    num = 0;
    for i in range(0, len(arr_x)):
        if arr_x[i] == item_x and arr_y[i] == item_y:
            num = num + 1
    return num

def QueryCategory(arr_x, arr_y, item_x):
    labels = unique(arr_y)
    CategoryProbability = {}
    for item_y in labels:
        num_xy = NUM_XY(arr_x, arr_y, item_x, item_y)
        num_x  = NUM_X(arr_x, item_x)
        if num_x != 0:
            CategoryProbability[item_y] = float(num_xy)/num_x
    ##Category = sorted(CategoryProbability.items(), lambda x,y:cmp(x[1],y[1]))
    return CategoryProbability
    
def CombineQuery(query0, query1):
    Combine = {}
    for item in query0:
        Combine[item] = query0[item] + query1[item]
    return Combine

def GetCategories(queryword):
    f = open("data.txt")
    line = f.readline()
    data_x = [];
    data_y = [];

    while line:
        input = str(line)
        seprated = input.split('&&&&&')
        data_x.append(seprated[0])
        data_y.append(seprated[1])
        line = f.readline()
    f.close()

    Category_pre = QueryCategory(data_x, data_y, queryword[0])
    combine = Category_pre
    for i in range(1,len(queryword)):
        Category_cur = QueryCategory(data_x, data_y, queryword[i])
        combine = CombineQuery(Category_pre, Category_cur)
        Category_pre = combine
    combine = sorted(combine.items(), lambda y,x:cmp(x[1],y[1]))
    result = []
    for item in combine:
        if item[1] != 0:
            result.append(item)
    return result