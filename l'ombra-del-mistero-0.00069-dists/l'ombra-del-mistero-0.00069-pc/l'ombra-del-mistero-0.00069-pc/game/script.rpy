#  Lo script di gioco va in questo file.

#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define Bkiller = Character("Killer (alle confessioni)", color="#ff0000")
define Akiller = Character("Mr Killer", color="#00ff00")
define pt = Character("Pensiero", color="#362c2cff")

define Titolare = Character("Titolare", color="#cf4040")
define Bagnina = Character("Bagnina", color="#ff17cd")
define Compratore = Character("Compratore", color="#8de02e")

# NVL charactersfor the phone logic
define n_nvl = Character("Noi", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Amica", kind=nvl, callback=Phone_ReceiveSound)

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
    menu:
        "vado al mannus":
            jump three
        "non vado al mannus":
            jump thirteen
label three:
    #pass
    show 03_obj_01
    jump four
label four:
    show 04_inq_01
    jump five
label five:
    show 05_inq_01
    jump six
label six:
    show 06_inq_01
    jump seven
label seven:
    "sento dei rumori"
    menu:
        "ascolto":
            jump eight_A
        "mi faccio i fatti miei":
            jump ten
label eight_A:
    show 08A_inq_01
    jump nine
label eight_B:
    show 08B_inq_02
label nine:
    show 09_inq_01
    jump seventeen
label ten:
    show 10_inq_01
    jump eleven
label eleven:
    "incontri un uomo arrabbiato"
    menu:
        "chiedi cos'è successo":
            jump eight_B
        "lo ignori":
            jump twelve
label twelve:
    jump HARD_DEATH
label thirteen:
    show 13_inq_01
    "telefonata in arrivo"
    menu:
        "rispondi":
            jump fifteen
        "ignora":
            jump fourteen
label fourteen:
    jump HARD_DEATH
label fifteen:
    #$ renpy.movie_cutscene("images/Videos/15_01.avi")
    "cutscene 15_01"
    show 16_inq_01
    "la aiuti?"
    menu:
        "si":
            jump four
        "no":
            jump sixteen
label sixteen:
    jump HARD_DEATH
label seventeen:
    show 17_inq_01
    Titolare "titolare"
    Bagnina "bagnina"
    Bkiller "Killer(svelato)"
    Akiller "Killer(anonimo)"
    Compratore "compratore"
    jump eightteen
label eightteen:
    #$ renpy.movie_cutscene("images/Video/18_01.avi")
    "cutscene 18_01"
    jump nineteen
label nineteen:
    #$ renpy.movie_cutscene("images/Video/19_01.avi")
    "cutscene 19_01"
    pt "potrebbe essere la mia occasione"
    menu:
        "invio il curriculum":
            jump twentyone
        "nah, oggi sono in vacanza":
            jump twenty
label twenty:
    jump HARD_DEATH
label twentyone:
    show 21_inq_01
    jump twentytwo
label twentytwo:
    show 22_inq_01
    jump preoffice
label preoffice:
    show 23_inq_01 #ufficio porta
    menu:
        "entri in ufficio":
            jump office
        "non entri":
            jump twentythree
label twentythree:
    "hanno arrestato caio"
    jump HARD_DEATH
label office:
    scene bg office
    "end of dev cycle"
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

