
class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Method to initialize object variables for television object
        :param self.__status: TV Power Status On / Off
        :param self.__muted: TV Muted Status On / Off
        :param self.__volume: TV Volume Level
        :param self.__channel: TV Channel Number
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Method to turn TV on or off
        '''
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False
    
    def mute(self) -> None:
        '''
        Method to mute or unmute TV
        '''
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            elif self.__muted == False:
                self.__muted = True

    def channel_up(self) -> None:
        '''
        Method to increase the TV channel number
        '''
        if self.__status == True:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Method to decrease the TV channel number
        '''
        if self.__status == True:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        Method to increase the TV volume
        '''
        if self.__status == True:
            self.__muted == False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Method to decrease the TV volume
        '''
        if self.__status == True:
            self.__muted == False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Method to return a string of the TV configurations Power, Channel, Volume
        '''
        if self.__muted == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
    