class Sklad:
   
    def __init__(self):
        self.chasti = []

    def dobavi_chast(self, ime, kategoriya, cena, broy):
    
        chast = {
            "ime": ime,
            "kategoriya": kategoriya,
            "cena": cena,
            "broy": broy
        }

        self.chasti.append(chast)

        print("\nUspeshno dobavena chast:", ime)

    def pokazhi_vsichki_chasti(self):
       
        if len(self.chasti) == 0:
            print("\nNqma dobaveni chasti.")
        else:
            print("\nVsichki chasti v sklada:")

            for chast in self.chasti:
                print("Ime:", chast["ime"], "| Kategoriya:", chast["kategoriya"], "| Cena:", chast["cena"], "eur. | Broy:", chast["broy"])

    def tursi_chast_po_ime(self, ime):
        namerena = False

        for chast in self.chasti:
        
            if chast["ime"].lower() == ime.lower():
                print("\nNamerena chast:")
                print("Ime:", chast["ime"], "| Kategoriya:", chast["kategoriya"], "| Cena:", chast["cena"], "eur. | Broy:", chast["broy"])
                namerena = True

        if namerena == False:
            print("\nNqma takava chast.")


    def sortirai_po_cena_vuzhodqshto(self):
        self.chasti.sort(key=lambda chast: chast["cena"])

        print("\nChastite sa sortirani po cena (vuzhodqshto):")

        for chast in self.chasti:
            print(chast["ime"], "-", chast["cena"], "eur.")

    def sortirai_po_cena_nizhodqshto(self):
        self.chasti.sort(key=lambda chast: chast["cena"], reverse=True)

        print("\nChastite sa sortirani po cena (nizhodqshto):")

        for chast in self.chasti:
            print(chast["ime"], "-", chast["cena"], "eur.")

    def pokazhi_nalichni_chasti(self):
        ima_nalichni = False

        for chast in self.chasti:
            if chast["broy"] > 0:
                ima_nalichni = True

        if ima_nalichni == True:
            print("\nNalichni chasti:")
            for chast in self.chasti:
                if chast["broy"] > 0:
                    print(chast["ime"], "-", chast["cena"], "eur. - broy:", chast["broy"])
        else:
            print("\nNqma nalichni chasti.")

    def iztrii_chast(self, ime):
        namerena = False

        for chast in self.chasti:
            if chast["ime"].lower() == ime.lower():
                self.chasti.remove(chast)
                print("\nUspeshno iztrita chast:", ime)
                namerena = True
                break

        if namerena == False:
            print("\nNqma takava chast za iztrivane.")

    def promeni_broy(self, ime, nov_broy):
        namerena = False

        for chast in self.chasti:
            if chast["ime"].lower() == ime.lower():
                chast["broy"] = nov_broy
                print("\nUspeshno promenen broy na chast:", ime)
                namerena = True
                break

        if namerena == False:
            print("\nNqma takava chast za redaktirane.")
