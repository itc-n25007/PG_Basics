import random

player_hand=input("どの手?(1:グー 2:チョキ 3:パー)")

if player_hand not in ["1", "2", "3"]:
    print("無効な入力です。ゲームを終了します。")
    exit()

choices=("グー", "チョキ", "パー")
player_hand=choices[int(player_hand) - 1]
#computer_hand=random.choices(choices)
computer_hand=choices[random.randint(0,2)]

def determine_winner(player, computer):
    print(f"あなたの手: {player}")
    print(f"コンピュータの手: {computer}")
    if player ==  computer: 
        return "引き分け" 
    elif (player == "1" and computer == "チョキ") or \
         (player == "2" and computer == "パー") or \
         (player == "3" and computer == "グー"):
        return "あなたの勝ち"
    else:
        return "コンピュータの勝ち"


result = determine_winner(player_hand, computer_hand)
print(f"結果: {result}")
