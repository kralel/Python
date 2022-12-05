import pandas as pd
import datetime as dt


try:
    input = pd.read_csv("vstup.csv", names=["ID", "QD", "datum", "průtok"], dtype={"datum":str, "průtok":float})
except IOError:
    print("Soubor nelze otevřít!")
    exit()
except ValueError:
    print("Chyba vstupních dat!")
    exit()



years = input.copy()
weeks = input.copy()

def getWeek(index):
    return int(index / 7)

try:
    years["datum"] = pd.to_datetime(years["datum"], format="%d.%m.%Y")
except ValueError:
    print("Špatný formát datumu!")
    exit()

years["průtok"] = years.groupby(years["datum"].dt.year)["průtok"].transform("mean")
years["průtok"] = round(years["průtok"], 4)

years["rok"] = years["datum"].dt.year
years = years.drop_duplicates(subset=["rok"], keep="first")

years.to_csv("vystup_rok.csv", columns=["ID", "QD", "datum", "průtok"], header=False, index=False, date_format="%d.%m.%Y", float_format="%.4f")


weeks["průtok"] = weeks.groupby(by=getWeek)["průtok"].transform("mean")
weeks["průtok"] = round(weeks["průtok"], 4)
weeks = weeks.iloc[::7]

weeks.to_csv("vystup_7dni.csv", header=False, index=False, float_format="%.4f")