numbers=[11,32,33,15,1]

while True:
    answer = input("数字を推測するか、ｑと入力して終了します。")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("終了するには数字またはｑを入力してください。")
    if answer in numbers:
        print("正解です。")
    else:
        print("あなたの推測は間違っています。！")
