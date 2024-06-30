#https://www.codewars.com/kata/5834a44e44ff289b5a000075
def my_crib(n):
    roof = str()
    for ro in range(n):
        roof+=" "*(n-ro) +"/" + (" "*ro)*2 + "\\" +" "*(n-ro)+ "\n"
    return roof + "/" + "_"*n*2 + "\\\n" + ("|" + " "*n*2 + "|\n")*(n-1) + "|" + "_"*n*2 + "|"