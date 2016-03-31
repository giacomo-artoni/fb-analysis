#coding: utf8 

class shot:

  def __init__ ( self, match_id, event, players, teams ):
    self.Id = event[ 'eventId' ]
    self.Minute = event[ 'minute' ]
    self.PlayerId = event[ 'playerId' ]
    self.Player = players[ self.PlayerId ]
    self.TeamId = event[ 'teamId' ]
    self.Team = teams[ self.TeamId ].Name
    self.MatchId = match_id
    self.X = event[ 'x' ]
    self.Y = event[ 'y' ]
    self.Outcome = event[ 'type' ][ 'displayName' ] 
    self.OutcomeId = event[ 'type' ][ 'displayName' ] 
    Outcomes = { 'Goal': 0, 'MissedShots': 1, 'SavedShot': 2, 'ShotOnPost': 3 }
    self.OutcomeId = Outcomes[ self.Outcome ]
    self.Type = None
    self.TypeId = None
    Types = { 'Head': 0, 'LeftFoot': 1, 'RightFoot': 2 }
    for qual in event[ 'qualifiers' ]:
      name = qual[ 'type' ][ 'displayName' ]
      if name in Types:
        self.Type = name
        self.TypeId = Types[ name ]

  def __str__ ( self ):
    return ' ------------------\n\n Id: %d \n Minute: %d \n Player: %s (%d)\n Team: %s (%d)\n X: %f \n Y: %f \n Outcome: %s \n Type: %s\n' % ( self.Id, self.Minute, self.Player, self.PlayerId, self.Team, self.TeamId, self.X, self.Y, self.Outcome, self.TypeName )

  def get_header ( self ):
    return 'shot_id:match_id:minute:player_id:team_id:outcome_id:type_id:x:y'

  def get_content ( self ):
    return '%d %d %d %d %d %d %d %.2f %.2f\n' % ( int( self.Id ), int( self.MatchId ), int( self.Minute ), int( self.PlayerId ), int( self.TeamId ), int( self.OutcomeId ), int( self.TypeId ), float( self.X ), float( self.Y ) )
