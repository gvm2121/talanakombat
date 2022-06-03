import json

j1 = {"player1":{"movimientos":["SDD", "DSD", "SA", "DSD"] ,"golpes":["K", "P", "K", "P"]},"player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P", "k"]}} # gana tonyn
j2 = {"player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]},"player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}} # gana arnold
j3 = {"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}} #el test del informe

a = json.dumps(j2)
b = json.loads(a)

p1 = len(b["player1"]["movimientos"] + b["player1"]["golpes"])
print(p1)
