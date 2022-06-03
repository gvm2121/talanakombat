import json

j1 = {"player1":{"movimientos":["SDD", "DSD", "SA", "DSD"] ,"golpes":["K", "P", "K", "P"]},"player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P", "k"]}} # gana tonyn
j2 = {"player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]},"player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}} # gana arnold
j3 = {"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}} #el test del informe


nombres = {
        "player1" : "Tonyn Stallone",
        "player2" : "Arnold Shuatseneguer"
        }
movimientos_simples_p1 = {
    "W" : "salta",
    "S" : "y se Agacha!",
    "A" : "Retrocede",
    "D" : "Avanza",
    "" : "No se mueve"

}
golpes = {
    "K" : "y patea",
    "P" : "y golpea",
    '' : " y un golpe al aireeee !"

}
movimientos_simples_p2 = {
    "W" : "salta",
    "S" : "y se Agacha!",
    "A" : "Avanza!",
    "D" : "Retrocede",
    '' : " no se mueve!"
  
}
movimientos_complejos_p1 ={
    "DSDP" : " conecta un Taladoken!",
    "SDK" : " aplica un Remuyuken!",
    
}
movimientos_complejos_p2 ={
    "SAK" : " conecta un Remuyuken!",
    "ASAP" : " aplica un Taladoken!",
    
}
ataques_p2 = {
    "ASAP" : 2,
    "SAK":3,
    "P" :1,
    "K":1,
    '' : 0
}
ataques_p1 = {
    "DSDP" : 3,
    "SDK":2,
    "P" :1,
    "K":1,
    '':0
}

a = json.dumps(j3)
b = json.loads(a)

p1 = b['player1']
p2 = b['player2']
i = 0
print(p1)
print(p2)
energia_p1 = 6
energia_p2 = 6

#aca vemos quien comienza:
#combinacio mejor de botones
comb1 = len(p1["movimientos"] + p1["golpes"])
comb2 = len(p2["movimientos"] + p2["golpes"])
if comb2 < comb1:
    p1,p2 = p2,p1
    movimientos_simples_p1,movimientos_simples_p2 = movimientos_simples_p2,movimientos_simples_p1
    movimientos_complejos_p1,movimientos_complejos_p2 = movimientos_complejos_p2,movimientos_complejos_p1
    ataques_p1,ataques_p2 = ataques_p2,ataques_p1

elif comb2 == comb1:
    if len(p2["movimientos"]) < len(p1["movimientos"]):
        p1,p2 = p2,p1
        movimientos_simples_p1,movimientos_simples_p2 = movimientos_simples_p2,movimientos_simples_p1
        movimientos_complejos_p1,movimientos_complejos_p2 = movimientos_complejos_p2,movimientos_complejos_p1
        ataques_p1,ataques_p2 = ataques_p2,ataques_p1
    elif len(p2["movimientos"]) == len(p1["movimientos"]):
        if p2["golpes"] < p1["golpes"]:
            p1,p2 = p2,p1
            movimientos_simples_p1,movimientos_simples_p2 = movimientos_simples_p2,movimientos_simples_p1
            movimientos_complejos_p1,movimientos_complejos_p2 = movimientos_complejos_p2,movimientos_complejos_p1
            ataques_p1,ataques_p2 = ataques_p2,ataques_p1
            

ciclos = max(len(p1['movimientos']),len(p2['movimientos']))

while i < ciclos:
    try:
        mov_1 = p1['movimientos'][i]
        gol_1 = p1['golpes'][i]
        texto_aux_1 = mov_1 + gol_1
        if len(texto_aux_1)>2:
            try:
                mov_comp = movimientos_complejos_p1[texto_aux_1]
                energia_p2 -= ataques_p1[texto_aux_1]
                if energia_p2<0:
                    break
            except KeyError:
                mov_comp = "Amaga una combinación!"
            
            texto_p1 = '{0} {1}'.format(nombres["player1"],mov_comp)
            
        elif len(texto_aux_1)==2 and gol_1 == '':
            texto_p1 = '{0} se mueve'.format(nombres["player1"])
            
        else:
            texto_p1 = '{0} {1} {2}'.format(nombres["player1"],movimientos_simples_p1[mov_1],golpes[gol_1])
            energia_p2 -= ataques_p1[gol_1]
            if energia_p2<0:
                    break

        print(texto_p1, texto_aux_1)
    except IndexError:
        pass

    try:
        mov_2 = p2['movimientos'][i]
        gol_2 = p2['golpes'][i]
        texto_aux_2 = mov_2 + gol_2
        if len(texto_aux_2)>2:
            try:
                mov_comp = movimientos_complejos_p2[texto_aux_2]
                energia_p1 -= ataques_p2[texto_aux_2]
                if energia_p1 < 0:
                    break
            except KeyError:
                mov_comp = "Amaga una combinación!"

            texto_p2 = '{0} {1}'.format(nombres["player2"],mov_comp)
        elif len(texto_aux_2)==2 and gol_2 == '' :
            texto_p2 = '{0} se mueve'.format(nombres["player2"])
            
        else:
            texto_p2 = '{0} {1} {2}'.format(nombres["player2"],movimientos_simples_p2[mov_2],golpes[gol_2])
            energia_p1 -= ataques_p2[gol_2]
            if energia_p1 < 0:
                    break
        print(texto_p2,texto_aux_2)
        i+=1
    except IndexError:
        pass


if energia_p1 > energia_p2:
    ganador,energia = nombres["player1"],energia_p1 
else:
    ganador,energia = nombres["player2"],energia_p2

print("Fin de la pelea")
print("El ganador es {0} y le quedaban todavía {1} de energia!".format(ganador,energia))


