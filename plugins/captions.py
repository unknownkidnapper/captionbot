#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#basic version

import asyncio
import os
import sqlite3
import time

from sample_config import Config
from translation import Translation

import pyrogram
from pyrogram import Client, filters as Filters



@Client.on_message(Filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_MSG,
    )
   

@Client.on_message(Filters.document & ~Filters.edited) # @pyrogram.Client.on_message(pyrogram.Filters.document | Filters.video) set like this to trigger both or remove filters.document and add filters.video for video only
async def old(bot, update):
    await bot.edit_message_caption(
        chat_id=update.chat.id,
        message_id=update.message_id,
        caption="""<b>❤️Fɪʀꜱᴛ Oɴ Tᴇʟᴇɢʀᴀᴍ❤️
━━━━━━━━━━━━━━━━
➠Cʜᴀɴɴᴇʟ : @Universal_Cinemas
➠Cʜᴀɴɴᴇʟ : @UC_Links</b>"""
        #also you can set html or none
        )
