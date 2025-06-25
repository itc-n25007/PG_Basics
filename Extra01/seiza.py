import random


mon=input("月を入力して:")
mon=int(mon)
day=input("日を入力して:")
day=int(day)

seiza_list = [
        "1: 山羊", "2: 水瓶", "3: 魚", "4: 牡羊", "5: 牡牛", "6: 双子", "7: 蟹", "8: 獅子", "9: 乙女", "10: 天秤", "11: 蠍", "12: 射手"
        ]

seiza=seiza_list[mon]

if mon == 1:
    if day < 20:
        seiza
    else:
        seiza = seiza_list[mon + 1]

if mon == 2:
    if day < 19:
        seiza
    else:
        seiza = seiza_list[mon + 1]

if mon == 3:
    if day < 21:
        seiza
    else:
        seiza = seiza_list[mon + 1]

if mon == 4:
    if day < 20:
        seiza
    else:
        seiza = seiza_list[mon + 1]

if mon == 5:
    if day < 21:
        seiza
    else:
        seiza = seiza_list[mon + 1]

if mon == 6:
    if day < 22:
        seiza
    else:
        seiza = seiza_list[mon + 1]

if mon == 7:
    if day < 23:
        seiza
    else:
        seiza = seiza_list[mon + 1]

if mon == 8:
    if day < 23:
        seiza
    else:
        seiza = seiza_list[mon + 1]

if mon == 9:
    if day < 23:
        seiza
    else:
        seiza = seiza_list[mon + 1]

if mon == 10:
    if day < 24:
        seiza
    else:
        seiza = seiza_list[mon + 1]

if mon == 11:
    if day < 23:
        seiza
    else:
        seiza = seiza_list[mon + 1]

if mon == 12:
    if day < 22:
        seiza
    else:
        seiza = seiza_list[mon + 1]

print("あなたの星座は{}です。".format(seiza))
