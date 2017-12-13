### 字符串的服务
* 1 状态码解读  

-- 404 Not Found  
  请求路径无法匹配RequestHandler 类相对应的模式   
-- 400 Bad Request  
如果你调用了一个没有默认值的get_argument 函数，同时也没有发现给定名称的参数，将会返回一个400  
-- 405 Method Not Allowed   
如果传入的请求使用了RequestHandler中没有定义的HTTP方法，定义的post,但是使用的get 方法。  
-- 500 Internal Server Error  
当程序遇到任何不能让其退出的错误时，返回500，代码中任何没有捕获的异常也会导致500 响应码  
-- 200 OK
请求响应成功，返回200  

