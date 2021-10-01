letter=''' Dear <|Name|>
You are selected
<|Date|>'''

name= (input("enter your name:\n" ))
date= (input("enter date:\n"))
letter=letter.replace("<|Name|>", name)
letter=letter.replace("<|Date|>", date)
print(letter)