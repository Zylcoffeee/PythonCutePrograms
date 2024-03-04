import random
import time

def displayIntro():
    print("林檎每天对于水果的喜好都不相同，这一天你要送她一袋水果，在苹果、橘子里选择。")
    print("如果选错了，林檎将丧失20的好感度。如果选对了，林檎会增加10的好感度并触发林檎线剧情。")

# 选择水果
def chooseFruit():
    fruitSelected = " "
    while fruitSelected != "apple" and fruitSelected != "orange":
        print("所以今天选什么水果送给林檎好呢？(apple or orange)")
        fruitSelected = input()

        if fruitSelected != "apple" and fruitSelected != "orange":
            print("请重新选择水果！")
    return fruitSelected

#检验林檎的态度
def checkFruit(chosenFruit):
    print("你将水果送给了林檎。")
    print("但是林檎真的喜欢它吗？")
    time.sleep(3)
    luckyNum = random.randint(1,2)
    linqinFacvorFruit = "apple" if (luckyNum == 1) else "orange"

    if chosenFruit == linqinFacvorFruit:
        print("林檎很满意，提出要和你明天一起去看灯展。")
    else:
        print("林檎一声不吭的离开了，看起来不太开心。")

boolGameAgain = True
while boolGameAgain:
    displayIntro()
    myFruit = chooseFruit()
    checkFruit(myFruit)
    print("是否继续游戏？")
    intputInf = input()
    boolGameAgain = True if (intputInf == 'y') else False

    





