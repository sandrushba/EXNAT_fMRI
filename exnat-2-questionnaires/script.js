// Define study
const study = lab.util.fromObject({
  "title": "root",
  "type": "lab.flow.Sequence",
  "parameters": {},
  "plugins": [
    {
      "type": "lab.plugins.Metadata",
      "path": undefined
    },
    {
      "type": "lab.plugins.Download",
      "filePrefix": "exnat-2-questionnaires",
      "path": undefined
    }
  ],
  "metadata": {
    "title": "EXNAT-2 Questionnaires",
    "description": "- Participant ID\n- Demographics (Age, Gender, Handedness, Health-related Qs, Reading\u002FSeeing\u002FListening Weaknesses)\n- SPQ-G (German Schizotypal Personality Questionnaire, 74 Items)\n- AQ-G (German Autism Spectrum Quotient Questionnaire, 50 Items)",
    "repository": "",
    "contributors": "Merle Schuckart"
  },
  "files": {},
  "responses": {},
  "content": [
    {
      "type": "lab.html.Page",
      "items": [
        {
          "type": "text",
          "title": "Persönlichkeits-Fragebogen",
          "content": ""
        },
        {
          "required": true,
          "type": "input",
          "label": "Bitte geben Sie hier Ihren Versuchspersonen-Code ein.",
          "help": "Der Code sieht in etwa so aus: part0001",
          "name": "ID"
        }
      ],
      "scrollTop": true,
      "submitButtonText": "Fragebogen starten",
      "submitButtonPosition": "right",
      "files": {},
      "responses": {
        "": ""
      },
      "parameters": {},
      "messageHandlers": {},
      "title": "ID"
    },
    {
      "type": "lab.html.Page",
      "items": [
        {
          "type": "text",
          "content": "Bevor das eigentliche Experiment startet, brauchen wir einige Informationen von Ihnen. Im folgenden finden Sie daher einige Fragebögen. Bitte füllen Sie die Fragebögen nach bestem Wissen und Gewissen aus. \n\u003Cbr\u003E\u003Cbr\u003E\nZur Erinnerung: Ihre Antworten werden nicht unter Ihrem Namen gespeichert, d.h. wir können bei der Analyse keine Rückschlüsse auf Ihre Person ziehen. ",
          "title": "Willkommen"
        }
      ],
      "scrollTop": true,
      "submitButtonText": "zum ersten Fragebogen →",
      "submitButtonPosition": "right",
      "files": {},
      "responses": {
        "": ""
      },
      "parameters": {},
      "messageHandlers": {},
      "title": "welcome"
    },
    {
      "type": "lab.html.Page",
      "items": [
        {
          "type": "text",
          "title": "Demographische Daten",
          "content": "\u003Cbr\u003EBevor das Experiment startet, benötige ich einige Informationen über Sie, um Ihre Ergebnisse später besser einordnen zu können. Bitte beantworten Sie hierzu die folgenden Fragen. \u003Cbr\u003E\u003Cbr\u003EBitte antworten Sie wahrheitsgemäß. Sollte Ihnen eine Frage unangenehm sein,  können Sie auch gern die Option \"Möchte ich nicht angeben.\" anklicken.\u003Cbr\u003E\u003Cbr\u003EZur Erinnerung: Ihre Daten werden anonymisiert gespeichert, d.h. ich kann keine Rückschlüsse auf einzelne Personen ziehen. \u003Cbr\u003E\u003Cbr\u003E\u003Cbr\u003E"
        },
        {
          "required": true,
          "type": "radio",
          "label": "Welchem Gender fühlen Sie sich am ehesten zugehörig?",
          "options": [
            {
              "label": "männlich",
              "coding": "m"
            },
            {
              "label": "weiblich",
              "coding": "f"
            },
            {
              "label": "divers",
              "coding": "nb"
            },
            {
              "label": "Möchte ich nicht angeben.",
              "coding": "no_ans"
            }
          ],
          "name": "gender",
          "help": ""
        },
        {
          "required": true,
          "type": "input",
          "label": "Wie alt sind Sie?",
          "attributes": {
            "type": "number",
            "min": "18",
            "max": "120",
            "step": "1"
          },
          "name": "age"
        },
        {
          "required": true,
          "type": "radio",
          "label": "Was ist Ihr höchster Bildungsabschluss?",
          "options": [
            {
              "label": "kein Schulabschluss"
            },
            {
              "label": "Hauptschulabschluss",
              "coding": "school_hauptschule"
            },
            {
              "label": "Realschulabschluss",
              "coding": "school_realschule"
            },
            {
              "label": "Fachhochschulreife \u002F Abitur"
            },
            {
              "label": "abgeschlossene Ausbildung",
              "coding": "apprentice"
            },
            {
              "label": "Bachelor\u002FMaster\u002FDiplom\u002FStaatsexamen",
              "coding": "undergrad"
            },
            {
              "label": "Dissertation",
              "coding": "diss"
            },
            {
              "label": "Habilitation",
              "coding": "habil"
            },
            {
              "label": "Möchte ich nicht angeben.",
              "coding": "no_ans"
            }
          ],
          "name": "education"
        },
        {
          "required": true,
          "type": "radio",
          "label": "Ist Deutsch Ihre Muttersprache?",
          "options": [
            {
              "label": "Ja",
              "coding": "True"
            },
            {
              "label": "Nein",
              "coding": "False"
            },
            {
              "label": "Möchte ich nicht angeben.",
              "coding": "False"
            }
          ],
          "name": "native_speaker"
        },
        {
          "required": true,
          "type": "radio",
          "label": "Haben Sie eine Leseschwäche?",
          "options": [
            {
              "label": "Ja",
              "coding": "True"
            },
            {
              "label": "Nein",
              "coding": "False"
            },
            {
              "label": "Möchte ich nicht angeben.",
              "coding": "no_ans"
            }
          ],
          "name": "reading_weakness"
        },
        {
          "required": true,
          "type": "radio",
          "label": "Haben Sie eine Sehschwäche?",
          "help": "Falls Sie eine Sehschwäche haben, aber gerade Kontaktlinsen tragen oder am Computer auch Sehhilfe alles gut lesen können, können Sie hier \"Nein\" anklicken.",
          "name": "seeing_impaired",
          "options": [
            {
              "label": "Ja",
              "coding": "True"
            },
            {
              "label": "Nein",
              "coding": "False"
            },
            {
              "label": "Möchte ich nicht angeben.",
              "coding": "no_ans"
            }
          ]
        },
        {
          "required": true,
          "type": "radio",
          "label": "Leiden Sie aktuell an einer psychologischen Erkrankung?",
          "help": "Es geht vor allem um Erkrankungen, die Ihre Sprachverarbeitung beeinträchtigen, Sie müde machen und\u002Foder Ihre Bewegungen beeinträchtigen. Hierzu gehören z.B. Schizophrenie, Depressionen und bipolare Störungen.",
          "options": [
            {
              "label": "Ja",
              "coding": "True"
            },
            {
              "label": "Nein",
              "coding": "False"
            },
            {
              "label": "Möchte ich nicht angeben.",
              "coding": "no_ans"
            }
          ],
          "name": "psych_disorder"
        },
        {
          "required": true,
          "type": "radio",
          "label": "Leiden Sie aktuell an einer neurologischen Störung?",
          "help": "z.B. Alzheimer Demenz, Morbus Parkinson oder Essentieller Tremor",
          "name": "neur_disorder",
          "options": [
            {
              "label": "Ja",
              "coding": "True"
            },
            {
              "label": "Nein",
              "coding": "False"
            },
            {
              "label": "Möchte ich nicht angeben.",
              "coding": "no_ans"
            }
          ]
        },
        {
          "required": true,
          "type": "radio",
          "label": "Hatten Sie schon einmal einen Schlaganfall (Hirninfarkt oder Hirnblutung) oder einen Hirntumor?",
          "options": [
            {
              "label": "Ja",
              "coding": "True"
            },
            {
              "label": "Nein",
              "coding": "False"
            },
            {
              "coding": "no_ans",
              "label": "Möchte ich nicht angeben."
            }
          ],
          "name": "stroke"
        },
        {
          "required": true,
          "type": "radio",
          "label": "Nehmen Sie aktuell Medikamente ein, die Sie müde machen?",
          "help": "Häufig müde machende Medikamente: einige Antidepressiva (bei Depressionen), Antidiabetika (bei Diabetes), Antihistaminika (bei Allergien), Beruhigungs- und Schlafmittel oder einige Erkältungmedikamente\u003Cbr\u003E\u003Cbr\u003E\nErklärung: Wenn Sie sich benommen fühlen, wirkt sich das auch auf Ihre Ergebnisse in dieser Studie aus. ",
          "options": [
            {
              "label": "Ja",
              "coding": "True"
            },
            {
              "label": "Nein",
              "coding": "False"
            },
            {
              "label": "Möchte ich nicht angeben.",
              "coding": "no_ans"
            }
          ],
          "name": "medicine"
        },
        {
          "required": true,
          "type": "radio",
          "label": "Haben Sie aktuell oder in den letzten 4 Wochen Drogen genommen?",
          "options": [
            {
              "label": "Ja",
              "coding": "True"
            },
            {
              "label": "Nein",
              "coding": "False"
            },
            {
              "label": "Möchte ich nicht angeben.",
              "coding": "no_ans"
            }
          ],
          "name": "drugs",
          "help": "z.B. Cannabis, Amphetamine (Speed), Ecstasy, Heroin, Kokain, Methamphetamin (Crystal Meth) oder LSD\u003Cbr\u003E\u003Cbr\u003E\nErklärung: Falls Sie aktuell oder in letzter Zeit Drogen konsumiert haben, kann das auch beeinflussen, wie Sie Reize verarbeiten. Das wiederum kann sich auf die Ergebnisse in dieser Studie auswirken."
        },
        {
          "required": true,
          "type": "radio",
          "label": "Haben Sie vor Beginn dieser Testung Alkohol getrunken?",
          "options": [
            {
              "label": "Ja",
              "coding": "True"
            },
            {
              "label": "Nein",
              "coding": "False"
            },
            {
              "label": "Möchte ich nicht angeben.",
              "coding": "no_ans"
            }
          ],
          "help": "Erklärung: Alkohol kann Ihre Reaktionsfähigkeit beeinträchtigen, was auch Ihre Ergebnisse in diesem Experiment beeinflussen kann. ",
          "name": "alcohol"
        },
        {
          "required": true,
          "type": "radio",
          "label": "Sind Sie eher links- oder rechtshändig?",
          "options": [
            {
              "label": "rechthändig",
              "coding": "r"
            },
            {
              "coding": "l",
              "label": "linkshändig"
            }
          ],
          "name": "handedness"
        },
        {
          "required": true,
          "type": "radio",
          "label": "Haben Sie eine Hörschwäche?",
          "options": [
            {
              "label": "Ja",
              "coding": "True"
            },
            {
              "label": "Nein",
              "coding": "False"
            },
            {
              "coding": "no_ans",
              "label": "Möchte ich nicht angeben."
            }
          ],
          "help": "",
          "name": "haben-sie-eine-horschwache"
        },
        {
          "required": true,
          "type": "radio",
          "label": "Tragen Sie eine Hörhilfe (Hörgerät oder Cochlear-Implantat)?",
          "options": [
            {
              "label": "Ja",
              "coding": "True"
            },
            {
              "label": "Nein",
              "coding": "False"
            },
            {
              "coding": "no_ans",
              "label": "Möchte ich nicht angeben."
            }
          ],
          "name": "CI_or_hearing_aid"
        }
      ],
      "scrollTop": true,
      "submitButtonText": "Weiter →",
      "submitButtonPosition": "right",
      "files": {},
      "responses": {
        "": ""
      },
      "parameters": {},
      "messageHandlers": {},
      "title": "demographics"
    },
    {
      "type": "lab.html.Page",
      "items": [
        {
          "type": "text",
          "title": "Edinburgh Handedness Inventory (EHI)",
          "content": "Bitte geben Sie Ihre Handpräferenz bei der Ausübung folgender Tätigkeiten bzw. bei der Benutzung folgender Objekte an, indem Sie in der entsprechenden Spalte ein ‚+‘ schreiben. Bitte markieren Sie ‚++‘, wenn Ihre Präferenz so stark ist, dass Sie nie versuchen würden, die andere Hand zu benutzen, es sei denn, Sie würden dazu gezwungen. Wenn Sie einmal wirklich nicht wissen, welche Hand Sie eher benutzen, schreiben Sie ein ‚+‘ in beide Spalten. \u003Cbr\u003E\u003Cbr\u003E\n\nEinige der aufgeführten Aktivitäten erfordern den Gebrauch beider Hände. In diesen Fällen ist in Klammern ein Teil der Aufgabe oder das Objekt angegeben, für das die Handpräferenz erfragt wird.\n\n\u003Cbr\u003E\u003Cbr\u003E\nBitte versuchen Sie alle Fragen zu beantworten. Lassen Sie nur die Frage offen, bei denen Sie keinerlei Erfahrung haben."
        },
        {
          "required": true,
          "type": "html",
          "content": " \u003C!DOCTYPE html\u003E\n\u003Chtml\u003E\n\u003Chead\u003E\n\u003Cstyle\u003E\ntable {\n  font-family: Arial, sans-serif;\n  border-collapse: collapse;\n  width: 100%;\n  margin: auto;\n}\n\ntd, th {\n  border: 1px solid #dddddd;\n  text-align: left;\n  padding: 15px;\n}\n\ntr:nth-child(even) {\n  background-color: #ebf5f7;\n}\n\u003C\u002Fstyle\u003E\n\u003C\u002Fhead\u003E\n\u003Cbody\u003E\n\n\n\n\u003Ctable\u003E\n  \u003Ctr\u003E\n    \u003Cth\u003E \u003C\u002Fth\u003E\n    \u003Cth\u003ELinke Hand (++)\u003C\u002Fth\u003E\n    \u003Cth\u003ELinke Hand (+)\u003C\u002Fth\u003E\n    \u003Cth\u003ERechte Hand (+)\u003C\u002Fth\u003E\n    \u003Cth\u003ERechte Hand (++)\u003C\u002Fth\u003E\n  \u003C\u002Ftr\u003E\n\n\n  \u003C!-- Repeat the following code for each item --\u003E\n  \u003Ctr\u003E\n    \u003Ctd\u003ESchreiben\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_01\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_01\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_01\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_01\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n  \u003C!-- end of item 1 --\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EZeichnen\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_02\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_02\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_02\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_02\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWerfen\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_03\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_03\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_03\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_03\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003ESchere\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_04\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_04\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_04\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_04\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EZahnbürste\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_05\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_05\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_05\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_05\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EMesser (ohne Gabel)\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_06\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_06\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_06\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_06\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003ELöffel\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_07\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_07\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_07\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_07\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EBesen (obere Hand)\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_08\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_08\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_08\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_08\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EStreichholz anzünden\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_09\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_09\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_09\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_09\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003ESchachtel öffnen (Deckel)\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_10\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_10\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_10\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"EHI_10\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E",
          "name": ""
        }
      ],
      "scrollTop": true,
      "submitButtonText": "Weiter →",
      "submitButtonPosition": "right",
      "files": {},
      "responses": {
        "": ""
      },
      "parameters": {},
      "messageHandlers": {},
      "title": "EHI (short)",
      "skip": true
    },
    {
      "type": "lab.html.Page",
      "items": [
        {
          "type": "text",
          "content": "Vielen Dank! Die nächsten Fragebögen sind etwas längere Persönlichkeitsfragebögen. Bitte antworten Sie auch hier nach bestem Wissen und Gewissen. \u003Cbr\u003EFalls Sie eine Frage nicht ganz eindeutig formuliert finden, antworten Sie einfach so, wie Sie sie verstehen."
        }
      ],
      "scrollTop": true,
      "submitButtonText": "Weiter zu den Persönlichkeitsfragebögen →",
      "submitButtonPosition": "right",
      "files": {},
      "responses": {
        "": ""
      },
      "parameters": {},
      "messageHandlers": {},
      "title": "questionnaire_info"
    },
    {
      "type": "lab.html.Page",
      "items": [
        {
          "type": "text",
          "content": "Sie werden im Folgenden eine Reihe von Aussagen und Fragen zu persönlichen Meinungen, Erlebnissen und Verhaltensweisen finden. Bitte geben Sie zu jeder Aussage oder Frage an, ob Sie ihr zustimmen oder nicht zustimmen. Antworten Sie bitte dabei so, wie es für Sie in den letzten Jahren im Allgemeinen zutrifft.\u003Cbr\u003E\u003Cbr\u003E",
          "title": "SPQ-G"
        },
        {
          "required": true,
          "type": "html",
          "content": "\u003C!--     \n    Table for all 74 SPQ Items\n\n      I divided the table into 7 parts (10 items in each, 14 in the last one) so you don't have to scroll all the way up to see which answer radio button has which label if you happen to forget it.\n\n      © Copyright 1999 Klein, Andresen & Jahn \u002F\u002F file d:\\agneuro\\spq-text.doc\n\n--\u003E\n\n\u003C!DOCTYPE html\u003E\n\u003Chtml\u003E\n\u003Chead\u003E\n\u003Cstyle\u003E\ntable {\n  font-family: Arial, sans-serif;\n  border-collapse: collapse;\n  width: 100%;\n  margin: auto;\n}\n\ntd, th {\n  border: 1px solid #dddddd;\n  text-align: left;\n  padding: 15px;\n}\n\ntr:nth-child(even) {\n  background-color: #ebf5f7;\n}\n\u003C\u002Fstyle\u003E\n\u003C\u002Fhead\u003E\n\u003Cbody\u003E\n\n\n\u003Ctable\u003E\n  \u003Ctr\u003E\n    \u003Cth\u003E \u003C\u002Fth\u003E\n    \u003Cth\u003E&nbsp;&nbsp;Ja&nbsp;&nbsp;\u003C\u002Fth\u003E\n    \u003Cth\u003ENein\u003C\u002Fth\u003E\n  \u003C\u002Ftr\u003E\n  \u003C!-- Repeat the following code for each item --\u003E\n  \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie manchmal das Gefühl, dass Dinge, die Sie im Fernsehen sehen oder in der Zeitung lesen, für Sie eine ganz besondere Bedeutung haben?\n    \u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_01_RI\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_01_RI\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n  \u003C!-- end of item 1 --\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch vermeide es manchmal, an Orte zu gehen, wo sich viele Menschen aufhalten, weil ich dort Angst bekomme.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_02_SA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_02_SA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie Erfahrungen mit dem Übersinnlichen gemacht?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_03_MD\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_03_MD\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie oftmals Gegenstände oder Schatten für Menschen gehalten, oder Geräusche für Stimmen?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_04_UW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_04_UW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EAndere Menschen halten mich für ein wenig seltsam.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_05_EV\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_05_EV\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch bin wenig daran interessiert, andere Menschen kennenzulernen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_06_KEF\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_06_KEF\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EAndere Leute finden es manchmal schwierig, zu verstehen, was ich sage.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_07_US\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_07_US\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EDie Leute finden mich manchmal unnahbar und distanziert.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_08_EA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_08_EA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch bin sicher, dass man hinter meinem Rücken über mich redet.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_09_AW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_09_AW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWenn ich zum Essen oder ins Kino ausgehe, merke ich, daß mich die Leute beobachten.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_10_RI\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_10_RI\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\u003C\u002Ftable\u003E\n\n\u003Cbr\u003E\u003Cbr\u003E\u003Cbr\u003E\n\n\u003Ctable\u003E\n  \u003Ctr\u003E\n    \u003Cth\u003E \u003C\u002Fth\u003E\n    \u003Cth\u003E&nbsp;&nbsp;Ja&nbsp;&nbsp;\u003C\u002Fth\u003E\n    \u003Cth\u003ENein\u003C\u002Fth\u003E\n  \u003C\u002Ftr\u003E\n\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch werde sehr nervös, wenn ich höfliche Konversation machen muss.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_11_SA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_11_SA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EGlauben Sie an Gedankenübertragung?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_12_MD\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_12_MD\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie jemals gespürt, dass irgendeine Person oder Kraft um Sie herum ist, auch wenn niemand zu sehen ist?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_13_UW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_13_UW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EDie Leute machen manchmal Bemerkungen über mein ungewöhnliches Gehabe und meine eigentümlichen Gewohnheiten.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_14_EV\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_14_EV\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch ziehe es vor, für mich allein zu bleiben.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_15_KEF\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_15_KEF\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWenn ich spreche, springe ich manchmal schnell von einem Thema zum anderen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_16_US\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_16_US\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch kann meine wahren Gefühle nicht gut durch meine Sprechweise und Mimik ausdrücken.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_17_EA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_17_EA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie oft das Gefühl, dass andere Leute es auf Sie abgesehen haben?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_18_AW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_18_AW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003ELassen manche Menschen Bemerkungen über Sie fallen, oder sagen sie Dinge mit einer doppelten Bedeutung?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_19_RI\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_19_RI\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWerden Sie jemals nervös, wenn jemand hinter Ihnen geht?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_20_SA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_20_SA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\u003C\u002Ftable\u003E\n\n\u003Cbr\u003E\u003Cbr\u003E\u003Cbr\u003E\n\n\u003Ctable\u003E\n  \u003Ctr\u003E\n    \u003Cth\u003E \u003C\u002Fth\u003E\n    \u003Cth\u003E&nbsp;&nbsp;Ja&nbsp;&nbsp;\u003C\u002Fth\u003E\n    \u003Cth\u003ENein\u003C\u002Fth\u003E\n  \u003C\u002Ftr\u003E\n\n\n  \u003Ctr\u003E\n    \u003Ctd\u003ESind Sie sich manchmal sicher, dass andere Menschen Ihre Gedanken lesen können?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_21_MD\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_21_MD\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWenn Sie einen Menschen anschauen oder sich selbst im Spiegel betrachten, haben Sie jemals beobachtet, daß sich das Gesicht vor ihren Augen verändert?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_22_UW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_22_UW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EManchmal denken andere Leute, daß ich ein bißchen merkwürdig bin.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_23_EV\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_23_EV\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIn Gegenwart anderer Menschen bin ich meistens ganz still.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_24_KEF\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_24_KEF\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch vergesse manchmal, was ich gerade zu sagen versuche.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_25_US\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_25_US\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch lache oder lächle selten.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_26_EA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_26_EA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EMachen Sie sich manchmal Sorgen darüber, ob Freunde oder Kollegen wirklich redlich und vertrauenswürdig sind ?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_27_AW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_27_AW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie jemals ein gewöhnliches Ereignis oder einen gewöhnlichen Gegenstand bemerkt, das oder der für Sie ein besonderes Zeichen darstellte?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_28_RI\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_28_RI\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWenn ich Menschen zum ersten Mal begegne, werde ich ängstlich.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_29_SA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_29_SA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EGlauben Sie an das Hellsehen?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_30_MD\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_30_MD\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\u003C\u002Ftable\u003E\n\n\u003Cbr\u003E\u003Cbr\u003E\u003Cbr\u003E\n\n\u003Ctable\u003E\n  \u003Ctr\u003E\n    \u003Cth\u003E \u003C\u002Fth\u003E\n    \u003Cth\u003E&nbsp;&nbsp;Ja&nbsp;&nbsp;\u003C\u002Fth\u003E\n    \u003Cth\u003ENein\u003C\u002Fth\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EIch höre oft eine Stimme meine Gedanken laut aussprechen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_31_UW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_31_UW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EManche Menschen denken, daß ich eine sehr wunderliche Person bin.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_32_EV\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_32_EV\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EIch finde es schwierig, einen engen emotionalen Kontakt zu anderen Menschen zu haben.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_33_KEF\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_33_KEF\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EBeim Sprechen schweife ich oft zu sehr ab.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_34_US\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_34_US\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EMeine \"nicht-sprachliche\" Kommunikation (z.B. Nicken oder Lächeln im Gespräch) ist nicht sehr ausgeprägt.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_35_EA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_35_EA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EIch spüre, dass ich selbst bei meinen Freunden auf der Hut sein muss.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_36_AW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_36_AW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003ESehen Sie manchmal besondere Bedeutungen in Anzeigen, Schaufenstern oder in der Art, wie Dinge um Sie herum angeordnet sind?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_37_RI\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_37_RI\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EFühlen Sie sich oft angespannt, wenn Sie sich in einer Gruppe fremder Menschen befinden?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_38_SA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_38_SA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EKönnen andere Menschen Ihre Gefühle fühlen, auch wenn sie gar nicht anwesend sind?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_39_MD\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_39_MD\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie jemals Dinge gesehen, die für andere Menschen unsichtbar waren?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_40_UW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_40_UW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\u003C\u002Ftable\u003E\n\n\u003Cbr\u003E\u003Cbr\u003E\u003Cbr\u003E\n\n\u003Ctable\u003E\n  \u003Ctr\u003E\n    \u003Cth\u003E \u003C\u002Fth\u003E\n    \u003Cth\u003E&nbsp;&nbsp;Ja&nbsp;&nbsp;\u003C\u002Fth\u003E\n    \u003Cth\u003ENein\u003C\u002Fth\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003ESind Sie der Meinung, dass es außerhalb Ihrer engsten Verwandtschaft niemanden gibt, dem Sie wirklich nahe stehen, oder daß es niemanden gibt, dem Sie vertrauen können oder mit dem Sie über persönliche Probleme reden können?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_41_KEF\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_41_KEF\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EManche Menschen finden, dass ich im Gespräch etwas unbestimmt und schwer zu begreifen bin.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_42_US\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_42_US\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EHöflichkeiten und gesellige Gesten kann ich nicht gut erwidern.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_43_EA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_43_EA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EErkennen Sie in dem, was andere sagen oder tun, oft versteckte Drohungen oder Demütigungen?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_44_AW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_44_AW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie während des Einkaufens das Gefühl, dass andere Menschen Notiz von Ihnen nehmen?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_45_RI\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_45_RI\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EUnter Menschen, die ich nicht näher kenne, fühle ich mich sehr unwohl.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_46_SA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_46_SA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EHatten Sie bereits Erfahrungen mit Astrologie, Vorhersehen der Zukunft,UFOs, übersinnlicher Wahrnehmung oder dem Sechsten Sinn?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_47_MD\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_47_MD\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EErscheinen alltägliche Gegenstände ungewöhnlich groß oder klein?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_48_UW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_48_UW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EBriefe an Freunde zu schreiben bringt mehr Schwierigkeiten als Gewinn.\n    \u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_49_KEF\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_49_KEF\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EIch benutze Worte manchmal in einer unüblichen Weise.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_50_US\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_50_US\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\u003C\u002Ftable\u003E\n\n\u003Cbr\u003E\u003Cbr\u003E\u003Cbr\u003E\n\n\u003Ctable\u003E\n\n  \u003Ctr\u003E\n    \u003Cth\u003E \u003C\u002Fth\u003E\n    \u003Cth\u003E&nbsp;&nbsp;Ja&nbsp;&nbsp;\u003C\u002Fth\u003E\n    \u003Cth\u003ENein\u003C\u002Fth\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWenn ich mich mit anderen unterhalte, neige ich dazu, den Blickkontakt zu vermeiden.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_51_EA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_51_EA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie die Erfahrung gemacht, dass es am besten ist, andere Leute nicht zu viel über Sie wissen zu lassen?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_52_AW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_52_AW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EWenn Sie sehen, dass andere Menschen sich unterhalten, fragen Sie sich dann öfters, ob sie sich über Sie unterhalten?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_53_RI\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_53_RI\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EIch würde mich sehr ängstlich fühlen, wenn ich vor einer großen Gruppe von Menschen eine Rede halten müßte.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_54_SA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_54_SA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie jemals das Gefühl gehabt, mit einer anderen Person mittels Gedankenübertragung zu kommunizieren?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_55_MD\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_55_MD\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWird Ihr Geruchssinn manchmal ungewöhnlich sensibel?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_56_UW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_56_UW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EBei geselligen Ereignissen neige ich dazu, im Hintergrund zu bleiben.\n    \u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_57_KEF\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_57_KEF\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003ENeigen Sie in einem Gespräch dazu, vom Thema abzukommen?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_58_US\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_58_US\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch habe oft das Gefühl, dass andere es auf mich abgesehen haben.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_59_AW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_59_AW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie manchmal das Gefühl, dass andere Menschen Sie beobachten?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_60_RI\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_60_RI\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n\u003C\u002Ftable\u003E\n\n\u003Cbr\u003E\u003Cbr\u003E\u003Cbr\u003E\n\n\u003Ctable\u003E\n\n  \u003Ctr\u003E\n    \u003Cth\u003E \u003C\u002Fth\u003E\n    \u003Cth\u003E&nbsp;&nbsp;Ja&nbsp;&nbsp;\u003C\u002Fth\u003E\n    \u003Cth\u003ENein\u003C\u002Fth\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EFühlen Sie sich jemals plötzlich von entfernten Geräuschen abgelenkt, die Sie normalerweise nicht wahrnehmen ?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_61_UW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_61_UW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EEnge Freunde zu haben bedeutet mir nicht viel.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_62_KEF\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_62_KEF\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie manchmal das Gefühl, dass die Leute über Sie reden?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_63_RI\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_63_RI\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003ESind Ihre Gedanken manchmal so stark, dass Sie sie fast hören können?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_64_UW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_64_UW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EMüssen Sie oft darauf acht geben, dass andere Sie nicht übervorteilen?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_65_AW\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_65_AW\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EHaben Sie das Gefühl, dass Sie mit anderen Menschen nicht \"warm\" werden können?\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_66_KEF\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_66_KEF\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch bin eine merkwürdige, ungewöhnliche Person.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_67_EV\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_67_EV\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EMeine Art zu reden ist weder ausdrucksvoll noch lebendig.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_68_EA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_68_EA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch finde es schwierig, meine Gedanken anderen klar mitzuteilen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_69_US\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_69_US\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch habe ein paar exzentrische Gewohnheiten.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_70_EV\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_70_EV\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EMir ist sehr unbehaglich zumute, wenn ich mit Leuten spreche, die ich nicht gut kenne.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_71_SA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_71_SA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EDie Leute sagen gelegentlich, dass das Gespräch mit mir verwirrend ist.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_72_US\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_72_US\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch neige dazu, meine Gefühle für mich zu behalten.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_73_EA\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_73_EA\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EManchmal starren mich die Leute wegen meines sonderbaren Auftretens an.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_74_EV\" value=\"1\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"SPQ_74_EV\" value=\"0\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n\u003C\u002Ftable\u003E\n\n\u003C\u002Fbody\u003E\n\u003C\u002Fhtml\u003E",
          "name": ""
        }
      ],
      "scrollTop": true,
      "submitButtonText": "Weiter →",
      "submitButtonPosition": "right",
      "files": {},
      "responses": {
        "": ""
      },
      "parameters": {},
      "messageHandlers": {},
      "title": "SPQ-G"
    },
    {
      "type": "lab.html.Page",
      "items": [
        {
          "type": "text",
          "title": "AQ-G",
          "content": "Nun folgt ein letzter Persönlichkeitsfragebogen. \u003Cbr\u003E\nBitte geben Sie auch hier wieder an, ob Sie den Aussagen zustimmen oder nicht zustimmen. Antworten Sie bitte dabei so, wie es für Sie in den letzten Jahren im Allgemeinen zutrifft.\n\u003Cbr\u003E\u003Cbr\u003E"
        },
        {
          "required": true,
          "type": "divider"
        },
        {
          "required": true,
          "type": "html",
          "content": "  \u003C!-- \n    \n    Table for all AQ Items\n\n      I divided the table into 2 parts so you don't have to scroll all the way up to see which answer radio button has which label if you happen to forget it.\n\n      Copyright:\n      Baron-Cohen, S., Wheelwright, S., Skinner, R., Martin, J., & Clubley, E. \n      AQ 50 – Autism Spectrum Quotient – Ages \u003E 16\n      German Version probably (?) by Jürgen Kremer - Universitätsklinikum Essen\n      I got the form from here: \n      https:\u002F\u002Fdocs.autismresearchcentre.com\u002Ftests\u002FAQ_Adult_German.pdf\n   --\u003E\n\n\n\n\u003C!DOCTYPE html\u003E\n\u003Chtml\u003E\n\u003Chead\u003E\n\u003Cstyle\u003E\ntable {\n  font-family: Arial, sans-serif;\n  border-collapse: collapse;\n  width: 100%;\n  margin: auto;\n}\n\ntd, th {\n  border: 1px solid #dddddd;\n  text-align: left;\n  padding: 15px;\n}\n\ntr:nth-child(even) {\n  background-color: #ebf5f7;\n}\n\u003C\u002Fstyle\u003E\n\u003C\u002Fhead\u003E\n\u003Cbody\u003E\n\n\n\n\u003Ctable\u003E\n  \u003Ctr\u003E\n    \u003Cth\u003E \u003C\u002Fth\u003E\n    \u003Cth\u003EStimme zu\u003C\u002Fth\u003E\n    \u003Cth\u003EStimme eher zu\u003C\u002Fth\u003E\n    \u003Cth\u003EStimme eher nicht zu\u003C\u002Fth\u003E\n    \u003Cth\u003EStimme nicht zu\u003C\u002Fth\u003E\n  \u003C\u002Ftr\u003E\n\n\n  \u003C!-- Repeat the following code for each item --\u003E\n  \u003Ctr\u003E\n    \u003Ctd\u003ERisiken gehe ich gerne ein.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E1\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E1\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E1\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E1\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n  \u003C!-- end of item 1 --\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EBrettspiele spiele ich gerne.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E2\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E2\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E2\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E2\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EEin Instrument spielen zu lernen, finde ich leicht.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E3\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E3\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E3\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E3\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EAndere Kulturen faszinieren mich.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E4\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E4\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E4\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_E4\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch mache Sachen lieber mit anderen als alleine.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_01\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_01\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_01\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_01\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch bevorzuge immer wieder dieselben Dinge, und Dinge immer wieder auf dieselbe Art und Weise zu machen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_02\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_02\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_02\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_02\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EWenn ich eine Idee habe, sehe ich davon sehr leicht ein auto-visualisiertes – imaginiertes – Bild.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_03\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_03\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_03\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_03\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIn Aufgaben vertiefe ich mich oft so sehr, dass mir alle anderen Dinge ringsherum nicht mehr bewusst sind.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_04\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_04\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_04\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_04\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch höre oft leise Geräusche, die andere nicht hören.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_05\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_05\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_05\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_05\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003ENummernschilder, Zeichen oder Symbole erwecken meine Assoziationen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_06\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_06\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_06\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_06\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EDas, was ich sage oder tue, wird gelegentlich als unkonventionell oder indiskret wahrgenommen, obwohl es nicht so beabsichtigt war.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_07\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_07\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_07\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_07\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EBei Geschichten stelle ich mir leicht vor,\nwie die Charaktere darin aussehen könnten.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_08\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_08\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_08\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_08\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EUhrzeiten und Datumsangaben faszinieren mich.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_09\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_09\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_09\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_09\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIn einer Diskussion kann ich gleichzeitig verschiedenen Beiträgen folgen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_10\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_10\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_10\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_10\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIn sozialen Situationen fühle ich mich wohl.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_11\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_11\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_11\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_11\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch nehme intensiv und öfters Details wahr als andere, weil ich Dinge von anderen Perspektiven aus wahrnehme.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_12\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_12\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_12\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_12\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch gehe lieber in eine Bibliothek als zu einer Party.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_13\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_13\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_13\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_13\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EEs fällt mir leicht zu fantasieren, und Geschichten zu erfinden.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_14\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_14\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_14\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_14\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch interessiere mich mehr für meine Mitmenschen als für Gegenstände, Räume oder Landschaften.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_15\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_15\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_15\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_15\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EMeine Neigungen entwickele ich aktiv, konstruktiv und zielorientiert, und bin glücklich, wenn dies möglich ist.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_16\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_16\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_16\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_16\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch genieße es, zu tratschen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_17\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_17\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_17\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_17\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWenn ich etwas vortrage, können mich andere kaum unter- brechen und es ist für das Publikum schwierig, mir zu folgen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_18\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_18\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_18\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_18\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EZahlen, Tabellen und Grafiken faszinieren mich.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_19\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_19\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_19\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_19\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EBei der Literatur, bei Hörspielen oder im Theater ist es für mich schwierig, die Absichten der Charaktere zu erraten.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_20\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_20\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_20\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_20\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch bevorzuge Sachbücher anstelle von Romane.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_21\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_21\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_21\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_21\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EEs ist für mich schwierig, neue Freundschaften zu schließen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_22\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_22\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_22\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_22\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EMir fallen Regelmäßigkeiten an Sachen oder Zusammenhängen auf.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_23\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_23\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_23\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_23\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch gehe lieber in ein Theater als in ein Museum.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_24\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_24\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_24\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_24\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch bin flexibel, wenn sich mein gewohnter Tagesablauf verändert.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_25\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_25\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_25\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_25\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\u003C\u002Ftable\u003E\n\n\u003Cbr\u003E\u003Cbr\u003E\u003Cbr\u003E\n\n\u003Ctable\u003E\n  \u003Ctr\u003E\n    \u003Cth\u003E \u003C\u002Fth\u003E\n    \u003Cth\u003EStimme zu\u003C\u002Fth\u003E\n    \u003Cth\u003EStimme eher zu\u003C\u002Fth\u003E\n    \u003Cth\u003EStimme eher nicht zu\u003C\u002Fth\u003E\n    \u003Cth\u003EStimme nicht zu\u003C\u002Fth\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch weiß oft nicht, wie ich eine Konversation aufrechterhalten soll.\n    \u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_26\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_26\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_26\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_26\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EZwischentöne – oder die eigentliche Botschaft – höre ich gut heraus; und kann gut „Zwischen den Zeilen lesen“.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_27\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_27\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_27\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_27\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n    \u003Ctr\u003E\n    \u003Ctd\u003EIch konzentriere mich mehr auf das Gesamtbild als auf Details.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_28\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_28\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_28\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_28\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003ETelefon- und Kontonummern vergesse ich schnell.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_29\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_29\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_29\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_29\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EKleine Veränderungen bei dem Erscheinungsbild von Personen oder in wiederkehrenden Situationen, bemerke ich kaum.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_30\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_30\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_30\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_30\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWenn ich mich unterhalte oder spiele, merke ich, wenn es anfängt, den anderen zu langweilen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_31\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_31\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_31\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_31\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EEs ist mir leicht, mehrere Sachen gleichzeitig zu tun.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_32\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_32\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_32\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_32\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWenn ich mich unterhalte, weiß ich nicht genau, wer gerade an der Reihe ist, das Wort zu ergreifen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_33\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_33\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_33\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_33\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch bin gerne spontan.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_34\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_34\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_34\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_34\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EBei einem Witz verstehe ich die Pointen oft als allerletzte\u002Fr.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_35\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_35\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_35\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_35\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWas jemand denkt oder fühlt, sehe ich an seinem Gesicht und Blick.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_36\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_36\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_36\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_36\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EWenn ich eine Pause mache oder unterbrochen werde, finde ich anschließend schnell wieder in eine angefangene Sache hinein.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_37\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_37\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_37\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_37\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EEs macht mir Freude, mit anderen einfach so dahin-zu-plaudern.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_38\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_38\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_38\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_38\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch spreche immer über dieselben Dinge oder tue dieselben Dinge.\n    \u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_39\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_39\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_39\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_39\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EAls ich jung war, spielte ich gerne Rollenspiele mit anderen Kindern.\n    \u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_40\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_40\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_40\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_40\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch sammele gerne Informationen und erforsche gerne Zusammenhänge in meinem Interessensgebiet.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_41\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_41\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_41\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_41\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EEs ist für mich schwierig, mich in andere hineinzuversetzen.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_42\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_42\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_42\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_42\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch plane alle Sachen immer sehr gründlich und bereite mich eingehend auf Aktivitäten oder Situationen vor.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_43\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_43\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_43\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_43\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003ESoziale Ereignisse oder Anlässe genieße ich.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_44\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_44\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_44\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_44\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EDie Absichten anderer zu erkennen oder voraus-zu-erahnen, ist für mich schwierig.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_45\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_45\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_45\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_45\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003ESituationen mit fremden Personen oder in unbekannten Räumen ängstigen mich.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_46\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_46\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_46\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_46\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch mache gerne neue Bekanntschaften.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_47\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_47\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_47\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_47\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EIch bin sehr diplomatisch.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_48\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_48\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_48\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_48\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EAn Geburtstage erinnere ich mich ungenau.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_49\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_49\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_49\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_49\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\n  \u003Ctr\u003E\n    \u003Ctd\u003EEs ist mir leicht, Phantasie-Spiele zu spielen, bei denen man schauspielern soll.\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_50\" value=\"2\"required\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_50\" value=\"1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_50\" value=\"-1\"\u003E\u003C\u002Ftd\u003E\n    \u003Ctd\u003E\u003Cinput type=\"radio\" name=\"AQ_50\" value=\"-2\"\u003E\u003C\u002Ftd\u003E\n  \u003C\u002Ftr\u003E\n\u003C\u002Ftable\u003E\n\n\u003C\u002Fbody\u003E\n\u003C\u002Fhtml\u003E",
          "name": ""
        }
      ],
      "scrollTop": true,
      "submitButtonText": "Weiter →",
      "submitButtonPosition": "right",
      "files": {},
      "responses": {
        "": ""
      },
      "parameters": {},
      "messageHandlers": {},
      "title": "AQ-G"
    },
    {
      "type": "lab.html.Page",
      "items": [
        {
          "type": "text",
          "title": "",
          "content": "Ende der Fragebögen, vielen Dank!\n\u003Cbr\u003E\nBitte klicken Sie auf \"Daten sichern\"."
        }
      ],
      "scrollTop": true,
      "submitButtonText": "Daten sichern →",
      "submitButtonPosition": "right",
      "files": {},
      "responses": {
        "": ""
      },
      "parameters": {},
      "messageHandlers": {},
      "title": "end"
    }
  ]
})

// Let's go!
study.run()