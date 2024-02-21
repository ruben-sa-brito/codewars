#https://www.codewars.com/kata/56bcaedfcf6b7f2125001118/train/python
def html_special_chars(data):
    replaces = {"&":"&amp;", "<": "&lt;", ">":"&gt;", '"':"&quot;"} 
    for key in replaces:
        data = data.replace(key, replaces[key])
        
    return data  