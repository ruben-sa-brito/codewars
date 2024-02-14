#https://www.codewars.com/kata/563cf89eb4747c5fb100001b
def remove_smallest(numbers):
    numbers2 = numbers.copy()
    try:
        numbers2.remove(min(numbers))
        return numbers2
    except:
        return numbers2
