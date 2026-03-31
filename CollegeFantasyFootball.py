class Team:
    def __init__(self, name):
        self.name = name
        self.teamlineup = TeamLineUp()
    def team_information(self):
        print(self.name)
        print(self.teamlineup.lineup)
    

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
    


def main():
    team1 = Team("jaccobs Team")
    team1.teamlineup.assign_player("QB","josh allen")
    team1.team_information()


if __name__ == '__main__':
    main()