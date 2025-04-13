
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTOR ACTOR_LIST AS BY COLON COMMA EXT FROM IDENTIFIER IN INC INH INHERITS LBRACE OF PACKAGE RBRACE RELATIONSHIPS SYSTEM USECASE USECASE_LISTdiagram : actor_decls system_declactor_decls : actor_decls actor_decl\n                  | actor_declactor_decl : ACTOR IDENTIFIER\n                 | ACTOR IDENTIFIER AS IDENTIFIER\n                 | ACTOR IDENTIFIER INHERITS IDENTIFIER\n                 | ACTOR IDENTIFIER AS IDENTIFIER INHERITS IDENTIFIER\n                 | ACTOR_LIST COLON actor_itemsactor_items : actor_items COMMA actor_item\n                  | actor_itemactor_item : IDENTIFIER\n                 | IDENTIFIER AS IDENTIFIER\n                 | IDENTIFIER INHERITS IDENTIFIER\n                 | IDENTIFIER AS IDENTIFIER INHERITS IDENTIFIERsystem_decl : SYSTEM IDENTIFIER LBRACE system_content RBRACE\n                  | emptysystem_content : usecase_decls package_decls relationship_declusecase_decls : usecase_decls usecase_decl\n                    | usecase_decl\n                    | USECASE_LIST COLON usecase_itemsusecase_items : usecase_items COMMA usecase_item\n                    | usecase_itemusecase_item : IDENTIFIER\n                   | IDENTIFIER AS IDENTIFIER\n                   | IDENTIFIER BY IDENTIFIER\n                   | IDENTIFIER AS IDENTIFIER BY IDENTIFIERusecase_decl : USECASE IDENTIFIER\n                   | USECASE IDENTIFIER AS IDENTIFIER\n                   | USECASE IDENTIFIER BY IDENTIFIER\n                   | USECASE IDENTIFIER AS IDENTIFIER BY IDENTIFIERpackage_decls : package_decls package_decl\n                    | package_declpackage_decl : PACKAGE IDENTIFIER LBRACE usecase_refs RBRACEusecase_refs : usecase_refs usecase_ref\n                   | usecase_refusecase_ref : IDENTIFIERrelationship_decl : RELATIONSHIPS LBRACE relationship_list RBRACE\n                        | emptyrelationship_list : relationship_list relationship\n                        | relationshiprelationship : EXT IDENTIFIER OF IDENTIFIER\n                   | INC IDENTIFIER IN IDENTIFIER\n                   | INH IDENTIFIER FROM IDENTIFIERempty :'
    
_lr_action_items = {'ACTOR':([0,2,3,7,10,15,16,17,19,20,30,31,32,40,52,],[4,4,-3,-2,-4,-8,-10,-11,-5,-6,-9,-12,-13,-7,-14,]),'ACTOR_LIST':([0,2,3,7,10,15,16,17,19,20,30,31,32,40,52,],[5,5,-3,-2,-4,-8,-10,-11,-5,-6,-9,-12,-13,-7,-14,]),'$end':([1,2,3,6,7,9,10,15,16,17,19,20,30,31,32,33,40,52,],[0,-44,-3,-1,-2,-16,-4,-8,-10,-11,-5,-6,-9,-12,-13,-15,-7,-14,]),'SYSTEM':([2,3,7,10,15,16,17,19,20,30,31,32,40,52,],[8,-3,-2,-4,-8,-10,-11,-5,-6,-9,-12,-13,-7,-14,]),'IDENTIFIER':([4,8,11,13,14,21,22,23,28,29,37,38,41,50,51,54,55,56,57,62,63,64,65,66,67,71,78,79,81,82,83,],[10,12,17,19,20,17,31,32,39,40,46,49,52,58,59,65,49,69,70,74,75,76,-36,65,-35,80,-34,84,85,86,87,]),'COLON':([5,27,],[11,38,]),'AS':([10,17,39,49,],[13,22,50,56,]),'INHERITS':([10,17,19,31,],[14,23,29,41,]),'LBRACE':([12,44,46,],[18,53,54,]),'COMMA':([15,16,17,30,31,32,47,48,49,52,68,69,70,84,],[21,-10,-11,-9,-12,-13,55,-22,-23,-14,-21,-24,-25,-26,]),'USECASE_LIST':([18,],[27,]),'USECASE':([18,25,26,35,39,47,48,49,58,59,68,69,70,80,84,],[28,28,-19,-18,-27,-20,-22,-23,-28,-29,-21,-24,-25,-30,-26,]),'RBRACE':([24,34,36,42,43,45,60,61,65,66,67,72,73,77,78,85,86,87,],[33,-44,-32,-17,-31,-38,72,-40,-36,77,-35,-37,-39,-33,-34,-41,-42,-43,]),'PACKAGE':([25,26,34,35,36,39,43,47,48,49,58,59,68,69,70,77,80,84,],[37,-19,37,-18,-32,-27,-31,-20,-22,-23,-28,-29,-21,-24,-25,-33,-30,-26,]),'RELATIONSHIPS':([34,36,43,77,],[44,-32,-31,-33,]),'BY':([39,49,58,69,],[51,57,71,79,]),'EXT':([53,60,61,73,85,86,87,],[62,62,-40,-39,-41,-42,-43,]),'INC':([53,60,61,73,85,86,87,],[63,63,-40,-39,-41,-42,-43,]),'INH':([53,60,61,73,85,86,87,],[64,64,-40,-39,-41,-42,-43,]),'OF':([74,],[81,]),'IN':([75,],[82,]),'FROM':([76,],[83,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'diagram':([0,],[1,]),'actor_decls':([0,],[2,]),'actor_decl':([0,2,],[3,7,]),'system_decl':([2,],[6,]),'empty':([2,34,],[9,45,]),'actor_items':([11,],[15,]),'actor_item':([11,21,],[16,30,]),'system_content':([18,],[24,]),'usecase_decls':([18,],[25,]),'usecase_decl':([18,25,],[26,35,]),'package_decls':([25,],[34,]),'package_decl':([25,34,],[36,43,]),'relationship_decl':([34,],[42,]),'usecase_items':([38,],[47,]),'usecase_item':([38,55,],[48,68,]),'relationship_list':([53,],[60,]),'relationship':([53,60,],[61,73,]),'usecase_refs':([54,],[66,]),'usecase_ref':([54,66,],[67,78,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> diagram","S'",1,None,None,None),
  ('diagram -> actor_decls system_decl','diagram',2,'p_diagram','parser.py',71),
  ('actor_decls -> actor_decls actor_decl','actor_decls',2,'p_actor_decls','parser.py',75),
  ('actor_decls -> actor_decl','actor_decls',1,'p_actor_decls','parser.py',76),
  ('actor_decl -> ACTOR IDENTIFIER','actor_decl',2,'p_actor_decl','parser.py',83),
  ('actor_decl -> ACTOR IDENTIFIER AS IDENTIFIER','actor_decl',4,'p_actor_decl','parser.py',84),
  ('actor_decl -> ACTOR IDENTIFIER INHERITS IDENTIFIER','actor_decl',4,'p_actor_decl','parser.py',85),
  ('actor_decl -> ACTOR IDENTIFIER AS IDENTIFIER INHERITS IDENTIFIER','actor_decl',6,'p_actor_decl','parser.py',86),
  ('actor_decl -> ACTOR_LIST COLON actor_items','actor_decl',3,'p_actor_decl','parser.py',87),
  ('actor_items -> actor_items COMMA actor_item','actor_items',3,'p_actor_items','parser.py',103),
  ('actor_items -> actor_item','actor_items',1,'p_actor_items','parser.py',104),
  ('actor_item -> IDENTIFIER','actor_item',1,'p_actor_item','parser.py',111),
  ('actor_item -> IDENTIFIER AS IDENTIFIER','actor_item',3,'p_actor_item','parser.py',112),
  ('actor_item -> IDENTIFIER INHERITS IDENTIFIER','actor_item',3,'p_actor_item','parser.py',113),
  ('actor_item -> IDENTIFIER AS IDENTIFIER INHERITS IDENTIFIER','actor_item',5,'p_actor_item','parser.py',114),
  ('system_decl -> SYSTEM IDENTIFIER LBRACE system_content RBRACE','system_decl',5,'p_system_decl','parser.py',126),
  ('system_decl -> empty','system_decl',1,'p_system_decl','parser.py',127),
  ('system_content -> usecase_decls package_decls relationship_decl','system_content',3,'p_system_content','parser.py',134),
  ('usecase_decls -> usecase_decls usecase_decl','usecase_decls',2,'p_usecase_decls','parser.py',142),
  ('usecase_decls -> usecase_decl','usecase_decls',1,'p_usecase_decls','parser.py',143),
  ('usecase_decls -> USECASE_LIST COLON usecase_items','usecase_decls',3,'p_usecase_decls','parser.py',144),
  ('usecase_items -> usecase_items COMMA usecase_item','usecase_items',3,'p_usecase_items','parser.py',153),
  ('usecase_items -> usecase_item','usecase_items',1,'p_usecase_items','parser.py',154),
  ('usecase_item -> IDENTIFIER','usecase_item',1,'p_usecase_item','parser.py',161),
  ('usecase_item -> IDENTIFIER AS IDENTIFIER','usecase_item',3,'p_usecase_item','parser.py',162),
  ('usecase_item -> IDENTIFIER BY IDENTIFIER','usecase_item',3,'p_usecase_item','parser.py',163),
  ('usecase_item -> IDENTIFIER AS IDENTIFIER BY IDENTIFIER','usecase_item',5,'p_usecase_item','parser.py',164),
  ('usecase_decl -> USECASE IDENTIFIER','usecase_decl',2,'p_usecase_decl','parser.py',176),
  ('usecase_decl -> USECASE IDENTIFIER AS IDENTIFIER','usecase_decl',4,'p_usecase_decl','parser.py',177),
  ('usecase_decl -> USECASE IDENTIFIER BY IDENTIFIER','usecase_decl',4,'p_usecase_decl','parser.py',178),
  ('usecase_decl -> USECASE IDENTIFIER AS IDENTIFIER BY IDENTIFIER','usecase_decl',6,'p_usecase_decl','parser.py',179),
  ('package_decls -> package_decls package_decl','package_decls',2,'p_package_decls','parser.py',192),
  ('package_decls -> package_decl','package_decls',1,'p_package_decls','parser.py',193),
  ('package_decl -> PACKAGE IDENTIFIER LBRACE usecase_refs RBRACE','package_decl',5,'p_package_decl','parser.py',201),
  ('usecase_refs -> usecase_refs usecase_ref','usecase_refs',2,'p_usecase_refs','parser.py',206),
  ('usecase_refs -> usecase_ref','usecase_refs',1,'p_usecase_refs','parser.py',207),
  ('usecase_ref -> IDENTIFIER','usecase_ref',1,'p_usecase_ref','parser.py',214),
  ('relationship_decl -> RELATIONSHIPS LBRACE relationship_list RBRACE','relationship_decl',4,'p_relationship_decl','parser.py',218),
  ('relationship_decl -> empty','relationship_decl',1,'p_relationship_decl','parser.py',219),
  ('relationship_list -> relationship_list relationship','relationship_list',2,'p_relationship_list','parser.py',223),
  ('relationship_list -> relationship','relationship_list',1,'p_relationship_list','parser.py',224),
  ('relationship -> EXT IDENTIFIER OF IDENTIFIER','relationship',4,'p_relationship','parser.py',231),
  ('relationship -> INC IDENTIFIER IN IDENTIFIER','relationship',4,'p_relationship','parser.py',232),
  ('relationship -> INH IDENTIFIER FROM IDENTIFIER','relationship',4,'p_relationship','parser.py',233),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',239),
]
