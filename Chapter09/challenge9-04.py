import csv

movies = [["トップガン", "卒業白書", "マイノリティ・リポート"], ["タイタニック", "レヴェナント", "インセプション"], ["トレーニング デイ", "マイ・ボディガード", "フライト"]]
with open("see.csv", "w", encoding="utf-8") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
