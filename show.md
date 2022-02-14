"""找到两种方法

方法一： pip install pyexcel_xls

测试没成功，还是报错。

方法二：后面需要弄清楚新的改动

先删除已安装的xlrd

pip uninstall xlrd

再安装低版本xlrd搞定

pip install xlrd==1.2.0"""






'''
参考
【方法】HTML网页调用本地Python程序
https://blog.csdn.net/yzy_1996/article/details/80223053?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164156497716780357230088%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=164156497716780357230088&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~sobaiduend~default-1-80223053.nonecase&utm_term=html%E8%B0%83%E7%94%A8python%E8%84%9A%E6%9C%AC&spm=1018.2226.3001.4450

python基础：web =html+ python
https://blog.csdn.net/eyeofeagle/article/details/86776642?spm=1001.2101.3001.6650.8&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-8.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-8.no_search_link&utm_relevant_index=11

PHP文件上传|菜鸟教程
https://www.runoob.com/php/php-file-upload.html

如何从html表单执行python脚本并返回resu
https://www.cnpython.com/qa/324090

'''


'''
<!-- 
    v1大致需求：2022.1.4知识点{PHP HTML PYTHON JSON}
    下拉框选择已导入（存在）班级数据
    "文本框"视图

已完败，准备转战flask框架，进入V2阶段

    v2改进方向：
    用python flask框架重构


    v3展望：
    数据库引用
    后台管理系统？慢慢来吧
    安全漏洞管理

    利用cookies 或 sessions 对不同用户提供差异化服务

 -->
 '''
逻辑： 
查看已经导入的班级并选择（加入cookies）->
上传文件（根据cookies命名）->


前言:
本网站是基于作者遇到的...


 更新记录
v1.0    2022.01.01
基本功能的实现 ：但技术复杂散乱 文件上传（php）check（python）   具有一定的小bug
v1.1    2022.02.12
用flask框架重构 羡慕逻辑优化 优化无用代码
