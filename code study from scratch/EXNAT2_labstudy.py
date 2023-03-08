####################################################
#                                                  #
#   Create EXNAT-2 EEG experiment using PsychoPy   #
#                                                  #
####################################################


# Author: Merle Schuckart (Auditory Cognition Group, Dep. for Psych. 1, University of Lübeck)
# Contact: merle.schuckart@uni-luebeck.de
# Version: 1.0 (08.03.2023)



''' ---- 1. Settings ----------------------------------------'''

# import packages 
# --> you might have to pip install some of the packages first

# os for getting/setting working directory
import os

import sys

# psychopy for creating study components
from psychopy import visual, core, event

# numpy for being able to calculate
import numpy as np

# for random number generator
import random

# pylsl for pushing triggers to lsl stream
#from pylsl import StreamInlet, resolve_stream, StreamOutlet, StreamInfo, local_clock, StreamInlet

#import socket
#import serial


# Set working directory
dir_path = os.path.dirname(os.path.realpath(__file__))
# set working directory to location of current file

''' ---- 2. Prep functions ----------------------------------------'''



def main_experiment():
    


        ## ################    Setup LSL Stream     ####################

        # Create trigger stream:
            
        global out_marker
        #info_marker_stream = StreamInfo('PsychoPyMarkers', 'Marker', 1, 0, 'string')
        #out_marker = StreamOutlet(info_marker_stream)


        ## ################    Demographics         ####################

        # get user input
        ID = input("Wie lautet Ihr Versuchspersonen-Code?") # ID
        age = input("Wie alt sind Sie?") # age
        gender = input("Welches Geschlecht steht \nin Ihrem Ausweis (m / w / d)?") # gender

        # push as triggers to LSL
        #out_marker.push_sample(["START EXPERIMENT"]) 
        #out_marker.push_sample(["ID: " + ID + ", age: " + age + ", gender: " + gender]) 

        
        ## ################    Setup Psychopy     ####################

        # Set window and remove mouse during experiment:
        global win
        win = visual.Window(size     = (800,600), # set window size
                            fullscr  = False, # make window full screen for better timing and less distractions
                            allowGUI = True, # False = draw window w/o frame or closing buttons
                            monitor  = 'testMonitor', 
                            units    = 'norm',
                            color    = [1,1,1])
        
        # make sure there are no key events defined so we start with a clean slate
        event.globalKeys.clear()
        
        
        ## ################    Experiment Settings     ####################

        """ set response keys """
        # to go from word to word, I use the Space bar
        # to indicate that an n-back target was detected & 
        # the key C for right-handed people 
        # (we don't test left-handed people in the EEG study)

        # add new global event keys "c" and "Space"
        # "c" calls the function target_response and Space calls the 
        # function next_word (both defined at the end of the script)
        target_key = "c"
        event.globalKeys.add(key = target_key, func = target_response)

        continue_key = "Space"
        event.globalKeys.add(key = continue_key, func = next_word)



        """ set colours """        
        global colours 
        colours = ["#D292F3", "#F989A2", "#2AB7EF", "#88BA3F"]
        #  #D292F3 = weird lilac with a 2000s vibe
        #  #F989A2 = bubblegum pink
        #  #2AB7EF = Twitter blue
        #  #88BA3F = medium grass green
        # (#D8A244 = dark curry-ish yellow --> excluded!)
        
        # All colours have a luminance of 70 and a chroma of 74.
        
        # The colours are selected for distinguishability (is that a word?!) 
        # for people with "normal" colour vision as well as for 
        # people with protanomaly (red olour vision deficiency (CVD)), 
        # deuteranomaly (green CVD) and 
        # tritanomaly (blue CVD).
        
        # People with a "true" colour blindness 
        # (i.e. protanopia, deuteranopia, tritanopia)
        # shouldn't participate in this study.


        """ set texts """
        # Prepare lists with words & additional information on the blocks
        # hint: escape " characters like this \"

        # Giant Squid
        global text_01
        text_01 = ["Beim", "Anblick", "der", "Tiere", "wird", "klar,", "warum", "die", "Seeleute", "vergangener", "Jahrhunderte", "Angst", "vor", "Seeungeheuern", "hatten.", "Meterlange", "Fangarme,", "spitze", "Mäuler", "und", "riesige", "Augen", "verleihen", "den", "großen", "Kalmaren", "ein", "furchterregendes", "Aussehen.", "Vor", "der", "Küste", "Chiles", "sind", "sie", "aktuell", "in", "Massen", "zu", "sehen.", "Hunderte", "von", "riesigen", "Tintenfischen", "schwimmen", "in", "den", "flachen", "Gewässern", "und", "fressen", "dort", "die", "Fische.", "Normalerweise", "sind", "die", "großen", "Kalmare", "nur", "schwer", "zu", "beobachten.", "Sie", "leben", "eigentlich", "im", "offenen", "Meer.", "Nur", "nachts", "kommen", "sie", "an", "die", "Oberfläche,", "um", "kleine", "Fische", "zu", "jagen.", "Seit", "zwei", "Wochen", "aber", "sind", "sie", "auch", "bei", "Tageslicht", "vor", "der", "Küste", "zu", "sehen.", "Zunächst", "wurden", "mehr", "als", "200", "Kalmare", "vor", "einer", "Insel", "vor", "Chile", "gesichtet.", "Später", "wurden", "dann", "weitere", "Kalmare", "an", "anderen", "Orten", "entlang", "der", "Küste", "Chiles", "beobachtet.", "Vor", "allem", "für", "die", "Fischer", "ist", "das", "ärgerlich.", "Die", "Kalmare", "fressen", "Hechte,", "Sardinen", "und", "Sardellen.", "Und", "sie", "haben", "großen", "Hunger -", "schlechte", "Karten", "für", "die", "kleineren", "Fische.", "Die", "Kalmare", "selbst", "haben", "hingegen", "Glück:", "Sie", "gelten", "zwar", "in", "manchen", "Ländern", "als", "Delikatesse,", "werden", "in", "Chile", "jedoch", "nicht", "gegessen.", "Meeresbiologen", "standen", "wegen", "des", "plötzlichen", "Erscheinens", "der", "Kalmare", "zunächst", "vor", "einem", "großen", "Rätsel.", "Nun", "ist", "jedoch", "klar,", "weshalb", "die", "Kalmare", "plötzlich", "auftauchten.", "Im", "Februar", "erwärmte", "sich", "das", "Meer", "verglichen", "mit", "den", "Temperaturen", "in", "den", "Vorjahren", "ungewöhnlich", "stark.", "Es", "sammelten", "sich", "viele", "kleine", "Fische", "vor", "der", "Küste.", "Die", "Kalmare", "wurden", "dadurch", "magisch", "angezogen.", "Die", "kleinen", "Fische", "bedeuten", "für", "sie", "reiche", "Beute.", "Für", "Forscher", "ist", "das", "ein", "besonderer", "Glücksfall.", "Normalerweise", "sind", "die", "großen", "Kalmare", "so", "schwer", "vor", "die", "Kamera", "zu", "bekommen,", "dass", "Forscher", "teilweise", "auf", "seltsame", "Ideen", "kommen.", "Ein", "Biologe", "aus", "Neuseeland", "etwa", "will", "versuchen,", "den", "legendären", "Riesenkalmar", "mit", "Sexualhormonen", "vor", "die", "Linse", "zu", "locken.", "Der", "Riesenkalmar", "ist", "mit", "bis", "zu", "20", "Metern", "Länge", "und", "einer", "halben", "Tonne", "Gewicht", "das", "größte", "wirbellose", "Tier", "der", "Welt.", "Bisher", "wurde", "er", "aber", "noch", "nie", "innerhalb", "seines", "natürlichen", "Lebensraums", "gefilmt."]
        
        # Hemingway / The old man and the sea
        global text_02
        text_02 = ["Zwanzig", "Jahre", "verbrachte", "Ernest", "Hemingway", "auf", "Kuba.", "Die", "meiste", "Zeit", "davon", "lebte", "er", "in", "Vigía,", "seinem", "legendären", "Haus", "vor", "den", "Toren", "Havannas.", "Seit", "seinem", "Tod", "Anfang", "der", "1960er", "lagern", "in", "Vigía", "etwa", "3000", "Manuskripte", "des", "Autors.", "In", "den", "vergangenen", "Jahren", "sind", "sie", "nach", "und", "nach", "digitalisiert", "worden.", "Nun", "will", "man", "sie", "zunächst", "in", "Kuba", "zeigen,", "bevor", "sie", "dann", "der", "Bibliothek", "von", "Boston", "übergeben", "werden.", "Die", "Leiterin", "des", "Archivs", "in", "Vigía", "sagte", "am", "Montag", "im", "kubanischen", "Fernsehen,", "es", "handele", "sich", "um", "bisher", "unveröffentlichte", "Stücke.", "Die", "Digitalisierung", "war", "zwischen", "den", "USA", "und", "Kuba", "bereits", "2002", "vereinbart", "worden.", "Damals", "berichtete", "die", "\"New", "York", "Times\",", "unter", "den", "Dokumenten", "befänden", "sich", "Texte,", "die", "auf", "lose", "Blätter", "und", "Buchrücken", "gekritzelt", "worden", "seien.", "Dies", "seien", "vor", "allem", "Briefe,", "Entwürfe", "und", "Aufzeichnungen", "zu", "Hemingways", "großen", "Romanen.", "Der", "Biograf", "Hemingways", "nannte", "den", "gesamten", "Nachlass", "eine", "\"Computertomografie", "von", "Hemingways", "Gehirn\".", "In", "Kuba", "schrieb", "Hemingway", "unter", "anderem", "seine", "berühmte", "Novelle", "\"Der", "alte", "Mann", "und", "das", "Meer\".", "Die", "Novelle", "handelt", "vom", "Kampf", "eines", "alten", "Fischers", "mit", "einem", "riesigen", "Schwertfisch.", "Zwei", "Tage", "und", "zwei", "Nächte", "ringt", "der", "Fischer", "mit", "dem", "Schwertfisch,", "bis", "er", "ihn", "schließlich", "am", "dritten", "Tag", "überwältigen", "kann.", "Da", "der", "Fisch", "zu", "groß", "ist,", "um", "ihn", "ins", "Boot", "zu", "ziehen,", "bindet", "er", "ihn", "von", "außen", "ans", "Boot.", "Das", "Blut", "des", "Schwertfisches", "lockt", "auf", "der", "Heimfahrt", "jedoch", "Haie", "an.", "Die", "Haie", "fressen", "nach", "und", "nach", "Teile", "des", "Schwertfischs,", "sodass", "dem", "Fischer", "nur", "das", "Skelett", "bleibt,", "als", "er", "wieder", "in", "den", "Heimathafen", "zurückkehrt.", "Die", "Figur", "des", "Fischers", "ist", "vermutlich", "angelehnt", "an", "den", "Fischer", "Gregorio", "Fuentes,", "der", "sich", "auf", "Kuba", "um", "Hemingways", "Boot", "kümmerte.", "Für", "sein", "Werk", "wurde", "Hemingway", "mit", "dem", "Literaturnobelpreis", "ausgezeichnet.", "Die", "Nobelpreis-Medaille", "schenkte", "er", "aus", "Verbundenheit", "zu", "Kuba", "der", "Wallfahrtskirche", "der", "barmherzigen", "Jungfrau", "von", "Cobre.", "Sie", "ist", "die", "Schutzpatronin", "Kubas.", "Die", "Medaille", "ist", "auch", "heute", "noch", "in", "der", "Kirche", "zu", "sehen."]
        
        # Einstein
        global text_03
        text_03 = ["Sie", "besuchte", "ihn", "oft", "in", "seinem", "Haus", "und", "bekam", "Briefe", "und", "Gedichte", "von", "ihm.", "Manchmal", "durfte", "sie", "ihm", "sogar", "die", "Haare", "schneiden.", "Johanna", "Fantova", "galt", "als", "letzte", "Freundin", "von", "Albert", "Einstein.", "Die", "beiden", "trafen", "sich", "regelmäßig,", "telefonierten", "viel", "und", "gingen", "miteinander", "segeln.", "Nun", "wurde", "bekannt,", "was", "offenbar", "nicht", "einmal", "Einstein", "wusste:", "Johanna", "Fantova", "fertigte", "Notizen", "über", "den", "Inhalt", "ihrer", "Gespräche", "an.", "In", "ihren", "Aufzeichnungen", "zeigt", "sie", "ihn", "nicht", "als", "den", "großen", "Mann,", "der", "zu", "Lebzeiten", "zur", "Legende", "wurde,", "sondern", "als", "Einstein,", "den", "Menschenfreund.", "Die", "Nachwelt", "dürfte", "ihr", "dankbar", "sein.", "Ohne", "die", "Notizen", "wüssten", "wir", "heute", "nichts", "von", "Bibo,", "dem", "traurigen", "Papagei.", "Auch", "eine", "ganze", "Reihe", "kluger", "und", "lustiger", "Zitate", "von", "Einstein", "wären", "verloren", "gegangen.", "Es", "ist", "bisher", "das", "einzige", "bekannte", "Tagebuch", "von", "einer", "Person,", "die", "während", "seiner", "letzten", "Jahre", "eng", "mit", "Einstein", "befreundet", "war.", "Die", "22", "Jahre", "jüngere", "Johanna", "Fantova", "stammte", "wie", "Einstein", "aus", "Europa.", "Die", "Eltern", "ihres", "Ehemannes", "Otto", "Fanta", "empfingen", "vor", "dem", "Krieg", "viele", "berühmte", "Gäste", "in", "ihrem", "Salon.", "Neben", "Einstein", "zählte", "dazu", "auch", "Franz", "Kafka.", "Johanna", "Fantova", "war", "für", "Einstein", "daher", "ein", "Teil", "der", "alten", "Welt.", "Sie", "war", "eine", "Verbindung", "zu", "Dingen,", "die", "er", "vermisste.", "In", "Fantovas", "Manuskript", "erscheint", "Einstein", "als", "komischer", "Eigenbrötler.", "Zugleich", "beschreibt", "sie", "ihn", "aber", "auch", "als", "Menschenfreund,", "der", "vielen", "seiner", "Freunde", "bei", "persönlichen", "Problemen", "half.", "Und", "doch", "fühlte", "sich", "Einstein", "nie", "wirklich", "mit", "seinen", "Mitmenschen", "verbunden.", "Angesichts", "seiner", "eigenen", "gescheiterten", "Beziehungen", "betrachtete", "er", "die", "Beziehungen", "seiner", "Freunde", "mit", "spöttischer", "Distanz:", "\"Ich", "war", "bei", "einem", "Nachbarn.", "Es", "besteht", "die", "Gefahr,", "dass", "sein", "Sohn", "heiratet.\"", "Rührend", "kümmerte", "er", "sich", "dagegen", "um", "sein", "Haustier,", "einen", "deprimierten", "Papagei", "namens", "Bibo.", "\"Der", "Papagei", "ist", "noch", "ganz", "verschüchtert.", "Er", "kam", "mit", "der", "Post.\"", "Einstein", "schritt", "sofort", "zur", "Tat.", "Der", "Erfolg", "blieb", "jedoch", "leider", "aus:", "\"Der", "Papagei", "ist", "traurig.", "Ich", "versuche", "ihn", "aufzuheitern,", "aber", "er", "versteht", "leider", "meine", "Witze", "nicht.\""]
        
        # Batman's Joker
        global text_04
        text_04 = ["Jerry", "Robinson", "war", "erst", "17,", "als", "er", "die", "wichtigste", "Entscheidung", "seines", "Lebens", "traf -", "und", "möglicherweise", "seinen", "größten", "Fehler", "beging.", "Statt", "wie", "geplant", "aufs", "College", "zu", "gehen,", "ließ", "er", "sich", "von", "einem", "Mann", "namens", "Bob", "Kane", "als", "Zeichner", "engagieren.", "Kane", "hatte", "gerade", "die", "Zeichnungen", "für", "ein", "Comicheft", "abgeliefert,", "in", "dem", "er", "eine", "völlig", "neue", "Figur", "auftreten", "ließ,", "genannt", "\"Batman\".", "Jetzt", "machte", "er", "Urlaub", "in", "den", "Poconos,", "einem", "Ausflugsgebiet", "in", "Pennsylvania.", "Der", "untergewichtige", "Jerry", "Robinson", "war", "auf", "einer", "Kur", "dort,", "um", "Gewicht", "zuzulegen.", "Um", "Bob", "Kane", "von", "seinem", "Talent", "als", "Zeichner", "zu", "überzeugen,", "fertigte", "Jerry", "Robinson", "für", "ihn", "ein", "paar", "Zeichnungen", "an.", "Da", "er", "kein", "Papier", "zur", "Hand", "hatte,", "zeichnete", "er", "kurzerhand", "auf", "seiner", "Jacke.", "Beeindruckt", "stellte", "Kane", "den", "Jungen", "an.", "Bereits", "ab", "der", "dritten", "Ausgabe", "der", "Batman-Comics", "war", "er", "der", "Hauptzeichner", "der", "Serie.", "Seine", "Zeichnungen", "fertigte", "er", "vor", "allem", "nachts", "an.", "Tagsüber", "studierte", "er", "Journalistik", "in", "New", "York.", "Neben", "dem", "Zeichnen", "tat", "er", "sich", "auch", "bei", "der", "Entwicklung", "der", "Figuren", "hervor.", "Von", "ihm", "stammten", "die", "Entwürfe", "für", "Batmans", "Butler", "Alfred", "und", "Batmans", "Helfer,", "den", "jungen", "Robin.", "Fast", "zeitgleich", "hatte", "der", "Joker,", "Batmans", "Erzfeind,", "seinen", "ersten", "Auftritt", "in", "einem", "weiteren", "Heft.", "Robinson", "behauptete", "später,", "die", "Idee", "zur", "Figur", "des", "Jokers", "sei", "von", "ihm", "ausgegangen.", "Inspiriert", "wurde", "er", "dabei", "durch", "ein", "Kartenspiel,", "das", "seine", "Kollegen", "immer", "zur", "Hand", "hatten.", "Laut", "Bob", "Kane", "beruht", "der", "Entwurf", "des", "Schurken", "dagegen", "auf", "einer", "Szene", "aus", "einem", "Stummfilm.", "\"Robinson", "hatte", "nichts", "damit", "zu", "tun\",", "war", "sein", "drastisches", "Urteil.", "Hier", "rächte", "es", "sich,", "dass", "Jerry", "Robinson", "lediglich", "als", "Assistent", "engagiert", "war,", "auch", "wenn", "er", "der", "Hauptzeichner", "war.", "Kane", "dagegen", "hatte", "sich", "alle", "Rechte", "an", "den", "Figuren", "zugesichert.", "Nicht", "zuletzt", "deshalb", "begann", "Jerry", "Robinson", "ab", "1940", "nicht", "mehr", "für", "Kane,", "sondern", "für", "den", "Comic-Verlag", "direkt", "zu", "arbeiten.", "In", "dessen", "Studio", "saß", "er", "zeitweise", "neben", "\"Superman\"-Miterfinder", "Joe", "Shuster", "am", "Zeichentisch."]
        
        # tiny chameleons
        global text_05
        text_05 = ["Die", "Korallenriffe", "und", "die", "sandigen", "Buchten", "sind", "perfekt", "für", "jede", "Urlaubsbroschüre.", "Insgesamt", "ist", "die", "Inselgruppe", "namens", "Nosy", "Hara", "vor", "Madagaskar", "aber", "doch", "recht", "karg.", "In", "dieser", "eher", "lebensfeindlichen", "Umgebung", "haben", "Biologen", "nun", "eine", "neue", "Tierart", "entdeckt:", "Das", "winzige", "Chamäleon", "Brookesia", "micra.", "Von", "der", "Schnauze", "bis", "zum", "Schwanzende", "misst", "es", "weniger", "als", "drei", "Zentimeter.", "Farblich", "machen", "die", "braunen", "Tierchen", "wenig", "her.", "Doch", "ihre", "winzige", "Körpergröße", "fasziniert", "die", "Forscher.", "\"Das", "ist", "nichts,", "wo", "man", "viele", "Untersuchungen", "machen", "muss.", "Man", "erkennt", "auch", "so,", "dass", "das", "etwas", "Neues", "ist\",", "sagt", "Miguel", "Vences.", "Der", "Zoologe", "berichtet", "in", "einem", "Fachartikel", "gleich", "von", "vier", "neuen", "Arten", "von", "Mini-Chamäleons.", "Laut", "den", "Forschern", "weiß", "man", "von", "den", "Tieren", "jedoch", "kaum", "mehr,", "als", "dass", "es", "sie", "gibt.", "Zu", "ihrer", "Lebensweise", "ist", "nur", "sehr", "wenig", "bekannt.", "Tagsüber", "leben", "die", "kleinen", "Chamäleons", "am", "Boden.", "Wenn", "möglich", "verbergen", "sie", "sich", "dabei", "unter", "einer", "Schicht", "Laub.", "Nachts", "geht", "es", "dann", "auf", "niedrig", "gelegene", "Äste", "zum", "Schlafen.", "Direkte", "Fressfeinde", "haben", "die", "Tierchen", "allerdings", "wohl", "eher", "nicht.", "Zu", "ihrem", "Glück,", "so", "die", "Forscher.", "Auf", "solchen", "kleinen", "Inseln", "kann", "die", "Konkurrenz", "zwischen", "den", "Tierarten", "schnell", "sehr", "groß", "werden.", "Auch", "die", "anderen", "neuen", "Chamäleon-Arten", "besiedeln", "nur", "kleine", "Gebiete", "auf", "Madagaskar.", "Durch", "die", "Zerstörung", "ihres", "Lebensraums", "sind", "sie", "jedoch", "besonders", "bedroht.", "Rund", "40", "Prozent", "der", "Reptilien-Arten", "auf", "Madagaskar", "gelten", "mittlerweile", "als", "gefährdet.", "Die", "Forscher", "befürchten,", "dass", "auch", "Brookesia", "tristis,", "eine", "weitere", "neu", "entdeckte", "Art,", "einer", "ungewissen", "Zukunft", "entgegen", "sieht.", "Zwar", "ist", "der", "Lebensraum", "des", "Chamäleons", "vor", "wenigen", "Jahren", "unter", "Schutz", "gestellt", "worden,", "doch", "die", "Abholzung", "des", "Gebiets", "hat", "seitdem", "leider", "sogar", "noch", "zugenommen.", "Mit", "der", "Wahl", "der", "Namen", "der", "neu", "entdeckten", "Chamäleon-Arten", "wollen", "sie", "auf", "die", "große", "Gefahr", "hinweisen,", "die", "den", "Chamäleons", "droht.", "Die", "Botschaft", "hinter", "den", "Namen", "Brookesia", "desperata", "und", "Brookesia", "tristis", "versteht", "man", "auch", "ohne", "Latein", "zu", "können:", "Desperata", "heißt", "verzweifelt", "und", "tristis", "so", "viel", "wie", "traurig."]
        
        # Mauritius
        global text_06
        text_06 = ["In", "den", "siebziger", "Jahren", "war", "Mauritius", "eine", "kleine", "Insel", "mitten", "im", "Indischen", "Ozean,", "die", "im", "Ausland", "niemand", "kannte.", "Heute", "ist", "sie", "dagegen", "weltweit", "als", "paradiesisches", "Urlaubsziel", "bekannt.", "Doch", "schon", "lange", "bevor", "die", "ersten", "Touristen", "kamen,", "war", "Mauritius", "in", "einigen", "Teilen", "der", "Welt", "sehr", "bekannt.", "Die", "Portugiesen", "waren", "die", "Ersten,", "die", "die", "Insel", "entdeckten.", "Sie", "nannten", "sie", "\"Schwaneninsel\",", "ließen", "sich", "aber", "nicht", "auf", "ihr", "nieder.", "Erst", "fast", "hundert", "Jahre", "später", "kamen", "die", "Holländer.", "Sie", "gaben", "der", "Insel", "zu", "Ehren", "des", "holländischen", "Prinzen", "Moritz", "den", "Namen", "\"Mauritius\".", "Den", "Namen", "Mauritius", "hat", "sie", "bis", "heute", "behalten.", "Die", "Holländer", "begannen,", "an", "der", "Küste", "Felder", "anzulegen.", "Sie", "brachten", "Zuckerrohr,", "Wild", "und", "Affen", "mit", "auf", "die", "Insel.", "Sie", "bauten", "Häuser", "und", "Festungen", "und", "holzten", "die", "dichten", "Wälder", "aus", "Ebenholz", "ab.", "Zu", "dieser", "Zeit", "lebten", "auf", "Mauritius", "noch", "viele", "Dodos.", "Die", "flugunfähigen", "Vögel", "hatten", "keine", "natürlichen", "Feinde", "auf", "der", "Insel", "und", "waren", "daher", "zu", "ihrem", "eigenen", "Unglück", "sehr", "zahm.", "Für", "die", "Holländer", "machte", "sie", "das", "zur", "perfekten", "Jagdbeute.", "Der", "Dodo", "wurde", "so", "stark", "bejagt,", "dass", "er", "schon", "einige", "Jahrzehnte", "nach", "Ankunft", "der", "Holländer", "vollständig", "ausgerottet", "war.", "Heute", "ist", "er", "das", "Nationalsymbol", "von", "Mauritius.", "Als", "kein", "Holz", "mehr", "zu", "holen", "und", "die", "Natur", "schwer", "geschädigt", "war,", "verließen", "die", "Holländer", "Mauritius.", "Um", "die", "Kontrolle", "der", "Insel", "brach", "ein", "erbitterter", "Krieg", "zwischen", "Briten", "und", "Franzosen", "aus.", "Aber", "wer", "lebt", "heute", "dort?", "Die", "Bevölkerung", "von", "Mauritius", "ist", "das", "Ergebnis", "einer", "Vermischung", "verschiedener", "Kulturen", "und", "Religionen.", "Viele", "der", "Menschen", "kamen", "nicht", "freiwillig.", "Die", "Holländer", "brachten", "afrikanische", "Sklaven", "mit", "auf", "die", "Insel.", "Aus", "Indien", "kamen", "Arbeiter", "für", "die", "Zuckerrohr-Plantagen", "und", "Handwerker,", "die", "beim", "Bau", "von", "Brücken", "und", "Straßen", "halfen.", "Zeitgleich", "mit", "den", "Indern", "kamen", "auch", "muslimische", "und", "chinesische", "Händler", "nach", "Mauritius. ", "Die", "Nachfahren", "von", "Indern,", "Franzosen,", "Chinesen,", "Arabern", "und", "afrikanischen", "Sklaven", "bilden", "heute", "auf", "Mauritius", "eine", "der", "wenigen", "echten", "multikulturellen", "Gesellschaften", "der", "Welt."]
        
        # Angkor Wat
        global text_07
        text_07 = ["Wer", "Angkor", "sagt,", "meint", "in", "der", "Regel", "Angkor", "Wat.", "Die", "berühmte", "Tempelanlage", "wurde", "vermutlich", "vor", "knapp", "900", "Jahren", "in", "den", "Dschungel", "Kambodschas", "gebaut.", "Seit", "mehr", "als", "hundert", "Jahren", "hat", "sich", "die", "Wissenschaft", "auf", "die", "riesigen", "Tempelanlagen", "und", "ihre", "Inschriften", "konzentriert.", "Für", "die", "Lebensweise", "der", "Bewohner", "der", "Region", "hat", "sich", "hingegen", "kaum", "jemand", "interessiert.", "Das", "Team", "um", "den", "Forscher", "Damian", "Evans", "hat", "nun", "erstmals", "eine", "Karte", "von", "Angkor", "Wat", "erstellt.", "Die", "Karte", "zeigt,", "dass", "Angkor", "Wat", "eine", "richtige", "Stadt", "war,", "nicht", "nur", "eine", "kleine", "Tempelanlage.", "Die", "Forscher", "gehen", "davon", "aus,", "dass", "Ihre", "Größe", "sogar", "New", "York", "übertroffen", "haben", "könnte.", "Damit", "ist", "\"Groß-Angkor\"", "die", "mit", "Abstand", "größte", "vorindustrielle", "Siedlung", "der", "Welt.", "Selbst", "die", "riesigen", "Städte", "der", "Maya", "erscheinen", "dagegen", "winzig.", "Die", "Forscher", "fanden", "außerdem", "heraus,", "dass", "Angkor", "eine", "hydraulische", "Stadt", "war.", "Dank", "eines", "komplizierten", "Bewässerungssystems", "konnten", "die", "mehr", "als", "eine", "Million", "Bewohner", "versorgt", "werden.", "Durch", "das", "riesige", "Netz", "aus", "Flüssen,", "Kanälen", "und", "Stauseen", "hat", "die", "mittelalterliche", "Stadt", "mehrmals", "im", "Jahr", "Reis", "ernten", "können.", "Das", "verschaffte", "den", "Bewohnern", "nicht", "nur", "volle", "Teller,", "sondern", "auch", "einen", "enormen", "Reichtum.", "Die", "Stadt", "umgab", "ein", "riesiges", "Geflecht", "aus", "Äckern,", "Häusern", "und", "Seen,", "das", "sich", "über", "mindestens", "tausend", "Quadratkilometer", "erstreckte.", "Auf", "dieser", "Fläche", "gibt", "es", "kaum", "einen", "Fleck,", "der", "nicht", "genutzt", "worden", "ist.", "Das", "Bewässerungsnetz", "war", "sogar", "dazu", "geeignet,", "den", "Reisanbau", "zu", "stärken.", "Für", "den", "Anbau", "von", "Reis", "braucht", "man", "jedoch", "extrem", "viel", "Wasser", "und", "riesige", "Flächen.", "Um", "die", "Felder", "und", "die", "künstlichen", "Seen,", "Flüsse", "und", "Kanäle", "anzulegen,", "mussten", "große", "Waldflächen", "gerodet", "werden.", "Mit", "der", "Zeit", "führte", "das", "wahrscheinlich", "zu", "riesigen", "Problemen", "wie", "Erdrutschen.", "Das", "gesamte", "System", "dürfte", "daher", "auch", "sehr", "empfindlich", "auf", "Naturkatastrophen", "reagiert", "haben.", "Insbesondere", "im", "Norden", "der", "Stadt", "fand", "man", "Spuren", "von", "hektischen", "Anpassungen", "und", "Deichbrüchen.", "Genaueres", "weiß", "man", "aber", "nicht.", "Die", "neue", "Karte", "der", "Stadt", "verrät", "aber", "zumindest,", "wo", "man", "nach", "Antworten", "suchen", "sollte."]
        
        # Petra
        global text_08
        text_08 = ["Ein", "solcher", "Anblick", "lässt", "selbst", "Indiana", "Jones", "Kinnlade", "herunterklappen:", "Nach", "einem", "spektakulären", "Ritt", "durch", "eine", "teils", "nur", "zwei", "Meter", "schmale", "Schlucht", "erhebt", "sich", "vor", "dem", "Filmhelden", "eine", "riesige", "Fassade.", "Die", "Szene", "aus", "dem", "Kinofilm", "machte", "die", "antike", "Felsenstadt", "Petra", "endgültig", "weltberühmt.", "Die", "prachtvolle", "Fassade", "ist", "eine", "der", "schönsten", "Bauten", "in", "der", "Felsenstadt", "mitten", "in", "der", "Wüste", "Jordaniens.", "Die", "Metropole", "war", "einst", "die", "Hauptstadt", "der", "Nabatäer.", "Zwei", "Jahrhunderte", "beherrschten", "die", "Nabatäer", "große", "Teile", "des", "Handels", "im", "Nahen", "Osten.", "So", "reich", "und", "mächtig", "wurde", "das", "Wüstenvolk,", "dass", "es", "sogar", "die", "Römer", "herausforderte.", "Doch", "wie", "ihre", "riesige", "Hauptstadt", "mitten", "in", "der", "Wüste", "funktioniert", "hat,", "weiß", "niemand", "genau.", "Sicher", "ist,", "dass", "die", "Stadt", "in", "atemberaubend", "kurzer", "Zeit", "entstand.", "Als", "die", "Nabatäer", "ins", "heutige", "Jordanien", "vordrangen,", "war", "die", "Region", "die", "reinste", "Goldgrube.", "Bei", "Petra", "kreuzten", "sich", "mehrere", "Handelswege,", "darunter", "die", "uralte", "Weihrauchstraße.", "Binnen", "weniger", "Jahrzehnte", "entstanden", "hunderte", "Höhlen", "mit", "prunkvollen", "Fassaden", "und", "teils", "gewaltigen", "Räumen.", "Von", "der", "eigentlichen", "Stadt", "ist", "heute", "nichts", "geblieben", "außer", "Steinhaufen", "und", "Mauerreste.", "Bis", "in", "die", "siebziger", "Jahre", "glaubte", "man", "daher,", "Petra", "sei", "eine", "Stadt", "für", "die", "Toten", "und", "die", "Götter", "gewesen,", "und", "die", "Menschen", "hätten", "woanders", "gewohnt.", "Aber", "Petra", "war", "eine", "ganz", "normale", "Stadt,", "nur", "an", "einem", "unmöglichen", "Ort.", "Die", "seltenen", "Regenfälle", "nutzten", "die", "Nabatäer", "mit", "einem", "genialen", "Bewässerungssystem.", "Überall", "in", "der", "Stadt", "waren", "Wasserbecken", "in", "den", "Fels", "geschlagen.", "Viele", "Kilometer", "Wasserleitungen", "leiteten", "das", "Wasser", "zuerst", "in", "die", "Speicher", "und", "von", "dort", "aus", "zu", "den", "Bewohnern.", "Die", "vielen", "Leitungen,", "die", "den", "Regen", "einst", "von", "den", "wertvollen", "Fassaden", "fernhielten,", "wurden", "von", "den", "Nabatäern", "dauernd", "instand", "gehalten.", "Doch", "wenn", "es", "jetzt", "regnet,", "strömt", "das", "Wasser", "unkontrolliert", "die", "Fassaden", "herab.", "Für", "den", "Sandstein", "ist", "das", "eine", "Katastrophe.", "Versuche", "zur", "Rettung", "der", "Fassaden", "gab", "es,", "doch", "wirklich", "erfolgreich", "war", "bislang", "leider", "keiner.", "Die", "antike", "Felsenstadt", "wird", "daher", "wohl", "eines", "Tages", "wieder", "zu", "Sand", "zerfallen."]
        
        # Shakespeare / Hamlet
        global text_09
        text_09 = ["William", "Shakespeare", "war", "etwa", "fünf", "Jahre", "alt,", "als", "gar", "nicht", "weit", "entfernt", "von", "seinem", "Heimatdorf", "die", "nur", "zweijährige", "Jane", "Shaxspere", "ums", "Leben", "kam.", "Das", "kleine", "Mädchen", "wollte", "Ringelblumen", "pflücken,", "die", "am", "Ufer", "eines", "Mühlteichs", "wuchsen.", "Beim", "Blumenpflücken", "rutschte", "Jane", "aus,", "fiel", "ins", "Wasser", "und", "ertrank.", "William", "Shakespeare,", "der", "etwa", "20", "Kilometer", "entfernt", "im", "Dorf", "Stratford-upon-Avon", "aufwuchs,", "sollte", "später", "zum", "größten", "Dramatiker", "aller", "Zeiten", "heranwachsen.", "Forscher", "der", "Universität", "von", "Oxford", "vermuten", "nun", "einen", "Zusammenhang", "dieses", "Unfalls", "mit", "Shakespeares", "Stück", "\"Hamlet\".", "Eine", "Nebenhandlung", "des", "Stücks", "erzählt", "die", "Geschichte", "der", "fiktiven", "Edeldame", "Ophelia,", "der", "Tochter", "eines", "Kämmerers.", "Ophelia", "wächst", "am", "dänischen", "Königshof", "auf,", "wo", "sie", "die", "Geliebte", "des", "Prinzen", "Hamlet", "wird.", "Ihre", "Beziehung", "wird", "von", "ihrem", "Vater", "und", "ihrem", "Bruder", "jedoch", "missbilligt.", "Sie", "bezweifeln,", "dass", "Hamlet", "die", "ehrliche", "Absicht", "hat,", "Ophelia", "zu", "heiraten.", "Als", "Hamlet", "aus", "Versehen", "Ophelias", "Vater", "tötet,", "verzweifelt", "sie", "und", "erleidet", "ein", "ähnliches", "Schicksal", "wie", "die", "kleine", "Jane.", "Beim", "Blumenpflücken", "an", "einem", "Bachufer", "verliert", "sie", "das", "Gleichgewicht", "und", "fällt", "in", "den", "Bach.", "Ihr", "Kleid", "saugt", "sich", "mit", "Wasser", "voll", "und", "zieht", "sie", "wie", "ein", "Gewicht", "nach", "unten.", "Ob", "ihr", "Tod", "ein", "Unfall", "ist", "oder", "sie", "sich", "mit", "Absicht", "nicht", "aus", "dem", "Wasser", "rettet,", "wird", "im", "Stück", "offengelassen.", "Die", "erstaunliche", "Verbindung", "zwischen", "realen", "Ereignissen", "und", "Shakespeares", "\"Hamlet\"", "fiel", "Historikern", "auf,", "als", "sie", "alte", "medizinische", "Akten", "untersuchten.", "Die", "Ähnlichkeit", "der", "Nachnamen", "könnte", "sogar", "darauf", "hinweisen,", "dass", "William", "und", "Jane", "Verwandte", "gewesen", "sein", "könnten.", "Feste", "Schreibweisen", "von", "Namen", "gab", "es", "zu", "Shakespeares", "Zeiten", "nicht.", "Für", "eine", "der", "Forscherinnen", "aus", "Oxford", "ist", "dieses", "Detail", "aber", "nicht", "entscheidend:", "\"Selbst", "wenn", "sie", "nicht", "verwandt", "gewesen", "sind,", "hat", "sich", "die", "Geschichte", "durch", "die", "Ähnlichkeit", "der", "Namen", "vielleicht", "in", "Shakespeares", "Kopf", "verankert.\"", "Neben", "historischen", "Grundlagen", "seien", "Shakespeares", "Stücke", "auch", "von", "Klatsch", "und", "Tratsch-Geschichten", "beeinflusst", "worden.", "Dazu", "könnte", "auch", "die", "Geschichte", "über", "den", "Tod", "von", "Jane", "Shaxspere", "gezählt", "haben."]



        """ shuffle order of texts """
        
        # collect texts in lists
        global all_texts_list 
        all_texts_list = [text_01, text_02, text_03, text_04, text_05, text_06, text_07, text_08, text_09]

        # collect the text IDs in lists so I know which text was shown
        global all_texts_nrs_list 
        all_texts_nrs_list = ["text_01", "text_02", "text_03", "text_04", "text_05", "text_06", "text_07", "text_08", "text_09"]

        # shuffle lists:
        # IMPORTANT: set seed!
        # the seed should be random number over participants but the same within a participant
        seed = random.randint(1, 100)
        # now shuffle texts & text numbers
        random.Random(seed).shuffle(all_texts_list)
        random.Random(seed).shuffle(all_texts_nrs_list)
        

        """ Set order of blocks """
        # The first blocks should be:
        #    - reading baseline + training
        #    - click training
        #    - in random order: 1-back (single task training & main & dual task main) & 2-back (single task training & main & dual task main)
        #    - in random order: 2x reading BL main, 2x 1-back main, 2x 2-back main
        
        # this always comes first in the experiment
        Reading_BL = ["Reading_Baseline_training", "Reading_Baseline_main", "click_training"]
        
        # then you get both n-back conditions with trainings (which of them is first is randomized)
        oneback = ["1back_single_training", "1back_single_main", "1back_dual_main"]
        twoback = ["2back_single_training", "2back_single_main", "2back_dual_main"]
        # shuffle the order of the 2 lists
        main_blocks1 = [oneback, twoback]
        random.shuffle(main_blocks1)
        # flatten nested list
        main_blocks1 = [elem for sublist in main_blocks1 for elem in sublist]
        
        # now shuffle order of the last 6 main blocks:
        main_blocks2 = ["Reading_Baseline_main", "Reading_Baseline_main", "2back_dual_main", 
                       "1back_dual_main", "1back_dual_main", 
                       "2back_dual_main"]
        random.shuffle(main_blocks2)
        
        # put them all together:
        global all_blocks 
        all_blocks = Reading_BL + main_blocks1 + main_blocks2
        







        ## ################    Stimuli Psychopy    #################

        ## intro
        global exp_text
        exp_text = visual.TextStim(win,
                                     pos=[0,0],
                                     color = (1,1,1)
                                     )

        ## main trial components
        global fixation
        fixation =  visual.TextStim(win,
                                    pos=[0,0],
                                    text = '+',
                                    height = 0.7,
                                    color = (1,1,1)
                                    )


        # Set timer
        global timer
        timer = core.Clock()
        
        ####################  START EXPERIMENT  ###################################










        ####################  TRAINING BLOCK ###################################

        # explain task 1
        #txt = "Now match the two bars by pressing the force Sensor with auditive feedback"
        #presTextPsychoPy(txt)
        #event.waitKeys()




        ## ################    END EXPERIMENT    ####################

        win.close() # close window
        core.quit() # quit PsychoPy and then exit Python
        print("Ended experiment")





######################################################################




####################################################
#                                                  #
#           DEFINE EXPERIMENT COMPONENTS           #
#                                                  #
####################################################


''' function for showing instructions '''
def displ_instr(text):
    
    # set text:
    global show_instr                    # init global variable show_instr
    show_instr.text  = text              # set text
    show_instr.font  = "Times New Roman" # set font
    show_instr.color = "black"           # font colour should be black
    
    # draw text:
    show_instr.draw()                    # draw image
    win.flip()                           # show image on screen
    

    
    
''' function for displaying words '''
# show text stimulus centered on screen 
# --> ends on button press (Space)
# --> records button press of buttons "c" or "m" (depending on handedness)
# input arguments: text to display
# optional: font size & font colour

def displ_word(word, colour, target, nback_cond = None):
    
    # create text stimulus object
    global text_stim  
    text_stim = visual.TextStim(win, text = word, font = "Times New Roman", color = colour)
    # show object in window
    text_stim.draw()                    # draw image
    win.flip()                          # show image on screen
    
    # send word onset trigger to lsl stream
    marker_text = "dual_main_" + nback_cond + "_" + word + "_" + colour + "_" + str(target)
    #out_marker.push_sample(["WORD_ONSET_" + marker_text]) # send scaling factor
    
    # wait for about 50 ms before participant is allowed to react 
    # (50 ms should be about 3 frames with a frame rate of 60 Hz aka 16.667 ms / cycle)



""" function for n-back task response (key: c)""" 
def target_response(win, nback_cond, word, colour, target, target_button):
    pass


""" function for going to the next stimulus (key: Space)""" 
def next_word(nback_cond, word, colour, target, target_detected):
    pass
    



def dual_task_trial(nback_cond, word, colour, target, target_button):

    # nback_con = which n-back condition we have in this block, can be either 1-back or 2-back 
    # word = which word to display
    # colour = which font colour the current word should have
    # target = is the current trial an n-back target trial?
    # target_button = which button should the participant press to indicate they saw an n-back target?
    
    
    """ Send marker to indicate the onset of the trial (aka word onset) """
    # create a marker that tells us which condition, colour, & word we have in this trial
    # and whether the trial was a target trial
    marker_text = "dual_main_" + nback_cond + "_" + word + "_" + colour + "_" + str(target)
    #out_marker.push_sample(["WORD_ONSET_" + marker_text]) 
    
    # show word
    # end if Space button was pressed & record duration
    #presTextPsychoPy(word)
    
    
    # reset trial timer
    #timer.reset()
    #countdownTimer = core.CountdownTimer(dur_trial)
    

    # reset input buffer from serial port
    #ser.reset_input_buffer()
    #c = 0 # init buffer for serial port reset
    
    # send trial onset marker to lsl
    #out_marker.push_sample(['trial_start_sf_{}'.format(scl_fctr_fdbck)]) # send scaling factor
    
    
    """ Send marker to indicate the offset of the trial (aka word offset) """
    #out_marker.push_sample(['end_trial']) # send 1 for start of fixation cross
    

