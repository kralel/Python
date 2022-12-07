# Domácí úkol 2 - Výpočet sedmidenního a ročního průměrného průtoku

Pro vybranou řeku program z průměrného denního průtoku dovede vypočítat sedmidenní a roční průtok. Vstupní data je potřeba uložit ve formátu .csv a musí být pojmenován jako "vstup.csv". Soubor však musí být uložen ve stejné složce jako samotný program, jinak se program nepodaří spustit.

Data je za potřebí uvést v tomto formátu (viz příklad):
    
    
    150000,QD,01.11.1980,   2.3700
    150000,QD,02.11.1980,   1.6500
    150000,QD,03.11.1980,   1.6500
    150000,QD,04.11.1980,   2.1800
    



Při spuštění se mohou vyskytnou tyto chyby a jejich příčina:
  1) "Soubor nelze otevřít!" - soubor se nachází v jiné složce, jiný název souboru
  2) "Chyba vstupních dat!" - data v sloupcích jsou jiného formátu (typu)
  3) "Prázdný soubor!" - správně pojmenovaný soubor ale bez vstupních dat
  4) "Špatný formát datumu!" - datum není ve formátu "den.měsíc.rok"




Výstupní data jsou uložena ve stejném formátu jako vstupní a jsou pojmenovány následovně:
  1) "vystup_rok" - roční průměrný průtok k prvnímu datu daného roku
  2) "vystup_7dni" - sedmidenní průměrný průtok po sedmi dnech od začátku vstupních dat


Program dokáže vypočítat i "maximální" a "minimální" průtok za celé pozorované období a vypíše je do terminálu.
