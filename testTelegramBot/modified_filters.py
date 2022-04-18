from telegram import Message
from telegram.ext import (
     MessageFilter
)


class NewFilter(MessageFilter):
    flag = 0

    def filter(self, message: Message) -> bool:
        self.flag = self.flag + 1
        return self.flag <= 2