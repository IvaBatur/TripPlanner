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



- .dockerignore-  specificira koje datoteke i direktoriji trebaju biti ignorirani od strane Dockera pri kreiranju slika, pomažući da veličina slike ostane mala i isključujući nepotrebne datoteke.
- 
