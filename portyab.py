#author: merzmostafaei, github: www.github.com/merkhub
-#-------------------------------------------------------
from typing import Final
import logging
from telegram import Update
from telegram.ext import *

import socket
import ipaddress
import re

TOKEN: Final = '6440698125:AAEt0-_R2RuLqPHIqsFIezdRjKmGwnHLjVc'
BOT_USERNAME: Final = 'PortyabBot'
port_min = 7
port_max = 996


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Send me the ip address before anyone finds out what happend,use /ip <ip address>, or /help command. i need 2 minutes to see all open port,please wait.. ')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('this bot work like Nmap tool to find important open port between 7-995,how to use? it''s too simple, just use the command and ip version 4, for Example : /ip 192.168.1.1 ')


#async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #await update.message.reply_text('what happen? ')

async def ip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):



     ip_address = context.args[0]

     if re.match(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", ip_address):
        open_ports = []
        ip_add_entered = ip_address.strip()

        for port in range(port_min, port_max + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.1)
                    s.connect((ip_add_entered, port))
                    open_ports.append(port)
            except:
                pass
     
        if open_ports:
            open_ports_str = ', '.join(str(port) for port in open_ports)
            return await update.message.reply_text(
 f"Open ports on {ip_add_entered}: {open_ports_str}")
        else:
            return await update.message.reply_text(
 f"No open ports found on {ip_add_entered}")

     else:
        await update.message.replay_text(f"Please Write only ipv4 , or use /help command")




async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('just ipv4 version Support ')
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('ip',ip_command))
    #app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.Text, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print("Polling.....")
    app.run_polling(poll_interval=3)  # Corrected parameter name
