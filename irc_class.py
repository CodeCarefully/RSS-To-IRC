#Credit Meenakshi Agarwal - https://www.techbeamers.com/create-python-irc-bot/
#shortlink: https://archive.st/ef60
#no license found for this file.


import socket
import sys
import time
import ssl
import socket

class IRC:
    irc = socket.socket()

    def __init__(self):
        # Define the socket
        ctx = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
        self.ircsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc = ctx.wrap_socket(self.irc)

    def send(self, channel, msg):
        # Transfer data
        self.irc.send(bytes("PRIVMSG " + channel + " " + msg + "\n", "UTF-8"))

    def connect(self, server, port, channel, botnick, botpass, botnickpass):
        # Connect to the server
        print("Connecting to: " + server)
        self.irc.connect((server, port))

        # Perform user authentication
        self.irc.send(bytes("USER " + botnick + " " + botnick + " " + botnick + " :python\n", "UTF-8"))
        self.irc.send(bytes("NICK " + botnick + "\n", "UTF-8"))
        if botnickpass != "guido" and botnickpass != "" and botpass != "<%= @guido_password %>" and botpass != "":
            self.irc.send(bytes("NICKSERV IDENTIFY " + botnickpass + " " + botpass + "\n", "UTF-8"))
        time.sleep(5)

        # join the channel
        self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))


    def get_response(self):
        time.sleep(1)
        # Get the response
        resp = self.irc.recv(2040).decode("UTF-8")


        if resp.find("PING") != -1:
            self.irc.send(bytes("PONG " + resp.split()[1] + "\n","UTF-8"))

        return resp