# 接口自动化测试框架

- 框架采用：python 的request库进行接口的post、get、delete...请求，并继承unittest单元测试框架
- 特点：可以实现接口流程测试，接口之间的数据可以相互依赖
- 实现方式和流程：

  1.入口:
  
  提交测试用例（xls文件或MySQL）
  
  2.处理：
  
  框架通过读取测试用例，获取‘操作对象’，‘执行动作，‘测试数据’，‘预期结果’，通过request库中的get、post、put、delete...模拟接口请求
  
  3.出口：
  
  将实际与预期的比较结果写入测试用例中，同时将用例的执行的情况（pass、fail）记录在报告中，通过邮件发给相关人员
