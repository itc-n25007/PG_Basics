me = {
    "height": "167",
    "fav_color": "black",
    "fav_anime": "onepice"
}

answer = input("height, fav_color or fav_anime")
if answer in me:
    result = me[answer]
    print(result)
