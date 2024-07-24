#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Instructions, Texts & MC questions for EXNAT-2 EEG study

Author: Merle Schuckart & Sandra Martin
Version: April 2024

"""

""" Instructions """

# for each block, set instruction texts + path to instruction image you want to show:
instr_pic_path = "Stimuli_and_Resources/EXNAT3_Instr_Pics/"

instr_Reading_Baseline_training_click = "Willkommen!\n\n\nIm folgenden Block werden Ihnen einzelne " \
                                        "Wörter angezeigt, die einen zusammenhängenden Text bilden.\n\nBitte lesen " \
                                        "Sie den Text, indem Sie mithilfe der Leertaste von Wort zu Wort " \
                                        "weiterklicken. Bitte reagieren Sie stets so schnell wie möglich!\n\nDie " \
                                        "Schriftfarbe der Wörter variiert, Sie können das jedoch " \
                                        "einfach ignorieren.\n\nAuf den Text folgen drei Fragen zum Textinhalt. " \
                                        "\n\nSie können die Aufgabe nun in einem kurzen Übungsblock testen. Bitte " \
                                        "drücken Sie die Leertaste, um den Übungsblock zu starten. "
instr_pic_Reading_Baseline_training_click = instr_pic_path + "BL_single.jpeg"

instr_Reading_Baseline_main_click = "LESEN MIT TASTENDRUCK\n\n\nGut gemacht!\n\nIm nun folgenden Block wird Ihnen ein längerer Text " \
                                    "angezeigt.\n\nBitte lesen Sie den Text, indem Sie mithilfe der Leertaste von " \
                                    "Wort zu Wort weiterklicken. Bitte ignorieren Sie wie eben auch die sich " \
                                    "verändernde Schriftfarbe.\n\nAm Ende des Texts werden Ihnen wieder Fragen zum " \
                                    "Inhalt gestellt.\n\nBitte drücken Sie die Leertaste, um den Block zu starten. "
instr_pic_Reading_Baseline_main_click = instr_pic_path + "BL_single.jpeg"

instr_Reading_Baseline_training_no_click = "LESEN OHNE TASTENDRUCK\n\n\nSehr gut!\n\nNun ändert sich die Aufgabe " \
                                           "etwas:\nIm folgenden Block werden die Wörter von " \
                                           "allein abgespielt. Sie müssen also diesmal nicht die Leertaste " \
                                           "drücken, lesen Sie aber bitte trotzdem den Text mit. Am Ende des Texts " \
                                           "werden Ihnen wieder Fragen zum Inhalt gestellt.\n\nSie können die " \
                                           "Aufgabe kurz üben, bevor der Hauptblock startet. Drücken Sie dafür die " \
                                           "Leertaste."
instr_pic_vis_task = instr_pic_path + "vis_task.jpeg"

instr_Reading_Baseline_main_no_click = "LESEN OHNE TASTENDRUCK\n\n\nGut gemacht!\n\nIm nun folgenden Block werden " \
                                       "die Wörter erneut " \
                                       "von allein abgespielt. Sie müssen also nicht die Leertaste drücken. " \
                                       "Der Text ist nun wieder etwas länger. " \
                                       "Am Ende des Texts werden Ihnen auch wieder Fragen zum Inhalt " \
                                       "gestellt.\n\nBitte " \
                                       "drücken Sie die " \
                                       "Leertaste, um den Block zu starten."

instr_Reading_pseudotext_no_click = "LESEN OHNE TASTENDRUCK\n\n\nGut gemacht!\n\nIm letzten Block dieser Übung werden " \
                                       "die Wörter erneut " \
                                       "von allein abgespielt. Allerdings handelt es sich diesmal um Wörter, die es gar nicht " \
                                        "gibt. Bitte lesen Sie den Text dennoch aufmerksam mit. Sie müssen sonst nichts tun. " \
                                        "\n\nBitte " \
                                       "drücken Sie die " \
                                       "Leertaste, um den Block zu starten."

instr_click_training = "Instruktionen\n\n\nNun kommt eine neue Aufgabe:\nIhnen werden gleich nacheinander " \
                       "verschiedenfarbige Rechtecke gezeigt. Wie auch eben bei der Leseaufgabe können Sie mit der " \
                       "Leertaste weiter klicken.\n\nBitte drücken Sie die Leertaste um den Übungsblock zu starten. "
instr_pic_click_training = instr_pic_path + "BL_single.jpeg"

instr_0back_single_training1 = ("ÜBUNG FARBERKENNUNG\n\n\nIm folgenden Block erscheinen Rechtecke in verschiedenen Farben. "
                                "Wie auch zuvor verwenden Sie die Leertaste, um zum nächsten Rechteck zu kommen. Zusätzlich sollen Sie auf die Farbe der Rechtecke achten."
                               "\n\nBitte drücken Sie die Taste C auf Ihrer Tastatur, wenn Sie ein "
                               "Rechteck in der folgenden Farbe sehen:")
instr_0back_single_training2 = "Bitte drücken Sie die Leertaste, um den Übungsblock zu starten."

instr_pic_0back = instr_pic_path + "vis_task.jpeg"

instr_0back_dual_main_click1 = "LESEN MIT FARBERKENNUNG UND TASTENDRUCK\n\n\nNun wird das Lesen mit der Farberkennung " \
                              "kombiniert. Sie lesen einen Text Wort für Wort und klicken mithilfe der Leertaste " \
                              "weiter zum nächsten Wort. Gleichzeitig sollen Sie auf die Farben der Wörter achten: " \
                              "\n\nBitte drücken Sie schnellstmöglich die Taste C, wenn das Wort die folgende Farbe hat:" \

instr_0back_dual_main_click2 = "Am Ende des Blocks werden Ihnen wieder Verständnisfragen zum Inhalt des " \
                              "Texts gestellt.\nBitte drücken Sie die Leertaste, um den Block zu starten. "

instr_0back_dual_main_no_click1 = "LESEN MIT FARBERKENNUNG OHNE TASTENDRUCK\n\n\nGut gemacht!\n\nIm folgenden Block werden " \
                                 "die Wörter " \
                                 "von allein abgespielt. Sie müssen also NICHT die Leertaste drücken.\n\nBitte " \
                                 "drücken Sie aber schnellstmöglich die Taste C, wenn das Wort die folgende Farbe hat: "

instr_0back_dual_main_no_click2 = "Am Ende des Blocks werden Ihnen wieder Verständnisfragen zum Inhalt des " \
                              "Texts gestellt.\nBitte drücken Sie die Leertaste, um den Block zu starten. "

instr_1back_single_training1 = "ÜBUNG 1-ZURÜCK\n\n\nIn den nun folgenden Blöcken geht es darum, auf Wiederholungen " \
                               "der Farben zu achten:\n\nBitte drücken Sie die Taste C auf Ihrer Tastatur, " \
                               "wenn die aktuelle Farbe die gleiche ist wie die des vorherigen Rechtecks (1 " \
                               "zurück).\n\nWie zuvor auch können Sie mithilfe der Leertaste weiterklicken.\n\nBitte " \
                               "drücken Sie die Leertaste, um den Übungsblock zu starten. "
instr_pic_1back_single_training1 = instr_pic_path + "1back_rect.jpeg"

instr_1back_single_training2 = "Gut gemacht!\n\nMöchten Sie die Übung noch einmal wiederholen oder möchten " \
                               "Sie mit dem Hauptblock fortfahren?\nBitte drücken Sie die Taste W, wenn sie die Übung " \
                               "wiederholen möchten oder die Leertaste, wenn Sie fortfahren möchten. "
instr_pic_1back_single_training2 = instr_pic_path + "1back_rect.jpeg"

instr_1back_single_main = "1-ZURÜCK\n\n\nNun folgt ein etwas längerer Block, die Aufgabe bleibt aber die " \
                          "gleiche:\n\nBitte drücken Sie die Taste C, wenn die aktuelle Farbe die gleiche ist wie die " \
                          "des vorherigen Rechtecks (1 zurück).\n\nWie auch zuvor können Sie mithilfe der Leertaste zum " \
                          "nächsten Rechteck weiterklicken.\n\nBitte drücken Sie die Leertaste, um den Block zu " \
                          "starten. "
instr_pic_1back_single_main = instr_pic_path + "1back_rect.jpeg"

instr_1back_single_main_no_click = "1-ZURÜCK OHNE TASTENDRUCK\n\n\nGut gemacht!\n\nIm folgenden Block werden " \
                                 "die Rechtecke " \
                                 "wieder von allein abgespielt. Sie müssen also nicht die Leertaste drücken.\n\nBitte " \
                                 "drücken Sie aber so schnell wie möglich die Taste C, wenn die Farbe des " \
                                 "aktuellen Rechtecks mit der des vorherigen Rechtecks (1 zurück) übereinstimmt.\n\nDrücken " \
                                 "Sie die Leertaste, um den Block zu starten."
instr_pic_1back_single_main_no_click = instr_pic_path + "1back_rect.jpeg"

instr_1back_dual_main_click = "LESEN MIT 1-ZURÜCK UND TASTENDRUCK\n\n\nNun wird das Lesen mit der Gedächtnisaufgabe " \
                              "kombiniert. Sie lesen einen Text Wort für Wort und klicken mithilfe der Leertaste " \
                              "weiter zum nächsten Wort. Gleichzeitig sollen Sie auf die Farben der Wörter achten: " \
                              "\n\nBitte drücken Sie die Taste C, " \
                              "wenn die Farbe des aktuellen Worts mit der des vorherigen Worts (1 zurück) " \
                              "übereinstimmt.\n\n " \
                              "Denken Sie daran: Reagieren Sie so schnell wie möglich!\n\n " \
                              "Am Ende des Blocks werden Ihnen wieder Verständnisfragen zum Inhalt des " \
                              "Texts gestellt.\n\nBitte drücken Sie die Leertaste, um den Block zu starten. "
instr_pic_1back_dual_main_click = instr_pic_path + "1back.jpeg"

instr_1back_dual_main_no_click = "LESEN MIT 1-ZURÜCK OHNE TASTENDRUCK\n\n\nGut gemacht!\n\nIm folgenden Block werden " \
                                 "die Wörter " \
                                 "wieder von allein abgespielt. Sie müssen also nicht die Leertaste drücken.\n\nBitte " \
                                 "drücken Sie aber so schnell wie möglich die Taste C, wenn die Farbe des " \
                                 "aktuellen Worts mit der des vorherigen Worts (1 zurück) übereinstimmt.\n\nDrücken " \
                                 "Sie die Leertaste, um den Block zu starten."
instr_pic_1back_dual_main_no_click = instr_pic_path + "1back.jpeg"

instr_2back_single_training1 = "ÜBUNG 2-ZURÜCK\n\n\nIn den nun folgenden Blöcken geht es darum, auf Wiederholungen " \
                               "der Farben zu achten:\n\nBitte drücken Sie die Taste C auf Ihrer Tastatur, " \
                               "wenn die aktuelle Farbe die gleiche ist wie die des vorletzten Rechtecks (2 zurück). " \
                               "Wie zuvor können Sie mithilfe der Leertaste weiterklicken.\n\nBitte drücken Sie " \
                               "die Leertaste, um den Übungsblock zu starten. "
instr_pic_2back_single_training1 = instr_pic_path + "2back_rect.jpeg"

instr_2back_single_training2 = "Gut gemacht!\n\nMöchten Sie die Übung noch einmal wiederholen oder möchten " \
                               "Sie mit dem Hauptblock fortfahren?\nBitte drücken Sie die Taste W, wenn sie die Übung " \
                               "wiederholen möchten oder die Leertaste, wenn Sie fortfahren möchten. "
instr_pic_2back_single_training2 = instr_pic_path + "2back_rect.jpeg"


instr_2back_single_main = "2-ZURÜCK\n\n\nNun folgt ein etwas längerer Block, die Aufgabe bleibt aber die " \
                          "Gleiche:\n\nBitte drücken Sie die Taste C, wenn die aktuelle Farbe die gleiche ist wie die " \
                          "des vorletzten Rechtecks (2 zurück).\n\nWie auch zuvor können Sie mithilfe der Leertaste " \
                          "zum nächsten Rechteck weiterklicken. Denken Sie daran: Reagieren Sie so schnell wie möglich!\n\nBitte drücken Sie die Leertaste, um den Block zu " \
                          "starten. "
instr_pic_2back_single_main = instr_pic_path + "2back_rect.jpeg"

instr_2back_single_main_no_click = "2-ZURÜCK OHNE TASTENDRUCK\n\n\nGut gemacht!\n\nIm folgenden Block werden " \
                                 "die Rechtecke " \
                                 "wieder von allein abgespielt. Sie müssen also nicht die Leertaste drücken.\n\nBitte " \
                                 "drücken Sie aber so schnell wie möglich die Taste C, wenn die Farbe des " \
                                 "aktuellen Rechtecks mit der des vorletzten Rechtecks (2 zurück) übereinstimmt.\n\nDrücken " \
                                 "Sie die Leertaste, um den Block zu starten."
instr_pic_2back_single_main_no_click = instr_pic_path + "2back_rect.jpeg"

instr_2back_dual_main_click = "LESEN MIT 2-ZURÜCK UND TASTENDRUCK\n\n\nNun wird das Lesen mit der Gedächtnisaufgabe " \
                              "kombiniert. Sie lesen einen Text Wort für Wort und klicken mithilfe der Leertaste " \
                              "weiter zum nächsten Wort. Gleichzeitig sollen Sie auf die Farben der Wörter achten: " \
                              "\n\nBitte drücken Sie so schnell wie möglich die Taste C, " \
                              "wenn die Farbe des aktuellen Worts mit der des vorletzten Worts (2 zurück) " \
                              "übereinstimmt.\n\n " \
                              "Am Ende des Blocks werden Ihnen wieder Verständnisfragen zum Inhalt des " \
                              "Texts gestellt.\n\nBitte drücken Sie die Leertaste, um den Block zu starten. "
instr_pic_2back_dual_main_click = instr_pic_path + "2back.jpeg"

instr_2back_dual_main_no_click = "LESEN MIT 2-ZURÜCK OHNE TASTENDRUCK\n\n\nGut gemacht!\n\nIm folgenden Block werden " \
                                 "die Wörter " \
                                 "wieder von allein abgespielt. Sie müssen also nicht die Leertaste drücken.\n\nBitte " \
                                 "drücken Sie aber die Taste C, wenn die Farbe des " \
                                 "aktuellen Worts mit der des vorletzten Worts (2 zurück) übereinstimmt.\n\nDrücken " \
                                 "Sie die Leertaste, um den Block zu starten."
instr_pic_2back_dual_main_no_click = instr_pic_path + "2back.jpeg"

# warning sign for change of task:
warning_sign = instr_pic_path + "warning.jpeg"

""" Reading Baseline Training: """

# the training text is the first paragraph of the novel "Die Schachnovelle" by Stefan Zweig
reading_bl_tr_text = ["Auf", "dem", "großen", "Passagierdampfer,", "der", "um", "Mitternacht", "von", "New", "York",
                      "nach", "Buenos", "Aires", "abgehen", "sollte,", "herrschte", "die", "übliche", "Geschäftigkeit",
                      "und", "Bewegung", "der", "letzten", "Stunde.", "Gäste", "vom", "Land", "verabschiedeten",
                      "sich,", "während", "das", "Orchester", "zur", "Deckshow", "aufspielte.", "Abseits", "des",
                      "Trubels", "bemerkten", "wir", "Blitzlichter:", "Reporter", "hatten", "den", "Weltschachmeister",
                      "Mirko", "Czentovic,", "der", "nach", "Turnieren", "in", "Amerika", "nun", "nach", "Argentinien",
                      "reiste,", "für", "ein", "Interview", "erwischt."]
# prepare questions & answers:
reading_bl_tr_Q1 = "Wo befinden sich die Personen im Text?"
reading_bl_tr_Q1_ans = ["1) auf einem Schiff", "2) in einem Flugzeug", "3) in einem Zug", "4) in einem Bus"]
reading_bl_tr_Q1_corr = "a"

reading_bl_tr_Q2 = "Wohin geht ihre Reise?"
reading_bl_tr_Q2_ans = ["1) Caracas (Venezuela)", "2) Lima (Peru)", "3) Buenos Aires (Argentinien)",
                        "4) Manaus (Brasilien)"]
reading_bl_tr_Q2_corr = "c"

reading_bl_tr_Q3 = "Einer der Reisenden hat einen ungewöhnlichen Beruf. Welchen?"
reading_bl_tr_Q3_ans = ["1) Schachspieler", "2) Dressurreiter", "3) Trickbetrüger", "4) Diamantenhändler"]
reading_bl_tr_Q3_corr = "a"

""" PACED Reading Baseline Training: """
reading_bl_tr_text_no_click = ["In", "einem", "Augenblick", "der", "Stille", "hörte", "man", "die", "Wellen",
                               "rauschen,", "das", "Radio", "aus", "dem", "Salon", "herüberjazzen", "und", "man",
                               "vernahm", "auf", "einmal", "jeden", "Schritt", "vom", "Promenadendeck.", "Keiner",
                               "von", "uns", "atmete,", "es", "war", "zu", "plötzlich", "gekommen", "und", "wir",
                               "alle", "noch", "geradezu", "erschrocken", "über", "das", "Unwahrscheinliche,", "dass",
                               "dieser", "Unbekannte", "dem", "Weltmeister", "in", "einer", "schon", "halb",
                               "verlorenen", "Partie", "Schach", "seinen", "Willen", "aufgezwungen", "haben", "sollte."]
# prepare questions & answers:
reading_bl_tr_no_click_Q1 = "Was hören die Personen vom Promenadendeck?"
reading_bl_tr_no_click_Q1_ans = ["1) Hunde", "2) Schritte", "3) Stimmen", "4) Geschrei"]
reading_bl_tr_no_click_Q1_corr = "b"

reading_bl_tr_no_click_Q2 = "Was machte keiner der Zuschauer laut dem Text?"
reading_bl_tr_no_click_Q2_ans = ["1) atmen", "2) rennen", "3) wegschauen", "4) jubeln"]
reading_bl_tr_no_click_Q2_corr = "a"

reading_bl_tr_no_click_Q3 = "Wer wurde im Schach besiegt?"
reading_bl_tr_no_click_Q3_ans = ["1) der Europameister", "2) der Großmeister", "3) der Unbekannte",
                                 "4) der Weltmeister"]
reading_bl_tr_no_click_Q3_corr = "d"

""" Main Blocks: """

# Elefants
# global text_01
text_01 = ["Ältere", "Leitkühe", "treffen", "bessere", "Entscheidungen", "für", "ihre", "Herde,", "als", "junge.",
           "Die", "Chefin", "der", "Elefanten", "muss", "wichtige", "Entscheidungen", "für", "die",
           "Gemeinschaft", "treffen,", "beispielsweise", "wohin", "die", "Herde", "geht", "oder", "wie", "man",
           "sich", "gegen", "Löwen", "verteidigt.", "Biologen", "konnten", "in", "Kenia", "zeigen,", "dass", "die",
           "älteren", "Tiere", "ihre", "Herden", "beim", "Gebrüll", "eines", "männlichen", "Löwen", "stärker",
           "warnen,", "als", "bei", "dem", "einer", "Löwin.", "Denn", "Löwen", "sind", "für", "junge", "Elefanten",
           "gefährlicher.", "jüngere", "Chefinnen", "machten", "diesen", "Unterschied", "kaum.", "Afrikanische",
           "Elefanten", "können", "in", "freier", "Wildbahn", "bis", "zu", "70", "Jahre", "alt", "werden.", "Die",
           "nützliche", "Erfahrung", "älterer", "Tiere", "könnte", "ein", "Grund", "dafür", "sein."]

text_01_Q1 = "In welchen Land haben die Biologen das Verhalten der Elefanten beobachtet?"
text_01_Q1_ans = ["1) Tansania",
                  "2) Kenia",
                  "3) Botswana",
                  "4) Uganda"]
text_01_Q1_corr = "b"

text_01_Q2 = "Was ist besonders gefährlich für junge Elefanten?"
text_01_Q2_ans = ["1) Hyänen", "2) Löwen", "3) Löwinnen", "4) Geparde"]
text_01_Q2_corr = "b"

text_01_Q3 = "Wie alt können afrikanische Elefanten in der freien Wildbahn werden?"
text_01_Q3_ans = ["1) 40 Jahre alt", "2) 50 Jahre alt", "3) 60 Jahre alt", "4) 70 Jahre alt"]
text_01_Q3_corr = "d"

# Crocodile
# global text_02
text_02 = ["In", "Tansania", "haben", "Forscher", "Überreste", "eines", "Urzeit-Krokodils", "entdeckt.", "Es", "zeigt",
          "Ähnlichkeiten", "zu", "Säugetieren.", "Es", "war", "so", "groß", "wie", "eine", "Katze.", "Das", "Tier",
          "lebte", "vor", "etwa", "105", "Millionen", "Jahren", "und", "jagte", "an", "Land", "nach", "Insekten",
          "und", "kleinen", "Tieren.", "Es", "besaß", "ungewöhnliche", "Merkmale,", "wie", "weniger", "Zähne", "und",
          "hatte", "Backenzähne", "zum", "Kauen", "von", "Nahrung.", "Außerdem", "war", "es", "weniger", "gepanzert.",
          "Die", "Forscher", "denken,", "dass", "Krokodile", "in", "der", "Vergangenheit", "auf", "der",
          "Südhalbkugel", "lebten,", "während", "sich", "Säugetiere", "auf", "der", "Nordhalbkugel", "ausbreiteten.",
          "Die", "Forscher", "werden", "in", "Zukunft", "versuchen", "mehr", "über", "die", "frühe", "Tierwelt", "auf",
          "der", "Südhalbkugel", "zu", "erfahren."]

text_02_Q1 = "Zu welchen Lebewesen zeigte das Urzeit-Krokodil Ähnlichkeit?"
text_02_Q1_ans = ["1) Vögel", "2) Fische",
                  "3) Säugetiere", "4) Insekten"]
text_02_Q1_corr = "c"

text_02_Q2 = "Das Urzeit-Krokodil war so groß wie welches Tier?"
text_02_Q2_ans = ["1) Adler", "2) Hund", "3) Hase", "4) Katze"]
text_02_Q2_corr = "d"

text_02_Q3 = "Wo lebten Krokodile früher hauptsächlich?"
text_02_Q3_ans = ["1) auf der Nordhalbkugel", "2) auf der Südhalbkugel",
                  "3) in den Tropen", "4) an den Polen"]
text_02_Q3_corr = "b"

# Orang-Utans
# global text_03
text_03 = ["Orang-Utans", "bauen", "sich", "jede", "Nacht", "gemütliche", "Schlafnester", "hoch", "in", "den",
           "Bäumen.", "Diese", "Nester", "bestehen", "aus", "Ästen", "und", "Blättern", "und", "bieten", "den",
           "Affen", "Komfort", "und", "Schutz.", "Forscher", "haben", "entdeckt,", "dass", "Orang-Utans", "sehr",
           "geschickt", "vorgehen:", "Sie", "wählen", "stabile", "Äste", "aus", "und", "biegen", "diese,", "ohne",
           "sie", "ganz", "zu", "brechen.", "So", "entsteht", "eine", "robuste", "Grundstruktur.", "Die", "Polsterung",
           "der", "Nester", "besteht", "aus", "dünneren", "Ästen", "und", "macht", "das", "Nest", "besonders",
           "bequem.", "Diese", "Bauweise", "schützt", "die", "Orang-Utans", "nicht", "nur", "vor", "dem",
           "Herunterfallen,", "sondern", "auch", "vor", "Feinden", "und", "Parasiten.", "So", "schlafen", "die",
           "Primaten", "sicher", "und", "komfortabel", "in", "ihren", "Nestern."]

text_03_Q1 = "Wie werden die „Betten“ der Orang-Utans genannt?"
text_03_Q1_ans = ["1) Schlafnester", "2) Schlafkobel", "3) Schlafräume", "4) Schlafbauten"]
text_03_Q1_corr = "a"

text_03_Q2 = "Wie häufig bauen die Orang-Utans ihre Schlafpätze neu?"
text_03_Q2_ans = ["1) Einmal am Tag", "2) Einmal in der Woche", "3) Einmal im Monat", "4) Einmal im Jahr"]
text_03_Q2_corr = "a"

text_03_Q3 = "Wovor schützen diese besonderen Schlafpätze auch?"
text_03_Q3_ans = ["1) Vor Regen", "2) Vor Parasiten", "3) Vor Sonne", "4) Vor Wind"]
text_03_Q3_corr = "b"

# Namibia
# global text_04
text_04 = ["Manche", "Orte", "sind", "nur", "aus", "der", "Luft", "wirklich", "zugänglich.", "Bertus", "Schoeman",
           "fliegt", "oft", "mit", "seinem", "Flugzeug", "über", "die", "unwirtliche,", "aber", "trotzdem",
           "wunderschöne", "Küste", "Namibias.", "Er", "zeigt", "Touristen", "die", "beeindruckenden", "Schiffswracks",
           "und", "die", "einzigartigen", "Landschaften", "von", "oben.", "Vom", "Flugzeug", "aus", "sieht", "man",
           "die", "Küste", "des", "Landes,", "die", "sich", "von", "Südafrika", "bis", "nach", "Angola", "erstreckt.",
           "Auch", "verschiedene", "Tiere,", "wie", "die", "berühmten", "Flamingos", "von", "Conception", "Bay", "und",
           "die", "Robbenkolonien", "von", "Cape", "Cross", "kann", "man", "aus", "der", "Vogelperspektive", "sehen.",
           "Diese", "Safari", "in", "der", "Luft", "bietet", "Touristen", "einen", "einzigartigen", "Blick", "auf",
           "Namibias", "raue", "und", "faszinierende", "Schönheit."]

text_04_Q1 = "Wer fliegt mit seinem Flugzeug über Namibia?"
text_04_Q1_ans = ["1) Ludwig Beukes", "2) Abiola Berger", "3) Bertus Schoeman", "4) Belay Thomas"]
text_04_Q1_corr = "c"

text_04_Q2 = "Was kann man aus der Luft sehen?"
text_04_Q2_ans = ["1) Schiffwracks", "2) Flugzeugwracks", "3) Alte Eisenbahnen", "4) Alte Autos"]
text_04_Q2_corr = "a"

text_04_Q3 = "Welche Robbenkolonie kann man sehen?"
text_04_Q3_ans = ["1) Robbenkolonie von Cape Cross", "2) Robbenkolonie von Cape Hope", "3) Robbenkolonie von Cape Wish",
                  "4) Robbenkolonie von Cape Circle"]
text_04_Q3_corr = "a"

# Trottellummen
# global text_05
text_05 = ["Trottellummen", "brüten", "auf", "steilen", "Felsklippen", "ohne", "Nester,", "so", "auch", "auf", "der",
           "deutschen", "Insel", "Helgoland.", "Ihre", "Eier", "sind", "einzigartig:", "spitz", "zulaufend,", "bunt",
           "und", "gemustert.", "Diese", "Form", "verhindert,", "dass", "sie", "vom", "Felsen", "rollen,", "denn",
           "sie", "drehen", "sich", "bei", "Berührung", "im", "engen", "Kreis.", "Forscher", "haben", "außerdem",
           "entdeckt,", "dass", "die", "Schale", "der", "Eier", "Nanostrukturen", "besitzt,", "die", "wasserabweisend",
           "und", "rau", "sind.", "Dies", "schützt", "die", "Eier", "vor", "Schmutz", "und", "Salzwasser,", "hält",
           "die", "Poren", "frei", "und", "erleichtert", "den", "Sauerstoffaustausch.", "Die", "bunten", "Muster",
           "helfen", "den", "Eltern,", "ihre", "eigenen", "Eier", "zu", "erkennen.", "So", "überstehen", "die", "Eier",
           "die", "gefährliche", "Brutzeit", "besser."]

text_05_Q1 = "Wo brüten Trottellummen in Deutschland?"
text_05_Q1_ans = ["1) Wangerooge", "2) Hallig Hooge", "3) Borkum", "4) Helgoland"]
text_05_Q1_corr = "d"

text_05_Q2 = "Was ist besonders an der Form der Eier?"
text_05_Q2_ans = ["1) Sie sind spitz zulaufend", "2) Sie sind kugelförmig",
                  "3) Sie sind sehr flach", "4) Sie sind halbrund"]
text_05_Q2_corr = "a"

text_05_Q3 = "Welche weitere besondere Eigenschaft haben die Eier?"
text_05_Q3_ans = ["1) Sie sind dunkelblau", "2) Sie sind grün",
                  "3) Sie sind wasserabweisend", "4) Sie können Wasser aufnehmen"]
text_05_Q3_corr = "c"

# life on the island
# global text_06
text_06 = ["Julia", "Baer", "arbeitet", "allein", "als", "Naturschutzwartin", "im", "Auftrag", "des", "Nabu", "auf",
           "der", "Nordseeinsel", "Trischen.", "Ihre", "Aufgabe", "ist", "es,", "Vögel", "wie", "Regenpfeifer,",
           "Austernfischer", "und", "Rotschenkel", "zu", "beobachten", "und", "zu", "zählen.", "Die", "studierte",
           "Landschafts-", "und", "Meeresökologin", "lebt", "in", "einer", "kleinen", "Holzhütte", "ohne",
           "fließendes", "Wasser", "und", "nutzt", "Solarzellen", "für", "Strom.", "Einmal", "pro", "Woche", "bringt",
           "der", "pensionierte", "Fischer", "Axel", "Rohwedder", "Vorräte", "und", "ein", "bisschen", "Gesellschaft.",
           "Julia", "liebt", "die", "Abgeschiedenheit", "und", "den", "fehlenden", "Großstadtlärm.", "Obwohl", "sie",
           "meistens", "allein", "ist,", "fühlt", "sie", "sich", "nie", "einsam.", "Sie", "genießt", "das", "einfache",
           "Leben", "und", "plant,", "weiterhin", "auf", "Inseln", "zu", "leben."]

text_06_Q1 = "Auf welcher Nordseeinsel lebt Julia Baer?"
text_06_Q1_ans = ["1) Pellworm", "2) Trischen", "3) Amrum", "4) Föhr"]
text_06_Q1_corr = "b"

text_06_Q2 = "Was hat sie studiert?"
text_06_Q2_ans = ["1) Meeresökologie", "2) Vogelkunde", "3) Ökonomie", "4) Meeresbiologie"]
text_06_Q2_corr = "a"

text_06_Q3 = "Was beobachtet Julia Baer auf der Nordseeinsel?"
text_06_Q3_ans = ["1) Fische", "2) Krabben", "3) Meeresschnecken", "4) Vögel"]
text_06_Q3_corr = "d"

# training text_07
text_07 = ["Der", "Kölner", "Fotograf", "Tobias", "Zimmer", "taucht", "im", "indonesischen", "Raja", "Ampat,", "einem",
           "Ort", "mit", "sehr", "großer", "Artenvielfalt", "unter", "Wasser.", "Hier", "fotografiert", "er", "viele",
           "einzigartige", "Meereslebewesen,", "wie", "farbenfrohe", "Fische,", "Haie,", "Rochen", "und",
           "Pygmäen-Seepferdchen.", "Beim", "Tauchen", "sieht", "er", "viele", "unterschiedliche", "Korallen.", "Er",
           "ist", "beeindruckt", "von", "der", "Schönheit", "und", "Unberührtheit", "der", "Natur.", "Seine",
           "Unterkunft", "bemüht", "sich", "um", "Umweltschutz", "und", "bietet", "gute", "Arbeitsbedingungen", "für",
           "die", "Einheimischen.", "Die", "Gegend", "ist", "sehr", "schwer", "zu", "erreichen", "und", "wenig",
           "touristisch.", "Es", "gibt", "keine", "Spuren", "von", "Fischerei.", "Zimmer", "genießt", "sein",
           "Abenteuer", "in", "diesem", "Tauchparadies", "und", "hält", "es", "mit", "der", "Kamera", "fest."]

text_07_Q1 = "In welchem Land taucht Tobias Zimmer?"
text_07_Q1_ans = ["1) Philippen", "2) Australien", "3) Indonesien", "4) Malaysia"]
text_07_Q1_corr = "c"

text_07_Q2 = "Wofür ist die Gegend Raja Ampat bekannt?"
text_07_Q2_ans = ["1) Ruinen", "2) Artenvielfalt", "3) Fischerei", "4) Vögel"]
text_07_Q2_corr = "b"

text_07_Q3 = "Worum bemüht sich seine Unterkunft?"
text_07_Q3_ans = ["1) Umweltschutz", "2) Tourismus", "3) Tauchunterricht", "4) Digitalisierung"]
text_07_Q3_corr = "a"

# training text_08
text_08 = ["Forscher", "der", "Universität", "Puerto", "Rico", "benutzen", "Mikrofone", "in", "Regenwäldern,", "um",
           "Tiere", "zu", "überwachen.", "Sie", "müssen", "so", "nicht", "mehr", "selbst", "in", "den", "Regenwald",
           "und", "stören", "die", "Tiere", "nicht.", "Diese", "Mikrofone", "zeichnen", "Tiergeräusche", "auf.",
           "Diese", "Technik", "macht", "es", "für", "Forscher", "einfacher", "und", "billiger,", "Daten", "zu",
           "sammeln.", "Sie", "werden", "dann", "von", "Computern", "analysiert", "und", "automatisch", "den", "Tieren",
           "zugeordnet.", "Die", "Wissenschaftler", "können", "so", "viele", "Tierarten", "gleichzeitig", "und",
           "dauerhaft", "beobachten.", "Zum", "Beispiel", "wurden", "Geräusche", "von", "Vögeln", "und", "Affen",
           "aufgezeichnet.", "Das", "kann", "helfen,", "die", "Artenvielfalt", "zu", "schützen.", "Die", "Mikrofone",
           "werden", "auch", "auf", "Hawaii", "und", "in", "Brasilien", "benutzt."]

text_08_Q1 = "Wer analysiert die Geräusche?"
text_08_Q1_ans = ["1) Biologen", "2) Ökologen", "3) Handys", "4) Computer"]
text_08_Q1_corr = "d"

text_08_Q2 = "Welche Tiergeräusche konnten unter anderem aufgezeichnet werden?"
text_08_Q2_ans = ["1) Ameisenbären", "2) Affen", "3) Pumas", "4) Fauchschaben"]
text_08_Q2_corr = "b"

text_08_Q3 = "Wo werden die Mikrofone noch benutzt?"
text_08_Q3_ans = ["1) Kolumbien", "2) Panama", "3) Brasilien", "4) Chile"]
text_08_Q3_corr = "c"

# pseudo
# pseudo_text01
""" PACED Reading Pseudo text """
reading_ps_text_no_click = ['Die', 'jittste', 'Vonwendinsternes', 'meuninierte', 'Masiosen', 'von', 'Känschen', 'im',
                            'vannen', 'Kand,', 'die', 'sech', 'verlonlelten,', 'um', 'dieses', 'roktene',
                            'aschagahische', 'Uneimdis', 'erbipen', 'zu', 'nöhnen.', 'An', 'jesem', 'Tut', 'strouten',
                            'Stramen', 'von', 'Estrauers', 'zurehmen,', 'eibbegüstet', 'mit', 'trekiegten', 'Drollen',
                            'und', 'Temegloßen,', 'um', 'den', 'reauskundwenden', 'Homell', 'zu', 'ermißen,', 'wenn',
                            'der', 'Tond', 'die', 'Honze', 'gerdetzt.', 'In', 'Stoyten', 'wie', 'Bürchen,', 'Mamburs',
                            'und', 'Berban', 'önrogisierten', 'winale', 'Benausschafte', 'ärlendliche',
                            'Zeransporbumgen,', 'um', 'Rutethanenten', 'nentdundige', 'Rinträge', 'zu', 'vefen', 'und',
                            'mokit', 'das', 'Verstänkmas', 'für', 'dieses', 'Zalusknümomem', 'zu', 'verleinen.',
                            'Tritz', 'eikages', 'Wonlen', 'am', 'Rämmel', 'torrten', 'gaule', 'der', 'Kiefnehmer',
                            'einen', 'abehmeleivenden', 'Frick', 'auf', 'die', 'verborcherte', 'Honze', 'erkistren',
                            'und', 'erbipten', 'mokit', 'ein', 'harklich', 'einmadales', 'Schaufreil', 'der', 'Zagur.']