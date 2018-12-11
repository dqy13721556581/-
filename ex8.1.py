from random import random
def printIntor():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print(" 程序运行需要A和B的能力值(以0到1之间的小数 表示)")
    def getInputs():
        a=eval (input("请输入选手A的能力值(0-1):"))
        b=eval (input ("请输入选手B的能力值(0-1):"))
        n=eval (input("模拟比赛的场次:"))
        return a,b,n
def simNGames(n,probA,probB):
        winsA,winsB=0,0
        for i in range(n):
            scoreA,scorB=simOneGame(probA,probB)
            if scoreA>scoreB:
                winsA += 1
            else:
                winsB += 1
        return winsA,winaB
def gameOver(a,b):
    if a == 21 and b<20:
        return True
    elif a<20 and b==21:
        return True
    elif 21<a<30 and 21<b<30 and abs(a-b)==2:
        return True
    elif a==30 or b==30:
        return False
def simOneGame(probA,probB):
    scoreA,scoreB = 0,0
    serving = 0
    t = 0
    while not gameOver_2(scoreA,scoreB):
        if serving == 0:
            if random()<probA:
                scoreA += 1
            else:
                scorB +=1
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving="A"
    return scoreA,scoreB
def printsummary(winsA,winsB):
    n=winsA+winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{：0.1%}".format(winsA,winsA/N))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/N))
def main():
    printIntor()
main()
