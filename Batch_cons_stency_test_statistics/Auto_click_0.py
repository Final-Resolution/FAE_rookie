from pymouse import PyMouse
import time

'''
    python实现鼠标自动点击屏幕
'''
print("三秒后获取鼠标坐标值！")
time.sleep(3)
m = PyMouse()
a = m.position()    #获取当前坐标的位置
print(a)
print("三秒后开始进行点击！")
time.sleep(3)
'''
m.move(a[0],a[1])   #鼠标移动到(x,y)位置
a = m.position()
print(a)
'''
#移动并且在(x,y)位置左击
m.click(a[0],a[1])
#循环49+1次
for i in range(49):
    print("正在进行第" + str(i) + "次测试")
    #延迟60秒点击
    time.sleep(60)
    #移动并且在(x,y)位置左击
    m.click(a[0],a[1])
    #延迟1秒点击
    time.sleep(1)
    #移动并且在(x,y)位置左击
    m.click(a[0],a[1])
#延迟60秒点击
time.sleep(60)
#注意点击的奇偶次，确保程序停止
m.click(a[0],a[1])    
print("测试完毕！")
