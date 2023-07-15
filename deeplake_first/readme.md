Welkom! 👋
🙋‍♀️ Wat is OpenCatalogi?
Een federatieve catalogus ‘OpenCatalogi’, passend in het nieuwe informatielandschap Common Ground. Het concept OpenCatalogi biedt overzicht per gekozen (individuele) gemeente en geaggregeerde informatie van deelnemende gemeenten. Elke deelnemende gemeente installeert de OpenCatalogi software ten behoeve van vulling van het individuele deel. Gemeenten gebruiken de publicatiefunctie van het individuele deel om herbruikbare en uitwisselbare onderdelen te publiceren zodat dit inzichtelijk wordt voor andere deelnemers van OpenCatalogi.

Lever je bijdrage hier: User Story indienen.

image

Aanleiding
Vanuit de Vereniging van Nederlandse Gemeenten (VNG) is er in het groeipact Common Ground een samenwerking aangegaan op het gebied van een nieuwe, moderne, gezamenlijke informatievoorziening voor gemeenten. Samen organiseren op de Common Ground houdt onder andere in dat gemeenten gebruikmaken van dezelfde componenten en services. Hiervoor is het van belang dat deze componenten en services vindbaar en herbruikbaar zijn, zodat andere gemeenten deze ook kunnen implementeren. Op deze manier worden maar één keer ontwikkelkosten gemaakt en hoeft niet elke gemeente het wiel opnieuw uit te vinden.

Omdat gemeenten steeds meer landelijk samenwerken en daarbij gebruikmaken van hetzelfde informatiekundige vijflaagsmodel, is een overzicht nodig van herbruikbare en uitwisselbare onderdelen binnen en tussen gemeenten, in alle ontwikkelingsfases. Daarnaast is inzicht nodig in de werking en samenhang van elk onderdeel. Idealiter zijn deze onderdelen ook direct op te halen vanuit dit overzicht (zowel bron als instructies). In deze zin is OpenCatalogi een opvolger van de huidige componentencatalogus.

👩‍💻 Useful resources
Demo omgeving: OpenCatalogi.nl
Installatie
OpenCatalogi is een Common Ground applicatie die is opgebouwd uit losse componenten, om deze componenten optioneel te maken, zijn ze ondergebracht in losse Kubernetescontainers. Dat betekent dat voor een totaal installatie van OpenCatalogi een aantal containers nodig zijn.

Momenteel zijn er twee beproefde methode om OpenCatalogi te installeren. De primaire route is door middel van een Helm installatie op Kubernetes. Daarvoor bieden we ook een voorgedefinieerde Helm repository aan.

De voor gedefinieerde repository kan worden binnengehaald via

$ helm repo add open-catalogi <https://raw.githubusercontent.com/OpenCatalogi/web-app/development/helm/index.yaml>
En vervolgens geïnstalleerd via

$ helm install [my-opencatalogi] open-catalogi/opencatalogi
Meer informatie over installeren via Helm kan worden gevonden op de helm. Verdere informatie over installatie opties kan worden gevonden op artifact hub.

Alternatieve installatie route
In sommige gevallen is er meer behoefte aan controle over de installatie (bijvoorbeeld omdat er geen Kubernetes omgeving beschikbaar is) in dat geval kan gebruik worden gemaakt van een ‘kale’ Common Gateway instalatie, zie voor meer informatie over het installeren van de Common Gateway de Common Gateway installatie handleiding.

Omdat OpenCatalogi een Common Gateway plugin is kan je vervolgens simpelweg in de Common Gatewayy naar plugins navigeren, zoeken naar OpenCatalogi, en op installeren klikken.

Bijwerken naar nieuwere versies
Er worden regelmatig nieuwe updates van OpenCatalogi gepubliceerd, deze kunnen via de Common Gateway Admin ui worden geïnstalleerd door naar plugins te navigeren OpenCatalogi te selecteren en op Update te drukken.

Communicatie
Sprint review gemist? Kijk ze hier terug!

Sprint review 11 november : <https://vimeo.com/779203040>

Lancering OpenCatalogi 31 oktober : <https://vimeo.com/766006826>

Sprint review 14 oktober : <https://vimeo.com/761501647>

Demo 6 oktober : <https://vimeo.com/758638790>

Sprint review 30 september : <https://vimeo.com/761502051>

Sprint review 16 september : <https://vimeo.com/757143986>

Sprint review 2 september : <https://vimeo.com/745780818>

Demo 25 augustus : <https://vimeo.com/743032298>

Sprint review 19 augustus: <https://vimeo.com/741787572>

Sprint review 5 augustus: <https://vimeo.com/738214652>

Sprint review 7 juli: <https://vimeo.com/738214716>

Kick Off 27 juni: <https://vimeo.com/740023163>

Datamodel
Het datamodel van OpenCatalogi is gebaseerd op Public Code, een Europese standaard voor het beschrijven van opensource projecten. Dit model vertaald naar een OpenAPI-beschrijving in lijn met de NL API-strategie. Deze is standaard is tevens aangevuld met elementen uit de huidige Common Ground catalogus en developer.overheid om te komen tot een overkoepeld datamodel voor opensource in Nederland.

Lees meer

Het volledige datamodel
Afwijkingen ten opzichte van publiccode
Projectinrichting
OpenCatalogi wordt ontwikkeld door de volgende groepen, partijen die willen bijdragen worden expliciet uitgenodigd deel te nemen. Zie daarvoor “Bijdragen”.

Gremium Samenstelling Verantwoordelijkheden
Ontwerpgroep - Rotterdam - Detailuitwerking userstories

- Overige Gemeenten - Beoordeling opgeleverde userstories
- Vertegenwoordiging Validatiegroep - Leveren input
- Conduction - Beoordelen en werken mee aan ontwerpen
- Raadplegen wanneer nodig de achterban
- Aanwezig bij 2-wekelijkse sprintreview
- Toegang tot acceptatieomgeving
- Eindacceptatieprocedure
Validatiegroep - Eindgebruikers OpenCatalogi (Rotterdam, … ) - Deelnemen aan gebruikerstests
- Feedback geven op gebruiksvriendelijkheid van de opgeleverde software
Stuurgroep - Opdrachtgever Rotterdam - Beslissen bij afwijkingen
- PO Rotterdam - Sturen op voortgang
- IPO Conduction 
Developmentteam - Conduction - Bouwen en testen van de code
- SIG (in een eind stadium) 
Aanpak
We werken met 8 sprints van twee weken, een volledig overizcht van alle sprints is terug te vinden op de roadmap. De eerste sprint noemen we design sprint. Hierin stellen we het plan van aanpak op, kaderen we de MVP en maken we het technisch ontwerp. Elke twee sprints (dus om de 4 weken) komt de stuurgroep bij elkaar. Om de 3 sprints (dus elke 6 weken) is er een release en publieke demo. Aan het einde van het project is er een oplevering en code review en acceptatie door de product owner.

image image

De indeling van de user stories naar sprints en een overzicht van de begin en einddatums van de verschillende sprints kan worden terug gevonden op de roadmap.

Wie Wat Wanneer Datums
Stuurgroep Stuurgroep overleg Eens in de vier weken 25-07, 22-08, 19-09
Ontwerpgroep Sprint Refinement & Review Eens in de twee weken 11-07, 25-07. 08-08, 22-08, 05-09, 19-09
Validatiegroep Sprint Review en Demo Eens in de twee weken 22-07, 05-08, 19-08, 02-09, 16-09, 30-09
Developmentteam Sprint Aantal dagen per week Te bepalen
Geïntresseerden Publieke Demo Eens in de 6 weken 25-08 13:00 - 14:30 Teams, 06-10-2022 13:00 -14:30 Teams
Alle datums worden gedeeld via deze GitHub organisatie, Pleio en agende uitnodigingen.

Open Source
Als project geloven wij in open source en open community. We kiezen er daarom bewust voor ons project open en eerlijk te draaien. Naast de code zijn ook alle user stories en de roadmap publiek toegankelijk. Overheden en leveranciers wordt gevraagd hier kennis van te nemen en actief bij te dragen.

Bijdragen
Overheden en leveranciers kunnen op een aantal manieren bijdragen aan dit project

Actief bijdragen aan discussies. Alle discussies van dit project worden gevoerd in de discussie pagina het staat iedereen vrij om discussie op te starten of hierin te participeren, maar de product owner neemt samen met de product steering group het eindbesluit. Eindbesluiten die niet tot user stories leiden worden vastgelegd in de DESIGN.md.
Participeren in de product steering group. De product steering group overlegt tweewekelijks en stelt de roadmap van het project vast. Het is in principe voor alle overheden en leveranciers mogelijk om deel te nemen aan de product steering group, het eindoordeel over deelname ligt echter bij de product owner. Als je het interessant vind om deel te nemen aan de product steering group kan je contact opnemen met de product owner.
Indienen van feature requests. Iedereen kan feature request indienen, je hoeft hiervoor geen lid te zijn van de product steering group of te beschikken over ontwikkelcapaciteit. Feature request worden besproken door de product steering group die bepaald of en waar ze op de roadmap komen. Hierbij kan gevraagd worden om toelichting of een ureninschatting door leveranciers
Bijdrage van code. Het staat iedere partij vrij om code voor te dragen aan het project door middel van een pull request. Let er wel op dat het voordragen van code niet automatisch leidt tot het accepteren hiervan. Lees de contributing.md voor een beschrijving van het aanleverproces en daaraan verbonden eisen.
Roadmap
Dit project volgt een openbare roadmap, je kunt deze terugvinden onder het bijbehorende board. De roadmap heeft een indicatief karakter en er kunnen geen rechten aan worden ontleend. De product owner stelt in overleg met de product steering group de roadmap vast. Partijen die goede ideeën hebben over de roadmap wordt gevraagd deze aan te dragen. Zie daarvoor “Bijdragen”.
