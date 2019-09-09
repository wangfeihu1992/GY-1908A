for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, "X", i, '=', i * j, "\t", end="")
    print()



def mao_pao():
    a = [90, 43, 2, 63, 6, 3, 4]
    #外层循环确定待排序的位置
    for i in range(len(a)-1,0,-1):
        #内层循环依次取相邻的两个数据
        for j in range(i):
            # if判断比较相邻两个数据的大小，如果前边大于后边的，则交换位置
            if (a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
    print(a)

    def zhi_shu():
        for i in range(2, 101):
            if (i == 2):
                print(i)
                continue
            f = 1  # 1代表这个数是质数，0代表这个数不是质数
            for j in range(2, i):
                if (i % j == 0):
                    f = 0
                    break
            if (f == 1):
                print(i)