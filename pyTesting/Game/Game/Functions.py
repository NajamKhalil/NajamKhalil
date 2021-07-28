class Functions():
    def __init__(self):
        self.location1 = '-';self.location2 = '-';self.location3 = '-'
        self.location4 = '-';self.location5 = '-';self.location6 = '-'
        self.location7 = '-';self.location8 = '-';self.location9 = '-'
        self.result = 'Game Test TicTacToe'
    def resetFunction(self):
        self.location1 = '-';
        self.location2 = '-';
        self.location3 = '-'
        self.location4 = '-';
        self.location5 = '-';
        self.location6 = '-'
        self.location7 = '-';
        self.location8 = '-';
        self.location9 = '-'
        self.result = 'Game Test TicTacToe'
    def winningLogic(self):
        if(self.location1==self.location2==self.location3=='X' or self.location1==self.location2==self.location3=='O'):
            self.result ="Congradulation " + self.location1+ " Wins"
        elif (self.location4== self.location5 == self.location6=='X' or self.location4== self.location5 == self.location6=='O'):
            self.result ="Congradulation " + self.location4+ " Wins"
        elif (self.location7 == self.location8 == self.location9=='X' or self.location7 == self.location8 ==self.location9=='O'):
            self.result ="Congradulation " + self.location7+ " Wins"
        elif (self.location1 == self.location4 == self.location7=='X' or self.location1 == self.location4 == self.location7=='O'):
            self.result ="Congradulation " + self.location1+ " Wins"
        elif (self.location2 == self.location5 == self.location8=='X' or self.location2 == self.location5 == self.location8=='O'):
            self.result ="Congradulation " + self.location2+ " Wins"
        elif (self.location3 == self.location6 == self.location9=='X' or self.location3 == self.location6 == self.location9=='O'):
            self.result ="Congradulation "+ self.location3+ " Wins"
        elif (self.location1 == self.location5 == self.location9=='X' or self.location1 == self.location5 ==self.location9=='O'):
            self.result ="Congradulation "+ self.location1+ " Wins"
        elif (self.location7 == self.location5 == self.location3=='X' or self.location7 == self.location5 ==self.location3=='O'):
            self.result ="Congradulation "+ self.location7+ " Wins"
        else:
            self.result = 'Game Test TicTacToe'
    def but1Function(self,playerFlag):
        if(playerFlag==True):
            self.location1='X'
        else:
            self.location1 = 'O'
        self.winningLogic()
    def but2Function(self,playerFlag):
        if (playerFlag == True):
            self.location2 = 'X'
        else:
            self.location2 = 'O'
        self.winningLogic()
    def but3Function(self,playerFlag):
        if (playerFlag == True):
            self.location3 = 'X'
        else:
            self.location3 = 'O'
        self.winningLogic()
    def but4Function(self,playerFlag):
        if (playerFlag == True):
            self.location4 = 'X'
        else:
            self.location4 = 'O'
        self.winningLogic()
    def but5Function(self,playerFlag):
        if (playerFlag == True):
            self.location5 = 'X'
        else:
            self.location5 = 'O'
        self.winningLogic()
    def but6Function(self,playerFlag):
        if (playerFlag == True):
            self.location6 = 'X'
        else:
            self.location6 = 'O'
        self.winningLogic()
    def but7Function(self,playerFlag):
        if (playerFlag == True):
            self.location7 = 'X'
        else:
            self.location7 = 'O'
        self.winningLogic()
    def but8Function(self,playerFlag):
        if (playerFlag == True):
            self.location8 = 'X'
        else:
            self.location8 = 'O'
        self.winningLogic()
    def but9Function(self,playerFlag):
        if (playerFlag == True):
            self.location9 = 'X'
        else:
            self.location9 = 'O'
        self.winningLogic()
