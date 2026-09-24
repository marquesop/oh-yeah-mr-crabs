# Playoff_PREDICTOR.py
team_name = "wildcats"

wins = 12
losses = 4

games_played = wins + losses

win_percentage = wins / games_played

if win_percentage > .58:
    print(team_name, "is likely to make the playoffs!")
else:
    print(team_name, "is unlikely to make the playoffs.")

print("Team:", team_name)

if wins > 10:
    print("Winning season!")

def winning_record(wins, losses):
    return wins > losses

result = winning_record(wins, losses)

print("Winning record?", result)

print("winning_record?", result)


print("Games played:", games_played)
print("win Percentage:", win_percentage)
print("win Percentage:", win_percentage * 100, "%")