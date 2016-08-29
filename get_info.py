#coding: utf8 
import optparse, sys, ROOT
import classes.utils as utils
from classes.shot import shot
from classes.match import match

def main():
  #==#==#==#==#
  parser = optparse.OptionParser()
  parser.add_option( '-i', '--input', dest = 'input_file', action = 'store', type = 'string', default = '', help = '' )
  ( options, args ) = parser.parse_args()
  #==#==#==#==#
  the_dict, matchId, matchInfo = utils.get_info( options.input_file )
  if not the_dict or not matchId or not matchInfo:
    return 
  #==#==#==#==#
  out_file = ROOT.TFile( 'flat_ntuples/shots_%s.root' % matchId, 'recreate' )
  out_tree = ROOT.TTree( 'shot_info', '' )
  players = {}
  teams = {}
  shot_file = open( 'text_based_info/shots_%s.list' % matchId, 'w' )
  last_shot = None
  the_match = match( matchId, matchInfo, the_dict )
  utils.add_teams( teams, the_match )
  for key in the_dict[ 'playerIdNameDictionary' ]:
    players[ int( key ) ] = the_dict[ 'playerIdNameDictionary' ][ key ]    
  
  events = the_dict[ 'events' ]
  for index, event in enumerate( events ):
    if 'isShot' in event:
      last_shot = shot( the_match, event, players, teams )
      shot_file.write( last_shot.get_content() )

  shot_file.close()
  out_tree.ReadFile( shot_file.name, last_shot.get_header() ) 
  out_file.Write()
  out_file.Close()

if __name__ == '__main__':
  sys.exit( main() )
