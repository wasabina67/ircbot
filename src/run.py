import time

import irc.bot  # type: ignore


class Bot(irc.bot.SingleServerIRCBot):

    def __init__(
        self, server="ngircd", port=6667, nickname="bot", channel="#botchannel"
    ):
        super().__init__(
            server_list=[(server, port)], nickname=nickname, realname=nickname
        )
        self.nickname = nickname
        self.channel = channel

    # def on_connect(self, connection, event):
    #     print("[debug] on_connect has been called.")

    def on_welcome(self, connection, event):
        print("[debug] on_welcome has been called.")
        print(f"[debug] {event.arguments[0]}")
        connection.join(self.channel)
        # self.reactor.scheduler.execute_every(10, self.notice_time)

    def on_nicknameinuse(self, connection, event):
        print("[debug] on_nicknameinuse has been called.")
        connection.nick(connection.get_nickname() + "2")

    def on_privmsg(self, connection, event):
        # connection.privmsg(event.source.nick, event.arguments[0])
        pass

    def on_pubmsg(self, connection, event):
        pass

    def get_current_time(self):
        return time.strftime("%Y-%m-%d (%a) %H:%M:%S")

    def notice_time(self):
        self.connection.notice(self.channel, self.get_current_time())

    def privmsg_time(self):
        self.connection.privmsg(self.channel, self.get_current_time())


def main():
    b = Bot()
    b.start()


if __name__ == "__main__":
    main()
