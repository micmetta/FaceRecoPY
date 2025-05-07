
import face_recognition
import cv2
import numpy as np
import pickle
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF
import textwrap


face_locations = []
face_encodings = []
face_names = [1]
face_names[0] = "Sconosciuto"
process_this_frame = True
Cluster = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
Cluster[0] = ["Harrison Ford, Richard Gere, Chad Smith e Will Ferrel"]
Cluster[1] = ["Scarlett Johansson, Nicole Kidman, Isla Fisher e Amy Adams"]
Cluster[2] = ["Bradley Cooper e George Clooney"]
Cluster[3] = ["Abigail Breslin Train"]
Cluster[4] = ["Aaron Taylor-Johnson"]
Cluster[5] = ["Al Pacino e Woody Allen"]
Cluster[6] = ["Anthony Hopkins"]
Cluster[7] = ["Adam Sandler Train e Matthew McConaughey"]
Cluster[8] = ["Benedict Cumberbatch"]
Cluster[9] = ["Jennifer Lawrence, Emma Watson, Kety Perry e Zooey Deschanel"]
Cluster[10] = ["Alan Rickman"]
Cluster[11] = ["Robert Redford, Jeffrey Dean Morgan e Javier Bardem"]
Cluster[12] = ["Logan Marshall Green e Tom Hardy"]
Cluster[13] = ["Aaron Judge, Jim Carrey, Jeremy Renner e Johnny Deep"]
Cluster[14] = ["Matt Bomer e Henry Cavill"]
Cluster[15] = ["Aaron Paul"]
Cluster[16] = ["Michele Metta"]
Cluster[17] = ["Daniel Radcliffe, Orlando Bloom e Tom Hiddleston"]
Cluster[18] = ["Mila Kunis e Sarah Hyland"]
Cluster[19] = ["Bruce Willis e Micheal Keaton"]
Cluster[20] = ["Cobie Smulders, Angelina Jolie, Megan Fox"]
Cluster[21] = ["Samuel L.Jackson e Keanu Reevs"]
Cluster[22] = ["Alexandra Daddario"]
Cluster[23] = ["Andy Garcia, Nicola Nargiso e Matteo Mariano"]
Cluster[24] = ["Jennifer Aniston e Meryl Streep"]




#deserializzo il modello
#with open('modello-Ing(clf-bayesian-finale).pickle', 'rb') as mp:
#    classificatore = pickle.load(mp)

with open('modello-K-means-ALLDataset.pickle', 'rb') as mp:
    k_means = pickle.load(mp)

with open('modello-Ing(clf-KNN-FINALE).pickle', 'rb') as mp:
    classificatore = pickle.load(mp)



# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)


while True:
    # Grab a single frame of video
	#In questa riga prendo un singolo frame di video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
		#Con la riga di sotto trovo tutte le facce nel frame e mi memorizzo la locazione del volto nel frame e poi mi calcolo
        #le 128 features del volto. I 128 valori sono contenuti nella lista face_encodings.
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        #passo il vettore delle feature trovate per il volto corrente al classificatore che restituirà una predizione

        if(len(face_encodings) != 0):
            if (face_encodings[0].shape[0] == 128):
                Valore0 = face_encodings[0][0]
                Valore1 = face_encodings[0][1]
                Valore2 = face_encodings[0][2]
                Valore3 = face_encodings[0][3]
                Valore4 = face_encodings[0][4]
                Valore5 = face_encodings[0][5]
                Valore6 = face_encodings[0][6]
                Valore7 = face_encodings[0][7]
                Valore8 = face_encodings[0][8]
                Valore9 = face_encodings[0][9]
                Valore10 = face_encodings[0][10]
                Valore11 = face_encodings[0][11]
                Valore12 = face_encodings[0][12]
                Valore13 = face_encodings[0][13]
                Valore14 = face_encodings[0][14]
                Valore15 = face_encodings[0][15]
                Valore16 = face_encodings[0][16]
                Valore17 = face_encodings[0][17]
                Valore18 = face_encodings[0][18]
                Valore19 = face_encodings[0][19]
                Valore20 = face_encodings[0][20]
                Valore21 = face_encodings[0][21]
                Valore22 = face_encodings[0][22]
                Valore23 = face_encodings[0][23]
                Valore24 = face_encodings[0][24]
                Valore25 = face_encodings[0][25]
                Valore26 = face_encodings[0][26]
                Valore27 = face_encodings[0][27]
                Valore28 = face_encodings[0][28]
                Valore29 = face_encodings[0][29]
                Valore30 = face_encodings[0][30]
                Valore31 = face_encodings[0][31]
                Valore32 = face_encodings[0][32]
                Valore33 = face_encodings[0][33]
                Valore34 = face_encodings[0][34]
                Valore35 = face_encodings[0][35]
                Valore36 = face_encodings[0][36]
                Valore37 = face_encodings[0][37]
                Valore38 = face_encodings[0][38]
                Valore39 = face_encodings[0][39]
                Valore40 = face_encodings[0][40]
                Valore41 = face_encodings[0][41]
                Valore42 = face_encodings[0][42]
                Valore43 = face_encodings[0][43]
                Valore44 = face_encodings[0][44]
                Valore45 = face_encodings[0][45]
                Valore46 = face_encodings[0][46]
                Valore47 = face_encodings[0][47]
                Valore48 = face_encodings[0][48]
                Valore49 = face_encodings[0][49]
                Valore50 = face_encodings[0][50]
                Valore51 = face_encodings[0][51]
                Valore52 = face_encodings[0][52]
                Valore53 = face_encodings[0][53]
                Valore54 = face_encodings[0][54]
                Valore55 = face_encodings[0][55]
                Valore56 = face_encodings[0][56]
                Valore57 = face_encodings[0][57]
                Valore58 = face_encodings[0][58]
                Valore59 = face_encodings[0][59]
                Valore60 = face_encodings[0][60]
                Valore61 = face_encodings[0][61]
                Valore62 = face_encodings[0][62]
                Valore63 = face_encodings[0][63]
                Valore64 = face_encodings[0][64]
                Valore65 = face_encodings[0][65]
                Valore66 = face_encodings[0][66]
                Valore67 = face_encodings[0][67]
                Valore68 = face_encodings[0][68]
                Valore69 = face_encodings[0][69]
                Valore70 = face_encodings[0][70]
                Valore71 = face_encodings[0][71]
                Valore72 = face_encodings[0][72]
                Valore73 = face_encodings[0][73]
                Valore74 = face_encodings[0][74]
                Valore75 = face_encodings[0][75]
                Valore76 = face_encodings[0][76]
                Valore77 = face_encodings[0][77]
                Valore78 = face_encodings[0][78]
                Valore79 = face_encodings[0][79]
                Valore80 = face_encodings[0][80]
                Valore81 = face_encodings[0][81]
                Valore82 = face_encodings[0][82]
                Valore83 = face_encodings[0][83]
                Valore84 = face_encodings[0][84]
                Valore85 = face_encodings[0][85]
                Valore86 = face_encodings[0][86]
                Valore87 = face_encodings[0][87]
                Valore88 = face_encodings[0][88]
                Valore89 = face_encodings[0][89]
                Valore90 = face_encodings[0][90]
                Valore91 = face_encodings[0][91]
                Valore92 = face_encodings[0][92]
                Valore93 = face_encodings[0][93]
                Valore94 = face_encodings[0][94]
                Valore95 = face_encodings[0][95]
                Valore96 = face_encodings[0][96]
                Valore97 = face_encodings[0][97]
                Valore98 = face_encodings[0][98]
                Valore99 = face_encodings[0][99]
                Valore100 = face_encodings[0][100]
                Valore101 = face_encodings[0][101]
                Valore102 = face_encodings[0][102]
                Valore103 = face_encodings[0][103]
                Valore104 = face_encodings[0][104]
                Valore105 = face_encodings[0][105]
                Valore106 = face_encodings[0][106]
                Valore107 = face_encodings[0][107]
                Valore108 = face_encodings[0][108]
                Valore109 = face_encodings[0][109]
                Valore110 = face_encodings[0][110]
                Valore111 = face_encodings[0][111]
                Valore112 = face_encodings[0][112]
                Valore113 = face_encodings[0][113]
                Valore114 = face_encodings[0][114]
                Valore115 = face_encodings[0][115]
                Valore116 = face_encodings[0][116]
                Valore117 = face_encodings[0][117]
                Valore118 = face_encodings[0][118]
                Valore119 = face_encodings[0][119]
                Valore120 = face_encodings[0][120]
                Valore121 = face_encodings[0][121]
                Valore122 = face_encodings[0][122]
                Valore123 = face_encodings[0][123]
                Valore124 = face_encodings[0][124]
                Valore125 = face_encodings[0][125]
                Valore126 = face_encodings[0][126]
                Valore127 = face_encodings[0][127]

                y_pred = classificatore.predict([[Valore0, Valore1,Valore2,Valore3, Valore4,Valore5,Valore6,Valore7,Valore8,Valore9, Valore10,Valore11,
                                 Valore12, Valore13,Valore14,Valore15, Valore16,Valore17,Valore18, Valore19,Valore20,Valore21,
                                 Valore22,Valore23,Valore24,Valore25,Valore26,Valore27, Valore28,Valore29,
                                 Valore30, Valore31,Valore32,Valore33, Valore34,Valore35,
                                 Valore36, Valore37,Valore38, Valore39, Valore40, Valore41, Valore42, Valore43, Valore44, Valore45,
                                 Valore46, Valore47,
                                 Valore48, Valore49,Valore50, Valore51, Valore52, Valore53,
                                 Valore54, Valore55,Valore56,Valore57, Valore58,Valore59,Valore60, Valore61,Valore62,Valore63, Valore64,Valore65,
                                 Valore66, Valore67,Valore68, Valore69,Valore70,Valore71, Valore72,Valore73,Valore74,
                                 Valore75,Valore76,Valore77,Valore78,Valore79,Valore80, Valore81,Valore82,
                                 Valore83, Valore84,Valore85,Valore86, Valore87,Valore88,
                                 Valore89, Valore90, Valore91, Valore92, Valore93, Valore94, Valore95, Valore96, Valore97, Valore98,
                                 Valore99, Valore100,
                                 Valore101, Valore102, Valore103, Valore104, Valore105, Valore106,
                                 Valore107, Valore108,Valore109,Valore110, Valore111,Valore112,Valore113, Valore114,Valore115,Valore116, Valore117,Valore118,
                                 Valore119, Valore120,Valore121,Valore122, Valore123,Valore124,Valore125, Valore126,Valore127]])

                p = classificatore.predict_proba([[Valore0, Valore1,Valore2,Valore3, Valore4,Valore5,Valore6,Valore7,Valore8,Valore9, Valore10,Valore11,
                                 Valore12, Valore13,Valore14,Valore15, Valore16,Valore17,Valore18, Valore19,Valore20,Valore21,
                                 Valore22,Valore23,Valore24,Valore25,Valore26,Valore27, Valore28,Valore29,
                                 Valore30, Valore31,Valore32,Valore33, Valore34,Valore35,
                                 Valore36, Valore37,Valore38, Valore39, Valore40, Valore41, Valore42, Valore43, Valore44, Valore45,
                                 Valore46, Valore47,
                                 Valore48, Valore49,Valore50, Valore51, Valore52, Valore53,
                                 Valore54, Valore55,Valore56,Valore57, Valore58,Valore59,Valore60, Valore61,Valore62,Valore63, Valore64,Valore65,
                                 Valore66, Valore67,Valore68, Valore69,Valore70,Valore71, Valore72,Valore73,Valore74,
                                 Valore75,Valore76,Valore77,Valore78,Valore79,Valore80, Valore81,Valore82,
                                 Valore83, Valore84,Valore85,Valore86, Valore87,Valore88,
                                 Valore89, Valore90, Valore91, Valore92, Valore93, Valore94, Valore95, Valore96, Valore97, Valore98,
                                 Valore99, Valore100,
                                 Valore101, Valore102, Valore103, Valore104, Valore105, Valore106,
                                 Valore107, Valore108,Valore109,Valore110, Valore111,Valore112,Valore113, Valore114,Valore115,Valore116, Valore117,Valore118,
                                 Valore119, Valore120,Valore121,Valore122, Valore123,Valore124,Valore125, Valore126,Valore127]])

                pred_esempio = k_means.predict([[Valore0, Valore1,Valore2,Valore3, Valore4,Valore5,Valore6,Valore7,Valore8,Valore9, Valore10,Valore11,
                                 Valore12, Valore13,Valore14,Valore15, Valore16,Valore17,Valore18, Valore19,Valore20,Valore21,
                                 Valore22,Valore23,Valore24,Valore25,Valore26,Valore27, Valore28,Valore29,
                                 Valore30, Valore31,Valore32,Valore33, Valore34,Valore35,
                                 Valore36, Valore37,Valore38, Valore39, Valore40, Valore41, Valore42, Valore43, Valore44, Valore45,
                                 Valore46, Valore47,
                                 Valore48, Valore49,Valore50, Valore51, Valore52, Valore53,
                                 Valore54, Valore55,Valore56,Valore57, Valore58,Valore59,Valore60, Valore61,Valore62,Valore63, Valore64,Valore65,
                                 Valore66, Valore67,Valore68, Valore69,Valore70,Valore71, Valore72,Valore73,Valore74,
                                 Valore75,Valore76,Valore77,Valore78,Valore79,Valore80, Valore81,Valore82,
                                 Valore83, Valore84,Valore85,Valore86, Valore87,Valore88,
                                 Valore89, Valore90, Valore91, Valore92, Valore93, Valore94, Valore95, Valore96, Valore97, Valore98,
                                 Valore99, Valore100,
                                 Valore101, Valore102, Valore103, Valore104, Valore105, Valore106,
                                 Valore107, Valore108,Valore109,Valore110, Valore111,Valore112,Valore113, Valore114,Valore115,Valore116, Valore117,Valore118,
                                 Valore119, Valore120,Valore121,Valore122, Valore123,Valore124,Valore125, Valore126,Valore127]])

                print("Cluster:", pred_esempio)




#                print("Predizione fatta dal classificatore: ", y_pred[0])
#                print("Probabilità di appartenenza alle classi (logaritmica): ", p)
                if ((y_pred[0] == 1) and (np.any(p == 0))):#bisogna mettere np.any perchè quando si ha un vettore con molti valori
                    #per chiedere se anche uno solo uguale è uguale ad un altro bisogna utilizzare o np.any()
                    #(controlla se alcuni valori sono uguali ad un certo numero)
                    #oppure np.all() che da vero solo se tutti i suoi valori sono uguali ad un certo numero.
                    name = "Aaron Judge"
                elif ((y_pred[0] == 2) and (np.any(p == 0))):
                    name = "Aaron Paul"
                elif ((y_pred[0] == 3) and (np.any(p == 0))):
                    name = "Aaron Taylor-Johnson"
                elif ((y_pred[0] == 4) and (np.any(p == 0))):
                    name = "Abigail Breslin"
                elif ((y_pred[0] == 5) and (np.any(p == 0))):
                    name = "Adam Sandler"
                elif ((y_pred[0] == 6) and (np.any(p == 0))):
                    name = "Alan Rickman"
                elif ((y_pred[0] == 7) and (np.any(p == 0))):
                    name = "Alexandra Daddario"
                elif ((y_pred[0] == 8) and (np.any(p == 0))):
                    name = "Andy Garcia"
                elif ((y_pred[0] == 9) and (np.any(p == 0))):
                    name = "Anthony Hopkins"
                elif ((y_pred[0] == 10) and (np.any(p == 0))):
                    name = "Benedict Cumberbatch"
                elif ((y_pred[0] == 11) and (np.any(p == 0))):
                    name = "Al Pacino"
                elif ((y_pred[0] == 12) and (np.any(p == 0))):
                    name = "Bradley Cooper"
                elif ((y_pred[0] == 13) and (np.any(p == 0))):
                    name = "Bruce Willis"
                elif ((y_pred[0] == 14) and (np.any(p == 0))):
                    name = "George Clooney"
                elif ((y_pred[0] == 15) and (np.any(p == 0))):
                    name = "Harrison Ford"
                elif ((y_pred[0] == 16) and (np.any(p == 0))):
                    name = "Jennifer Aniston"
                elif ((y_pred[0] == 17) and (np.any(p == 0))):
                    name = "Jennifer Lawrence"
                elif ((y_pred[0] == 18) and (np.any(p == 0))):
                    name = "Jim Carrey"
                elif ((y_pred[0] == 19) and (np.any(p == 0))):
                    name = "Richard Gere"
                elif ((y_pred[0] == 20) and (np.any(p == 0))):
                    name = "Samuel L.Jackson"
                elif ((y_pred[0] == 21) and (np.any(p == 0))):
                    name = "Woody Allen"
                elif ((y_pred[0] == 22) and (np.any(p == 0))):
                    name = "Cobie Smulders"
                elif ((y_pred[0] == 23) and (np.any(p == 0))):
                    name = "Jeremy Renner"
                elif ((y_pred[0] == 24) and (np.any(p == 0))):
                    name = "Angelina Jolie"
                elif ((y_pred[0] == 25) and (np.any(p == 0))):
                    name = "Daniel Radcliffe"
                elif ((y_pred[0] == 26) and (np.any(p == 0))):
                    name = "Emma Watson"
                elif ((y_pred[0] == 27) and (np.any(p == 0))):
                    name = "Johnny Depp"
                elif ((y_pred[0] == 28) and (np.any(p == 0))):
                    name = "Keanu Reeves"
                elif ((y_pred[0] == 29) and (np.any(p == 0))):
                    name = "Megan Fox"
                elif ((y_pred[0] == 30) and (np.any(p == 0))):
                    name = "Nicole Kidman"
                elif ((y_pred[0] == 31) and (np.any(p == 0))):
                    name = "Orlando Bloom"
                elif ((y_pred[0] == 32) and (np.any(p == 0))):
                    name = "Tom Hiddleston"
                elif ((y_pred[0] == 33) and (np.any(p == 0))):
                    name = "Matthew McConaughey"
                elif ((y_pred[0] == 34) and (np.any(p == 0))):
                    name = "Meryl Streep"
                elif ((y_pred[0] == 35) and (np.any(p == 0))):
                    name = "Micheal Keaton"
                elif ((y_pred[0] == 36) and (np.any(p == 0))):
                    name = "Robert Redford"
                elif ((y_pred[0] == 37) and (np.any(p == 0))):
                    name = "Scarlett Johansson"
                elif ((y_pred[0] == 39) and (np.any(p == 0))):
                    name = "Chad Smith"
                elif ((y_pred[0] == 40) and (np.any(p == 0))):
                    name = "Will Ferrel"
                elif ((y_pred[0] == 41) and (np.any(p == 0))):
                    name = "Katy Perry"
                elif ((y_pred[0] == 42) and (np.any(p == 0))):
                    name = "Zooey Deschanel"
                elif ((y_pred[0] == 43) and (np.any(p == 0))):
                    name = "Jeffrey Dean Morgan"
                elif ((y_pred[0] == 44) and (np.any(p == 0))):
                    name = "Javier Bardem"
                elif ((y_pred[0] == 45) and (np.any(p == 0))):
                    name = "Matt Bomer"
                elif ((y_pred[0] == 46) and (np.any(p == 0))):
                    name = "Henry Cavill"
                elif ((y_pred[0] == 47) and (np.any(p == 0))):
                    name = "Logan Marshall-Green"
                elif ((y_pred[0] == 48) and (np.any(p == 0))):
                    name = "Tom Hardy"
                elif ((y_pred[0] == 49) and (np.any(p == 0))):
                    name = "Isla Fisher"
                elif ((y_pred[0] == 50) and (np.any(p == 0))):
                    name = "Amy Adams"
                elif ((y_pred[0] == 51) and (np.any(p == 0))):
                    name = "Mila Kunis"
                elif ((y_pred[0] == 52) and (np.any(p == 0))):
                    name = "Sarah Hyland"
                elif ((y_pred[0] == 53) and (np.any(p == 0))):
                    name = "Nicola Nargiso"
                elif ((y_pred[0] == 54) and (np.any(p == 0))):
                    name = "Michele Metta"
                elif ((y_pred[0] == 55) and (np.any(p == 0))):
                    name = "Matteo Mariano"
                else:
                    name = "Sconosciuto" #setto la variabile name a "Sconosciuto"

                print ("y_pred: ", y_pred)
                face_names[0] = name






    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size

        name = ''.join(name)
        print(name)
        if (name != "Sconosciuto" and name!= "Michele Metta" and name != "Matteo Mariano" and name != "Nicola Nargiso"):
            attore = name
            attore = attore.replace(" ", "_")


            query = """
                PREFIX dbo: <http://dbpedia.org/ontology/>
                SELECT ?abstract 
                WHERE {

                    <http://dbpedia.org/resource/""" + attore + """> dbo:abstract ?abstract .
                    FILTER langMatches( lang(?abstract), "en")
                }"""

            print(query)

            sparql = SPARQLWrapper("http://dbpedia.org/sparql")
            sparql.setReturnFormat(JSON)
            sparql.setQuery(query)  # the previous query as a literal string
            results = sparql.query().convert()

            if not results:
                risultato = []

            for result in results["results"]["bindings"]:
                risultato = result['abstract']['value']


            # ottengo 3  elementi della lista che erano divisi dal "."(punto),creo una nuova lista con questi elemeti
            # li unisco in una stringa e aggiungo i punti eliminati precedentemente.
            risultato = risultato.split('.', 3)
            i = 0
            result = ''
            my_list = risultato[0] + "." + risultato[1] + "."
            my_string = str(my_list)

            if ";" in my_string:
                my_stringa = my_string.split(";", 1)
                my_lista = my_stringa[0] + my_stringa[1]
                my_string = str(my_lista)
                my_string = my_string.split("/", 1)[0] + my_stringa[1]

            if ";" in my_string:
                my_stringo = my_string.split(";", 1)
                stringo = my_stringo[0]
                stringo = stringo.split("(", 1)
                my_lista = stringo[0] + "(" + my_stringo[1]
                my_string = str(my_lista)

            wrapper = textwrap.TextWrapper(width=50)

            word_list = wrapper.wrap(text=my_string)

            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            font_scale = 0.55
            margin = 8
            thickness = 1
            color = (255, 255, 255)
            font = cv2.FONT_HERSHEY_SIMPLEX
            # size = cv2.getTextSize( word_list[0], font, font_scale, thickness)
            # text_width = size[0][0]
            # text_height = size[0][1]
            # line_height = text_height + size[1] + margin
            # x = frame.shape[1] - margin - text_width
            # y = margin + size[0][1] * line_height
            # overlay = frame.copy()

            # Draw a label with a name below the face
            # cv2.rectangle(frame, (left, bottom + text_height), (right, bottom), (0, 0, 255), cv2.FILLED)

            i = 20

            right = 1
            bottom = 1
            left = 1
            for element in word_list:
                size = cv2.getTextSize(element, font, font_scale, thickness)
                text_width = size[0][0]
                text_height = size[0][1]
                cv2.rectangle(frame, (left, bottom - 6 - text_height + i), (text_width + 10, 6 - bottom + i),
                              (128, 255, 128), -1)
                cv2.putText(frame, element, (left, bottom + i), font, font_scale, color, thickness)
                i = i + 20



        else:
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.55
            margin = 5
            thickness = 2
            color = (255, 255, 255)
            size = cv2.getTextSize(name, font, font_scale, thickness)
            text_width = size[0][0]
            text_height = size[0][1]
            line_height = text_height + size[1] + margin
            x = frame.shape[1] - margin - text_width
            y = margin + size[0][1] * line_height

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 60), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left, bottom - 40), font, font_scale, color, thickness)

        # cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()




'''
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):

        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

'''