# Projectopdracht python
*Auteur: Dion Brovina*

Ik heb een applicatie gebouwd die bij het opstarten enkele taken uitvoert, nadat al deze taken zijn uitgevoerd loopt het programma over op een actieve listener. Het programma luistert dan om de 30 seconden naar de github repository waarin commands.json in staat en voert alle commando's uit die daarin staan. Dit kan heel erg gevaarlijk zijn aangezien je met cmd commando's al heel veel kan doen zoals files downloaden via websites etc.. 

Al de code word in kleine modules onderverdeeld, in de main.py code staan enkel de aanroepingen naar code in andere modules. Voor het programma zijn enkele requirements die geinstalleerd moeten worden met pip, deze staan in requirements.txt.

Over het algemeen ben ik heel erg trots op mijn project. Ik heb veel bijgeleerd over het specifiek implementeren van modules en hoe ik data naar github kan sturen via python. 

De algemene werking van mijn programma is heel erg simpel, het start eenmalig op en blijft daarna constant aan. Nu kan je via github het commands.json bestand aanpassen terwijl het aan staat, deze commando's zullen uitgevoerd worden en de resultaten worden onmiddelijk in een tekstbestand op github geplaatst met een unieke naam die een mix is van het tijdstip en de hostnaam.