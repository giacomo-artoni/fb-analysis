#coding: utf8 

class gen_team:

  def __init__ ( self, Id, Name ):
    self.Id = Id
    self.Name = Name

  def __str__ ( self ):
    return 'Team: %s (%d)' % ( self.Name, self.Id )
