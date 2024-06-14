# TripPlanner
- Projekt za kolegij Informacijski sustavi
- Autor: *Iva Batur *
- JMBAG: 0269125088
- <img src="https://upload.wikimedia.org/wikipedia/hr/e/eb/Unipu-logo-lat.png"  width="4%" height="4%"> Sveučilište: Sveučilište Jurja Dobrile u Puli 

___
## Opis projekta
**TripPlanner** je web aplikacija dizajnirana za planiranje i praćenje putovanja. Glavne funkcionalnosti aplikacije uključuju dodavanje, pregledavanje, uređivanje i brisanje destinacija koje korisnik želi posjetiti. Omogućava unos detalja kao što su naziv destinacije, opis, lokacija i datum. Aplikacija također omogućuje označavanje posjećenih destinacija.
___

### Funkcionalnost
Aplikacija koristi lokalno skladište (localStorage) za pohranu podataka o destinacijama, što znači da podaci ostaju pohranjeni čak i kada korisnik zatvori preglednik. Korisnici mogu dodavati nove destinacije putem forme na početnoj stranici, koje se zatim prikazuju na stranici "Destinations". Tu mogu uređivati ili brisati destinacije prema potrebi.

### Opis strukture projekta 
#### static 
- skript.js- omogućuje korisnicima da dodaju nove destinacije putem forme, sprema te destinacije u lokalnu pohranu preglednika i automatski ažurira popis destinacija bez potrebe za slanjem podataka na server.
- style.css- sadrži stilove za web aplikaciju, definirajući izgled i dojam web stranica.

#### templates
- destinations.html-  prikazuje popis korisničkih destinacija i omogućuje interakciju s tim destinacijama kroz funkcionalnosti uređivanja, brisanja i označavanja kao posjećene. 
- index.html- sadrži osnovnu strukturu početne stranice koja korisnicima omogućuje dodavanje novih destinacija.
- interesting.html- Ova stranica korisnicima omogućuje pregled zanimljivih mjesta za posjetiti zajedno s slikama, pružajući inspiraciju i informacije za buduća putovanja 

# 
- .dockerignore-  specificira koje datoteke i direktoriji trebaju biti ignorirani od strane Dockera pri kreiranju slika, pomažući da veličina slike ostane mala i isključujući nepotrebne datoteke.
- Dockerfile- sadrži upute za izgradnju Docker slike web aplikacije, specificirajući osnovnu sliku, ovisnosti i naredbe za postavljanje.
- README.md- pruža važne informacije o projektu. Sadrži opis, funkcionalnosti te upute za instalaciju web aplikacije  
- Use case diagram.jpeg- Ova slikovna datoteka sadrži vizualni prikaz slučajeva upotrebe za web aplikaciju
- app.py- glavna Python aplikacijska datoteka, koja sadrži logiku na strani servera, definicije ruta i postavljanje aplikacije za TripPlanner web aplikaciju.
- docker-compose.yml- omogućuje definiranje i pokretanje višestrukih Docker kontejnera kao jednog aplikacijskog servisa
- models.py - definira model podataka za Flask aplikaciju koristeći SQLAlchemy, što je popularna biblioteka za rad s bazama podataka u Pythonu. 
- requirements.txt - osigurava konzistentnosti okruženja i izbjegava probleme s kompatibilnošću između različitih verzija paketa.
## 

## UseCase dijagram
![alt text](https://github.com/IvaBatur/TripPlanner/blob/main/Use%20case%20diagram.jpeg)

## Instalacija
```
cd ~/Downloads
git clone https://github.com/IvaBatur/TripPlanner.git
cd TripPlanner
```
```
docker build -t tripplanner .
docker ps
docker run -p 8080:8080 tripplanner
```

