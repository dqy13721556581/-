TempStr=input("请输入带有符号的温度值：")

if TempStr[-1] in ['F','f']:

    C=(eval(TempStr[0:-1])-32)/1.8

    print("转换后的温度是{:.0f}C".format(C))

elif TempStr[-1] in ['c','C']:

    F=1.8*eval(TempStr[0:-1])+32

    print("转换后的温度是{:.0f}".format(F))

