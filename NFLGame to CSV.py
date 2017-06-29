import nflgame
import csv
"""
Creates .csv of certains stats over 8 year span. This is rewritten version, but can still be improved.

Author: Mitchell T. Diedrich
"""
def main():
    # Necessary lists
    seasonList, seasons, score, firstDowns, totalYards, passingYards, rushingYards, penaltyCount, penaltyYards, \
    turnovers, puntCount, puntYards, puntAverage = [], [], [], [], [], [], [], [], [], [], [], [], []
    # Creates each season
    for x in range(0,8):
        seasonListIteration = nflgame.games(x+2009)
        seasons += [x+2009 for y in range (0, len(seasonListIteration))]
        seasonList += seasonListIteration
    # Populates lists for each season
    for x in seasonList:
        score += [x.score_home, x.score_away]
        firstDowns += [x.stats_home.first_downs, x.stats_away.first_downs]
        totalYards += [x.stats_home.total_yds, x.stats_away.total_yds]
        passingYards += [x.stats_home.passing_yds, x.stats_away.passing_yds]
        rushingYards += [x.stats_home.rushing_yds, x.stats_away.rushing_yds]
        penaltyCount += [x.stats_home.penalty_cnt, x.stats_away.penalty_cnt]
        penaltyYards += [x.stats_home.penalty_yds, x.stats_away.penalty_yds]
        turnovers += [x.stats_home.turnovers, x.stats_away.turnovers]
        puntCount += [x.stats_home.punt_cnt, x.stats_away.punt_cnt]
        puntYards += [x.stats_home.punt_yds, x.stats_away.punt_yds]
        puntAverage += [x.stats_home.punt_avg, x.stats_away.punt_avg]
    # Writes .CSV with format Score, First Downs, Total Yards, Passing Yards, Rushing Yards, Penalty Count,
    # Penalty Yards, Turnovers, Punt Count, Punt Yards, Punt Average
    with open('NFL Stats Rewrite.csv', 'wb') as csvfile:
        gameWriter = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        gameWriter.writerow(['Score', 'First Downs', 'Total Yards', 'Passing Yards', 'Rushing Yards', 'Penalty Count',
                             'Penalty Yards', 'Turnovers', 'Punt Count', 'Punt Yards', 'Punt Average'])
        for x in range(0, len(score)):
            gameWriter.writerow(
                [score[x], firstDowns[x], totalYards[x], passingYards[x], rushingYards[x], penaltyCount[x],
                 penaltyYards[x], turnovers[x], puntCount[x], puntYards[x], puntAverage[x]])

if __name__ == "__main__":
    main()