### 流程控制语句
1 if else  
格式基本如下:  

```
     {% if friut is 'nothing' %}
    <h1>my favorite friut is apple and banana</h1>
    {% else %}
    <h1>my favorite friut is {{ friut }}</h1>
    {% end %}

```  

2 在模板中使用函数  
* escape(s) 替换字符串s中的& < > 为对应的HTML 格式编码  
*url_escape(s) 使用urllib.quote_plus 替换字符串s中的字符为URL编码格式  
* json_encode(val) 将val 编码成json 格式  
* squeeze(s) 过滤字符串s，把连续多个空白字符替换成一个空格  
