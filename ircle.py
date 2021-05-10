#!/usr/bin/env python3

import asyncio
import os
import sys
import reddit_posts

# Constants

HOST = 'chat.ndlug.org'
PORT = 6697
NICK = f'buireddit'

# Functions

async def ircle():
    reader, writer = await asyncio.open_connection(HOST, PORT, ssl=True)

    # Identify ourselves
    writer.write(f'USER {NICK} 0 * :{NICK}\r\n'.encode())
    writer.write(f'NICK {NICK}\r\n'.encode())
    await writer.drain()

    # Join #bots channel
    writer.write(f'JOIN #bots\r\n'.encode())
    await writer.drain()

    # Write message to channel
	
	# get comment to write
    token = reddit_posts.get_token()
    comment = reddit_posts.get_random_reddit_comment(token)



    writer.write(f"PRIVMSG #bots :I'm bui and I post insightful comments.\r\n".encode())
    await writer.drain()

    # Read and display
    while True:
	#	data = irc.recv( 4096  )

        message = (await reader.readline()).decode().strip()
        if "PING" in message:
            new_message = message.split()[1]
            writer.write(f"PONG {new_message}\r\n".encode())
            await writer.drain()
        if '!bui_test' in message:
            token = reddit_posts.get_token()
            comment = reddit_posts.get_random_reddit_comment(token)
            writer.write(f"PRIVMSG #bots :{comment}\r\n".encode())
            await writer.drain()
        print(message)

# Main execution

def main():
    asyncio.run(ircle())

if __name__ == '__main__':
    main()
