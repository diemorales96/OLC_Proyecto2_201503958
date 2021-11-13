
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftEQUALSEQUALSDISTINTleftGREATEREQUALLESSEQUALGREATERLESSleftPLUSMINUSleftTIMESDIVrightNOTrightUMINUSAND BOOL BREAK COLON COMMA CONTINUE DISTINT DIV ELSE ELSEIF END EQUALS EQUALSEQUALS FALSE FLOATLITERAL FUNCTION GREATER GREATEREQUAL ID IF INT64 INTLITERAL LEPAR LESS LESSEQUAL MINUS NOT OR PLUS POINT POT PRINT PRINTLN RETURN RIPAR SEMICOLON STRING STRINGLITERAL STRUCT TIMES TRUE WHILEstart : instructionsinstructions : instructions instruction\n                    | instructioninstruction  : printST SEMICOLON\n                    | ifST SEMICOLON\n                    | declarationST SEMICOLON\n                    | whileST SEMICOLON\n                    | callFunc SEMICOLON\n                    | declareFunc SEMICOLON\n                    | returnST SEMICOLON\n                    | breakST SEMICOLON\n                    | continueST SEMICOLON\n                    | createStruct SEMICOLON\n                    | declareStructST SEMICOLON\n                    | assignAccessST SEMICOLONtypes : INT64\n            |  STRING\n            |  BOOLstatement : instructionsdeclareFunc :  FUNCTION ID LEPAR RIPAR COLON COLON types statement END\n                    | FUNCTION ID LEPAR decParams RIPAR COLON COLON types statement ENDdecParams :    decParams COMMA ID COLON COLON types\n                    | ID COLON COLON typesreturnST : RETURN\n                | RETURN expressiondeclarationST : ID EQUALS expressiondeclarationST : ID EQUALS expression COLON COLON typesprintST  : PRINTLN LEPAR expression RIPARprintST  : PRINT LEPAR expression RIPARifST : IF expression statement END\n            | IF expression statement ELSE statement END\n            | IF expression statement elseIfList ENDelseIfList   : ELSEIF expression statement\n                    | ELSEIF expression statement ELSE statement\n                    | ELSEIF expression statement elseIfListcreateStruct : STRUCT ID attList ENDattList :  attList SEMICOLON ID COLON COLON types SEMICOLON\n                | ID COLON COLON typesdeclareStructST : ID COLON COLON IDassignAccessST : ID POINT ID EQUALS expressionwhileST : WHILE expression statement ENDbreakST : BREAKcontinueST : CONTINUEcallFunc : ID LEPAR RIPAR\n                | ID LEPAR expList RIPARexpList :  expList COMMA expression\n                | expressionexpression   : MINUS expression %prec UMINUS\n                    | NOT expression %prec UMINUS\n                    \n                    | expression PLUS expression\n                    | expression MINUS expression\n                    | expression TIMES expression\n                    | expression DIV expression\n                    | expression POT expression\n\n                    | expression GREATER expression\n                    | expression LESS expression\n                    | expression GREATEREQUAL expression\n                    | expression LESSEQUAL expression\n                    | expression EQUALSEQUALS expression\n                    | expression DISTINT expression\n                    \n                    | expression OR expression\n                    | expression AND expression\n                    | finalExpfinalExp : LEPAR expression RIPAR\n                | INTLITERAL\n                | FLOATLITERAL\n                | STRINGLITERAL\n                | TRUE\n                | FALSE\n                | ID\n                | callFunc\n                | accessSTaccessST : ID POINT ID'
    
_lr_action_items = {'PRINTLN':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,85,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,141,142,143,150,153,159,],[16,16,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,16,-63,-65,-66,-67,-68,-69,-70,-71,-72,16,16,-48,-49,-44,16,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,16,-16,-17,-18,16,16,16,]),'PRINT':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,85,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,141,142,143,150,153,159,],[17,17,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,17,-63,-65,-66,-67,-68,-69,-70,-71,-72,17,17,-48,-49,-44,17,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,17,-16,-17,-18,17,17,17,]),'IF':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,85,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,141,142,143,150,153,159,],[18,18,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,18,-63,-65,-66,-67,-68,-69,-70,-71,-72,18,18,-48,-49,-44,18,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,18,-16,-17,-18,18,18,18,]),'ID':([0,2,3,18,20,21,22,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,56,57,58,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,84,85,90,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,117,118,125,128,135,141,142,143,150,153,159,],[19,19,-3,51,51,59,51,61,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,51,51,19,51,51,-63,51,-65,-66,-67,-68,-69,-70,-71,-72,51,51,88,19,91,51,51,51,51,51,51,51,51,51,51,51,51,51,19,-48,-49,113,115,-44,120,19,51,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,51,51,137,19,147,-16,-17,-18,19,19,19,]),'WHILE':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,85,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,141,142,143,150,153,159,],[20,20,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,20,-63,-65,-66,-67,-68,-69,-70,-71,-72,20,20,-48,-49,-44,20,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,20,-16,-17,-18,20,20,20,]),'FUNCTION':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,85,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,141,142,143,150,153,159,],[21,21,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,21,-63,-65,-66,-67,-68,-69,-70,-71,-72,21,21,-48,-49,-44,21,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,21,-16,-17,-18,21,21,21,]),'RETURN':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,85,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,141,142,143,150,153,159,],[22,22,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,22,-63,-65,-66,-67,-68,-69,-70,-71,-72,22,22,-48,-49,-44,22,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,22,-16,-17,-18,22,22,22,]),'BREAK':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,85,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,141,142,143,150,153,159,],[23,23,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,23,-63,-65,-66,-67,-68,-69,-70,-71,-72,23,23,-48,-49,-44,23,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,23,-16,-17,-18,23,23,23,]),'CONTINUE':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,85,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,141,142,143,150,153,159,],[24,24,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,24,-63,-65,-66,-67,-68,-69,-70,-71,-72,24,24,-48,-49,-44,24,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,24,-16,-17,-18,24,24,24,]),'STRUCT':([0,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,41,44,46,47,48,49,50,51,52,53,58,78,79,80,85,96,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,141,142,143,150,153,159,],[25,25,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,25,-63,-65,-66,-67,-68,-69,-70,-71,-72,25,25,-48,-49,-44,25,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,25,-16,-17,-18,25,25,25,]),'$end':([1,2,3,26,27,28,29,30,31,32,33,34,35,36,37,38,],[0,-1,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,]),'END':([3,26,27,28,29,30,31,32,33,34,35,36,37,38,64,78,89,92,97,126,139,141,142,143,148,151,157,158,163,165,],[-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,95,-19,119,124,127,138,-33,-16,-17,-18,-38,-35,-34,162,166,-37,]),'ELSE':([3,26,27,28,29,30,31,32,33,34,35,36,37,38,64,78,139,],[-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,96,-19,150,]),'ELSEIF':([3,26,27,28,29,30,31,32,33,34,35,36,37,38,64,78,139,],[-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,98,-19,98,]),'SEMICOLON':([4,5,6,7,8,9,10,11,12,13,14,15,22,23,24,44,46,47,48,49,50,51,52,53,60,79,80,83,85,92,93,94,95,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,115,116,119,124,127,131,138,140,141,142,143,148,161,162,165,166,],[27,28,29,30,31,32,33,34,35,36,37,38,-24,-42,-43,-63,-65,-66,-67,-68,-69,-70,-71,-72,-25,-48,-49,-26,-44,125,-28,-29,-30,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-39,-45,-41,-36,-32,-40,-31,-27,-16,-17,-18,-38,165,-20,-37,-21,]),'LEPAR':([16,17,18,19,20,22,39,40,42,43,45,51,54,56,59,65,66,67,68,69,70,71,72,73,74,75,76,77,98,117,118,],[39,40,45,56,45,45,45,45,45,45,45,56,45,45,90,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'MINUS':([18,20,22,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,81,83,85,87,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,117,118,128,130,131,],[42,42,42,42,42,66,42,42,-63,42,-65,-66,-67,-68,-69,-70,-71,-72,42,42,66,66,66,66,42,42,42,42,42,42,42,42,42,42,42,42,42,-48,-49,66,66,-44,66,42,-50,-51,-52,-53,66,66,66,66,66,66,66,66,66,-64,-73,-45,42,42,66,66,66,]),'NOT':([18,20,22,39,40,42,43,45,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,98,117,118,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'INTLITERAL':([18,20,22,39,40,42,43,45,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,98,117,118,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'FLOATLITERAL':([18,20,22,39,40,42,43,45,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,98,117,118,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'STRINGLITERAL':([18,20,22,39,40,42,43,45,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,98,117,118,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'TRUE':([18,20,22,39,40,42,43,45,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,98,117,118,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'FALSE':([18,20,22,39,40,42,43,45,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,98,117,118,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'EQUALS':([19,88,],[54,118,]),'COLON':([19,44,46,47,48,49,50,51,52,53,55,79,80,83,85,91,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,120,121,123,132,133,134,137,146,147,149,155,],[55,-63,-65,-66,-67,-68,-69,-70,-71,-72,84,-48,-49,114,-44,123,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,129,-45,132,133,136,144,145,146,149,154,155,156,160,]),'POINT':([19,51,],[57,82,]),'PLUS':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,85,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,130,131,],[65,-63,-65,-66,-67,-68,-69,-70,-71,-72,65,65,65,65,-48,-49,65,65,-44,65,-50,-51,-52,-53,65,65,65,65,65,65,65,65,65,-64,-73,-45,65,65,65,]),'TIMES':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,85,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,130,131,],[67,-63,-65,-66,-67,-68,-69,-70,-71,-72,67,67,67,67,-48,-49,67,67,-44,67,67,67,-52,-53,67,67,67,67,67,67,67,67,67,-64,-73,-45,67,67,67,]),'DIV':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,85,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,130,131,],[68,-63,-65,-66,-67,-68,-69,-70,-71,-72,68,68,68,68,-48,-49,68,68,-44,68,68,68,-52,-53,68,68,68,68,68,68,68,68,68,-64,-73,-45,68,68,68,]),'POT':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,85,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,130,131,],[69,-63,-65,-66,-67,-68,-69,-70,-71,-72,69,69,69,69,-48,-49,69,69,-44,69,-50,-51,-52,-53,69,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,69,69,69,]),'GREATER':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,85,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,130,131,],[70,-63,-65,-66,-67,-68,-69,-70,-71,-72,70,70,70,70,-48,-49,70,70,-44,70,-50,-51,-52,-53,70,-55,-56,-57,-58,70,70,70,70,-64,-73,-45,70,70,70,]),'LESS':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,85,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,130,131,],[71,-63,-65,-66,-67,-68,-69,-70,-71,-72,71,71,71,71,-48,-49,71,71,-44,71,-50,-51,-52,-53,71,-55,-56,-57,-58,71,71,71,71,-64,-73,-45,71,71,71,]),'GREATEREQUAL':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,85,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,130,131,],[72,-63,-65,-66,-67,-68,-69,-70,-71,-72,72,72,72,72,-48,-49,72,72,-44,72,-50,-51,-52,-53,72,-55,-56,-57,-58,72,72,72,72,-64,-73,-45,72,72,72,]),'LESSEQUAL':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,85,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,130,131,],[73,-63,-65,-66,-67,-68,-69,-70,-71,-72,73,73,73,73,-48,-49,73,73,-44,73,-50,-51,-52,-53,73,-55,-56,-57,-58,73,73,73,73,-64,-73,-45,73,73,73,]),'EQUALSEQUALS':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,85,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,130,131,],[74,-63,-65,-66,-67,-68,-69,-70,-71,-72,74,74,74,74,-48,-49,74,74,-44,74,-50,-51,-52,-53,74,-55,-56,-57,-58,-59,-60,74,74,-64,-73,-45,74,74,74,]),'DISTINT':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,85,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,130,131,],[75,-63,-65,-66,-67,-68,-69,-70,-71,-72,75,75,75,75,-48,-49,75,75,-44,75,-50,-51,-52,-53,75,-55,-56,-57,-58,-59,-60,75,75,-64,-73,-45,75,75,75,]),'OR':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,85,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,130,131,],[76,-63,-65,-66,-67,-68,-69,-70,-71,-72,76,76,76,76,-48,-49,76,76,-44,76,-50,-51,-52,-53,76,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,76,76,76,]),'AND':([41,44,46,47,48,49,50,51,52,53,58,60,62,63,79,80,81,83,85,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,128,130,131,],[77,-63,-65,-66,-67,-68,-69,-70,-71,-72,77,77,77,77,-48,-49,77,77,-44,77,-50,-51,-52,-53,77,-55,-56,-57,-58,-59,-60,77,-62,-64,-73,-45,77,77,77,]),'RIPAR':([44,46,47,48,49,50,51,52,53,56,62,63,79,80,81,85,86,87,90,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,122,130,141,142,143,152,164,],[-63,-65,-66,-67,-68,-69,-70,-71,-72,85,93,94,-48,-49,112,-44,116,-47,121,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,134,-46,-16,-17,-18,-23,-22,]),'COMMA':([44,46,47,48,49,50,51,52,53,79,80,85,86,87,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,116,122,130,141,142,143,152,164,],[-63,-65,-66,-67,-68,-69,-70,-71,-72,-48,-49,-44,117,-47,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-64,-73,-45,135,-46,-16,-17,-18,-23,-22,]),'INT64':([129,136,144,145,154,156,160,],[141,141,141,141,141,141,141,]),'STRING':([129,136,144,145,154,156,160,],[142,142,142,142,142,142,142,]),'BOOL':([129,136,144,145,154,156,160,],[143,143,143,143,143,143,143,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'instructions':([0,41,58,96,128,150,153,159,],[2,78,78,78,78,78,78,78,]),'instruction':([0,2,41,58,78,96,128,150,153,159,],[3,26,3,3,26,3,3,3,3,3,]),'printST':([0,2,41,58,78,96,128,150,153,159,],[4,4,4,4,4,4,4,4,4,4,]),'ifST':([0,2,41,58,78,96,128,150,153,159,],[5,5,5,5,5,5,5,5,5,5,]),'declarationST':([0,2,41,58,78,96,128,150,153,159,],[6,6,6,6,6,6,6,6,6,6,]),'whileST':([0,2,41,58,78,96,128,150,153,159,],[7,7,7,7,7,7,7,7,7,7,]),'callFunc':([0,2,18,20,22,39,40,41,42,43,45,54,56,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,96,98,117,118,128,150,153,159,],[8,8,52,52,52,52,52,8,52,52,52,52,52,8,52,52,52,52,52,52,52,52,52,52,52,52,52,8,8,52,52,52,8,8,8,8,]),'declareFunc':([0,2,41,58,78,96,128,150,153,159,],[9,9,9,9,9,9,9,9,9,9,]),'returnST':([0,2,41,58,78,96,128,150,153,159,],[10,10,10,10,10,10,10,10,10,10,]),'breakST':([0,2,41,58,78,96,128,150,153,159,],[11,11,11,11,11,11,11,11,11,11,]),'continueST':([0,2,41,58,78,96,128,150,153,159,],[12,12,12,12,12,12,12,12,12,12,]),'createStruct':([0,2,41,58,78,96,128,150,153,159,],[13,13,13,13,13,13,13,13,13,13,]),'declareStructST':([0,2,41,58,78,96,128,150,153,159,],[14,14,14,14,14,14,14,14,14,14,]),'assignAccessST':([0,2,41,58,78,96,128,150,153,159,],[15,15,15,15,15,15,15,15,15,15,]),'expression':([18,20,22,39,40,42,43,45,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,98,117,118,],[41,58,60,62,63,79,80,81,83,87,99,100,101,102,103,104,105,106,107,108,109,110,111,128,130,131,]),'finalExp':([18,20,22,39,40,42,43,45,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,98,117,118,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'accessST':([18,20,22,39,40,42,43,45,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,98,117,118,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'statement':([41,58,96,128,150,153,159,],[64,89,126,139,157,158,163,]),'expList':([56,],[86,]),'attList':([61,],[92,]),'elseIfList':([64,139,],[97,151,]),'decParams':([90,],[122,]),'types':([129,136,144,145,154,156,160,],[140,148,152,153,159,161,164,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> instructions','start',1,'p_start','grammar.py',195),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','grammar.py',200),
  ('instructions -> instruction','instructions',1,'p_instructions','grammar.py',201),
  ('instruction -> printST SEMICOLON','instruction',2,'p_instruction','grammar.py',209),
  ('instruction -> ifST SEMICOLON','instruction',2,'p_instruction','grammar.py',210),
  ('instruction -> declarationST SEMICOLON','instruction',2,'p_instruction','grammar.py',211),
  ('instruction -> whileST SEMICOLON','instruction',2,'p_instruction','grammar.py',212),
  ('instruction -> callFunc SEMICOLON','instruction',2,'p_instruction','grammar.py',213),
  ('instruction -> declareFunc SEMICOLON','instruction',2,'p_instruction','grammar.py',214),
  ('instruction -> returnST SEMICOLON','instruction',2,'p_instruction','grammar.py',215),
  ('instruction -> breakST SEMICOLON','instruction',2,'p_instruction','grammar.py',216),
  ('instruction -> continueST SEMICOLON','instruction',2,'p_instruction','grammar.py',217),
  ('instruction -> createStruct SEMICOLON','instruction',2,'p_instruction','grammar.py',218),
  ('instruction -> declareStructST SEMICOLON','instruction',2,'p_instruction','grammar.py',219),
  ('instruction -> assignAccessST SEMICOLON','instruction',2,'p_instruction','grammar.py',220),
  ('types -> INT64','types',1,'p_type','grammar.py',225),
  ('types -> STRING','types',1,'p_type','grammar.py',226),
  ('types -> BOOL','types',1,'p_type','grammar.py',227),
  ('statement -> instructions','statement',1,'p_statement','grammar.py',237),
  ('declareFunc -> FUNCTION ID LEPAR RIPAR COLON COLON types statement END','declareFunc',9,'p_function','grammar.py',242),
  ('declareFunc -> FUNCTION ID LEPAR decParams RIPAR COLON COLON types statement END','declareFunc',10,'p_function','grammar.py',243),
  ('decParams -> decParams COMMA ID COLON COLON types','decParams',6,'p_decParams','grammar.py',250),
  ('decParams -> ID COLON COLON types','decParams',4,'p_decParams','grammar.py',251),
  ('returnST -> RETURN','returnST',1,'p_return','grammar.py',260),
  ('returnST -> RETURN expression','returnST',2,'p_return','grammar.py',261),
  ('declarationST -> ID EQUALS expression','declarationST',3,'p_declaration','grammar.py',269),
  ('declarationST -> ID EQUALS expression COLON COLON types','declarationST',6,'p_declaration2','grammar.py',273),
  ('printST -> PRINTLN LEPAR expression RIPAR','printST',4,'p_printlnST','grammar.py',278),
  ('printST -> PRINT LEPAR expression RIPAR','printST',4,'p_printST','grammar.py',282),
  ('ifST -> IF expression statement END','ifST',4,'p_ifST','grammar.py',287),
  ('ifST -> IF expression statement ELSE statement END','ifST',6,'p_ifST','grammar.py',288),
  ('ifST -> IF expression statement elseIfList END','ifST',5,'p_ifST','grammar.py',289),
  ('elseIfList -> ELSEIF expression statement','elseIfList',3,'p_elseIfList','grammar.py',298),
  ('elseIfList -> ELSEIF expression statement ELSE statement','elseIfList',5,'p_elseIfList','grammar.py',299),
  ('elseIfList -> ELSEIF expression statement elseIfList','elseIfList',4,'p_elseIfList','grammar.py',300),
  ('createStruct -> STRUCT ID attList END','createStruct',4,'p_createStruct','grammar.py',311),
  ('attList -> attList SEMICOLON ID COLON COLON types SEMICOLON','attList',7,'p_attList','grammar.py',315),
  ('attList -> ID COLON COLON types','attList',4,'p_attList','grammar.py',316),
  ('declareStructST -> ID COLON COLON ID','declareStructST',4,'p_declareStruct','grammar.py',327),
  ('assignAccessST -> ID POINT ID EQUALS expression','assignAccessST',5,'p_assignAccess','grammar.py',332),
  ('whileST -> WHILE expression statement END','whileST',4,'p_while','grammar.py',337),
  ('breakST -> BREAK','breakST',1,'p_break','grammar.py',342),
  ('continueST -> CONTINUE','continueST',1,'p_continue','grammar.py',347),
  ('callFunc -> ID LEPAR RIPAR','callFunc',3,'p_callfunc','grammar.py',352),
  ('callFunc -> ID LEPAR expList RIPAR','callFunc',4,'p_callfunc','grammar.py',353),
  ('expList -> expList COMMA expression','expList',3,'p_callparams','grammar.py',361),
  ('expList -> expression','expList',1,'p_callparams','grammar.py',362),
  ('expression -> MINUS expression','expression',2,'p_expression','grammar.py',371),
  ('expression -> NOT expression','expression',2,'p_expression','grammar.py',372),
  ('expression -> expression PLUS expression','expression',3,'p_expression','grammar.py',374),
  ('expression -> expression MINUS expression','expression',3,'p_expression','grammar.py',375),
  ('expression -> expression TIMES expression','expression',3,'p_expression','grammar.py',376),
  ('expression -> expression DIV expression','expression',3,'p_expression','grammar.py',377),
  ('expression -> expression POT expression','expression',3,'p_expression','grammar.py',378),
  ('expression -> expression GREATER expression','expression',3,'p_expression','grammar.py',380),
  ('expression -> expression LESS expression','expression',3,'p_expression','grammar.py',381),
  ('expression -> expression GREATEREQUAL expression','expression',3,'p_expression','grammar.py',382),
  ('expression -> expression LESSEQUAL expression','expression',3,'p_expression','grammar.py',383),
  ('expression -> expression EQUALSEQUALS expression','expression',3,'p_expression','grammar.py',384),
  ('expression -> expression DISTINT expression','expression',3,'p_expression','grammar.py',385),
  ('expression -> expression OR expression','expression',3,'p_expression','grammar.py',387),
  ('expression -> expression AND expression','expression',3,'p_expression','grammar.py',388),
  ('expression -> finalExp','expression',1,'p_expression','grammar.py',389),
  ('finalExp -> LEPAR expression RIPAR','finalExp',3,'p_finalExp','grammar.py',424),
  ('finalExp -> INTLITERAL','finalExp',1,'p_finalExp','grammar.py',425),
  ('finalExp -> FLOATLITERAL','finalExp',1,'p_finalExp','grammar.py',426),
  ('finalExp -> STRINGLITERAL','finalExp',1,'p_finalExp','grammar.py',427),
  ('finalExp -> TRUE','finalExp',1,'p_finalExp','grammar.py',428),
  ('finalExp -> FALSE','finalExp',1,'p_finalExp','grammar.py',429),
  ('finalExp -> ID','finalExp',1,'p_finalExp','grammar.py',430),
  ('finalExp -> callFunc','finalExp',1,'p_finalExp','grammar.py',431),
  ('finalExp -> accessST','finalExp',1,'p_finalExp','grammar.py',432),
  ('accessST -> ID POINT ID','accessST',3,'p_accessST','grammar.py',454),
]
