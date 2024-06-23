文件简单说明（最新版本）：
test.sql：创建数据库memorized；在该数据库中创建总单词表words，
插入所有单词记录（包括CET4,CET6_2,SAT_2,TOEFL_2等词典内容），
不需要直接执行，“设置词库”页面调用main.py中的main函数并传递book_id；
main.py：在其main函数中创建词库，设置当前词典并初始化已背词表与未背词表；
test.py:测试各项功能；
vocabulary.py:通过其中的change_book(new_book_id)函数可以切换词典，并重置已背词表与未背词表；
其他文件功能省略介绍
app.py文件中实现flask架构的后端服务器，后续其他功能接口在该文件中添加；



6/21/16:42
v2 edited by 付芷怡 then 邵虹
修改内容：
把main函数中的词性和词义注释取消了，然后修改了vocabulary中的获取词性词义；
修改test.sql row 2内容（ 'ɪk''splosɪv; ɪk''splozɪv', ->'''ɪk''splozɪv'

6/21/17:05
v3 edited by 付芷怡 then 邵虹
修改内容：
main函数中增加了一个单独变量book_id，用于导入未背词表和完整词库的查询
unmemorized.py中的transfer_to_unmemorized函数增加了有效输入
vocabulary.py中的get_word_meaning和get_word_example增加了book_id作为参数输入
修改了test.sql，加入了完整的词库

6/21/21：23
v4 edited by 邵虹
1.vocabulary增加全局变量book_id，增加函数change_book用于修改词典，重置已背词表和未背词表；
get_word_meaning和get_word_example用全局变量代替book_id参数输入；
增加clear_Memorized_Database用于删除词库memorized；
2.memorized.py增加clear_memorized_vocabulary函数清空已背词表
3.在main.py中增加create_database函数创建词库memorized，并初始化总词表words；
将main.py重构为main.py和test.py，main.py和test.py功能见文件简单说明。



