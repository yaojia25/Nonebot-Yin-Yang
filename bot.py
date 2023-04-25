#!/usr/bin/python",
# coding:utf-8",
"""
@file       : 
@date       :  
@Author     : Jasyo
@Description: 
"""
import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter


# 初始化 NoneBot
nonebot.init()

# 注册适配器
driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

# 在这里加载插件
nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run()