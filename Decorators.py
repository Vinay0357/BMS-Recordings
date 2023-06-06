def decofun(func):
    def myfirst():
        print("I have completed my B.Tech in 2017")
        func()
        print("I have completed my 10th standard in 2010")
    return myfirst
@decofun
def otherfun():
    print("I have completed my 12th standard in 2012")

oo = otherfun()
