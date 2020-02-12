from random import seed
from random import randint
# coding=utf-8

cardnames = {
0:'Vacío',
1:'Toba Ah.',
2:'Juanxa ~Pistolas~',
3:'Flavia ~No está, faltó~',
4:'Nico ~Ver. anime~',
5:'VTZ army',
6:'VTZ Mokin',
7:'Toba Ah ~Topoide~',
8:'Niko ~Máscar berde ahre~',
9:'Gonza ~Carta que va a ser censurada por ser racista ndeah~',
10:'English tichah',
11:'Juanxa religioso',
12:'Mokin biolador',
13:'Nico ~Angra Manyú~',
14:'Langostina, but menos fea',
15:'Toba Crux',
16:'Mokin Dios de las Pajas',
17:'Juanxa ~Nerox~',
18:'Alejo ~Ryonim~',
19:'Mokin ~DM~',
20:'Juada VTZ',
21:'TEAM PIJA',
22:'Juanxa Pija',
23:'Toba Pija',
24:'Mokin Pija',
25:'Nico Pija',
26:'Alejo Pija',
27:'Santi Jei',
28:'Casa de Nico',
29:'Comiste del Toba',
30:'Maca Despeinada',
31:'Toba Rusiano',
32:'Toba cagando',
33:'TOBA AH CAGADO',
34:'La pulsera gay del Mokin',
35:'Mikeas',
36:'La sube del Nico',
37:'Nico arañando',
38:'Juanxa haciendo algo',
39:'Navaja reveladora del gonza',
40:'Iglesia cristianista',
41:'Nico satanista',
42:'Aleho satanista',
43:'Juanxa satanista',
44:'Mokin satanista',
45:'La sofi',
46:'Fran Horozko',
47:'Khal Lannister Tiguesito Suricato Cascote',
48:'Pacha :v',
49:'Felisia and The black',
50:'Jumanji HOUDINI!'}

cardtext = {
0:'Vacío/ Nada',
1:'Toba Ah./Efecto / Es gay. | Sube 1 punto de homosexualidad al ser invocado.',
2:'Juanxa ~Pistolas~/ Dispara S.W.A.G.',
3:'Flavia ~No está, faltó~/Efecto | Como no está no recibe daño.',
4:'Nico ~Ver. anime~/ Alto virgo, pero tira flow en japonés y los menores c ofenden en chino.',
5:'VTZ army/Efecto / Si se combinan con un mokin, él hace -10 de daño y le pasan pack. | Reduce el ataque de un mokin en 10',
6:'VTZ Mokin/ Te tira hate en chino y como es sad se viste de negro ahre emo.',
7:'Toba Ah ~Topoide~/Efecto / Es re pete. Tiró un rayo y como estaban en una cueva casi se mueren todos. | Todos quedan con 1HP.',
8:'Niko ~Máscara berde ahre~/Efecto / Ndeah re turbio. | +10DEF porque si.',
9:'Gonza ~Carta que va a ser censurada por ser racista ndeah~/Efecto / Es invocado y automáticamente se van todos del miedo | Todas las cartas menos él se van al descarte.',
10:'English tichah/ In inglish plis.',
11:'Juanxa religioso/Efecto/ Activa el poder del comiste y te envía un waskaso con +10 de daño | Al ser invocado puede hacer un ataque extra con +10ATK',
12:'Mokin biolador/ Re govir',
13:'Nico ~Angra Manyú~/Efecto / Se tira dos kill con arco re picante el pibe | Elimina dos cartas al entrar en juego.',
14:'Langostina, but menos fea/Efecto / Es alta rancia, si se combina con un toba le roba la campera y el toba aumenta su homosexualidad | Sube un punto de homosexualidad a un Toba',
15:'Toba Crux ah/Efecto / En un equipo conformado por tobitos, todos le ofrendan su DEF y este sube +10 a sus estadísticas | Si todos los del campo local son Tobas, reducir su DEF a 0 para ganar +10ATK, +10DEF, +10HP para Toba Crux.',
16:'Mokin Dios de las Pajas/Efecto / Con el caudal de waska de los pajeros del mundo, aciega a quienes tiene cerca, y los pegotea con semen, evitando que lo ataquen otros personajes que no sean de religión | Sólo recibe ataques de personajes Religión',
17:'Juanxa ~Nerox~/Efecto / Como la tiene corta, se esconde y no muere, pero si se queda solo se va. | No puede ser destruido en combate',
18:'Alejo ~Ryonim~/Efecto / No es muy gay, pero si un toba lo ve se enamora y le sube la homosexualité al toba | Los Tobas activos al momento de ser invocada esta carta, suben 1 punto de homosexualidad',
19:'Mokin ~DM~ Si comparte equipo con otros personajes D&D, les sube +10ATK. Como el no juega está ausente. Si no tiene otros personajes D&D, se tira un pedo y se va | No puede ser destruido en combate, suma 10ATK a personajes D&D, es descartada si no hay otros D&D en el campo local.',
20:'Juada VTZ/Efecto / Si ataca un miqueas le hace +20 de daño xqsi. Si se combina con cualquier mokin, lo friendzonea al toke y lo saca de la partida | +20ATK al combatir contra Mikeas, puede eliminar un mokin',
21:'TEAM PIJA/Fusión / El SQUAD completo, Sólo invocación especial/ Juan Pija, Toba pija, Mokn Pija, Nico Pija, Ale Pija(Combinar 3 de estos para la invocación)',
22:'Juanxa Pija/ Para invocar al team pija, debe mantenerse al menos dos turnos',
23:'Toba pija/ Para invocar al team pija, debe mantenerse al menos dos turnos',
24:'Mokin Pija/ Para invocar al team pija, debe mantenerse al menos dos turnos',
25:'Nico Pija/ Para invocar al team pija, debe mantenerse al menos dos turnos',
26:'Alejo Pija/ Para invocar al team pija, debe mantenerse al menos dos turnos',
27:'Santi Jei/ No juega al piedra papel o tijera con Nico.',
28:'Casa de Nico/Consumible / Los del team pija se van a comer empanadas, así que quedan fuera del juego | Envía todos los Nico, Ale, Mokin, Toba y Juan al descarte',
29:'Comiste del Toba/Consumible / Elimina una carta del otro porque comió | Envía una carta del campo rival al descarte',
30:'Maca Despeinada/Efecto / Si ve un toba, le mete el dedo y lo domina | Toma el control de un Toba',
31:'Toba Ah ~Rusiano~/Efecto / Sólo es posible quitarlo del juego si lo atacan entre tres del team pija | Para eliminarlo debe ser atacado por 3 personajes Ale, Juan, Toba, Nico o Mokin al mismo tiempo',
32:'Toba cagando/Efecto / Como está cagando, no se encuentra en la batalla | No recibe daño de combate',
33:'TOBA AH CAGADO/Fusión / Ataca con su caquita uwu/ Toba cagando',
34:'La pulsera gay del Mokin/Consumible / Descarta a todos los tobas',
35:'Mikeas/Efecto / Las profes le hacen el doble de daño porque es re molesto eu | Recibe x2ATK de personajes Profe',
36:'La sube del Nico/Consumible / Nico se toma el palo y el micro atropella una carta del rival | Descarta un Nico de tu lado para descartar una carta del campo rival',
37:'Nico arañando/Efecto / Si Juan responde haciendo ese movimiento rancio, ambos juegan como una carta única con sus estadísticas sumadas | Puede mezclarse con [Juan haciendo algo], para poner ambos en un sólo espacio, atacar una sola vez, y sumar sus ATK y DEF.',
38:'Juanxa haciendo algo/ La sociedad secreta del Japish, Japish.',
39:'Navaja reveladora del gonza/Efecto / El gonzalo te amenaza y del cagaso que te agarra por su negrura le mostras las cartas en tu mano al rival | Al activar esta carta, tu rival te muestra sus cartas',
40:'Iglesia cristianista/Efecto /Efecto pasivo / Aumenta al toba crux en +10 e inhibe otros personajes religiosos | Las estadísticas de un Toba Crux en tu campo local son aumentadas en 10 | [Estructura] Es incapaz de realizar ataques',
41:'Nico satanista/Efecto Pasivo / [Nico satánico] Activa las habilidades de los personajes satanistas',
42:'Aleho satanista/Efecto Inactivo/ Como está a favor del Ndeahismo, no le hace daño a los personajes no religiosos, pero estos no lo atacan | No puede combatir con personajes no Religión',
43:'Juanxa satanista/Efecto Inactivo / Como no profesa el credo , los personajes de otras religionses no le hacen daño | Los personajes Religión que no tengan Satanista en su nombre, no pueden atacarlo',
44:'Mokin satanista/Efecto Inactivo / Como no practica el Tobaísmo, los Tobas no le hacen daño | No puede ser atacado por Tobas',
45:'La sofi/Efecto / Si se combina con un Mokin, los dos se homosexualizan por estar hablando de chinos | Aumenta en 1 la homosexualidad de un Mokin, y se aumenta en 1 su propia homosexualidad',
46:'Fran Horozko/Efecto / Al primero que golpea le hace el doble de daño',
47:'Khal Lannister Tiguesito Suricato Cascote/Efecto / Como todo gato sabe arañar, y como la tiene re grande te deja una cortadura que quita 1 de salud por turno | Una vez por turno, puede poner Cortadura sobre una carta del rival, esta pierde 1 HP por turno',
48:'Pacha :\'v/Consumible continua / Con sus poderes de angelito,| le da +10DEF a los gatitos <3',
49:'Felisia and The black/Efecto / Como son dos gatas, atacan dos veces',
50:'Jumanji HOUDINI!/Efecto / Gatiza un personaje no Gatuno, haciendo que los efectos para Gatitos apliquen sobre este'}

inplay = {
1:0,
2:0,
3:0}

card = {
1:0,
2:0,
3:0
}

sss = 10
cm1 = 'draw'
cm2 = 'exit'
print('Usa [draw] para levantar cartas!')
print('Usa [exit] para salir')
print('Usa [inplay] para ver las cartas en juego')
while (1):
    seed(sss)
    cmd = input('>')

    if cmd == cm2:
        exit()

    elif cmd == cm1:
        card[1] = randint(1,50)
        card[2] = randint(1,50)
        card[3] = randint(1,50)
        print (cardnames[card[1]], ', ', cardnames[card[2]],', ', cardnames[card[3]], '.')
        sss += card[3] + card[2] + card[1]
    elif cmd == 'inplay':
        print (cardnames[inplay[1]], ' | ', cardnames[inplay[2]], ' | ', cardnames[inplay[3]])
        sss += 1
    elif cmd == 'play':
        print ('Qué carta quieres jugar?(1, 2, 3)')
        buffer = int(input(' >'))
        print ('En qué zona la quieres jugar?(1, 2, 3)')
        buffera = int(input('  >'))
        inplay[buffera] = card[buffer]
        card[buffer] = 0
        sss += buffer + buffera
    elif cmd == 'hand':
        print (cardnames[card[1]], ' | ', cardnames[card[2]], ' | ', cardnames[card[3]])
        sss += 5
    elif cmd == 'text':
        print ('1:', cardnames[card[1]])
        print ('2:', cardnames[card[2]])
        print ('3:', cardnames[card[3]])
        print ('4:', cardnames[inplay[1]])
        print ('5:', cardnames[inplay[2]])
        print ('6:', cardnames[inplay[3]])
        print ('Qué carta quieres leer?')
        tosee = int(input(' >'))
        if tosee < 4:
            print (cardtext[card[tosee]])
        elif tosee > 3:
            tosee -= 3
            print (cardtext[inplay[tosee]])
        else:
            print ('Número inválido')
        sss += tosee
    elif cmd == 'clear':
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        print (' ')
        sss += randint(0,100)
    elif cmd == 'toba':
        print ('El toba es re puto dea')
        sss += 19843
    else:
        print ('Nope')
        sss += cmd
