answer=input("好きな食べ物は？")
with open("food.txt","w") as f:
    f.write(answer)
