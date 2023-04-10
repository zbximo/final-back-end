x = [{"x": "x'"}]

y = "AA'''"
y = y.replace("'","")
print(y)
str_x = str(x)
print(y)
str_x = str_x.replace('"', "'")
y += str_x

print(y)
