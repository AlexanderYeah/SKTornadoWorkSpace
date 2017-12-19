### block 的使用

简单来讲,模板的扩展可以服用之前写的代码。
父模板: main.html 定时一个header 使用

{% block header %} {% end %}

子模板：
* 扩展父模板
{% extends "main.html" %}
进行使用
{% block header %} 这里可以加上自己定义的东西{% end %}


