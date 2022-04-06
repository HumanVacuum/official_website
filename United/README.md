## United

网站前后端合并版本，不包含数据库或自购的服务器，均在本地运行。


### 文件
- folder: resources_tem

    用于演示的txt和json文件，后续会移除

- folder: templates

    所有HTML文件

- Main.py
  
    flask编写的web后端

### 日志：

**_@ 2022.4.6_**

实现：

- 网站大致结构和功能
- 网页跳转逻辑
- 模拟前后端数据交互

欠缺：
- 账户安全
- 界面美化
- 数据库
- 部署到服务器

**_@ 2022.4.5_**

做不下去版：

主程序在main.py里面

需要链接的html页面也在

如果要运行需要在和main.py并列的文件夹下面开一个temlates的python package然后调用flask的render_templates方法来显示html文件


