#coding: utf8 

class team:

  def __init__ ( self, info ):
    self.Id = info[ 'teamId' ]
    self.Field = info[ 'field' ]
    self.Coach = info[ 'managerName' ]
    self.Name = info[ 'name' ]
    self.Age = info[ 'averageAge' ]
    self.Goals = info[ 'scores' ][ 'fulltime' ] 
    self.YellowCards = 0 
    self.RedCards = 0
    self.Subs = 0 
    for el in info[ 'incidentEvents' ]:
      if 'cardType' in el:
        if 'Yellow' in el[ 'cardType' ][ 'displayName' ]:
          self.YellowCards += 1
        elif 'Red' in el[ 'cardType' ][ 'displayName' ]:
          self.RedCards += 1
      if 'SubstitutionOff' in el[ 'type' ][ 'displayName' ]:
        self.Subs += 1

  def __str__ ( self ):
    return 'Team: %s (%d) -- Coach: %s -- Average Age: %.2f -- Goals: %d -- Cards: %d(%d) -- Subs: %d' % ( self.Name, self.Id, self.Coach, self.Age, self.Goals, self.YellowCards, self.RedCards, self.Subs )
