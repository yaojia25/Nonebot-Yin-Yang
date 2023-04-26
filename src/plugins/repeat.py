#!/usr/bin/python
# coding:utf-8
"""
@file       : repeat.py
@date       : 2023/4/25 17:38
@Author     : Jasyo
@Description: 
"""
from nonebot import on_keyword, on_command
from nonebot.adapters.onebot.v11 import Event, MessageSegment, Message, GroupMessageEvent
from nonebot.params import CommandArg


def _check_group(event: Event) -> bool:
    return event.get_type == 'group'


envy = on_keyword({"羡慕"})
fudu = on_command('echo', aliases={'复读'}, priority=10, block=True)


@envy.handle()
async def _(event: GroupMessageEvent):
    await envy.finish(MessageSegment.at(event.user_id) + Message("这值得你羡慕！"))


@fudu.handle()
async def _(args: Message = CommandArg()):
    if text := args.extract_plain_text():
        await fudu.finish(Message(text))
    else:
        await fudu.finish(Message('你想说啥呀？'))
