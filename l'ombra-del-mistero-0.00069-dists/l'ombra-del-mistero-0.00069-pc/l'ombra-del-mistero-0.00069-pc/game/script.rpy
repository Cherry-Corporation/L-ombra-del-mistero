#  Lo script di gioco va in questo file.

#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define Bkiller = Character("Killer (alle confessioni)", color="#ff0000")
define Akiller = Character("Mr Killer", color="#00ff00")
define pt = Character("Pensiero", color="#362c2cff")

define Titolare = Character("Titolare", color="#cf4040")
define Bagnina = Character("Bagnina", color="#ff17cd")
define Compratore = Character("Compratore", color="#8de02e")
define Capo = Character("Capo", color="#9fbd1c")

# NVL charactersfor the phone logic
define Io_nvl = Character("Noi", kind=nvl, image="Io", callback=Phone_SendSound)
define Capo_nvl = Character("Capo", kind=nvl, image="Capo", callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)
###################################################################

#############################################
#nvl ex
#    e_nvl "Ciao, posso chiamarti?"
#    n_nvl "Certo! Chiama pure adesso!"
#############################################

#screens

######################################################


# Il gioco comincia qui.
label start:
    #Spotmannus
#    $ renpy.movie_cutscene("images/Video/cutscene_iniziale.webm")
######################################################################################
label one:
    $ renpy.movie_cutscene("images/Video/cutscene_iniziale.webm")
    jump two
label two:
    #mostra il form qui
    "Fuori fa caldo, molto caldo. Le giornate di luglio in città sembrano non finire mai. Hai appena visto
questo spot in rete e, compilando il form, puoi passare una giornata gratis nella piscina del Mannus."
    menu:
        "Compili il form?"

        "Sì":
            jump three
        "No":
            jump thirteen
label three:
    #pass
    show 03_obj_01
    "Complimenti! Ecco il tuo pass per una splendida giornata in piscina al Mannus Club"
    jump four
label four:
    show 04_inq_01
    "Finalmente sei al Mannus, vedi la piscina, alcuni bambini che giocano sul prato, persone che si fanno il
bagno e altri al bar con un aperitivo"
    jump five
label five:
    show 05_inq_01
    "Ti avvicini al bar per ordinare qualcosa da bere, il tuo vicino sta parlando con il proprietario, sembra
voglia proporre la compravendita del club."
    jump six
label six:
    show 06_inq_01
    "Il barista ti porge una bibita, non fai in tempo a bere che si materializza una splendida ragazza, Celesta.
Saluta il titolare con un occhiolino."
    Titolare "Cinque minuti e inizio la lezione di Zumba."
    jump seven
label seven:
    "Stai seguendo con lo sguardo i bagnanti che si preparano alla lezione di zumba, quando dalla cucina
stanno alzando la voce."
    menu:
        "Vuoi ascoltare?"
        "Sì":
            jump eight_A
        "No":
            jump ten
label eight_A:
    show 08A_inq_01
    "Il litigio è fra il cuoco e il titolare, senza farti scorgere riesci a sentire"
    jump nine
label eight_B:
    "Guarda, mi sono licenziato, basta. Oggi mi hanno pure accusato di aver incendiato il fienile! Meglio che
vada."
    "Fai un sorriso di circostanza e saluti l'uomo."
    jump seventeen
label nine:
    show 09_inq_01
    "Il titolare si avvicina"
    Titolare "Mi spiace che tu abbia dovuto assistere alla scena, ma quel ragazzo.... E in merito
all'incendio al fienile so chi posso ringraziare.... Vabbé. Posso offrire la consumazione?"
    jump seventeen
label ten:
    show 10_inq_01
    "A fianco della zona piscina vedi una scuderia, Ti avvicini per accarezzare un cavallo.
Nel frattempo vedi arrivare un uomo molto arrabbiato."
    menu:
        "Chiedi cos'è successo?"
        "Sì":
            jump eleven
        "No":
            jump twelve
    jump eleven
label eleven:
    jump eight_B
label twelve:
    jump HARD_DEATH
label thirteen:
    show 13_inq_01
    "Accendi la televisione in cerca di un film, ma non trovi nulla. Prendi un libro, inizi a sfogliarlo, ma non ti
affascina quando... squilla il telefono."
    "Rispondi?"
    menu:
        "Sì":
            jump fifteen
        "No":
            jump fourteen
label fourteen:
    jump HARD_DEATH
label fifteen:
    #$ renpy.movie_cutscene("images/Videos/15_01.avi")
    "AUDIO AMICA"
    show 16_inq_01
    menu:
        "la aiuti?"
        "si":
            jump four
        "no":
            jump sixteen
label sixteen:
    jump HARD_DEATH
label seventeen:
    show 17_inq_01
    "In serata ti rechi nella pizzeria del paese. Mentre sorseggi la tua birra vedi nel tavolo a fianco il titolare
del Mannus, riconosci anche il compratore. Al tavolo sono seduti anche un uomo e una donna"
    jump eightteen
label eightteen:
    #$ renpy.movie_cutscene("images/Video/18_01.avi")
    "cutscene 18"
    jump nineteen
label nineteen:
    #$ renpy.movie_cutscene("images/Video/19_01.avi")
    "cutscene 19_01"
    "Stai scorrendo le news su internet, leggi dell'omicidio al Mannus, e a seguire un annuncio di lavoro per
una agenzia investigativa."
    menu:
        "Vuoi inviare un curriculum?"
        "invio il curriculum":
            jump twentyone
        "nah, oggi sono in vacanza":
            jump twenty
label twenty:
    jump HARD_DEATH
label twentyone:
    show 21_inq_01
    "Non sono passate neanche 24 ore, ricevi una telefonata in piena notte: alle 8 ti devi presentare in ufficio
per il tuo nuovo lavoro."
    "Il capo ti mostra la foto della vittima"
    show vittima
    Capo "Devi recarti al Mannus a cercare indizi"
    jump twentytwo
label twentytwo:
    show 22_inq_01
    jump preoffice
label preoffice:
    show 23_inq_01 #ufficio porta
    "Arrivato al Mannus, trovi tutto chiuso, superi i sigilli messi dalla polizia e senti dei rumori in ufficio."
    menu:
        "Cosa fai?"
        "entro in ufficio":
            jump officeluisa
        "non entro":
            jump twentythree
label twentythree:
    "Ti allontani furtivamente cercando di non farti notare."
    "Ti senti chiamare, è un poliziotto."
    "Vieni arrestato"
    jump HARD_DEATH
#24 is HD
label twentyfive:
    "Apri la porta e vedi una figura di schiena che sta cercando qualcosa in un armadietto. Si gira
all'improvviso:"
    unk "Ahhh! Chi sei tu? Cosa ci fai qui?"
    menu:
        "La interroghi?"
        "Sì":
            jump thirtythree
        "No, scappi":
            jump twentysix
label twentysix:
    "Ti giri e corri più forte che puoi. Un poliziotto sembra vederti ma non riesce a raggiungerti. Riesci a
scavalcare il muro di cinta e torni a casa."
    jump twentyseven
label twentyseven:
    "Sei a casa, ti squilla il telefono"
    Capo "Com'è andato il sopralluogo?"
    Io "Ehm... Abbastanza, nel senso che..."
    Capo "Hai interrogato qualcuno?"
    menu:
        "Oh cavolo, cosa gli dico?"
        "Sono scappato":
            jump twentyeight
        "Racconto della donna che non ho interrogato":
            jump thirty
label twentyeight:
    Io "Non ho interrogato nessuno, ho visto una persona e sono scappato."
    Capo "Inammissibile! SEI LICENZIATO!!!"
    jump FIRED
#29 fired
label thirty:
    Io "Veramente qualcuno ho visto..."
    Capo "?"
    Io "Insomma c'era una donna in ufficio che trafficava cercando qualcosa...
mi ha visto e io l'ho vista in faccia."
    jump thirtyone
label thirtyone:
    "Il tuo capo ti invia una fotografia:"
    Capo "Se la donna è questa, è la segretaria di Sir XX."
    Capo "Ti mando il suo numero di cellulare."
    #ToDo: nvl cell
    Capo "+39 347 962 2421"
    menu:
        "La chiami?"
        "Sì":
            jump thirtythree
        "No":
            "Decidi di non contattarla. Il tuo capo si inalbera"
            Capo "Prima scappi e poi hai paura di interrogare i sospettati... Sei licenziato!"
            jump FIRED
label thirtythree:
    jump officeluisa
label officeluisa: #33
    "Terzo capitolo"
    return
#
#
#
####################################################################
#Death section
####################################################################
label HARD_DEATH:
    "Hard death"
    return
label FIRED:
    "SEI LICENZIATO!!!!"
    return
######################################################################################
    # Gioco go kaboom @ return instr.
    return

