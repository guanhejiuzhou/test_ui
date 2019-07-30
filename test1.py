#-*-coding:utf-8-*-
import json

list1=[1,2,3,4,5]
print('\n 对列表进行序列化和反序列化的处理：')
print('列表未序列化之前的数据类型：',type(list1))
#对列表list1进行序列化处理
list_str=json.dumps(list1)
#序列化后数据类型为str
print('列表list1序列化后的内容:{0}和类型{1}'.format(list_str,type(list_str)))
#对字符串list_str进行反序列化处理
str_list=json.loads(list_str)
#反序列化后类型为list
print('字符串list_str反序列化后的内容:{0}和类型:{1}'.format(str_list,type(str_list)))

print('哈哈哈')
print('哈哈哈')