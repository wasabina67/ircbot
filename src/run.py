import irc.bot


class Bot(irc.bot.SingleServerIRCBot):

    def __init__(self, server="ngircd", port=6667, nickname="bot", channel="#bot"):
        super().__init__(server_list=[(server, port)], nickname=nickname, realname=nickname)
        self.nickname = nickname
        self.channel = channel

    def on_welcome(self, connection, event):
        connection.join(self.channel)


def main():
    b = Bot()
    b.start()


if __name__ == "__main__":
    main()
