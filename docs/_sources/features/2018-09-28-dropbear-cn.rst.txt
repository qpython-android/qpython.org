如何在QPython 使用 SSH
========================

近来悄悄更新了不少好玩的包，但是我最喜欢的是今天介绍的这个特性，刚被集成到QPython中的dropbear SSH工具。

Dropbear SSH 是很多嵌入式linux系统首选的ssh工具，结合qpython，能让你方便地进行编程来自动管理服务器或你的手机。

如何远程登录 你的服务器？
----------------------------

.. image:: https://mmbiz.qpic.cn/mmbiz_jpg/tuObYW62d0iaJIF2ibzmISF2PBd92KzAPnZfLlIbyOglK3NOvD508VccuQafhhic036KuxGeiasAQDqb2YMDmHWo2w/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1
   :alt: 1 Dashboard 长按Terminal, 选择Shell Terminal

*1 Dashboard 长按Terminal, 选择Shell Terminal*

.. image:: https://mmbiz.qpic.cn/mmbiz_jpg/tuObYW62d0iaJIF2ibzmISF2PBd92KzAPncIibPKFhA6RtwC5tQyia66nDWcnccv8aSrZJDNKzBiaduvy23rib1oLv5A/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1
   :alt: 2 Shell中输入ssh <user>@<host>

*2 Shell中输入ssh <user>@<host>*

.. image:: https://mmbiz.qpic.cn/mmbiz_jpg/tuObYW62d0iaJIF2ibzmISF2PBd92KzAPnEpC5zNbJJejeGCvnNgEIHDKLX9S72GjVybShlqvtzvPATsh4Fg13Kw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1
   :alt: 3 已经登录到了远端服务器

*3 已经登录到了远端服务器*


除了从手机上登录服务器外，你还可以登录到你的手机。

如何登录到你的手机?
-----------------------

这个功能适合高级玩家，因为一些权限的问题，在手机上开sshd服务需要root权限。
第一次使用，需要从shell terminal中进行下初始化操作

```
su -  #切换为root用户，

mkdir dropbear # 在 /data/data/org.qpython.qpy/files下创建dropbear目录

初始化对应的key

dbkey -t dss -f dropbear/dropbear_dss_host_key

dbkey -t rsa -f dropbear/dropbear_rsa_host_key

dbkey -t ecdsa -f  dropbear/dropbear_ecdsa_host_key

```

完成上述步骤之后，即可启动sshd服务。

.. image:: https://mmbiz.qpic.cn/mmbiz_jpg/tuObYW62d0iaJIF2ibzmISF2PBd92KzAPnLL1eeZvpzyJXLfBLJT1hmbQEKs1QDodeugXPh8vOvJ77HNvHyT6sDg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1
   :alt: 启动sshd服务：sshd -p 8088 -P dropbear/db.pid -F # 前台启动，端口 8088

*启动sshd服务：sshd -p 8088 -P dropbear/db.pid -F # 前台启动，端口 8088*

接下来从你的电脑中就可以登录了你的手机了默认密码就是我们的app名字，你懂得。

.. image:: https://mmbiz.qpic.cn/mmbiz_png/tuObYW62d0iaJIF2ibzmISF2PBd92KzAPn4FOhNFPVKEpZE8mCibia8Cgf4sUK41cldnFWYpqtaY62LfX6MiabwYquQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1
   :alt: 从你的笔记本登录手机

*从你的笔记本登录手机*

**另外还支持下面高级特性：**

- ssh 支持证书登录，借助dbconvert，可以把你的openssh证书转换过来，存到对应的目录，用 ssh -i <id_private>指定证书即可
- sshd 支持 authorized_keys, 只需要把该文件保存到你的dropbear目录下，即可
- scp，远程拷贝文件

后续计划移植更多有用的工具

其他
------

不想玩了记得kill掉sshd进程，之前需要指定pid文件就是方便你获得 pid

kill `cat dropbear/db.pid`

`获得QPython App <https://github.com/qpython-android/qpython/releases/tag/v2.4.0>`_
