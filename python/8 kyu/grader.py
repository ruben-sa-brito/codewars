# https://www.codewars.com/kata/53d16bd82578b1fb5b00128c
def grader(score):
    if score > 1 or score < 0.6: return 'F'
    scores = {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}
    return scores[int(score*10)]