# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝚃𝚎𝚗𝚝𝚊𝚗𝚐 𝙰𝚔𝚞 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝚃𝚞𝚝𝚞𝚙 𝙰𝚔𝚞 •", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝙶𝚛𝚘𝚞𝚙", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝚃𝚎𝚗𝚝𝚊𝚗𝚐 𝙰𝚔𝚞 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝚃𝚞𝚝𝚞𝚙 𝙰𝚔𝚞 •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝙲𝚑𝚊𝚗𝚗𝚎𝚕01", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• 𝚃𝚎𝚗𝚝𝚊𝚗𝚐 𝙰𝚔𝚞 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝚃𝚞𝚝𝚞𝚙 𝙰𝚔𝚞 •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝙲𝚑𝚊𝚗𝚗𝚎𝚕02", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• 𝚃𝚎𝚗𝚝𝚊𝚗𝚐 𝙰𝚔𝚞 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝚃𝚞𝚝𝚞𝚙 𝙰𝚔𝚞 •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝚃𝚎𝚗𝚝𝚊𝚗𝚐 𝙰𝚔𝚞 •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="𝙲𝚑𝚊𝚗𝚗𝚎𝚕01", url=client.invitelink),
                InlineKeyboardButton(text="𝙲𝚑𝚊𝚗𝚗𝚎𝚕02", url=client.invitelink3),
                InlineKeyboardButton(text="𝙶𝚛𝚘𝚞𝚙", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="• 𝚃𝚞𝚝𝚞𝚙 𝙰𝚔𝚞 •", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝙹𝚘𝚒𝚗 𝙶𝚛𝚘𝚞𝚙", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="𝙺𝚕𝚒𝚔 𝚂𝚊𝚢𝚊",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝙹𝚘𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕01", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝙹𝚘𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕02", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="𝙺𝚕𝚒𝚔 𝚂𝚊𝚢𝚊",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝙹𝚘𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕01", url=client.invitelink),
                InlineKeyboardButton(text="𝙹𝚘𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕02", url=client.invitelink3),
                InlineKeyboardButton(text="𝙹𝚘𝚒𝚗 𝙶𝚛𝚘𝚞𝚙", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="𝙺𝚕𝚒𝚔 𝚂𝚊𝚢𝚊",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
