Herstel: Ik bereken voor mast M1205 met het aangepaste bodemmodel 59N uit onderstaande Excel, Ra=2,2Ohm ipv Ra<1Ohm, zoals hieronder gesteld. Groeten, Michel

**Van:** Dagelinckx, Michel <michel.dagelinckx@tennet.eu>
**Verzonden:** dinsdag 27 mei 2025 17:00
**Aan:** Koppes, Juriaan <juriaan.koppes@croonwolterendros.nl>; Mos, Wouter <Wouter.Mos@tennet.eu>; Kees Post <c.f.post@lambdaengineering.nl>
**Onderwerp:** RE: EMC Tilburg

Heren,

Weergave Juriaan hieronder klopt, afgezien van naam aannemer; dat is DNV ipv RHDHV.

Ten aanzien van onderdeel 4.1 stuur ik jullie een pdf van de E-mail wisseling tussen collega Harald Prins en mij over de soortelijke bodemweerstand metingen en de twijfels die we hierbij hebben. Ik heb dit zelf ook weer eens doorgelezen en geconstateerd dat het probleem hiermee vooral de hoge soortelijke bodemweerstand van de diepe laag is. Hiermee wordt kennelijk een Ra van het station berekend die 0,931 Ohm bedraagt, terwijl uitgangspunt voor een station maximaal 0,1 Ohm is. Dat is op zich al vreemd; en te bedenken dat mast 1205 alleen al een Ra kleiner dan 1 Ohm heeft. Als je vervolgens in dat stationsaardnet 29,1kA kortsluitstroom in injecteert, kom je op een GPR van 29,1k*0,931=27,1kV. Dat is een super hoge spanning, waarmee wij problemen met kabels en leidingen in de omgeving verwachten te krijgen.

Voor de goede orde heb ik ook een Excelsheet toegevoegd waarin een overzicht gegeven is van alle ons beschikbare meetgegevens. Mijns inziens is niet zinvol om nog meer metingen ter plaatse te gaan doen.

Met vriendelijke groeten / Kind regards / Mit freundlichen Grüßen,

**Ir. M.H.P. (Michel) Dagelinckx**

EMC Engineer

Large Projects Netherlands Engineering | ZuidWest-Oost | Standaardisatie EMC

*Twee dagen per week (in principe op dinsdag en donderdag) werkzaam voor TenneT; anders via *[*michel@demad.nl*](mailto:michel@demad.nl "mailto:michel@demad.nl")* bereikbaar*

| | **M** | +31 (0)6 21 81 52 09                                                                             |
| -------- | -------------------------------------------------------------------------------------------------- |
| **E** | [Michel.Dagelinckx@tennet.eu](mailto:Michel.Dagelinckx@tennet.eu "mailto:Michel.Dagelinckx@tennet.eu") |
| **I** | [../../../../../802576/Desktop/www.tennet.eu]**www.tennet.eu**                                  |
|        |                                                                                                  |

| ![]() | TenneT TSO B.V.``Utrechtseweg 310``Arnhem``Postbus 718``6800 AS Arnhem``Nederland |
| --- | -------------------------------------------------------------------------------------------------------------------- |

**Handelsregister:** Arnhem  09155985

Denk aan het milieu. Print dit bericht alleen als het noodzakelijk is.

**Van:** Koppes, Juriaan <[juriaan.koppes@croonwolterendros.nl](mailto:juriaan.koppes@croonwolterendros.nl "mailto:juriaan.koppes@croonwolterendros.nl")>
**Verzonden:** dinsdag 27 mei 2025 15:15
**Aan:** Mos, Wouter <[Wouter.Mos@tennet.eu](mailto:Wouter.Mos@tennet.eu "mailto:Wouter.Mos@tennet.eu")>; Dagelinckx, Michel <[michel.dagelinckx@tennet.eu](mailto:michel.dagelinckx@tennet.eu "mailto:michel.dagelinckx@tennet.eu")>; Kees Post <[c.f.post@lambdaengineering.nl](mailto:c.f.post@lambdaengineering.nl "mailto:c.f.post@lambdaengineering.nl")>
**Onderwerp:** [EXTERNAL] RE: EMC Tilburg

Mannen, Als resultaat van onze meeting van zojuist; hierbij een korte samenvatting op basis van de inhoud van het memo. 4. 1 Nieuwe wenner meting is niet zilvol ivm reeds aangelegde aardnet. TenneT vindt de aannames worst case (500 ohm*meter). 

ZjQcmQRYFpfptBannerStart

| | | **This message is from an external sender| Dit bericht is van een externe afzender | Diese Nachricht stammt von einem externen Absender** |
| -------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                            |

|  |
| - |

|  |
| - |

ZjQcmQRYFpfptBannerEnd

Mannen,

Als resultaat van onze meeting van zojuist; hierbij een korte samenvatting op basis van de inhoud van het memo.

4.1

Nieuwe wenner meting is niet zilvol ivm reeds aangelegde aardnet.

* TenneT vindt de aannames worst case (500 ohm*meter). Daardoor is een robuust aardnet aangelegd. Dit kan negatief uitwerken op de ‘ground potential rise’.  Michiel stuurt mailwisseling hierover door voor achtergrond.
* Ground potential rise moet berekend worden (kilovolts)
* Weerstandsbeinvloeding moet bepaald worden vanuit CDEGS
* Dit moet geplot worden op het terrein en actuele KLIC

Risico-objecten nu alvast gezien:

* Middenspanningskabel
* Oude aansluiting boerderij (verlaten)

SC&M gaat onderzoeken of we dit kunnen doen, echter is de voormelding dat beschikbaarheid van capaciteit met specifieke kennis beperkt is.

4.3 Gaat RHDHV doen. Vraag aan SC&M vervalt vooralsnog.

4.4 Gaat RHDHV doen. Vraag aan SC&M vervalt vooralsnog.

Bedankt voor het overleg; indien uit 4.1 meer informatie beschikbaar is hebben Wouter en ondergetekende contact.

Met vriendelijke groet,

**ing. J.J.T. (Juriaan) Koppes**
Projectmanager

M +31630065064** |** [juriaan.koppes@croonwolterendros.nl](mailto:juriaan.koppes@croonwolterendros.nl "mailto:juriaan.koppes@croonwolterendros.nl")

**From:** Mos, Wouter <[Wouter.Mos@tennet.eu](mailto:Wouter.Mos@tennet.eu "mailto:Wouter.Mos@tennet.eu")>
**Sent:** donderdag 13 maart 2025 16:13
**To:** Koppes, Juriaan <[juriaan.koppes@croonwolterendros.nl](mailto:juriaan.koppes@croonwolterendros.nl "mailto:juriaan.koppes@croonwolterendros.nl")>
**Subject:** EMC Tilburg

Hoi Juriaan,

Zoals net besproken bij dezen de bijgesloten notitie en de vraag of jullie iets kunnen betekenen voor de geel gearceerde delen.

Neem de inhoud even rustig tot je en dan hebben we volgende week hier nog wel contact over.

Ter info: de berekening van de 100uT contour wilde ik bewust niet aan jullie vragen. We hebben een 0,4uT contour en in mijn beleving kan met een stukje rework hier de 100uT contour uit worden gehaald. Dit zal naar alle waarschijnlijkheid altijd binnen de hekken zijn.

Mocht je vragen hebben dan hoor ik het graag en alvast bedankt.

Met vriendelijke groeten / Kind regards / Mit freundlichen Grüßen,

**Ing. W. (Wouter) Mos**

Technisch Manager

Large Projects (LPN-ENG-TM)

*Aanwezig: ma/di/wo/do*

| | **T** | +31 (0)26 373 34 35                                                                                                                                                                                                                                                                                                                                                                                          |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **M** | +31 (0)6 12 06 97 49                                                                                                                                                                                                                                                                                                                                                                                         |
| **E** | [Wouter.Mos@tennet.eu](mailto:Wouter.Mos@tennet.eu "mailto:Wouter.Mos@tennet.eu")                                                                                                                                                                                                                                                                                                                                  |
| **I** | [**www.tennet.eu**](https://urldefense.com/v3/__http:/0.12.63.16/Desktop/www.tennet.eu__;!!DLrcCis!_xTaGK-OpRfQx4fOeI7LaHYUNpJ9x5KLAy-Pa-NwuX-2CMGteyUAh0WBLdIjto8uCveSFCOFWPec0S9qhkkBjigvFdzMkpUYV1UhgDSf8kNF$ "https://urldefense.com/v3/__http:/0.12.63.16/Desktop/www.tennet.eu__;!!DLrcCis!_xTaGK-OpRfQx4fOeI7LaHYUNpJ9x5KLAy-Pa-NwuX-2CMGteyUAh0WBLdIjto8uCveSFCOFWPec0S9qhkkBjigvFdzMkpUYV1UhgDSf8kNF$")  |

| ![]() | TenneT TSO B.V.``Utrechtseweg 310``Arnhem``Postbus 718``6800 AS Arnhem``Nederland |
| --- | -------------------------------------------------------------------------------------------------------------------- |
