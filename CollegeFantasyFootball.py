def main():
    import CollegeFantasyFootballAPI
    import mysql.connector

    programIsRunning = True
   
    print("College Fantasy Football!")
    print("_________________________")
    start = input("what would you like to do: ")

    #this is used to start asking the user what they would like to do
    '''while programIsRunning:
        pass
    '''
    #CollegeFantasyFootballAPI.callPlayerSeasonStats(2019,"LSU",2,2) this is how you can make calls to the API


class Team:
    def __init__(self):
        self.name = input("Enter your team name: ")
        self.teamlineup = TeamLineUp()
    def team_information(self): # call if you want all the information on a team at once
        print(self.name)
        print(self.teamlineup.lineup)
    def changeTeamName(self):# use to change the name if wanted
        self.name = input("what do you want you new name to be: ")
    

class GetPlayerInfo:
    pass

#creates the line up and can add players to the line up
class TeamLineUp:
    def __init__(self):
        self.lineup = {"QB" : "", "RB1": " ","RB2" : "","WR1" : "","WR2" : "","FLEX" : "","DEF" : "" ,"KICKER" : ""}
    def assign_player(self, position, player):
        if position not in self.lineup:#will check to see if the position the user typed is in the line up
            print("That player does not play that position")
        else:
            self.lineup[position] = player # assigns the player to the postion 
    


if __name__ == '__main__':
    main()
    