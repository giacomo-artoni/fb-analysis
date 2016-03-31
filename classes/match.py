#coding: utf8 
import team

class match:

  def __init__ ( self, the_id, info ):
    self.Id = the_id 
    self.LastMinute = info[ 'maxMinute' ]
    self.HomeTeam = team.team( info[ 'home' ] )
    self.AwayTeam = team.team( info[ 'away' ] )
    self.ScoreHalf = info[ 'htScore' ]
    self.Score = info[ 'score' ]
    self.Referee = info[ 'refereeName' ]
    self.Date = info[ 'startTime' ]

  def __str__ ( self ):
    return 'MatchId: %s -- %s vs %s -- %s (%s) -- Referee: %s -- Last Minute Played: %d' % ( self.Id, self.HomeTeam.Name, self.AwayTeam.Name, self.Score, self.ScoreHalf, self.Referee, self.LastMinute )
