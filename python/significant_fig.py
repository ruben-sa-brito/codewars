#https://www.codewars.com/kata/5d9fe0ace0aad7001290acb7/train/python
def number_of_sigfigs(number):
    if number == '0': return 0
    try:
        number = int(number)
        return len(str(int(str(number)[::-1])))
    except:
        number = number.replace('.', '')
        return(len(str(int(number))))                  