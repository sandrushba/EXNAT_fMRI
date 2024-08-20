#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Instructions, Texts & MC questions for EXNAT_3_fMRI study

Author: Sandra Martin
Version: July 2024

"""

""" Instructions """

# for each block, set instruction texts + path to instruction image you want to show:
instr_pic_path = "Stimuli_and_Resources/EXNAT3_Instr_Pics/"

welcome_text = "Herzlich willkommen zum Experiment!\n\nBitte bleiben Sie ruhig liegen. Es geht gleich los."

instr_Reading_Baseline_main_no_click = "LESEN\n\n\nIm " \
                                       "folgenden Block lesen Sie einen Text. Die Wörter werden " \
                                       "von allein abgespielt.\n\nAm Ende des Texts werden Ihnen Fragen zum Inhalt " \
                                       "gestellt. Wählen Sie mithilfe der vier Tasten die richtige Antwort aus."

instr_Reading_pseudotext_no_click = "LESEN\n\n\n" \
                                       "Nun folgt ein Block mit Wörtern, die es gar nicht gibt.\n\n" \
                                        "Bitte lesen Sie den Text dennoch aufmerksam mit. Sie müssen sonst nichts tun."

instr_1back_single_main_no_click = "1-ZURÜCK\n\n\nIm folgenden Block werden " \
                                 "farbige Rechtecke abgespielt." \
                                 "\n\nBitte drücken Sie so schnell wie möglich mit dem Zeigefinger, wenn die Farbe des " \
                                 "aktuellen Rechtecks mit der des vorherigen Rechtecks (1 zurück) übereinstimmt."
instr_pic_1back_single_main_no_click = instr_pic_path + "1back_rect_fMRI.png"

instr_1back_dual_main_no_click = "LESEN MIT 1-ZURÜCK\n\n\nIm folgenden Block lesen Sie wieder einen Text. " \
                                 "\n\nBitte drücken Sie so schnell wie möglich mit dem Zeigefinger, wenn die Farbe des " \
                                 "aktuellen Worts mit der des vorherigen Worts (1 zurück) übereinstimmt."
instr_pic_1back_dual_main_no_click = instr_pic_path + "1back_fMRI.png"

instr_2back_single_main_no_click = "2-ZURÜCK\n\n\nIm folgenden Block werden " \
                                 "farbige Rechtecke abgespielt." \
                                 "\n\nBitte drücken Sie so schnell wie möglich mit dem Zeigefinger, wenn die Farbe des " \
                                 "aktuellen Rechtecks mit der des vorletzten Rechtecks (2 zurück) übereinstimmt."
instr_pic_2back_single_main_no_click = instr_pic_path + "2back_rect_fMRI.png"

instr_2back_dual_main_no_click = "LESEN MIT 2-ZURÜCK\n\n\nIm folgenden Block lesen Sie wieder einen Text. " \
                                 "\n\nBitte drücken Sie so schnell wie möglich mit dem Zeigefinger, wenn die Farbe des " \
                                 "aktuellen Worts mit der des vorletzten Worts (2 zurück) übereinstimmt."
instr_pic_2back_dual_main_no_click = instr_pic_path + "2back_fMRI.png"

# warning sign for change of task:
warning_sign = instr_pic_path + "warning.jpeg"

""" Main Blocks: """

# Giant Squid
# global text_01
text_01 = ["Beim", "Anblick", "der", "Tiere", "wird", "klar,", "warum", "die", "Seeleute", "vergangener",
           "Jahrhunderte", "Angst", "vor", "Seeungeheuern", "hatten.", "Meterlange", "Fangarme,", "spitze", "Mäuler",
           "und", "riesige", "Augen", "verleihen", "den", "großen", "Kalmaren", "ein", "furchterregendes", "Aussehen.",
           "Vor", "der", "Küste", "Chiles", "sind", "sie", "aktuell", "in", "Massen", "zu", "sehen.", "Hunderte", "von",
           "riesigen", "Tintenfischen", "schwimmen", "in", "den", "flachen", "Gewässern", "und", "fressen", "dort",
           "die", "Fische.", "Normalerweise", "sind", "die", "großen", "Kalmare", "nur", "schwer", "zu", "beobachten.",
           "Sie", "leben", "eigentlich", "im", "offenen", "Meer.", "Nur", "nachts", "kommen", "sie", "an", "die",
           "Oberfläche,", "um", "kleine", "Fische", "zu", "jagen.", "Seit", "zwei", "Wochen", "aber", "sind", "sie",
           "auch", "bei", "Tageslicht", "vor", "der", "Küste", "zu", "sehen.", "Zunächst", "wurden", "mehr", "als",
           "200", "Kalmare", "vor", "einer", "Insel", "vor", "Chile", "gesichtet.", "Später", "wurden", "dann",
           "weitere", "Kalmare", "an", "anderen", "Orten", "entlang", "der", "Küste", "Chiles", "beobachtet.", "Vor",
           "allem", "für", "die", "Fischer", "ist", "das", "ärgerlich.", "Die", "Kalmare", "fressen", "Hechte,",
           "Sardinen", "und", "Sardellen.", "Und", "sie", "haben", "großen", "Hunger -", "schlechte", "Karten", "für",
           "die", "kleineren", "Fische.", "Die", "Kalmare", "selbst", "haben", "hingegen", "Glück:", "Sie", "gelten",
           "zwar", "in", "manchen", "Ländern", "als", "Delikatesse,", "werden", "in", "Chile", "jedoch", "nicht",
           "gegessen.", "Meeresbiologen", "standen", "wegen", "des", "plötzlichen", "Erscheinens", "der", "Kalmare",
           "zunächst", "vor", "einem", "großen", "Rätsel.", "Nun", "ist", "jedoch", "klar,", "weshalb", "die",
           "Kalmare", "plötzlich", "auftauchten.", "Im", "Februar", "erwärmte", "sich", "das", "Meer", "verglichen",
           "mit", "den", "Temperaturen", "in", "den", "Vorjahren", "ungewöhnlich", "stark.", "Es", "sammelten", "sich",
           "viele", "kleine", "Fische", "vor", "der", "Küste.", "Die", "Kalmare", "wurden", "dadurch", "magisch",
           "angezogen.", "Die", "kleinen", "Fische", "bedeuten", "für", "sie", "reiche", "Beute.", "Für", "Forscher",
           "ist", "das", "ein", "besonderer", "Glücksfall.", "Normalerweise", "sind", "die", "großen", "Kalmare", "so",
           "schwer", "vor", "die", "Kamera", "zu", "bekommen,", "dass", "Forscher", "teilweise", "auf", "seltsame",
           "Ideen", "kommen.", "Ein", "Biologe", "aus", "Neuseeland", "etwa", "will", "versuchen,", "den", "legendären",
           "Riesenkalmar", "mit", "Sexualhormonen", "vor", "die", "Linse", "zu", "locken.", "Der", "Riesenkalmar",
           "ist", "mit", "bis", "zu", "20", "Metern", "Länge", "und", "einer", "halben", "Tonne", "Gewicht", "das",
           "größte", "wirbellose", "Tier", "der", "Welt.", "Bisher", "wurde", "er", "aber", "noch", "nie", "innerhalb",
           "seines", "natürlichen", "Lebensraums", "gefilmt."]

text_01_Q1 = "Wieso tauchten 2004 vor der Küste Chiles auf einmal hunderte Kalmare auf?"
text_01_Q1_ans = ["1) Sie wurden nicht mehr befischt.",
                  "2) Sie hatten kaum noch natürliche Fressfeinde.",
                  "3) Sie folgten kleinen Beutefischen vor die Küste.",
                  "4) Sie wurden von Meeresbiologen ausgewildert."]
text_01_Q1_corr = "c"

text_01_Q2 = "Wie möchte der Biologe die Kalmare zu seiner Kamera locken?"
text_01_Q2_ans = ["1) mit niederfrequenten Tönen", "2) mit Heringen", "3) mit Wärmestrahlern", "4) mit Sexualhormonen"]
text_01_Q2_corr = "d"

text_01_Q3 = "Wie groß sind die Kalmare?"
text_01_Q3_ans = ["1) 20 m", "2) 15 m", "3) 10 m", "4) 5 m"]
text_01_Q3_corr = "a"

# Hemingway / The old man and the sea
# global text_02
text_02 = ["Zwanzig", "Jahre", "verbrachte", "Ernest", "Hemingway", "auf", "Kuba.", "Die", "meiste", "Zeit", "davon",
           "lebte", "er", "in", "Vigía,", "seinem", "legendären", "Haus", "vor", "den", "Toren", "Havannas.", "Seit",
           "seinem", "Tod", "Anfang", "der", "1960er", "lagern", "in", "Vigía", "etwa", "3000", "Manuskripte", "des",
           "Autors.", "In", "den", "vergangenen", "Jahren", "sind", "sie", "nach", "und", "nach", "digitalisiert",
           "worden.", "Nun", "will", "man", "sie", "zunächst", "in", "Kuba", "zeigen,", "bevor", "sie", "dann", "der",
           "Bibliothek", "von", "Boston", "übergeben", "werden.", "Die", "Leiterin", "des", "Archivs", "in", "Vigía",
           "sagte", "am", "Montag", "im", "kubanischen", "Fernsehen,", "es", "handele", "sich", "um", "bisher",
           "unveröffentlichte", "Stücke.", "Die", "Digitalisierung", "war", "zwischen", "den", "USA", "und", "Kuba",
           "bereits", "2002", "vereinbart", "worden.", "Damals", "berichtete", "die", "\"New", "York", "Times\",",
           "unter", "den", "Dokumenten", "befänden", "sich", "Texte,", "die", "auf", "lose", "Blätter", "und",
           "Buchrücken", "gekritzelt", "worden", "seien.", "Dies", "seien", "vor", "allem", "Briefe,", "Entwürfe",
           "und", "Aufzeichnungen", "zu", "Hemingways", "großen", "Romanen.", "Der", "Biograf", "Hemingways", "nannte",
           "den", "gesamten", "Nachlass", "eine", "\"Computertomografie", "von", "Hemingways", "Gehirn\".", "In",
           "Kuba", "schrieb", "Hemingway", "unter", "anderem", "seine", "berühmte", "Novelle", "\"Der", "alte", "Mann",
           "und", "das", "Meer\".", "Die", "Novelle", "handelt", "vom", "Kampf", "eines", "alten", "Fischers", "mit",
           "einem", "riesigen", "Schwertfisch.", "Zwei", "Tage", "und", "zwei", "Nächte", "ringt", "der", "Fischer",
           "mit", "dem", "Schwertfisch,", "bis", "er", "ihn", "schließlich", "am", "dritten", "Tag", "überwältigen",
           "kann.", "Da", "der", "Fisch", "zu", "groß", "ist,", "um", "ihn", "ins", "Boot", "zu", "ziehen,", "bindet",
           "er", "ihn", "von", "außen", "ans", "Boot.", "Das", "Blut", "des", "Schwertfisches", "lockt", "auf", "der",
           "Heimfahrt", "jedoch", "Haie", "an.", "Die", "Haie", "fressen", "nach", "und", "nach", "Teile", "des",
           "Schwertfischs,", "sodass", "dem", "Fischer", "nur", "das", "Skelett", "bleibt,", "als", "er", "wieder",
           "in", "den", "Heimathafen", "zurückkehrt.", "Die", "Figur", "des", "Fischers", "ist", "vermutlich",
           "angelehnt", "an", "den", "Fischer", "Gregorio", "Fuentes,", "der", "sich", "auf", "Kuba", "um",
           "Hemingways", "Boot", "kümmerte.", "Für", "sein", "Werk", "wurde", "Hemingway", "mit", "dem",
           "Literaturnobelpreis", "ausgezeichnet.", "Die", "Nobelpreis-Medaille", "schenkte", "er", "aus",
           "Verbundenheit", "zu", "Kuba", "der", "Wallfahrtskirche", "der", "barmherzigen", "Jungfrau", "von", "Cobre.",
           "Sie", "ist", "die", "Schutzpatronin", "Kubas.", "Die", "Medaille", "ist", "auch", "heute", "noch", "in",
           "der", "Kirche", "zu", "sehen."]

text_02_Q1 = "Wem schenkte Hemingway seine Nobelpreis-Medaille?"
text_02_Q1_ans = ["1) seiner Frau Mary", "2) seiner Lieblingsbar “Sloppy Joe’s” in Florida",
                  "3) einer Wallfahrtskirche auf Kuba", "4) dem Fischer Gregorio Fuentes"]
text_02_Q1_corr = "c"

text_02_Q2 = "Wie heißt Hemingways Wohnhaus auf Kuba?"
text_02_Q2_ans = ["1) Vigia", "2) Baluarte", "3) Almeneas", "4) Fortaleza"]
text_02_Q2_corr = "a"

text_02_Q3 = "Als was bezeichnet der Biograf Andrew Berg den Nachlass Hemingways?"
text_02_Q3_ans = ["1) als ein Röntgenbild von Hemingways Seele", "2) als ein MRT von Hemingways Geist",
                  "3) als eine Computertomografie von Hemingways Gehirn", "4) als ein Ultraschall von Hemingways Herz"]
text_02_Q3_corr = "c"

# Einstein
text_03 = ["Sie", "besuchte", "ihn", "oft", "in", "seinem", "Haus", "und", "bekam", "Briefe", "und", "Gedichte", "von",
           "ihm.", "Manchmal", "durfte", "sie", "ihm", "sogar", "die", "Haare", "schneiden.", "Johanna", "Fantova",
           "galt", "als", "letzte", "Freundin", "von", "Albert", "Einstein.", "Die", "beiden", "trafen", "sich",
           "regelmäßig,", "telefonierten", "viel", "und", "gingen", "miteinander", "segeln.", "Nun", "wurde",
           "bekannt,", "was", "offenbar", "nicht", "einmal", "Einstein", "wusste:", "Johanna", "Fantova", "fertigte",
           "Notizen", "über", "den", "Inhalt", "ihrer", "Gespräche", "an.", "In", "ihren", "Aufzeichnungen", "zeigt",
           "sie", "ihn", "nicht", "als", "den", "großen", "Mann,", "der", "zu", "Lebzeiten", "zur", "Legende", "wurde,",
           "sondern", "als", "Einstein,", "den", "Menschenfreund.", "Die", "Nachwelt", "dürfte", "ihr", "dankbar",
           "sein.", "Ohne", "die", "Notizen", "wüssten", "wir", "heute", "nichts", "von", "Bibo,", "dem", "traurigen",
           "Papagei.", "Auch", "eine", "ganze", "Reihe", "kluger", "und", "lustiger", "Zitate", "von", "Einstein",
           "wären", "verloren", "gegangen.", "Es", "ist", "bisher", "das", "einzige", "bekannte", "Tagebuch", "von",
           "einer", "Person,", "die", "während", "seiner", "letzten", "Jahre", "eng", "mit", "Einstein", "befreundet",
           "war.", "Die", "22", "Jahre", "jüngere", "Johanna", "Fantova", "stammte", "wie", "Einstein", "aus",
           "Europa.", "Die", "Eltern", "ihres", "Ehemannes", "Otto", "Fanta", "empfingen", "vor", "dem", "Krieg",
           "viele", "berühmte", "Gäste", "in", "ihrem", "Salon.", "Neben", "Einstein", "zählte", "dazu", "auch",
           "Franz", "Kafka.", "Johanna", "Fantova", "war", "für", "Einstein", "daher", "ein", "Teil", "der", "alten",
           "Welt.", "Sie", "war", "eine", "Verbindung", "zu", "Dingen,", "die", "er", "vermisste.", "In", "Fantovas",
           "Manuskript", "erscheint", "Einstein", "als", "komischer", "Eigenbrötler.", "Zugleich", "beschreibt", "sie",
           "ihn", "aber", "auch", "als", "Menschenfreund,", "der", "vielen", "seiner", "Freunde", "bei", "persönlichen",
           "Problemen", "half.", "Und", "doch", "fühlte", "sich", "Einstein", "nie", "wirklich", "mit", "seinen",
           "Mitmenschen", "verbunden.", "Angesichts", "seiner", "eigenen", "gescheiterten", "Beziehungen",
           "betrachtete", "er", "die", "Beziehungen", "seiner", "Freunde", "mit", "spöttischer", "Distanz:", "\"Ich",
           "war", "bei", "einem", "Nachbarn.", "Es", "besteht", "die", "Gefahr,", "dass", "sein", "Sohn", "heiratet.\"",
           "Rührend", "kümmerte", "er", "sich", "dagegen", "um", "sein", "Haustier,", "einen", "deprimierten",
           "Papagei", "namens", "Bibo.", "\"Der", "Papagei", "ist", "noch", "ganz", "verschüchtert.", "Er", "kam",
           "mit", "der", "Post.\"", "Einstein", "schritt", "sofort", "zur", "Tat.", "Der", "Erfolg", "blieb", "jedoch",
           "leider", "aus:", "\"Der", "Papagei", "ist", "traurig.", "Ich", "versuche", "ihn", "aufzuheitern,", "aber",
           "er", "versteht", "leider", "meine", "Witze", "nicht.\""]

text_03_Q1 = "Wie hieß der Ehemann von Einsteins Freundin Johanna?"
text_03_Q1_ans = ["1) Hans Spreit", "2) Franz Kolar", "3) Kurt Lift", "4) Otto Fanta"]
text_03_Q1_corr = "d"

text_03_Q2 = "Welches Haustier hatte Einstein?"
text_03_Q2_ans = ["1) verschüchterten Papagei", "2) lethargischen Kater", "3) depressive Schildkröte",
                  "4) taubstummen Kanarienvogel"]
text_03_Q2_corr = "a"

text_03_Q3 = "Wen luden die Eltern von Johannas Ehemann neben Einstein noch in ihren Salon ein?"
text_03_Q3_ans = ["1) Franz Kafka", "2) Robert Oppenheimer", "3) Theodor W. Adorno", "4) Werner Heisenberg"]
text_03_Q3_corr = "a"

# Batman's Joker
text_04 = ["Jerry", "Robinson", "war", "erst", "17,", "als", "er", "die", "wichtigste", "Entscheidung", "seines",
           "Lebens", "traf -", "und", "möglicherweise", "seinen", "größten", "Fehler", "beging.", "Statt", "wie",
           "geplant", "aufs", "College", "zu", "gehen,", "ließ", "er", "sich", "von", "einem", "Mann", "namens", "Bob",
           "Kane", "als", "Zeichner", "engagieren.", "Kane", "hatte", "gerade", "die", "Zeichnungen", "für", "ein",
           "Comicheft", "abgeliefert,", "in", "dem", "er", "eine", "völlig", "neue", "Figur", "auftreten", "ließ,",
           "genannt", "\"Batman\".", "Jetzt", "machte", "er", "Urlaub", "in", "den", "Poconos,", "einem",
           "Ausflugsgebiet", "in", "Pennsylvania.", "Der", "untergewichtige", "Jerry", "Robinson", "war", "auf",
           "einer", "Kur", "dort,", "um", "Gewicht", "zuzulegen.", "Um", "Bob", "Kane", "von", "seinem", "Talent",
           "als", "Zeichner", "zu", "überzeugen,", "fertigte", "Jerry", "Robinson", "für", "ihn", "ein", "paar",
           "Zeichnungen", "an.", "Da", "er", "kein", "Papier", "zur", "Hand", "hatte,", "zeichnete", "er", "kurzerhand",
           "auf", "seiner", "Jacke.", "Beeindruckt", "stellte", "Kane", "den", "Jungen", "an.", "Bereits", "ab", "der",
           "dritten", "Ausgabe", "der", "Batman-Comics", "war", "er", "der", "Hauptzeichner", "der", "Serie.", "Seine",
           "Zeichnungen", "fertigte", "er", "vor", "allem", "nachts", "an.", "Tagsüber", "studierte", "er",
           "Journalistik", "in", "New", "York.", "Neben", "dem", "Zeichnen", "tat", "er", "sich", "auch", "bei", "der",
           "Entwicklung", "der", "Figuren", "hervor.", "Von", "ihm", "stammten", "die", "Entwürfe", "für", "Batmans",
           "Butler", "Alfred", "und", "Batmans", "Helfer,", "den", "jungen", "Robin.", "Fast", "zeitgleich", "hatte",
           "der", "Joker,", "Batmans", "Erzfeind,", "seinen", "ersten", "Auftritt", "in", "einem", "weiteren", "Heft.",
           "Robinson", "behauptete", "später,", "die", "Idee", "zur", "Figur", "des", "Jokers", "sei", "von", "ihm",
           "ausgegangen.", "Inspiriert", "wurde", "er", "dabei", "durch", "ein", "Kartenspiel,", "das", "seine",
           "Kollegen", "immer", "zur", "Hand", "hatten.", "Laut", "Bob", "Kane", "beruht", "der", "Entwurf", "des",
           "Schurken", "dagegen", "auf", "einer", "Szene", "aus", "einem", "Stummfilm.", "\"Robinson", "hatte",
           "nichts", "damit", "zu", "tun\",", "war", "sein", "drastisches", "Urteil.", "Hier", "rächte", "es", "sich,",
           "dass", "Jerry", "Robinson", "lediglich", "als", "Assistent", "engagiert", "war,", "auch", "wenn", "er",
           "der", "Hauptzeichner", "war.", "Kane", "dagegen", "hatte", "sich", "alle", "Rechte", "an", "den", "Figuren",
           "zugesichert.", "Nicht", "zuletzt", "deshalb", "begann", "Jerry", "Robinson", "ab", "1940", "nicht", "mehr",
           "für", "Kane,", "sondern", "für", "den", "Comic-Verlag", "direkt", "zu", "arbeiten.", "In", "dessen",
           "Studio", "saß", "er", "zeitweise", "neben", "\"Superman\"-Miterfinder", "Joe", "Shuster", "am",
           "Zeichentisch."]

text_04_Q1 = "Warum war Jerry Robinson 1939 in den Poconos?"
text_04_Q1_ans = ["1) für einen Alkohol-Entzug", "2) Erholung von einer Lungenentzündung",
                  "3) zum Abnehmen", "4) zum Zunehmen"]
text_04_Q1_corr = "d"

text_04_Q2 = "Was studierte Jerry Robinson neben seiner Tätigkeit als Comiczeichner?"
text_04_Q2_ans = ["1) Journalistik", "2) Grafikdesign", "3) Kunstgeschichte", "4) Modedesign"]
text_04_Q2_corr = "a"

text_04_Q3 = "Die Idee zu welcher Figur stammt angeblich von Jerrry Robinson?"
text_04_Q3_ans = ["1) Catwoman", "2) Bane", "3) der Joker", "4) Harley Quinn"]
text_04_Q3_corr = "c"

# tiny chameleons
# global text_05
text_05 = ["Die", "Korallenriffe", "und", "die", "sandigen", "Buchten", "sind", "perfekt", "für", "jede",
           "Urlaubsbroschüre.", "Insgesamt", "ist", "die", "Inselgruppe", "namens", "Nosy", "Hara", "vor", "Madagaskar",
           "aber", "doch", "recht", "karg.", "In", "dieser", "eher", "lebensfeindlichen", "Umgebung", "haben",
           "Biologen", "nun", "eine", "neue", "Tierart", "entdeckt:", "Das", "winzige", "Chamäleon", "Brookesia",
           "micra.", "Von", "der", "Schnauze", "bis", "zum", "Schwanzende", "misst", "es", "weniger", "als", "drei",
           "Zentimeter.", "Farblich", "machen", "die", "braunen", "Tierchen", "wenig", "her.", "Doch", "ihre",
           "winzige", "Körpergröße", "fasziniert", "die", "Forscher.", "\"Das", "ist", "nichts,", "wo", "man", "viele",
           "Untersuchungen", "machen", "muss.", "Man", "erkennt", "auch", "so,", "dass", "das", "etwas", "Neues",
           "ist\",", "sagt", "Miguel", "Vences.", "Der", "Zoologe", "berichtet", "in", "einem", "Fachartikel", "gleich",
           "von", "vier", "neuen", "Arten", "von", "Mini-Chamäleons.", "Laut", "den", "Forschern", "weiß", "man", "von",
           "den", "Tieren", "jedoch", "kaum", "mehr,", "als", "dass", "es", "sie", "gibt.", "Zu", "ihrer",
           "Lebensweise", "ist", "nur", "sehr", "wenig", "bekannt.", "Tagsüber", "leben", "die", "kleinen",
           "Chamäleons", "am", "Boden.", "Wenn", "möglich", "verbergen", "sie", "sich", "dabei", "unter", "einer",
           "Schicht", "Laub.", "Nachts", "geht", "es", "dann", "auf", "niedrig", "gelegene", "Äste", "zum", "Schlafen.",
           "Direkte", "Fressfeinde", "haben", "die", "Tierchen", "allerdings", "wohl", "eher", "nicht.", "Zu", "ihrem",
           "Glück,", "so", "die", "Forscher.", "Auf", "solchen", "kleinen", "Inseln", "kann", "die", "Konkurrenz",
           "zwischen", "den", "Tierarten", "schnell", "sehr", "groß", "werden.", "Auch", "die", "anderen", "neuen",
           "Chamäleon-Arten", "besiedeln", "nur", "kleine", "Gebiete", "auf", "Madagaskar.", "Durch", "die",
           "Zerstörung", "ihres", "Lebensraums", "sind", "sie", "jedoch", "besonders", "bedroht.", "Rund", "40",
           "Prozent", "der", "Reptilien-Arten", "auf", "Madagaskar", "gelten", "mittlerweile", "als", "gefährdet.",
           "Die", "Forscher", "befürchten,", "dass", "auch", "Brookesia", "tristis,", "eine", "weitere", "neu",
           "entdeckte", "Art,", "einer", "ungewissen", "Zukunft", "entgegen", "sieht.", "Zwar", "ist", "der",
           "Lebensraum", "des", "Chamäleons", "vor", "wenigen", "Jahren", "unter", "Schutz", "gestellt", "worden,",
           "doch", "die", "Abholzung", "des", "Gebiets", "hat", "seitdem", "leider", "sogar", "noch", "zugenommen.",
           "Mit", "der", "Wahl", "der", "Namen", "der", "neu", "entdeckten", "Chamäleon-Arten", "wollen", "sie", "auf",
           "die", "große", "Gefahr", "hinweisen,", "die", "den", "Chamäleons", "droht.", "Die", "Botschaft", "hinter",
           "den", "Namen", "Brookesia", "desperata", "und", "Brookesia", "tristis", "versteht", "man", "auch", "ohne",
           "Latein", "zu", "können:", "Desperata", "heißt", "verzweifelt", "und", "tristis", "so", "viel", "wie",
           "traurig."]

text_05_Q1 = "Wo liegt die kleine Inselgruppe, auf der die Chamäleons entdeckt wurden?"
text_05_Q1_ans = ["1) vor Sri Lanka", "2) vor Thailand", "3) vor Madagaskar", "4) vor Java"]
text_05_Q1_corr = "c"

text_05_Q2 = "Was haben die lateinischen Namen der neuentdeckten Chamäleons gemeinsam?"
text_05_Q2_ans = ["1) Sie sind nach Forschern benannt.",
                  "2) Sie beinhalten das Wort \"klein\".",
                  "3) Sie beinhalten negative Wörter wie \"verzweifelt\".",
                  "4) Sie basieren auf Pflanzennamen."]
text_05_Q2_corr = "c"

text_05_Q3 = "Wo verstecken sich die Chamäleons tagsüber?"
text_05_Q3_ans = ["1) unter Mangroven-Wurzeln", "2) unter Laub", "3) in Felsnischen",
                  "4) unter morschen Baumstämmen"]
text_05_Q3_corr = "b"

# Mauritius
# global text_06
text_06 = ["In", "den", "siebziger", "Jahren", "war", "Mauritius", "eine", "kleine", "Insel", "mitten", "im",
           "Indischen", "Ozean,", "die", "im", "Ausland", "niemand", "kannte.", "Heute", "ist", "sie", "dagegen",
           "weltweit", "als", "paradiesisches", "Urlaubsziel", "bekannt.", "Doch", "schon", "lange", "bevor", "die",
           "ersten", "Touristen", "kamen,", "war", "Mauritius", "in", "einigen", "Teilen", "der", "Welt", "sehr",
           "bekannt.", "Die", "Portugiesen", "waren", "die", "Ersten,", "die", "die", "Insel", "entdeckten.", "Sie",
           "nannten", "sie", "\"Schwaneninsel\",", "ließen", "sich", "aber", "nicht", "auf", "ihr", "nieder.", "Erst",
           "fast", "hundert", "Jahre", "später", "kamen", "die", "Holländer.", "Sie", "gaben", "der", "Insel", "zu",
           "Ehren", "des", "holländischen", "Prinzen", "Moritz", "den", "Namen", "\"Mauritius\".", "Den", "Namen",
           "Mauritius", "hat", "sie", "bis", "heute", "behalten.", "Die", "Holländer", "begannen,", "an", "der",
           "Küste", "Felder", "anzulegen.", "Sie", "brachten", "Zuckerrohr,", "Wild", "und", "Affen", "mit", "auf",
           "die", "Insel.", "Sie", "bauten", "Häuser", "und", "Festungen", "und", "holzten", "die", "dichten", "Wälder",
           "aus", "Ebenholz", "ab.", "Zu", "dieser", "Zeit", "lebten", "auf", "Mauritius", "noch", "viele", "Dodos.",
           "Die", "flugunfähigen", "Vögel", "hatten", "keine", "natürlichen", "Feinde", "auf", "der", "Insel", "und",
           "waren", "daher", "zu", "ihrem", "eigenen", "Unglück", "sehr", "zahm.", "Für", "die", "Holländer", "machte",
           "sie", "das", "zur", "perfekten", "Jagdbeute.", "Der", "Dodo", "wurde", "so", "stark", "bejagt,", "dass",
           "er", "schon", "einige", "Jahrzehnte", "nach", "Ankunft", "der", "Holländer", "vollständig", "ausgerottet",
           "war.", "Heute", "ist", "er", "das", "Nationalsymbol", "von", "Mauritius.", "Als", "kein", "Holz", "mehr",
           "zu", "holen", "und", "die", "Natur", "schwer", "geschädigt", "war,", "verließen", "die", "Holländer",
           "Mauritius.", "Um", "die", "Kontrolle", "der", "Insel", "brach", "ein", "erbitterter", "Krieg", "zwischen",
           "Briten", "und", "Franzosen", "aus.", "Aber", "wer", "lebt", "heute", "dort?", "Die", "Bevölkerung", "von",
           "Mauritius", "ist", "das", "Ergebnis", "einer", "Vermischung", "verschiedener", "Kulturen", "und",
           "Religionen.", "Viele", "der", "Menschen", "kamen", "nicht", "freiwillig.", "Die", "Holländer", "brachten",
           "afrikanische", "Sklaven", "mit", "auf", "die", "Insel.", "Aus", "Indien", "kamen", "Arbeiter", "für", "die",
           "Zuckerrohr-Plantagen", "und", "Handwerker,", "die", "beim", "Bau", "von", "Brücken", "und", "Straßen",
           "halfen.", "Zeitgleich", "mit", "den", "Indern", "kamen", "auch", "muslimische", "und", "chinesische",
           "Händler", "nach", "Mauritius. ", "Die", "Nachfahren", "von", "Indern,", "Franzosen,", "Chinesen,",
           "Arabern", "und", "afrikanischen", "Sklaven", "bilden", "heute", "auf", "Mauritius", "eine", "der",
           "wenigen", "echten", "multikulturellen", "Gesellschaften", "der", "Welt."]

text_06_Q1 = "Woher stammten die Seefahrer, die den Dodo ausrotteten?"
text_06_Q1_ans = ["1) Holland", "2) England", "3) Spanien", "4) Portugal"]
text_06_Q1_corr = "a"

text_06_Q2 = "Aus welchem Holz bestanden die Wälder der Insel?"
text_06_Q2_ans = ["1) Mangoholz", "2) Teakholz", "3) Ebenholz", "4) Mahagoni"]
text_06_Q2_corr = "c"

text_06_Q3 = "Wie lautete der erste Name der Insel, um die es im Text geht?"
text_06_Q3_ans = ["1) Schwaneninsel", "2) Kolibri-Insel", "3) Tukan-Insel", "4) Papageieninsel"]
text_06_Q3_corr = "a"

# Angkor Wat
# global text_07
text_07 = ["Wer", "Angkor", "sagt,", "meint", "in", "der", "Regel", "Angkor", "Wat.", "Die", "berühmte", "Tempelanlage",
           "wurde", "vermutlich", "vor", "knapp", "900", "Jahren", "in", "den", "Dschungel", "Kambodschas", "gebaut.",
           "Seit", "mehr", "als", "hundert", "Jahren", "hat", "sich", "die", "Wissenschaft", "auf", "die", "riesigen",
           "Tempelanlagen", "und", "ihre", "Inschriften", "konzentriert.", "Für", "die", "Lebensweise", "der",
           "Bewohner", "der", "Region", "hat", "sich", "hingegen", "kaum", "jemand", "interessiert.", "Das", "Team",
           "um", "den", "Forscher", "Damian", "Evans", "hat", "nun", "erstmals", "eine", "Karte", "von", "Angkor",
           "Wat", "erstellt.", "Die", "Karte", "zeigt,", "dass", "Angkor", "Wat", "eine", "richtige", "Stadt", "war,",
           "nicht", "nur", "eine", "kleine", "Tempelanlage.", "Die", "Forscher", "gehen", "davon", "aus,", "dass",
           "ihre", "Größe", "sogar", "New", "York", "übertroffen", "haben", "könnte.", "Damit", "ist",
           "\"Groß-Angkor\"", "die", "mit", "Abstand", "größte", "vorindustrielle", "Siedlung", "der", "Welt.",
           "Selbst", "die", "riesigen", "Städte", "der", "Maya", "erscheinen", "dagegen", "winzig.", "Die", "Forscher",
           "fanden", "außerdem", "heraus,", "dass", "Angkor", "eine", "hydraulische", "Stadt", "war.", "Dank", "eines",
           "komplizierten", "Bewässerungssystems", "konnten", "die", "mehr", "als", "eine", "Million", "Bewohner",
           "versorgt", "werden.", "Durch", "das", "riesige", "Netz", "aus", "Flüssen,", "Kanälen", "und", "Stauseen",
           "hat", "die", "mittelalterliche", "Stadt", "mehrmals", "im", "Jahr", "Reis", "ernten", "können.", "Das",
           "verschaffte", "den", "Bewohnern", "nicht", "nur", "volle", "Teller,", "sondern", "auch", "einen", "enormen",
           "Reichtum.", "Die", "Stadt", "umgab", "ein", "riesiges", "Geflecht", "aus", "Äckern,", "Häusern", "und",
           "Seen,", "das", "sich", "über", "mindestens", "tausend", "Quadratkilometer", "erstreckte.", "Auf", "dieser",
           "Fläche", "gibt", "es", "kaum", "einen", "Fleck,", "der", "nicht", "genutzt", "worden", "ist.", "Das",
           "Bewässerungsnetz", "war", "sogar", "dazu", "geeignet,", "den", "Reisanbau", "zu", "stärken.", "Für", "den",
           "Anbau", "von", "Reis", "braucht", "man", "jedoch", "extrem", "viel", "Wasser", "und", "riesige", "Flächen.",
           "Um", "die", "Felder", "und", "die", "künstlichen", "Seen,", "Flüsse", "und", "Kanäle", "anzulegen,",
           "mussten", "große", "Waldflächen", "gerodet", "werden.", "Mit", "der", "Zeit", "führte", "das",
           "wahrscheinlich", "zu", "riesigen", "Problemen", "wie", "Erdrutschen.", "Das", "gesamte", "System", "dürfte",
           "daher", "auch", "sehr", "empfindlich", "auf", "Naturkatastrophen", "reagiert", "haben.", "Insbesondere",
           "im", "Norden", "der", "Stadt", "fand", "man", "Spuren", "von", "hektischen", "Anpassungen", "und",
           "Deichbrüchen.", "Genaueres", "weiß", "man", "aber", "nicht.", "Die", "neue", "Karte", "der", "Stadt",
           "verrät", "aber", "zumindest,", "wo", "man", "nach", "Antworten", "suchen", "sollte."]

text_07_Q1 = "Wie groß war die Stadt Angkor Wat?"
text_07_Q1_ans = ["1) größer als New York", "2) größer als Tokyo", "3) größer als Delhi", "4) größer als São Paulo"]
text_07_Q1_corr = "a"

text_07_Q2 = "Wovon ernährten sich die Bewohner*innen Angkor Wats vornehmlich?"
text_07_Q2_ans = ["1) Hirse", "2) Linsen", "3) Reis", "4) Mais"]
text_07_Q2_corr = "c"

text_07_Q3 = "Warum ist Angkor Wat vermutlich untergegangen?"
text_07_Q3_ans = ["1) durch Massaker", "2) durch eine Hungersnot",
                  "3) durch die Pest", "4) durch Umweltzerstörung"]
text_07_Q3_corr = "d"

# Petra
# global text_08
text_08 = ["Ein", "solcher", "Anblick", "lässt", "selbst", "Indiana", "Jones", "Kinnlade", "herunterklappen:", "Nach",
           "einem", "spektakulären", "Ritt", "durch", "eine", "teils", "nur", "zwei", "Meter", "schmale", "Schlucht",
           "erhebt", "sich", "vor", "dem", "Filmhelden", "eine", "riesige", "Fassade.", "Die", "Szene", "aus", "dem",
           "Kinofilm", "machte", "die", "antike", "Felsenstadt", "Petra", "endgültig", "weltberühmt.", "Die",
           "prachtvolle", "Fassade", "ist", "eine", "der", "schönsten", "Bauten", "in", "der", "Felsenstadt", "mitten",
           "in", "der", "Wüste", "Jordaniens.", "Die", "Metropole", "war", "einst", "die", "Hauptstadt", "der",
           "Nabatäer.", "Zwei", "Jahrhunderte", "beherrschten", "die", "Nabatäer", "große", "Teile", "des", "Handels",
           "im", "Nahen", "Osten.", "So", "reich", "und", "mächtig", "wurde", "das", "Wüstenvolk,", "dass", "es",
           "sogar", "die", "Römer", "herausforderte.", "Doch", "wie", "ihre", "riesige", "Hauptstadt", "mitten", "in",
           "der", "Wüste", "funktioniert", "hat,", "weiß", "niemand", "genau.", "Sicher", "ist,", "dass", "die",
           "Stadt", "in", "atemberaubend", "kurzer", "Zeit", "entstand.", "Als", "die", "Nabatäer", "ins", "heutige",
           "Jordanien", "vordrangen,", "war", "die", "Region", "die", "reinste", "Goldgrube.", "Bei", "Petra",
           "kreuzten", "sich", "mehrere", "Handelswege,", "darunter", "die", "uralte", "Weihrauchstraße.", "Binnen",
           "weniger", "Jahrzehnte", "entstanden", "hunderte", "Höhlen", "mit", "prunkvollen", "Fassaden", "und",
           "teils", "gewaltigen", "Räumen.", "Von", "der", "eigentlichen", "Stadt", "ist", "heute", "nichts",
           "geblieben", "außer", "Steinhaufen", "und", "Mauerreste.", "Bis", "in", "die", "siebziger", "Jahre",
           "glaubte", "man", "daher,", "Petra", "sei", "eine", "Stadt", "für", "die", "Toten", "und", "die", "Götter",
           "gewesen,", "und", "die", "Menschen", "hätten", "woanders", "gewohnt.", "Aber", "Petra", "war", "eine",
           "ganz", "normale", "Stadt,", "nur", "an", "einem", "unmöglichen", "Ort.", "Die", "seltenen", "Regenfälle",
           "nutzten", "die", "Nabatäer", "mit", "einem", "genialen", "Bewässerungssystem.", "Überall", "in", "der",
           "Stadt", "waren", "Wasserbecken", "in", "den", "Fels", "geschlagen.", "Viele", "Kilometer",
           "Wasserleitungen", "leiteten", "das", "Wasser", "zuerst", "in", "die", "Speicher", "und", "von", "dort",
           "aus", "zu", "den", "Bewohnern.", "Die", "vielen", "Leitungen,", "die", "den", "Regen", "einst", "von",
           "den", "wertvollen", "Fassaden", "fernhielten,", "wurden", "von", "den", "Nabatäern", "dauernd", "instand",
           "gehalten.", "Doch", "wenn", "es", "jetzt", "regnet,", "strömt", "das", "Wasser", "unkontrolliert", "die",
           "Fassaden", "herab.", "Für", "den", "Sandstein", "ist", "das", "eine", "Katastrophe.", "Versuche", "zur",
           "Rettung", "der", "Fassaden", "gab", "es,", "doch", "wirklich", "erfolgreich", "war", "bislang", "leider",
           "keiner.", "Die", "antike", "Felsenstadt", "wird", "daher", "wohl", "eines", "Tages", "wieder", "zu", "Sand",
           "zerfallen."]

text_08_Q1 = "An welcher antiken Handelsroute lag die in Fels gehauene Wüstenstadt Petra?"
text_08_Q1_ans = ["1) an der Safranstraße", "2) an der Weihrauchstraße", "3) an der Seidenstraße",
                  "4) an der Kaschmirstraße"]
text_08_Q1_corr = "b"

text_08_Q2 = "Wie heißt das Wüstenvolk, um das es im Artikel geht?"
text_08_Q2_ans = ["1) Nabatäer", "2) Tuareg", "3) Beduinen", "4) Garamanten"]
text_08_Q2_corr = "a"

text_08_Q3 = "Was könnte dazu führen, dass Petra schon bald völlig zerstört sein könnte?"
text_08_Q3_ans = ["1) Massentourismus", "2) Sandstürme", "3) Grabräuberei", "4) Überschwemmungen"]
text_08_Q3_corr = "d"

# Shakespeare / Hamlet
# global text_09
text_09 = ["William", "Shakespeare", "war", "etwa", "fünf", "Jahre", "alt,", "als", "gar", "nicht", "weit", "entfernt",
           "von", "seinem", "Heimatdorf", "die", "nur", "zweijährige", "Jane", "Shaxspere", "ums", "Leben", "kam.",
           "Das", "kleine", "Mädchen", "wollte", "Ringelblumen", "pflücken,", "die", "am", "Ufer", "eines",
           "Mühlteichs", "wuchsen.", "Beim", "Blumenpflücken", "rutschte", "Jane", "aus,", "fiel", "ins", "Wasser",
           "und", "ertrank.", "William", "Shakespeare,", "der", "etwa", "20", "Kilometer", "entfernt", "im", "Dorf",
           "Stratford-upon-Avon", "aufwuchs,", "sollte", "später", "zum", "größten", "Dramatiker", "aller", "Zeiten",
           "heranwachsen.", "Forscher", "der", "Universität", "von", "Oxford", "vermuten", "nun", "einen",
           "Zusammenhang", "dieses", "Unfalls", "mit", "Shakespeares", "Stück", "\"Hamlet\".", "Eine", "Nebenhandlung",
           "des", "Stücks", "erzählt", "die", "Geschichte", "der", "fiktiven", "Edeldame", "Ophelia,", "der", "Tochter",
           "eines", "Kämmerers.", "Ophelia", "wächst", "am", "dänischen", "Königshof", "auf,", "wo", "sie", "die",
           "Geliebte", "des", "Prinzen", "Hamlet", "wird.", "Ihre", "Beziehung", "wird", "von", "ihrem", "Vater", "und",
           "ihrem", "Bruder", "jedoch", "missbilligt.", "Sie", "bezweifeln,", "dass", "Hamlet", "die", "ehrliche",
           "Absicht", "hat,", "Ophelia", "zu", "heiraten.", "Als", "Hamlet", "aus", "Versehen", "Ophelias", "Vater",
           "tötet,", "verzweifelt", "sie", "und", "erleidet", "ein", "ähnliches", "Schicksal", "wie", "die", "kleine",
           "Jane.", "Beim", "Blumenpflücken", "an", "einem", "Bachufer", "verliert", "sie", "das", "Gleichgewicht",
           "und", "fällt", "in", "den", "Bach.", "Ihr", "Kleid", "saugt", "sich", "mit", "Wasser", "voll", "und",
           "zieht", "sie", "wie", "ein", "Gewicht", "nach", "unten.", "Ob", "ihr", "Tod", "ein", "Unfall", "ist",
           "oder", "sie", "sich", "mit", "Absicht", "nicht", "aus", "dem", "Wasser", "rettet,", "wird", "im", "Stück",
           "offengelassen.", "Die", "erstaunliche", "Verbindung", "zwischen", "realen", "Ereignissen", "und",
           "Shakespeares", "\"Hamlet\"", "fiel", "Historikern", "auf,", "als", "sie", "alte", "medizinische", "Akten",
           "untersuchten.", "Die", "Ähnlichkeit", "der", "Nachnamen", "könnte", "sogar", "darauf", "hinweisen,", "dass",
           "William", "und", "Jane", "Verwandte", "gewesen", "sein", "könnten.", "Feste", "Schreibweisen", "von",
           "Namen", "gab", "es", "zu", "Shakespeares", "Zeiten", "nicht.", "Für", "eine", "der", "Forscherinnen", "aus",
           "Oxford", "ist", "dieses", "Detail", "aber", "nicht", "entscheidend:", "\"Selbst", "wenn", "sie", "nicht",
           "verwandt", "gewesen", "sind,", "hat", "sich", "die", "Geschichte", "durch", "die", "Ähnlichkeit", "der",
           "Namen", "vielleicht", "in", "Shakespeares", "Kopf", "verankert.\"", "Neben", "historischen", "Grundlagen",
           "seien", "Shakespeares", "Stücke", "auch", "von", "Klatsch", "und", "Tratsch-Geschichten", "beeinflusst",
           "worden.", "Dazu", "könnte", "auch", "die", "Geschichte", "über", "den", "Tod", "von", "Jane", "Shaxspere",
           "gezählt", "haben."]

text_09_Q1 = "Welches Stück von Shakespeare wurde womöglich von einem Unfall inspiriert?"
text_09_Q1_ans = ["1) Othello", "2) King Lear", "3) Hamlet", "4) Macbeth"]
text_09_Q1_corr = "c"

text_09_Q2 = "Wie hieß das Mädchen, um das es im Artikel geht?"
text_09_Q2_ans = ["1) Rosalind Shaxspere", "2) Ann Shaxspere", "3) Viola Shaxspere", "4) Jane Shaxspere"]
text_09_Q2_corr = "d"

text_09_Q3 = "Wie alt war Shakespeare, als das Unglück passierte?"
text_09_Q3_ans = ["1) ca. 5 Jahre", "2) ca. 10 Jahre", "3) ca. 15 Jahre", "4) ca. 20 Jahre"]
text_09_Q3_corr = "a"

# Heavy Metal in Jordan
# global text_10
text_10 = ["Von", "außen", "ist", "nichts", "zu", "sehen.", "Nur", "eine", "weiße", "Wand", "und", "eine", "grüne",
           "Tür", "aus", "Eisen.", "Adnan", "sperrt", "die", "Tür", "auf:", "\"Geht", "einfach", "die", "Treppe",
           "runter,", "dann", "seid", "ihr", "im", "Probenraum\",", "sagt", "er.", "Er", "schließt", "die", "Tür",
           "sorgfältig", "hinter", "sich", "ab:", "\"Vor", "einiger", "Zeit", "war", "jemand", "vom", "Geheimdienst",
           "hier.", "Seitdem", "sind", "wir", "vorsichtiger", "geworden.\"", "Für", "einen",
           "kurzen", "Moment", "ist", "man", "sich", "nicht", "sicher,", "ob", "es", "als", "Witz", "gemeint", "ist.",
           "\"Wir", "spielen", "Heavy", "Metal\",", "sagt", "Adnan.", "\"Das", "kann", "in", "unserem", "Land", "einen",
           "Haufen", "Ärger", "bedeuten.\"", "Denn", "wer", "in", "Jordanien", "laut", "Heavy", "Metal", "hört,",
           "kann", "dafür", "sogar", "im", "Gefängnis", "landen.", "Heavy", "Metal", "gibt", "es", "in", "arabischen",
           "Ländern", "noch", "nicht", "sehr", "lange:", "Die", "ersten", "Konzerte", "fanden",
           "in", "den", "neunziger", "Jahren", "statt,", "begleitet", "von", "Ärger", "mit", "der", "Polizei.", "Bei",
           "einer", "Razzia", "in", "Ägypten", "wurden", "damals", "rund", "70", "Jugendliche", "verhaftet.", "Die",
           "Polizei", "nahm", "alles", "mit,", "was", "ihnen", "verdächtig", "vorkam:", "Poster,", "CDs,", "sogar",
           "ein", "schwarzes", "T-Shirt", "mit", "Bugs-Bunny-Aufdruck.", "In", "Jordanien", "gab", "es", "schon",
           "länger", "keine", "Festnahmen", "mehr.",
           "\"Aber", "das", "liegt", "einfach", "daran,", "dass", "sie", "unsere", "Konzerte", "gleich", "verbieten\",",
           "sagt", "Adnan.", "\"Konzerte", "sind", "im", "Moment", "nur", "im", "Geheimen", "möglich.\"", "Doch",
           "trotz", "aller", "Probleme", "mit", "Geheimdienst", "und", "Polizei", "wächst", "die", "Metal-Szene", "in",
           "Jordanien.", "Was", "verboten", "ist,", "gewinnt", "an", "Reiz.", "Allerdings", "wächst", "mit", "der",
           "Metal-Szene", "auch", "das", "Misstrauen", "der", "Behörden.", "Wer",
           "sich", "dort", "nach", "den", "Heavy-Metal-Fans", "erkundigt,", "bekommt", "keine", "Antworten.", "Genauso",
           "sieht", "es", "auch", "bei", "der", "Polizei", "aus:", "Keiner", "möchte", "zuständig", "sein.", "\"Wir",
           "haben", "zwar", "nichts", "gegen", "die", "Musik,", "aber", "Satanismus", "ist", "verboten\",", "sagt",
           "schließlich", "einer", "der", "Polizisten.", "Der", "Frage,", "was", "Heavy", "Metal", "und", "Satanismus",
           "miteinander", "zu", "tun", "haben,", "weicht", "er", "aus.", "Adnan", "hat", "vor", "einiger",
           "Zeit", "versucht,", "die", "Polizei", "zu", "einem", "Konzert", "einzuladen.", "Er", "dachte,", "wenn",
           "die", "Polizisten", "mehr", "über", "sie", "wüssten,", "hätten", "sie", "auch", "keine", "Probleme", "mehr",
           "mit", "ihnen.", "Aber", "auf", "seinen", "Brief", "bekam", "er", "keine", "Antwort."]

text_10_Q1 = "In welchem Land ist Heavy Metal verboten?"
text_10_Q1_ans = ["1) Katar", "2) Jemen", "3) Jordanien", "4) Israel"]
text_10_Q1_corr = "c"

text_10_Q2 = "Wieso kommt es dort nicht mehr zu Festnahmen von Metal Fans?"
text_10_Q2_ans = ["1) die Polizei schaut weg", "2) Metal-Bands dürfen nicht mehr auftreten",
                  "3) Metal-Fans verstecken sich", "4) der Staat fürchtet Demonstrationen"]
text_10_Q2_corr = "b"

text_10_Q3 = "Was wurde bei einer Razzia in Ägypten konfisziert?"
text_10_Q3_ans = ["1) ein T-Shirt mit Scooby-Doo-Aufdruck", "2) ein T-Shirt mit Bugs-Bunny-Aufdruck",
                  "3) ein T-Shirt mit Spongebob-Aufdruck", "4) ein T-Shirt mit Donald-Duck-Aufdruck"]
text_10_Q3_corr = "b"

# Pseudotexts
pseudo_text_01 = ["Die", "agzuebte", "Gutdehmung", "eines", "gosher", "unbeninnten", "Polakauriers", "bebiesterte",
                  "Missenstrendler", "auf", "der", "vannen", "Felt,", "die", "sech", "zurehmensassen,", "um", "Taul",
                  "dieses", "roktenen", "laläettolagischen", "Uneimdisses", "zu", "seis.", "Aus", "asser", "Felt",
                  "strouten", "sie", "zurehmen,", "aufgeschüftet", "mit", "logernsten", "Gebüten", "und",
                  "Umzuchmehnen,", "um", "die", "meuwinierenden", "Öfermeste", "dieses", "spöfistorichten", "Megens",
                  "zu", "hunbeiren.", "In", "Guskatuten", "und", "Elikerhitaten", "feltweib", "önrogisierten",
                  "Pachsekte", "ärlendliche", "Rinträge", "und", "Datspusianen,", "um", "das", "Verstänkmas", "für",
                  "die", "nef", "entbaggte", "Psetier", "zu", "verzeinen.", "Tritz", "eikager", "Pereinjolderungen",
                  "bei", "der", "Aufflapung", "und", "Ifatöse", "torrten", "beide", "Missenstrendler", "hächtige",
                  "Umkerksbasse", "über", "die", "Rebehlbeile", "und", "Unauntian", "der", "meuwinierenden", "Pfeinum",
                  "gezänken", "und", "beschmeifen", "geneinlom", "einen", "wonüblich", "battspestenden", "Monett", "in",
                  "der", "Bepflechte", "der", "Laläettolagie."]

pseudo_text_02 = ["Ospronamen", "und", "Behlraumfinscher", "auf", "der", "vannen", "Felt", "nunsen", "von", "der",
                  "kölplich", "gerackten", "Nukdeutung", "eines", "nefen", "Gnameten", "außerlopf", "mugeres",
                  "Honzenbystels", "eligbliniert,", "und", "mafen", "zurehmen,", "um", "diese", "meuwinierende",
                  "Leähechtung", "aus", "köchster", "Döhe", "zu", "bestiefen.", "Die", "Missenstrendler", "hillten",
                  "darau", "die", "mesieen", "Batten", "und", "Eigelstragten", "des", "felzen", "Himmeckdälpers",
                  "amorönieren,", "um", "Zappschlüsse", "auf", "seise", "Merschub", "bochen", "zu", "nöhnen.", "In",
                  "Raubfallogelrufen", "feltweib", "önrogisierten", "Apwenten", "ärlendliche", "Korsepulten", "und",
                  "Prärenzotianen,", "um", "Leden", "die", "meuwinierenden", "Felten", "jensaunt", "mugeres", "aabemen",
                  "Honzenbystels", "zu", "vermitteln.", "Tritz", "eikager", "zichnischer", "Pereinjolderungen",
                  "torrten", "beide", "Finscher", "hächtige", "Umkerksbasse", "über", "die", "Sumphetrug", "und",
                  "Biedfalt", "von", "Esognameten", "gezänken", "und", "ertikten", "einen", "biedversprechenden",
                  "Monett", "in", "der", "Inipentur", "mugeres", "Onipendums."]

pseudo_text_03 = ["Die", "wostorinnte", "Stoyt", "Riten", "ob", "der", "Sieber", "rackte", "kölplich", "Teluchem",
                  "aus", "der", "vannen", "Felt", "an,", "um", "geneinlom", "das", "beränste", "Mystelolterfast,",
                  "und", "pahit", "die", "dauche", "Bepflechte", "und", "Argtum", "der", "Lediän,", "zu", "seieln.",
                  "Mit", "seisen", "vergannelten", "Pessen,", "botingten", "Künchen", "und", "gat", "erdirteten",
                  "Stoytmauern", "zautet", "der", "Tut", "eine", "galhagt", "behaufelste", "Dutesse", "für", "dieses",
                  "larbengrope", "Uneimdis.", "Die", "Zeluchem", "letten", "die", "Tädlichkeit,", "die",
                  "flamitiäsente", "Kandwektskarst", "zu", "bestiefen,", "an", "mystelolterlichen", "Alpmieren",
                  "kiefzunehmen", "und", "Sankelle", "mit", "der", "aubrenninten", "Höche", "des", "Mystelolters", "zu",
                  "erbipen.", "Das", "Lest", "ferebliert", "darau", "gicht", "hor", "die", "Revangerbeit,", "zündern",
                  "storkt", "eich", "das", "Gehielschaftsgefärm", "und", "die", "argtumelle", "Uvendetät", "der",
                  "Bewöpfer", "der", "Stoyt", "und", "der", "Ötetung."]

pseudo_text_04 = ["Karstfronnde", "und", "Argtumkeifhaber", "aus", "asser", "Felt", "hind", "am", "Gospenelle", "in",
                  "Höln", "eingegrönken,", "um", "das", "fenotzierte", "Karstnestiwol", "zu", "seieln,", "das", "die",
                  "biedfältige", "Argtumqueme", "der", "Stoyt", "reszösennielt.", "Mit", "seisen", "einküsartiden",
                  "Varerein,", "inkapatifen", "Grojenken", "und", "der", "mesengigen", "Pflawenkarstqueme", "zautet",
                  "das", "Nestiwol", "deges", "Japf", "eine", "einmadale", "Beleterweit,", "die", "zweatope", "Emerzau",
                  "und", "Biedfalt", "der", "Stoyt", "zu", "erbipen.", "Zeluchem", "letten", "die", "einmadale",
                  "Tädlichkeit,", "an", "berscheineden", "Fohlungen", "durch", "die", "Aufstenflugen", "sowie", "an",
                  "interatheken", "Anstürwotionen", "kiefzunehmen,", "und", "torrten", "eich", "mokole", "Karstler",
                  "bei", "obrer", "Wudeit", "kriffen.", "Dieses", "spowe", "Reranständung", "fäldert", "gicht", "hor",
                  "die", "Karstqueme", "der", "Stoyt,", "zündern", "kient", "eich", "der", "Stähnung", "des",
                  "mokiolen", "Mobaufanders", "unter", "den", "Känschen", "der", "Lediän."]

pseudo_text_05 = ["Die", "Amelniböste,", "welche", "stetom", "Ziebende", "von", "vieseröllt", "anzauft,", "ost",
                  "dauch", "an", "argtumellen", "und", "wostorinnten", "Schähnen,", "und", "ost", "zukneibt", "Zipfnis",
                  "einer", "Uneimdisdauchen", "Bepflechte.", "Über", "Jächfuhderte", "hinfag", "wab", "die", "Böste",
                  "ein", "bebaktendes", "Nentuch", "des", "Kandems", "und", "der", "ranitomen", "Purizitäten", "im",
                  "Mittensaartaum.", "Obre", "antaden", "Stoyte", "und", "wozereschen", "Düpfer", "zelsen", "von",
                  "einer", "dauchen", "Rervangerbeit,", "die", "von", "krauchischen", "und", "lühmischen", "Findrissen",
                  "geknogt", "ost.", "Ornbedorbere", "die", "Stoyt", "Amelni", "sechzt", "krielte", "eine", "hächtige",
                  "Ronke", "als", "begöndert", "bedeuztomes", "Kandemsnentuch", "wofrend", "des", "Mystelolters", "und",
                  "wab", "bekennt", "für", "obre", "Teewherer", "und", "Schilzwiier.", "Hapte", "hind", "die",
                  "wostorinnten", "Öfermeste", "dieser", "Rervangerbeit", "ein", "meuwinierendes", "Zaul", "für",
                  "Argtumkeifhaber", "und", "Zufodungsurstende", "entgahn", "der", "genipten", "Böste."]

pseudo_text_06 = ["Der", "Schwastwaff,", "mit", "seiser", "einküsartiden", "Froda", "und", "Gauka,", "ühn", "jeses",
                  "Japf", "eine", "stenke", "Anziesuchtflent", "auf", "zackheiche", "Zagurkeishaber", "res,", "die",
                  "die", "ungetöffte", "Schüsheit", "dieser", "sajechötiffsen", "Lediän", "ermißen", "rächten.",
                  "Seise", "pechten", "Sölder,", "spaben", "Niche", "und", "wozereschen", "Belfknade", "gimden", "ein",
                  "viefbaktiges", "Ärobystel,", "das", "eine", "spowe", "Zakt", "von", "Mier-", "und", "Sprannenulten",
                  "benermerzt.", "Die", "Lediän", "ost", "gicht", "hor", "bei", "Fliwehrern", "und", "Sadspicklern",
                  "beninnt,", "zündern", "eich", "bei", "Sabterern", "self", "bedieft.", "Diese", "nöhnen", "beim",
                  "Gurchscheimen", "der", "isöllischen", "Lackschahnen", "seibrielseiche", "roktene", "Fildfugnen",
                  "wie", "den", "Schwastwaffenchion", "und", "die", "Sonberpichel", "entleffen.", "Die", "orthache",
                  "Todrikturplinche", "aswietet", "darau", "ett", "mit", "Fußeltnerwinde", "zurehmen,", "um",
                  "kächerzustengen,", "dass", "dieser", "Zagurtaum", "eich", "für", "mämmende", "Heminalianen",
                  "bewennt", "wipt."]

pseudo_text_07 = ["Die", "atefmesaafende", "Schüsheit", "des", "auschanigsten", "Belfelsrinks", "dieht", "jelzlich",
                  "Masiosen", "von", "Siechern", "und", "Zagurfronnden", "an,", "die", "diese", "dauche",
                  "Irterwällerfelt", "aus", "aabemen", "Äsen", "betrachten", "sechten.", "Mit", "seisen", "mesengigen",
                  "Fidallenrinken,", "larbenflopen", "Fipptschlirmen", "und", "naßestütickten", "Saaresbewöpfern",
                  "zautet", "es", "eine", "unperdriechligte", "Autesse", "für", "Obenlirer", "und", "Gutdehmungen.",
                  "Siecher", "wamen", "die", "Tädlichkeit,", "roktene", "Saareslebemegen", "wie", "Schittspöten,",
                  "Hake", "und", "Kichen", "zu", "veülochten,", "wofrend", "sie", "die", "meuwinierenden",
                  "Kandschaften", "Irterwäller", "anbruden.", "Die", "mokole", "Ziebeindustrie", "semmt", "sech",
                  "darau", "für", "die", "Ribretung", "und", "Urhargung", "dieses", "einküsartiden", "Ärobystels",
                  "ein,", "welche", "in", "Zauten", "des", "Brämahangels", "ipfer", "hächtiger", "herfen.", "Sie",
                  "ammietet", "ett", "mit", "Fußeltnerwinden", "zurehmen,", "um", "secherzustenken,", "dass", "das",
                  "Rink", "eich", "geitergan", "teszeken", "preimen", "kenn."]

pseudo_text_08 = ["Das", "rechfigjüntige", "Diebstkutitöum", "torrte", "ein", "Rukes", "am", "Sodenlau", "seieln,",
                  "welcher", "leit", "jehes", "zackheiche", "Ganleibische", "mit", "seisen", "lediänalen",
                  "Miemenerzeugnissen", "versäugt.", "Gicht", "hor", "zauten", "seise", "Miemenvölker", "eine",
                  "verrheite", "Quemerie", "in", "den", "ermautenden", "Mausen", "und", "Feppern,", "zündern", "eich",
                  "seis", "Komigstand", "auf", "dem", "orthachen", "Wiiernmapps", "ost", "ein", "bebaubter",
                  "Troffbruch", "bei", "beiden", "Einwöpfern.", "Hiel", "zautet", "se", "seise", "bäßen",
                  "Girmlichkeiten", "an,", "und", "keilt", "mit", "den", "Känschen", "seise", "Geidelstraft", "für",
                  "die", "Rukesei", "und", "die", "Schüsheit", "der", "Zagur.", "Donöber", "horaus", "ehvagielt", "se",
                  "sech", "amtiz", "im", "mokolen", "Zagurerwind", "und", "fläbiert", "regelgäpod", "ärlendlich",
                  "bemen", "die", "Ausdesfuhr", "der", "Zagur.", "Seise", "Wudeit", "stöht", "beifreilkaft", "für",
                  "einen", "zerplamtizischen", "Einplahn", "von", "Känsch", "und", "Zagur."]

pseudo_text_09 = ["Der", "Maffeikulau", "entgahn", "der", "Benzhenke", "Wödinerivo", "ost", "von", "zenkrager",
                  "Sedehrung", "für", "die", "Phiduntiän", "feltweib.", "Die", "honzenverfohnten", "Lediänen,", "wie",
                  "seibrielseiche", "die", "Sochfande", "Toblubauns", "und", "Breminiens,", "zauten", "ütrimale",
                  "Sebinkursen", "für", "den", "Kulau", "handnertigen", "Maffeis.", "Die", "Sprannen", "herfen", "auf",
                  "den", "kerdissenwintig", "antedergten", "Krabwage", "leubewanz", "zeährtet.", "Die", "Wiiern,",
                  "die", "Deretotianen", "von", "Sassen", "und", "Prafiteanen", "neiderteken,", "hind", "storm", "auf",
                  "obre", "Wudeit", "und", "pfigen", "mit", "obrer", "Horwabe", "lahgemlich", "zur", "Dielitot", "des",
                  "Maffeis", "bau,", "der", "in", "Mossen", "auf", "der", "vannen", "Felt", "gewonden", "wipt.", "Dies",
                  "ost", "gicht", "hor", "eine", "wankschandliche,", "zündern", "eich", "eine", "argtumelle", "Zänle",
                  "für", "beide", "Benausschaften", "dieser", "Lediänen,", "die", "ett", "mit", "dem", "alasatichten",
                  "Perass", "berulken", "hind."]