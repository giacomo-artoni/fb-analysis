#coding: utf8 

import json, re
import gen_team

def get_info( input_file ):
  reg = re.compile( '.*page_(\d+)' )
  #check = reg.mtiamotantoatch( input_file )
  check = reg.match( input_file )
  if check:
    for line in open( input_file ).readlines():
      if 'var matchCentreData' in line:
        line = line.replace( 'var matchCentreData = ', '' )
        line = line.replace( ';', '' )
        return ( json.loads( unicode( line, 'utf' ) ), check.group( 1 ) )
  return ( None, None )

def add_teams( team_dict, match_info ):
  if not match_info.HomeTeam.Id in team_dict:
    team_dict[ match_info.HomeTeam.Id ] = gen_team.gen_team( match_info.HomeTeam.Id, match_info.HomeTeam.Name )
  if not match_info.AwayTeam.Id in team_dict:
    team_dict[ match_info.AwayTeam.Id ] = gen_team.gen_team( match_info.AwayTeam.Id, match_info.AwayTeam.Name )

