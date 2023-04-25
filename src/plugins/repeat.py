#!/usr/bin/python",
# coding:utf-8",
"""
@file       : repeat.py
@date       : 2023/4/25 17:38
@Author     : Jasyo
@Description: 
"""
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Event, MessageSegment,Message,GroupMessageEvent


def _check_group(event: Event) -> bool:
    return event.get_type == 'group'


envy = on_keyword({"羡慕"})


@envy.handle()
async def _(event: GroupMessageEvent):
    await envy.finish(MessageSegment.at(event.user_id) + Message("这值得你羡慕！"))
