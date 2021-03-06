
# astropy/coordinates/angle_parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = "'\xecW6\xc1\x00\x86\x9f\x84\x0er\xa4\xfb\x91\xa6;"
    
_lr_action_items = {u'HOUR':([2,8,10,17,18,21,25,26,27,28,34,],[-15,12,-14,20,-16,-12,-13,-9,-8,-10,-11,]),u'DEGREE':([2,8,10,17,18,21,25,26,27,28,34,],[-15,13,-14,19,-16,-12,-13,-9,-8,-10,-11,]),u'SIGN':([0,],[5,]),u'SECOND':([2,8,10,17,18,21,25,26,27,28,32,33,34,],[-15,14,-14,-17,-16,-12,-13,-9,-8,-10,35,36,-11,]),u'COLON':([17,28,],[22,31,]),u'UINT':([0,5,11,17,19,20,21,22,29,30,31,],[-7,-6,17,21,23,24,26,28,26,26,26,]),u'SIMPLE_UNIT':([2,8,10,17,18,21,25,26,27,28,34,],[-15,15,-14,-17,-16,-12,-13,-9,-8,-10,-11,]),u'UFLOAT':([0,5,11,21,29,30,31,],[-7,-6,18,27,27,27,27,]),u'MINUTE':([2,8,10,17,18,21,23,24,25,26,27,28,34,],[-15,16,-14,-17,-16,-12,29,30,-13,-9,-8,-10,-11,]),'$end':([1,2,3,4,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,32,33,34,35,36,],[-4,-15,0,-5,-3,-1,-30,-2,-14,-23,-29,-32,-31,-33,-17,-16,-24,-18,-12,-25,-19,-13,-9,-8,-10,-26,-20,-27,-21,-11,-28,-22,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {u'arcminute':([0,],[1,]),u'angle':([0,],[3,]),u'simple':([0,],[4,]),u'arcsecond':([0,],[6,]),u'hms':([0,],[7,]),u'generic':([0,],[8,]),u'dms':([0,],[9,]),u'colon':([0,],[10,]),u'spaced':([0,],[2,]),u'sign':([0,],[11,]),u'ufloat':([21,29,30,31,],[25,32,33,34,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> angle","S'",1,None,None,None),
  (u'angle -> hms',u'angle',1,'p_angle','astropy/coordinates/angle_utilities.py',115),
  (u'angle -> dms',u'angle',1,'p_angle','astropy/coordinates/angle_utilities.py',116),
  (u'angle -> arcsecond',u'angle',1,'p_angle','astropy/coordinates/angle_utilities.py',117),
  (u'angle -> arcminute',u'angle',1,'p_angle','astropy/coordinates/angle_utilities.py',118),
  (u'angle -> simple',u'angle',1,'p_angle','astropy/coordinates/angle_utilities.py',119),
  (u'sign -> SIGN',u'sign',1,'p_sign','astropy/coordinates/angle_utilities.py',125),
  (u'sign -> <empty>',u'sign',0,'p_sign','astropy/coordinates/angle_utilities.py',126),
  (u'ufloat -> UFLOAT',u'ufloat',1,'p_ufloat','astropy/coordinates/angle_utilities.py',135),
  (u'ufloat -> UINT',u'ufloat',1,'p_ufloat','astropy/coordinates/angle_utilities.py',136),
  (u'colon -> sign UINT COLON UINT',u'colon',4,'p_colon','astropy/coordinates/angle_utilities.py',142),
  (u'colon -> sign UINT COLON UINT COLON ufloat',u'colon',6,'p_colon','astropy/coordinates/angle_utilities.py',143),
  (u'spaced -> sign UINT UINT',u'spaced',3,'p_spaced','astropy/coordinates/angle_utilities.py',152),
  (u'spaced -> sign UINT UINT ufloat',u'spaced',4,'p_spaced','astropy/coordinates/angle_utilities.py',153),
  (u'generic -> colon',u'generic',1,'p_generic','astropy/coordinates/angle_utilities.py',162),
  (u'generic -> spaced',u'generic',1,'p_generic','astropy/coordinates/angle_utilities.py',163),
  (u'generic -> sign UFLOAT',u'generic',2,'p_generic','astropy/coordinates/angle_utilities.py',164),
  (u'generic -> sign UINT',u'generic',2,'p_generic','astropy/coordinates/angle_utilities.py',165),
  (u'hms -> sign UINT HOUR',u'hms',3,'p_hms','astropy/coordinates/angle_utilities.py',174),
  (u'hms -> sign UINT HOUR UINT',u'hms',4,'p_hms','astropy/coordinates/angle_utilities.py',175),
  (u'hms -> sign UINT HOUR UINT MINUTE',u'hms',5,'p_hms','astropy/coordinates/angle_utilities.py',176),
  (u'hms -> sign UINT HOUR UINT MINUTE ufloat',u'hms',6,'p_hms','astropy/coordinates/angle_utilities.py',177),
  (u'hms -> sign UINT HOUR UINT MINUTE ufloat SECOND',u'hms',7,'p_hms','astropy/coordinates/angle_utilities.py',178),
  (u'hms -> generic HOUR',u'hms',2,'p_hms','astropy/coordinates/angle_utilities.py',179),
  (u'dms -> sign UINT DEGREE',u'dms',3,'p_dms','astropy/coordinates/angle_utilities.py',192),
  (u'dms -> sign UINT DEGREE UINT',u'dms',4,'p_dms','astropy/coordinates/angle_utilities.py',193),
  (u'dms -> sign UINT DEGREE UINT MINUTE',u'dms',5,'p_dms','astropy/coordinates/angle_utilities.py',194),
  (u'dms -> sign UINT DEGREE UINT MINUTE ufloat',u'dms',6,'p_dms','astropy/coordinates/angle_utilities.py',195),
  (u'dms -> sign UINT DEGREE UINT MINUTE ufloat SECOND',u'dms',7,'p_dms','astropy/coordinates/angle_utilities.py',196),
  (u'dms -> generic DEGREE',u'dms',2,'p_dms','astropy/coordinates/angle_utilities.py',197),
  (u'simple -> generic',u'simple',1,'p_simple','astropy/coordinates/angle_utilities.py',210),
  (u'simple -> generic SIMPLE_UNIT',u'simple',2,'p_simple','astropy/coordinates/angle_utilities.py',211),
  (u'arcsecond -> generic SECOND',u'arcsecond',2,'p_arcsecond','astropy/coordinates/angle_utilities.py',220),
  (u'arcminute -> generic MINUTE',u'arcminute',2,'p_arcminute','astropy/coordinates/angle_utilities.py',226),
]
