# Klas za upravlenie na sklad s avto chasti
class Sklad:
    # Tuk suzdavame prazen spisuk za chasti
    def __init__(self):
        self.chasti = []

    # Funkciq za dobavqne na nova chast
    def dobavi_chast(self, ime, kategoriya, cena, broy):
        # Pravim rechnik za edna chast
        chast = {
            "ime": ime,
            "kategoriya": kategoriya,
            "cena": cena,
            "broy": broy
        }

        # Dobavqme chastta v spisuka
        self.chasti.append(chast)

        # Suobshtenie za uspeshno dobavqne
        print("\nUspeshno dobavena chast:", ime)

    # Funkciq za pokazvane na vsichki chasti
    def pokazhi_vsichki_chasti(self):
        # Ako nqma chasti v spisuka
        if len(self.chasti) == 0:
            print("\nNqma dobaveni chasti.")
        else:
            print("\nVsichki chasti v sklada:")

            # Minavame prez vsqka chast i q printirame
            for chast in self.chasti:
                print("Ime:", chast["ime"], "| Kategoriya:", chast["kategoriya"], "| Cena:", chast["cena"], "lv. | Broy:", chast["broy"])

    # Funkciq za tursene na chast po ime
    def tursi_chast_po_ime(self, ime):
        namerena = False

        # Obhojdame vsichki chasti
        for chast in self.chasti:
            # Sravnqvame imenata
            if chast["ime"].lower() == ime.lower():
                print("\nNamerena chast:")
                print("Ime:", chast["ime"], "| Kategoriya:", chast["kategoriya"], "| Cena:", chast["cena"], "lv. | Broy:", chast["broy"])
                namerena = True

        # Ako ne e namerena
        if namerena == False:
            print("\nNqma takava chast.")

    # Funkciq za sortirane po cena vuzhodqshto
    def sortirai_po_cena_vuzhodqshto(self):
        # Sortira po cenata ot nai-malka kum nai-golqma
        self.chasti.sort(key=lambda chast: chast["cena"])

        print("\nChastite sa sortirani po cena (vuzhodqshto):")

        # Printira ime i cena
        for chast in self.chasti:
            print(chast["ime"], "-", chast["cena"], "lv.")

    # Funkciq za sortirane po cena nizhodqshto
    def sortirai_po_cena_nizhodqshto(self):
        # Sortira po cenata ot nai-golqma kum nai-malka
        self.chasti.sort(key=lambda chast: chast["cena"], reverse=True)

        print("\nChastite sa sortirani po cena (nizhodqshto):")

        # Printira ime i cena
        for chast in self.chasti:
            print(chast["ime"], "-", chast["cena"], "lv.")

    # Funkciq za pokazvane samo na nalichnite chasti
    def pokazhi_nalichni_chasti(self):
        ima_nalichni = False

        # Proverqvame dali ima pone edna chast s broy nad 0
        for chast in self.chasti:
            if chast["broy"] > 0:
                ima_nalichni = True

        # Ako ima nalichni, gi printirame
        if ima_nalichni == True:
            print("\nNalichni chasti:")
            for chast in self.chasti:
                if chast["broy"] > 0:
                    print(chast["ime"], "-", chast["cena"], "lv. - broy:", chast["broy"])
        else:
            print("\nNqma nalichni chasti.")

    # Funkciq za iztrivane na chast po ime
    def iztrii_chast(self, ime):
        namerena = False

        # Tursim chastta v spisuka
        for chast in self.chasti:
            if chast["ime"].lower() == ime.lower():
                self.chasti.remove(chast)
                print("\nUspeshno iztrita chast:", ime)
                namerena = True
                break

        # Ako ne e namerena
        if namerena == False:
            print("\nNqma takava chast za iztrivane.")

    # Funkciq za promqna na broq na dadena chast
    def promeni_broy(self, ime, nov_broy):
        namerena = False

        # Tursim chastta po ime
        for chast in self.chasti:
            if chast["ime"].lower() == ime.lower():
                chast["broy"] = nov_broy
                print("\nUspeshno promenen broy na chast:", ime)
                namerena = True
                break

        # Ako ne e namerena
        if namerena == False:
            print("\nNqma takava chast za redaktirane.")
