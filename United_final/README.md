## United_Final

重置了网站结构的版本，均在本地运行。


### 日志：

**_@ 2022.5.17_**

完成：
- 对接登陆注册模块和其他页面
- menu封装为模板
- 登录状态检测

还需要：
- 在menu模板中加入登入信息条



### 文件
- folder: blueprints

存放登录注册模块的蓝图

- folder: migrations

存放数据库数据

- folder: static

存放所有静态资源：css，img，js……

- folder: templates

所有HTML文件

- app.py

flask编写的web后端

- config.py

数据库配置文件

- exts.py

邮件模块代码

- models.py

存储模块，验证码、用户信息等

