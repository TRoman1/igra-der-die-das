# ***********************************************************************
# Ime programa: game_german.py                                          *
# Datum: 03. 11. 2024                                                   *
# Verzija: 1.0                                                          *
# Avtor: Roman Tušek                                                    *
# Opis: gre za igro s katero ponavljamo določne člene (der, die, das) v *
#       nemškem jeziku. Program poišče vse datoteke s končnico .csv v   *
#       mapi v kateri se izvaja Python program ter ponudi v izbiro eno  *
#       od teh datotek. Ko uporabnik izbere datoteko, program prebere   *
#       vsebino datoteke in v zanki generira naključno število v obsegu * 
#       elementov v datoteki ter izpisuje samostalnike za katere mora   *
#       uporabnik vnesti pravilen določen člen. Program sešteva         *
#       število pravilnih in napačnih odgovorov. V primeru vnos "end"   *
#       se izvajanje programa zaključi.                                 *
# ***********************************************************************

# Uvoz knjižnic oziroma modulov
import csv
import random
import os

# Definiranje spremenljivk 
csv_files_global = []           # Prazen seznam najdenih datotek v mapi
file_choosen_global = " "       # Spremenljivka za izbrano datoteko
data = []                       # Prazen seznam za shranjevanje vrstic
current_string = ""             # Prazen string
numb_correct_answers = 0
numb_wrong_answers = 0

# Funkcija za poisk datotek s končnico .csv v mapi, v kateri se izvaja Python program
def files_find():
    
    # Definiramo prazen seznam najdenih datotek v mapi
    csv_files = []

    # Dobi trenutno mapo, kjer se izvaja Python program
    current_dir = os.path.dirname(__file__)

    # Pridobi vse datoteke s končnico .csv v trenutni mapi
    csv_files = [file_1 for file_1 in os.listdir(current_dir) if file_1.endswith(".csv")]
    
    return csv_files
# Konec funkcije files_find()


# Funkcija v kateri uporabnik izbere določeno datoteko s podatki za igranje
def file_choose():
    
    print("Na voljo imate sledeče datoteke: ")
     
    counter_int = 0
    for file_1 in csv_files_global:
        print(str(counter_int) + " --- " + file_1)
        counter_int = counter_int +1

    while True:
        
        user_input = input("Izberi številko pred imenom željene datoteke! ")

        # Preverimo če je vnos ustrezen in znotraj meja
        try:
            file_choosen = int(user_input)  # Poskusimo pretvoriti v int
            if file_choosen >=0 and file_choosen <= counter_int:
                break
            else:
                print("To ni veljavno število!") 
        
        except ValueError:
            print("To ni veljaven vnos!")
     
    return file_choosen
# Konec funkcije file_choose()  
 


# Glavni del programa
print("")
print("Igra za vadenje določnih členov der, di, das:")

csv_files_global = files_find()  # Klic funkc., ki v nizu vrne imena vseh datotek s končnico .csv v mapi, v kateri se izvaja Python program

if len(csv_files_global) == 0:          # Najdena ni niti ena CSV datoteka v mapi
   
    print("Nobene CSV datoteke ni najdene v mapi!")

else:                                   # Najdena je vsaj ena CSV datoteka v mapi
    
    file_choosen_global = csv_files_global[file_choose()] # Izbrana datoteka

    # Odpremo datoteko v načinu branja
    with open(file_choosen_global, "r") as rfile:  
        # Uporabimo csv.reader, da preberemo vsako vrstico
        reader = csv.reader(rfile)
    
        # Preskočimo prvo vrstico (naslovi stolpcev)
        next(reader)  
    
        # Dodajamo vsako vrstico kot seznam v 'data'
        counter = 0
        for row in reader:
            data.append(row)
            counter = counter + 1

    print("Izbrana je bila datoteka: " + file_choosen_global)

    while True:

        random_number = random.randint(0,counter-1)

        current_string = data[random_number]

        # current_string[0].split(';'): values[0] vzame prvi (in edini) niz iz seznama values, nato pa .split(';') 
        # razdeli ta niz na tri dele, kjerkoli se pojavi podano ločilo ;.
        value1, value2, value3 = current_string[0].split(";")

        definite_article = input("Vnesi določni člen za besedo (end za konec): " + str(value2) + " : ")

        if definite_article.lower() == str(value1).lower():
            numb_correct_answers = numb_correct_answers + 1
            print(f"Pravilen odgovor! Število pravilnih: {numb_correct_answers}, število napačnih: {numb_wrong_answers}.")
    
        elif (definite_article.lower() == "der") or (definite_article.lower() == "die") or (definite_article.lower() == "das"):
            numb_wrong_answers = numb_wrong_answers + 1
            print(f"Napačen odgovor! Število pravilnih: {numb_correct_answers}, število napačnih: {numb_wrong_answers}.")
    
        elif definite_article.lower() == "end":
            print(f"Konec igre! Število pravilnih: {numb_correct_answers}, število napačnih: {numb_wrong_answers}.")
            break
    
        else:
            print("Napačen vnos!")

# Konec programa