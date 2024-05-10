#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json2lua
import json

# 指定JSON文件的路径
file_name = 'C:\\Users\\user\\Documents\\youdu\\14640746-100681-linchuzhang\\file\\pc_player_load_data.json'

# 使用with语句打开文件并读取内容
with open(file_name, 'r') as file:
    # 使用json.load()将文件内容转换为Python对象，并赋值给jsonStr
    jsonStr = json.load(file)

# 此时，jsonStr变量包含了JSON文件中的数据，可以根据需要进一步处理
# print(jsonStr)
# print(jsonStr)

# print(type({}),end='\n')
# print(type([]),end='\n')
# print(type(""),end='\n')
# print(type(1),end='\n')
# print(type(1.2),end='\n')
# print(type(True),end='\n')
# print(type(False),end='\n')
# print(type(None),end='\n')
print(json2lua.str_to_lua_table(jsonStr))
json2lua.file_to_lua_file(file_name,"./test.lua")
