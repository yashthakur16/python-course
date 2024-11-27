message=input(">")
msg=message.split()

length=len(msg)



emoji={
    ":)":"😊",
    ":(":"😔",
}

for i in msg:
    print(emoji.get(i,i),end=" ")