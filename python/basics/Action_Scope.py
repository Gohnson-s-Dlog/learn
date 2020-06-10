
'''
    闭包是指在函数声明时的作用域以外的地方被调用的函数
　　在函数声明时的作用域以外的地方调用函数，需要通过将该函数作为返回值或者作为参数被传递
'''
arg = '全局变量中的arg'  # 定义的arg是全局作用域
def secondFloor():
    print(arg)  # 定义的arg是局部作用域
    # global arg
    # msg+='secondFloor'
    def thirdFloor():
        #global arg
        print(arg)  #1.调用arg变量时当自己方法中没有这个变量,默认会逐层向外去找这个arg变量
                    #2.当上层没有这个变量时,会报错,
                    #3.当局部变量与全局变量同时有这个变量时,使用的局部变量
                    #4.如果要使用全局变量时,需要声明这个全局变量 global arg(见上第9行)
                    #5.如果要使用并改变全局变量,需要在当前函数中声明global arg(见上第6\7行)
    return thirdFloor  # 为什么要return?return的是什么?
sf = secondFloor()  # 这是什么意思?创建方法?
sf()  # 这是谁调的?
