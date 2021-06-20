#TableHelper
tableinput = input("Table?:")
tableinput=int(tableinput)
while tableinput != exit:
    for i in range(11):
        print(tableinput*i)
    if i <= 11:
        break