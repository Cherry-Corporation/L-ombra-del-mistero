#  Lo script di gioco va in questo file.

#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define s = Character("Segretaria", color="#ffffffff")
define v = Character("Vittima HAI SBAGLIATO QUALCOSA SE LO VEDI!!!", color="#ff0000")
define k = Character("Killer", color="#20ad43ff")
define p = Character("Pregiudicato", color="#ffae00ff")

# NVL charactersfor the phone logic
define n_nvl = Character("Noi", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Amica", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#nvl ex
#    e_nvl "Ciao, posso chiamarti?"
#    n_nvl "Certo! Chiama pure adesso!"
#############################################
# Il gioco comincia qui.

label start:
    #Spotmannus
#    $ renpy.movie_cutscene("images/Video/cutscene_iniziale.webm")
    scene bg casa_protagonista
    "200ok"
    e_nvl "Amica"
    n_nvl "player"
    "200ok"


    




    # Gioco go kaboom @ return instr.
    return

