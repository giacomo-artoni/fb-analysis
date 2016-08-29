#coding: utf8 

import json, re
import gen_team

SeasonsDict = { ( 108, 5 ):  { 2010: 2626, 2011: 3054, 2012: 3512, 2013: 3978, 2014: 5441, 2015: 5970 }, 
                ( 252, 2 ):  { 2010: 2458, 2011: 2935, 2012: 3389, 2013: 3853, 2014: 4311, 2015: 5826 },
                ( 206, 4 ):  { 2010: 2596, 2011: 3004, 2012: 3470, 2013: 3922, 2014: 5435, 2015: 5933 },
                ( 81, 3 ):   { 2010: 2520, 2011: 2949, 2012: 3424, 2013: 3863, 2014: 4336, 2015: 5870 },
                ( 74, 22 ):  { 2010: 2417, 2011: 2920, 2012: 3356, 2013: 3836, 2014: 4279, 2015: 5830 },
                ( 250, 12 ): { 2010: 2474, 2011: 2944, 2012: 3416, 2013: 3872, 2014: 4333, 2015: 5848 },
                ( 250, 30 ): { 2010: 2469, 2011: 2945, 2012: 3418, 2013: 3871, 2014: 4332, 2015: 5849 } }

def get_info( input_file ):
  reg = re.compile( '.*page_(\d+)' )
  seas_reg = re.compile( '.*"/Regions/(\d+)/Tournaments/(\d+)/Seasons/(\d+).*' )
  check = reg.match( input_file )
  moreMatchInfo = None 
  if check:
    # Identify Tournament and Season
    for line in open( input_file ).readlines():
      if 'separator' in line and 'Tournaments' in line and 'Region' in line and not 'popular-tournaments-list' in line:
        another_check = seas_reg.match( line )
        if another_check:
          res = ( int( another_check.group( 1 ) ), int( another_check.group( 2 ) ), int( another_check.group( 3 ) ) )
          if ( res[ 0 ], res[ 1 ] ) in SeasonsDict:
            SmallSeasonsDict = SeasonsDict[ ( res[ 0 ], res[ 1 ] ) ]   
            for Key in SmallSeasonsDict:
              if SmallSeasonsDict[ Key ] == res[ 2 ]:
                moreMatchInfo = ( res[ 0 ], res[ 1 ], Key )
    for line in open( input_file ).readlines():
      if 'var matchCentreData' in line:
        line = line.replace( 'var matchCentreData = ', '' )
        line = line.replace( ';', '' )
        return ( json.loads( unicode( line, 'utf' ) ), check.group( 1 ), moreMatchInfo )
  return ( None, None, moreMatchInfo )

def add_teams( team_dict, match_info ):
  if not match_info.HomeTeam.Id in team_dict:
    team_dict[ match_info.HomeTeam.Id ] = gen_team.gen_team( match_info.HomeTeam.Id, match_info.HomeTeam.Name )
  if not match_info.AwayTeam.Id in team_dict:
    team_dict[ match_info.AwayTeam.Id ] = gen_team.gen_team( match_info.AwayTeam.Id, match_info.AwayTeam.Name )

