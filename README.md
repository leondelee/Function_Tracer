# Function Tracer
## 1.功能
追踪函数
- 记录函数运行时间
- 记录函数被调用次数
## 2.环境配置
python3（这里使用的是python3.6）
## 3.使用方法
- import trcfunc.tracer
- 在想要调试的函数前面加上装饰器@tracer
- 在运行函数结束的时候，会在相同的文件内生成txt格式的文件，记录相关信息
- 可以使用exemple.logclean来清除日志
## 4.使用实例
- 导入
```
from tracer.trcfunc import tracer   #你储存的位置不同，这个导入语句也不同
```
- 实现
```
import time
@tracer
def add(x,y):
    time.sleep(1.5) #否则运行时间过短
    print(x+y)
if __name__ == '__main__':
    add(5,8)
```
- 运行效果
[image](https://github.com/leondelee/Function_Tracer/blob/master/im1.png)
- 生成的txt文件

```
2017-10-14 18:29:44 :function"add" is called 1 times which takes 1.505441 seconds.
```
- 使用logclean清除日志

```
if __name__ == '__main__':
    add(5,8)
    add.logclean  #输出的日志文件会被清空
```


