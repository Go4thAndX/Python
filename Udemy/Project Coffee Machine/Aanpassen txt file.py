# Hier is een voorbeeld van Python-code die een bepaalde string kan zoeken in een externe tekstbestand en deze string kan aanpassen:
# In dit voorbeeld wordt de functie `zoek_en_vervang` gedefinieerd. Deze functie neemt een zoekterm, een vervangterm en een bestandsnaam als invoer. Het opent het opgegeven tekstbestand in de leesmodus, leest de inhoud en zoekt naar de zoekterm. Vervolgens wordt de zoekterm vervangen door de vervangterm. Daarna wordt het bestand opnieuw geopend in de schrijfmodus en wordt de aangepaste inhoud geschreven. Ten slotte wordt een bevestiging weergegeven dat de aanpassingen zijn voltooid.
# Je moet de waarden van `zoekterm`, `vervangterm` en `bestandsnaam` aanpassen aan je specifieke vereisten.


def zoek_en_vervang(zoekterm, vervangterm, bestandsnaam):
    # Open het bestand in de leesmodus
    with open(
        "G:\Mijn Drive\GoogleMap Python\Python Udemy\Projects\Project Coffee Machine\lists_test.txt",
        "r",
    ) as bestand:
        inhoud = bestand.read()

    # Zoek naar de zoekterm in de inhoud en vervang deze door de vervangterm
    aangepaste_inhoud = inhoud.replace(zoekterm, vervangterm)

    # Open het bestand in de schrijfmodus en schrijf de aangepaste inhoud
    with open(bestandsnaam, "w") as bestand:
        bestand.write(aangepaste_inhoud)

    print("Aanpassingen zijn voltooid.")


# Voorbeeldgebruik:
zoekterm = "oude string"
vervangterm = "nieuwe string"
bestandsnaam = "tekstbestand.txt"

zoek_en_vervang(zoekterm, vervangterm, bestandsnaam)
