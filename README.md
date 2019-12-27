# RoadPython
图说Python菜鸟版配套源码
## 学习路线图
居中的图片: ![Alt](https://github.com/zhangziliang04/RoadPython/blob/master/chapter000/01-%E5%AD%A6%E4%B9%A0%E8%B7%AF%E7%BA%BF/%E5%AD%A6%E4%B9%A0%E8%B7%AF%E7%BA%BF%E5%9B%BE.jpg)

## 章节目录
---------------------------
- 第01章 Python语言简介
- 第02章 Python环境部署
- 第03章 Python语法基础
- 第04章 Python数据类型
- 第05章 Python控制语句
- 第06章 Python输入输出
- 第07章 Python文件操作
- 第08章 Python目录操作
- 第09章 Python函数模块 
- 第10章 Python面向对象
- 第11章 Python异常调试



列表
---------------------------
- 项目
  * 项目
    + 项目

1. 项目1
2. 项目2
3. 项目3

- [ ] 计划任务
- [x] 完成任务

链接
---------------------------
链接: [link](https://mp.csdn.net).

图片: ![Alt](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hdmF0YXIuY3Nkbi5uZXQvNy83L0IvMV9yYWxmX2h4MTYzY29tLmpwZw)

带尺寸的图片: ![Alt](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hdmF0YXIuY3Nkbi5uZXQvNy83L0IvMV9yYWxmX2h4MTYzY29tLmpwZw =30x30)

居中的图片: ![Alt](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hdmF0YXIuY3Nkbi5uZXQvNy83L0IvMV9yYWxmX2h4MTYzY29tLmpwZw#pic_center)

居中并且带尺寸的图片: ![Alt](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hdmF0YXIuY3Nkbi5uZXQvNy83L0IvMV9yYWxmX2h4MTYzY29tLmpwZw#pic_center =30x30)

代码片
---------------------------
下面展示一些 `内联代码片`。

```
// A code block
var foo = 'bar';
```

```javascript
// An highlighted block
var foo = 'bar';
```

表格
---------------------------
项目     | Value
-------- | -----
电脑  | $1600
手机  | $12
导管  | $1

| Column 1 | Column 2      |
|:--------:| -------------:|
| centered 文本居中 | right-aligned 文本居右 |

自定义列表
---------------------------
Markdown
:  Text-to-HTML conversion tool

Authors
:  John
:  Luke

注脚
---------------------------
一个具有注脚的文本。[^1]

[^1]: 注脚的解释

注释
---------------------------
Markdown将文本转换为 HTML。

*[HTML]:   超文本标记语言

LaTeX 数学公式
---------------------------
[参考文档](https://khan.github.io/KaTeX/)

Gamma公式展示 $\Gamma(n) = (n-1)!\quad\forall
n\in\mathbb N$ 是通过 Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

插入甘特图
---------------------------
[参考文档](https://mermaidjs.github.io/#/gantt)

```mermaid
gantt
        dateFormat  YYYY-MM-DD
        title Adding GANTT diagram functionality to mermaid
        section 现有任务
        已完成               :done,    des1, 2014-01-06,2014-01-08
        进行中               :active,  des2, 2014-01-09, 3d
        计划中               :         des3, after des2, 5d
```

插入UML图
---------------------------
[参考文档](https://mermaidjs.github.io/#/sequenceDiagram)

```mermaid
sequenceDiagram
张三 ->> 李四: 你好！李四, 最近怎么样?
李四-->>王五: 你最近怎么样，王五？
李四--x 张三: 我很好，谢谢!
李四-x 王五: 我很好，谢谢!
Note right of 王五: 李四想了很长时间, 文字太长了<br/>不适合放在一行.

李四-->>张三: 打量着王五...
张三->>王五: 很好... 王五, 你怎么样?
```

插入Mermaid流程图
---------------------------
[参考文档](https://mermaidjs.github.io/#/flowchart?id=graph)

```mermaid
graph LR
A[长方形] -- 链接 --> B((圆))
A --> C(圆角长方形)
B --> D{菱形}
C --> D
```

插入Flowchart流程图
---------------------------
[参考文档](http://flowchart.js.org/)

```mermaid
flowchat
st=>start: 开始
e=>end: 结束
op=>operation: 我的操作
cond=>condition: 确认？

st->op->cond
cond(yes)->e
cond(no)->op