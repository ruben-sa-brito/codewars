# https://www.codewars.com/kata/57b06f90e298a7b53d000a86
def queue_time(customers, n):
    if len(customers) == 0: return 0
    total_time = 0
    serving = list()

    while len(serving) < n and len(customers) != 0:
        serving.append(customers.pop(0))

    while True:
        duration = min(serving)
        serving = [x for x in serving if x != duration]
        serving = list(map(lambda x: x - duration, serving))
        while len(serving) != n and len(customers) != 0:
            serving.append(customers.pop(0))
        total_time += duration
        if len(serving) == 0: return total_time