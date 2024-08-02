# https://www.codewars.com/kata/58db9545facc51e3db00000a
# this one gave me trouble 
def compress(raw):
    diffs = list()
    for num in range(1, len(raw)):
        diffs.append(raw[num]-raw[num-1])
    intervals = list()
    temp = ['x']
    start = 0
    for i, diff in enumerate(diffs):
        if diff == temp[0]:
            temp.append(diff)
        else:
            if len(temp)>1 or temp[0]==0: 
                intervals.append([start, i+1]) 
                temp.clear()
                temp.append('x')
            else:
                temp.clear() 
                temp.append(diff)
            start = i
    else:
        if len(temp)>1 or temp[0]==0: 
            intervals.append([start, i+2])       
        else:
            temp.append(diff)
    intervals = {x:y for x, y in intervals}
    print(intervals)
    compressed = list()
    included = 0
    for i, num in enumerate(raw):
        if i in intervals:
            diff = abs(raw[i] - raw[i+1])
            if diff == 0: compressed.append(f'{raw[i]}*{intervals[i]-i}')
            elif diff == 1: compressed.append(f'{raw[i]}-{raw[intervals[i]-1]}')
            else: compressed.append(f'{raw[i]}-{raw[intervals[i]-1]}/{diff}')
            included = intervals[i]
        else:
            if i >= included: compressed.append(str(num))    

    return ','.join(compressed)

print(compress([ 1,10,8,6,-2,-2]))  
# print(compress([1,10,6,8,6,7]))  

