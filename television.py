
class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False
        return self.__status
    
    def mute(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            elif self.__muted == False:
                self.__muted = True

        return self.__muted

    def channel_up(self):
        if self.__status == True:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

        return self.__channel

    def channel_down(self):
        if self.__status == True:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

        return self.__channel

    def volume_up(self):
        if self.__status == True:
            self.__muted == False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

        return self.__volume

    def volume_down(self):
        if self.__status == True:
            self.__muted == False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
         
        return self.__volume

    def __str__(self):
        if self.__muted == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
    