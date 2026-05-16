# Vnasqme klasa Sklad ot faila models.py
from models import Sklad


# Funkciq za vuvejdane na chislo
def vuvedi_chislo(suobshtenie):
    while True:
        vhod = input(suobshtenie)

        # Proverka dali vavedenoto e chislo
        if vhod.isdigit():
            return int(vhod)
        else:
            print("Molq, vuvedete chislo.")


# Suzdavame obekt ot klasa Sklad
sklad = Sklad()

# Dobavqme nqkolko nachalni chasti
sklad.dobavi_chast("Maslen filtur", "Filtri", 12, 8)
sklad.dobavi_chast("Vuzdushen filtur", "Filtri", 18, 5)
sklad.dobavi_chast("Spirachni nakladki", "Spirachki", 45, 3)
sklad.dobavi_chast("Akumulator", "Elektro", 120, 0)

# Bezkraen cikul za menuto
while True:
    print("\n--- SKLADOVA NALICHNOST ZA AVTO CHASTI ---")
    print("1. Pokazvane na vsichki chasti")
    print("2. Dobavqne na nova chast")
    print("3. Tursene na chast po ime")
    print("4. Sortirane po cena (vuzhodqshto)")
    print("5. Sortirane po cena (nizhodqshto)")
    print("6. Pokazvane samo na nalichnite chasti")
    print("7. Iztrivane na chast")
    print("8. Promqna na broy")
    print("9. Izhod")

    # Chetem izbora na potrebitelq
    izbor = input("Izberete opciq: ")

    # Opciq 1 - pokazva vsichki chasti
    if izbor == "1":
        sklad.pokazhi_vsichki_chasti()

    # Opciq 2 - dobavq nova chast
    elif izbor == "2":
        ime = input("Vuvedete ime na chastta: ")
        kategoriya = input("Vuvedete kategoriya: ")
        cena = vuvedi_chislo("Vuvedete cena: ")
        broy = vuvedi_chislo("Vuvedete broy: ")
        sklad.dobavi_chast(ime, kategoriya, cena, broy)

    # Opciq 3 - tursi chast po ime
    elif izbor == "3":
        ime = input("Vuvedete ime za tursene: ")
        sklad.tursi_chast_po_ime(ime)

    # Opciq 4 - sortira po cena vuzhodqshto
    elif izbor == "4":
        sklad.sortirai_po_cena_vuzhodqshto()

    # Opciq 5 - sortira po cena nizhodqshto
    elif izbor == "5":
        sklad.sortirai_po_cena_nizhodqshto()

    # Opciq 6 - pokazva samo nalichnite chasti
    elif izbor == "6":
        sklad.pokazhi_nalichni_chasti()

    # Opciq 7 - trie chast
    elif izbor == "7":
        ime = input("Vuvedete ime na chastta za iztrivane: ")
        sklad.iztrii_chast(ime)

    # Opciq 8 - promenq broq na chast
    elif izbor == "8":
        ime = input("Vuvedete ime na chastta: ")
        nov_broy = vuvedi_chislo("Vuvedete nov broy: ")
        sklad.promeni_broy(ime, nov_broy)

    # Opciq 9 - izhod ot programata
    elif izbor == "9":
        print("Krai na programata.")
        break

    # Ako e vavedena greshna opciq
    else:
        print("Nevaliden izbor. Opitaite otnovo.")
