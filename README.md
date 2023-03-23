Aktuálny stav kódu na RPi. (ls_dashboard-main):

- Program ktorý sa spúšťa = AIMS_LS_Dashboard.ipynb
- Všetky nami nadefinované funkcie = AIMS_LS_library.py
- Všetky dodatočné knižnice = requirements.py
- Obrázky sú v zložke  = assets
- Väčšina nastavaní už je v zložke = config
- Nastavenie farieb = colours.py
- Nastavenie písma  = fonts.py
- Nastavenie veľkostí okien a pod. = sizes.py
- Nastavenie dôb obnovy a pod. = timings.py
- Dáta ktoré si ťahá sú v zložke = dataframes
- Ak by chcelo niečo outputovať, tak do zložky = output
- Ak by si niečo dočasne ukladal, tak do zložky = temp

\

Hlavná štruktúra kódu je:
- Úvodné importy
- Vytvoria sa layouty jednotlivých blokov aj s nastavením.
- Tieto bloky sa spolu spoja a nastavia sa ich pozície a pod.
- Nadefinujú sa funkcie ktoré obnovujú informácie v dashboarde (Bola jedna veľká, teraz má každý blok vlastnú, možno sa to opäť hodí do jednej [úspora CPU času]).
- Spustenie
- Aktuálne je obnova každých 10 sekúnd a len berie postupne údaje z syntetického dataframu.
 
\

Čo nefunguje aktuálne:
- Zobrazenie šípky na smer vetra.
- Škály na grafoch.
- Stredovanie niektorých blokov.
 
\

Konkrétne úlohy ktoré je potrebné na DASH-boarde vykonať:
- Na graf smeru vetra použiť plotly plotly quiver.
- Prepísať stupnice z matplotlib na px.bar.
- Na polkruhovú stupnicu použiť plotly Indicator.
- Pridať logá.
- Volania na obnovu dať do jednej funckie (urýchlenie aby sa dataframe nemusel viac krát načítať). Následne volanie na obnovu budú na jednu funkciu ktorá len zavolá všetky ostatné.
- Preniesť veľkosti a rozmery do config súboru.
- Slnečný svit urobiť lepšie ako je len číslo. Niečo na štýl meniaceho sa obrázku (ako je veterná ponožka).
