#Taable
import turtle

turtle.title("Taable")
root = turtle.Screen()._root
root.iconbitmap("Icon.ico")
wn = turtle.Screen()
wn.bgcolor("sky blue")

text1 = turtle.Turtle()
text2 = turtle.Turtle()

text1.hideturtle()
text2.hideturtle()
input1 = wn.textinput("", "Times Table Number")
input1=int(input1)
input2 = wn.textinput("What Times Table", "Do you want until")
input2=int(input2)


text2.write("Times Table of ", font=("Verdana",30, "normal"), align="right")
text1.write( input1, font=("Verdana",30, "normal"), align="left")

for i in range(input2+1):
    print(input1,"x ",i,"= ",input1*i)



wn.mainloop()
wn.exitonclick()



