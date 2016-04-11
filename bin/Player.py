import sys


#def main(args):
#    j = Player(False, False, "Enzo Valverdi", "Armador")
#    j.add_assists()
#    j.add_caps()
#    j.add_counterattack()
#    j.add_foul()
#    j.add_goal(9)
#    print(j.name_lastname)
#    print(j.position)
#    print(j.goals)
#    sys.exit()


class Player:
    # Player data
    name_lastname = ""
    position = ""

    # Player data of match
    goals_9m = 0
    goals_6m = 0
    goals = 0
    lost_goals = 0
    counter_attack = 0
    assists = 0
    won_balls = 0
    caps = 0
    lost_balls = 0
    foul = 0
    foul_received = 0
    yellow_card = 0
    two_minutes = 0
    red_card = 0
    is_goalkeeper = False
    is_rival = False
    head_off = 0

    def __init__(self, goalkeeper = False, rival = False, name = "Jugador ",
                 position = "Jugador de Campo"):
        self.goalkeeper = goalkeeper
        self.is_rival = rival
        self.name_lastname = name
        self.position = position

    def add_goal(self, metre):
        if metre == 9:
            self.goals_9m += 1
        else:
            self.goals_6m += 1
        self.goals += 1

    def add_lostgoal(self):
        self.lost_goals += 1

    def add_counterattack(self):
        self.counter_attack += 1

    def add_assists(self):
        self.assists += 1

    def add_wonball(self):
        self.won_balls += 1

    def add_lostball(self):
        self.lost_balls += 1

    def add_caps(self):
        self.caps += 1

    def add_foul(self):
        self.foul += 1

    def add_foulreceived(self):
        self.foul_received += 1

    def set_yellowcard(self):
        self.yellow_card += 1

    def add_twominutes(self):
        self.two_minutes += 1

    def set_redcard(self):
        self.red_card += 1

    def add_headoff(self):
        self.head_off += 1

    def get_off_goal(self, metre):
        if metre == 9:
            self.goals_9m -= 1
        else:
            self.goals_6m -= 1
        self.goals -= 1

    def get_off_lostgoal(self):
        self.lost_goals -= 1

    def get_off_counterattack(self):
        self.counter_attack -= 1

    def get_off_assists(self):
        self.assists -= 1

    def get_off_wonball(self):
        self.won_balls -= 1

    def get_off_lostball(self):
        self.lost_balls -= 1

    def get_off_caps(self):
        self.caps -= 1

    def get_off_foul(self):
        self.foul -= 1

    def get_off_foulreceived(self):
        self.foul_received -= 1

    def get_off_yellowcard(self):
        self.yellow_card -= 1

    def get_off_redcard(self):
        self.red_card -= 1

    def get_off_twominutes(self):
        self.two_minutes -= 1

    def get_off_headoff(self):
        self.head_off -= 1

    def get_score(self):
        if self.is_goalkeeper:
            score = (self.goals + self.assists + self.won_balls + self.caps +
                     self.foul_received + self.head_off - self.lost_goals -
                     self.lost_balls - self.foul - self.two_minutes)
        else:
            score = (self.goals + self.assists + self.won_balls + self.caps +
                     self.foul_received - self.lost_goals - self.lost_balls -
                     self.foul - self.two_minutes)
        return(score)

#if __name__ == '__main__':
#    main(sys.argv)
