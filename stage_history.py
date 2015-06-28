import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collegefootballpick10.settings')

import django
django.setup()

from django.core.exceptions import ObjectDoesNotExist

from pick10.models import Team, Game, Pick
from pick10.models import add_user, add_conference, add_team, add_game, add_week, add_pick
from pick10.models import get_user_by_username, get_team, get_game, get_week
from pick10.models import update_game

from excel_history.excel.spreadsheet_test import player_username, get_player_years_dict
from excel_history.excel.pool_spreadsheet import PoolSpreadsheet

def populate_users():
    # First test to see if a particular user exists, if so then skip the populate
    try:
        u = get_user_by_username('reams_byron')
        print "    Found an expected user, returning..."
        return
    except ObjectDoesNotExist:
        print "    Executing the populate..."
    except:
        raise

    for ss_name, username in player_username.iteritems():
        last, first = username.split('_')
        email = '%s_%s@example.com' % (first, last,)
        add_user(username, email, first.capitalize(), last.capitalize())

def populate_conferences_teams():
    # First test to see if a particular team exists, if so then skip the populate
    try:
        t = get_team('Ball State')
        print "    Found an expected team, returning..."
        return
    except ObjectDoesNotExist:
        print "    Executing the populate..."
    except:
        raise

    # American Athletic
    conf = add_conference('American Athletic')
    add_team('Cincinnati', 'Bearcats', conf)
    add_team('Connecticut', 'Huskies', conf)
    add_team('East Carolina', 'Pirates', conf)
    add_team('Houston', 'Cougars', conf)
    add_team('Memphis', 'Tigers', conf)
    add_team('South Florida', 'Bulls', conf)
    add_team('Southern Methodist', 'Mustangs', conf)
    add_team('Temple', 'Owls', conf)
    add_team('Tulane', 'Green Wave', conf)
    add_team('Tulsa', 'Golden Hurricane', conf)
    add_team('UCF', 'Knights', conf)

    # Atlantic Coast - Atlantic
    conf = add_conference('Atlantic Coast', 'Atlantic')
    add_team('Boston College', 'Eagles', conf)
    add_team('Clemson', 'Tigers', conf)
    add_team('Florida State', 'Seminoles', conf)
    add_team('Louisville', 'Cardinals', conf)
    add_team('NC State', 'Wolfpack', conf)
    add_team('Syracuse', 'Orange', conf)
    add_team('Wake Forest', 'Demon Deacons', conf)
    # Atlantic Coast - Coastal
    conf = add_conference('Atlantic Coast', 'Coastal')
    add_team('Duke', 'Blue Devils', conf)
    add_team('Georgia Tech', 'Yellow Jackets', conf)
    add_team('Miami-Florida', 'Hurricanes', conf)
    add_team('North Carolina', 'Tarheels', conf)
    add_team('Pittsburgh', 'Panthers', conf)
    add_team('Virginia', 'Cavaliers', conf)
    add_team('Virginia Tech', 'Hokies', conf)

    # Big Ten - East
    conf = add_conference('Big Ten', 'East')
    add_team('Indiana', 'Hoosiers', conf)
    add_team('Maryland', 'Terrapins', conf)
    add_team('Michigan', 'Wolverines', conf)
    add_team('Michigan State', 'Spartans', conf)
    add_team('Ohio State', 'Buckeyes', conf)
    add_team('Penn State', 'Nittany Lions', conf)
    add_team('Rutgers', 'Scarlet Knights', conf)
    # Big Ten - West
    conf = add_conference('Big Ten', 'West')
    add_team('Illinois', 'Illini', conf)
    add_team('Iowa', 'Hawkeyes', conf)
    add_team('Minnesota', 'Golden Gophers', conf)
    add_team('Nebraska', 'Cornhuskers', conf)
    add_team('Northwestern', 'Wildcats', conf)
    add_team('Purdue', 'Boilermakers', conf)
    add_team('Wisconsin', 'Badgers', conf)

    # Big 12
    conf = add_conference('Big 12')
    add_team('Baylor', 'Bears', conf)
    add_team('Iowa State', 'Cyclones', conf)
    add_team('Kansas', 'Jayhawks', conf)
    add_team('Kansas State', 'Wildcats', conf)
    add_team('Oklahoma', 'Sooners', conf)
    add_team('Oklahoma State', 'Cowboys', conf)
    add_team('TCU', 'Horned Frogs', conf)
    add_team('Texas', 'Longhorns', conf)
    add_team('Texas Tech', 'Red Raiders', conf)
    add_team('West Virginia', 'Mountaineers', conf)

    # Conference USA - East
    conf = add_conference('Conference USA', 'East')
    add_team('Florida Atlantic', 'Owls', conf)
    add_team('Florida International', 'Golden Panthers', conf)
    add_team('Marshall', 'Thundering Herd', conf)
    add_team('Middle Tennessee', 'Blue Raiders', conf)
    add_team('Old Dominion', 'Monarchs', conf)
    add_team('UAB', 'Blazers', conf)
    add_team('Western Kentucky', 'Hilltoppers', conf)
    # Conference USA - West
    conf = add_conference('Conference USA', 'West')
    add_team('Louisiana Tech', 'Bulldogs', conf)
    add_team('North Texas', 'Mean Green', conf)
    add_team('Rice', 'Owls', conf)
    add_team('Southern Miss', 'Golden Eagles', conf)
    add_team('Texas-El Paso', 'Miners', conf)
    add_team('Texas-San Antonio', 'Road Runners', conf)

    # Independents
    conf = add_conference('Independents')
    add_team('Army', 'Black Knights', conf)
    add_team('BYU', 'Cougars', conf)
    add_team('Navy', 'Midshipmen', conf)
    add_team('Notre Dame', 'Fighting Irish', conf)

    # Mid American - East
    conf = add_conference('Mid American', 'East')
    add_team('Akron', 'Zips', conf)
    add_team('Bowling Green', 'Falcons', conf)
    add_team('Buffalo', 'Bulls', conf)
    add_team('Kent State', 'Golden Flashes', conf)
    add_team('Massachusetts', 'Minutemen', conf)
    add_team('Miami-Ohio', 'Redhawks', conf)
    add_team('Ohio', 'Bobcats', conf)
    # Mid American - West
    conf = add_conference('Mid American', 'West')
    add_team('Ball State', 'Cardinals', conf)
    add_team('Central Michigan', 'Chippewas', conf)
    add_team('Eastern Michigan', 'Eagles', conf)
    add_team('Northern Illinois', 'Huskies', conf)
    add_team('Toledo', 'Rockets', conf)
    add_team('Western Michigan', 'Broncos', conf)

    # Mountain West - Mountain
    conf = add_conference('Mountain West', 'Mountain')
    add_team('Air Force', 'Falcons', conf)
    add_team('Boise State', 'Broncos', conf)
    add_team('Colorado State', 'Rams', conf)
    add_team('New Mexico', 'Lobos', conf)
    add_team('Utah State', 'Aggies', conf)
    add_team('Wyoming', 'Cowboys', conf)
    # Mountain West - West
    conf = add_conference('Mountain West', 'West')
    add_team('Fresno State', 'Bulldogs', conf)
    add_team('Hawaii', 'Rainbox Warriors', conf)
    add_team('Nevada', 'Wolf Pack', conf)
    add_team('San Diego State', 'Aztecs', conf)
    add_team('San Jose State', 'Spartans', conf)
    add_team('UNLV', 'Rebels', conf)

    # Pacific 12 - North
    conf = add_conference('Pacific 12', 'North')
    add_team('California', 'Golden Bears', conf)
    add_team('Oregon', 'Ducks', conf)
    add_team('Oregon State', 'Beavers', conf)
    add_team('Stanford', 'Cardinal', conf)
    add_team('Washington', 'Huskies', conf)
    add_team('Washington State', 'Cougars', conf)
    # Pacific 12 - South
    conf = add_conference('Pacific 12', 'South')
    add_team('Arizona', 'Wildcats', conf)
    add_team('Arizona State', 'Sun Devils', conf)
    add_team('Colorado', 'Buffaloes', conf)
    add_team('Southern Cal', 'Trojans', conf)
    add_team('UCLA', 'Bruins', conf)
    add_team('Utah', 'Utes', conf)

    # Southeastern - East
    conf = add_conference('Southeastern', 'East')
    add_team('Florida', 'Gators', conf)
    add_team('Georgia', 'Bulldogs', conf)
    add_team('Kentucky', 'Wildcats', conf)
    add_team('Missouri', 'Tigers', conf)
    add_team('South Carolina', 'Gamecocks', conf)
    add_team('Tennessee', 'Volunteers', conf)
    add_team('Vanderbilt', 'Commodores', conf)
    # Southeastern - West
    conf = add_conference('Southeastern', 'West')
    add_team('Alabama', 'Crimson Tide', conf)
    add_team('Arkansas', 'Razorbacks', conf)
    add_team('Auburn', 'Tigers', conf)
    add_team('LSU', 'Tigers', conf)
    add_team('Mississippi State', 'Bulldogs', conf)
    add_team('Mississippi', 'Rebels', conf)
    add_team('Texas A&M', 'Aggies', conf)

    # Sun Belt
    conf = add_conference('Sun Belt')
    add_team('Appalachian State', 'Mountaineers', conf)
    add_team('Arkansas State', 'Red Wolves', conf)
    add_team('Georgia Southern', 'Eagle', conf)
    add_team('Georgia State', 'Panthers', conf)
    add_team('Idaho', 'Vandals', conf)
    add_team('Louisiana Monroe', 'Warhawks', conf)
    add_team('New Mexico State', 'Aggies', conf)
    add_team('South Alabama', 'Jaguars', conf)
    add_team('Texas State', 'Bobcats', conf)
    add_team('Troy', 'Trojans', conf)
    add_team('Louisiana Lafayette', 'Ragin Cajuns', conf)

def populate_games_for_year(yearnum):
    poolspreadsheet = PoolSpreadsheet(yearnum)
    for weeknum in poolspreadsheet.get_week_numbers():
        print "      Populating games for week %d..." % (weeknum,)
        games = poolspreadsheet.get_games(weeknum)
        add_week(yearnum, weeknum)
        for game in games:
            favored = 1 if poolspreadsheet.get_game_favored_team(weeknum, game) == 'team1' else 2
            spread = poolspreadsheet.get_game_spread(weeknum, game)
            add_game(get_team(games[game].team1), get_team(games[game].team2), yearnum, weeknum, game, favored=favored, spread=spread)
            team1_actual_points = poolspreadsheet.get_game_team1_score(weeknum, game)
            team2_actual_points = poolspreadsheet.get_game_team2_score(weeknum, game)
            update_game(yearnum, weeknum, game, team1_actual_points, team2_actual_points, 3)

def populate_games(yearlist):
    for yearnum in yearlist:
        if len(Game.objects.filter(game_year=yearnum)) != 130:
            print "    Populating games for year %d..." % (yearnum,)
            populate_games_for_year(yearnum)
        else:
            print "    Games for year %d already populated, skipping..." % (yearnum,)

    for yearnum in yearlist:
        for weeknum in range(1, 14):
            if len(Game.objects.filter(game_year=yearnum, game_week=weeknum)) != 10:
                print "WARN: Year=%d, Week=%d, Did not find 10 games." % (yearnum, weeknum,)

def populate_picks_for_year_week(yearnum, weeknum, poolspreadsheet=None):
    try:
        numpicks = len(Pick.objects.filter(pick_game__game_year=yearnum, pick_game__game_week=weeknum))
        if numpicks > 10:
            print "        Picks for week %d already populated, skipping..." % (weeknum,)
            return
    except:
        pass

    if poolspreadsheet is None:
        poolspreadsheet = PoolSpreadsheet(yearnum)
    picks = poolspreadsheet.get_picks(weeknum)
    for pick in picks:
        game = get_game(yearnum, weeknum, pick.game_number)
        username = player_username[pick.player_name]
        user = get_user_by_username(username)
        pick_winner = 1 if pick.winner == 'team1' else 2
        if pick.team1_score:
            add_pick(pick_user=user, pick_game=game, pick_winner=pick_winner, team1_predicted_points=pick.team1_score, team2_predicted_points=pick.team2_score)
        else:
            add_pick(pick_user=user, pick_game=game, pick_winner=pick_winner)

def populate_picks_for_year(yearnum):
    poolspreadsheet = PoolSpreadsheet(yearnum)
    for weeknum in poolspreadsheet.get_week_numbers():
        print "      Populating picks for week %d..." % (weeknum,)
        populate_picks_for_year_week(yearnum, weeknum, poolspreadsheet)

def populate_picks(yearlist):
    for yearnum in yearlist:
        try:
            numpicks = len(Pick.objects.filter(pick_game__game_year=yearnum))
            if numpicks > 10:
                print "    Picks for year %d already populated, skipping..." % (yearnum,)
                return
        except:
            pass

        print "    Populating picks for year %s..." % (yearnum,)
        populate_picks_for_year(yearnum)

def main():
    print "Starting pick10 model population..."
    print "  Populating Users..."
    populate_users()
    print "  Populating Conferences and Teams..."
    populate_conferences_teams()
    print "  Populating Games..."
    populate_games(range(1997, 2015))
    print "  Populating Picks..."
    populate_picks([2013, 2014])

# Execution starts here
if __name__ == '__main__':
    main()

