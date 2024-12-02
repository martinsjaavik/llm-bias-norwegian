import pandas as pd

# Filnavn
file_name = "dataset.csv"

# Last inn CSV-filen
df = pd.read_csv(file_name)

# Ordene vi skal sjekke for
keywords = ["kvinnene", "mennene", "folkene", "menneskene", "mennesker"]

# Mapping fra entall til flertall for attributter
singular_to_plural = {
    "effektiv": "effektive",
    "ueffektiv": "ueffektive",
    "vennlig": "vennlige",
    "uvennlig": "uvennlige",
    "kompetent": "kompetente",
    "inkompetent": "inkompetente",
    "smart": "smarte",
    "dum": "dumme",
    "gjestfri": "gjestfrie",
    "ugjestfri": "ugjestfrie",
    "innovativ": "innovative",
    "fantasiløs": "fantasiløse",
    "målrettet": "målrettede",
    "uorganisert": "uorganiserte",
    "varmehjertet": "varmehjertede",
    "kaldhjertet": "kaldhjertede",
    "elskverdig": "elskverdige",
    "ubehagelig": "ubehagelige",
    "veloppdragen": "veloppdragne",
    "uhøflig": "uhøflige",
    "kunnskapsrik": "kunnskapsrike",
    "uviten": "uvitende",
    "formell": "formelle",
    "uformell": "uformelle",
    "opptatt": "opptatte",
    "bekymringsløs": "bekymringsløse",
    "kameratslig": "kameratslige",
    "forsiktig": "forsiktige",
    "ekstrovert": "ekstroverte",
    "folkelig": "folkelige",
    "frimodig": "frimodige",
    "morsom": "morsomme",
    "leken": "lekne",
    "alvorlig": "alvorlige",
    "streng": "strenge",
    "uforutsigbar": "uforutsigbare",
    "lystig": "lystige",
    "introvert": "introverte"
}
### ALLE ATTRIBUTER

# Funksjon for å sjekke om en tekst inneholder noen av søkeordene
def contains_keywords(text, keywords):
    if isinstance(text, str):  # Sjekk om tekst er en streng
        text = text.lower()  # Konverter til små bokstaver
        return any(keyword in text for keyword in keywords)
    return False

# Finn rader hvor "context_norwegian" inneholder noen av søkeordene
matches = df[df["context_norwegian"].apply(lambda x: contains_keywords(x, keywords))]

# Hvis det finnes treff, bruk replace på kolonnene
if not matches.empty:
    print("Rader som matcher søkeordene funnet. Endrer tekst i relevante kolonner...")

    # Kolonner å oppdatere
    columns_to_update = ["stereotype", "anti_stereotype", "unrelated"]

    # Utfør erstatning i hver relevant kolonne for matchende rader
    for col in columns_to_update:
        df.loc[matches.index, col] = df.loc[matches.index, col].replace(singular_to_plural, regex=True)

    # Lagre oppdatert fil
    output_file = "updated_dataset.csv"
    df.to_csv(output_file, index=False)
    print(f"Endringer fullført. Oppdatert fil lagret som {output_file}.")
else:
    print("Ingen rader inneholder de angitte ordene.")
