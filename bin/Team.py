import sys
from Player import Player

#def main(args):
#    j = Team()
#    j.add_assists()
#    j.add_caps()
#    j.add_counterattack()
#    j.add_foul()
#    j.goals = 1
#    print(j.name_lastname)
#    print(j.team_name)
#    print(j.position)
#    print(j.goals)
#    print(j.is_rival)
#    print(j.shots_rate(), "%")
#    sys.exit()


class Team(Player):
    team_name = ""
    team_players = []

    def __init__(self, name = "Equipo de Handball", players = []):
        Player.__init__(self, rival = rival_t)
        self.team_name = name
        self.team_players = players

    def goals_team(self, team_players):
        for p in team_players:
            self.goals = self.goals + p.goals
            self.goals_6m = self.goals_6m + p.goals_6m
            self.goals_9m = self.goals_9m + p.goals_9m

    def goals_team(self, team_players):
        for p in team_players:
            self.goals = self.goals + p.goals
            self.goals_6m = self.goals_6m + p.goals_6m
            self.goals_9m = self.goals_9m + p.goals_9m

    def lost_goals_team(self, team_players):
        for p in team_players:
            self.lost_goals = self.lost_goals + p.lost_goals

    def counter_attack_team(self, team_players):
        for p in team_players:
            self.counter_attack = self.counter_attack + p.counter_attack

    def won_balls_team(self, team_players):
        for p in team_players:
            self.won_balls = self.won_balls + p.won_balls

    def caps_team(self, team_players):
        for p in team_players:
            self.caps = self.caps + p.caps

    def lost_balls_team(self, team_players):
        for p in team_players:
            self.lost_balls = self.lost_balls + p.lost_balls

    def foul_team(self, team_players):
        for p in team_players:
            self.foul = self.foul + p.foul

    def foul_received_team(self, team_players):
        for p in team_players:
            self.foul_received = self.foul_received + p.foul_received

    def yellow_card_team(self, team_players):
        for p in team_players:
            self.yellow_card = self.yellow_card + p.yellow_card

    def red_card_team(self, team_players):
        for p in team_players:
            self.red_card = self.red_card + p.red_card

    def two_minutes_team(self, team_players):
        for p in team_players:
            self.two_minutes = self.two_minutes + p.two_minutes

    def head_off_team(self, team_players):
        for p in team_players:
            if p.is_goalkeeper:
                self.head_off = self.head_off + p.head_off

    def shots_rate(self):
        return((self.goals / (self.goals + self.lost_goals) * 100))

    def arch_vulnerability(self, rival_goals):
        return((rival_goals / (self.head_off_team + rival_goals) * 100))


#if __name__ == '__main__':
#    main(sys.argv)
