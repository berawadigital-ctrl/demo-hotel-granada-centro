# Contenido de la demo Hotel Granada Centro (Granada) (es/en/fr/de). Hechos de hotelgranadacentro.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios, descuentos ni ofertas; sin valoraciones ni opiniones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hotel real.','en':' Images are illustrations and do not show the actual hotel.','fr':' Les images sont des illustrations et ne montrent pas l’hôtel réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hotel.'}
H={'es':['Dobles e individuales','Triple y familiar'],'en':['Double and single rooms','Triple and family rooms'],'fr':['Doubles et individuelles','Triple et familiale'],'de':['Doppel- und Einzelzimmer','Dreibett- und Familienzimmer']}
RD={
'es':['Doble estándar, doble superior con cama de 1,80 m, doble matrimonial, matrimonial pequeña, doble económica en planta baja e individual.','Triple con tres camas individuales y familiar con dos dormitorios dobles comunicados, baño y aseo; uno de ellos con terraza con vistas a la ciudad.'],
'en':['Standard double, superior double with 1.80 m bed, double with double bed, small double, economy double on the ground floor and single.','Triple with three single beds and family room with two connecting double bedrooms, bathroom and toilet; one of them with a terrace with city views.'],
'fr':['Double standard, double supérieure avec lit de 1,80 m, double avec lit double, petite double, double économique au rez-de-chaussée et individuelle.','Triple avec trois lits simples et familiale avec deux chambres doubles communicantes, salle de bains et toilettes ; l’une avec terrasse et vue sur la ville.'],
'de':['Standard-Doppelzimmer, Superior-Doppelzimmer mit 1,80-m-Bett, Doppelzimmer mit Doppelbett, kleines Doppelzimmer, Economy-Doppelzimmer im Erdgeschoss und Einzelzimmer.','Dreibettzimmer mit drei Einzelbetten und Familienzimmer mit zwei verbundenen Doppelschlafzimmern, Bad und WC; eines davon mit Terrasse und Stadtblick.']}
ART={
'hero':('skyline',7711,['#1c1a1f','#c0784f','#f0d9c3','#6c4b3d','#46332c','#241c19']),
'intro':('arches',7712,['#f5efe8','#fbf8f2','#9c5b3c','#66402e','#2d1f19']),
'r1':('arches',7721,['#f0e8df','#d39c78','#9c5b3c','#66402e','#2d1f19']),
'r2':('hills',7722,['#1c1a1f','#c98560','#f2dfca','#765344','#4e3a31','#28201c']),
'g1':('skyline',7731,['#efe7dc','#f4e4ce','#d39c78','#a68a6c','#78624e','#4d3f33']),
'g2':('arches',7732,['#1c1a1f','#c0784f','#f0d9c3','#6c4b3d','#46332c','#241c19']),
'g3':('columns',7733,['#f3ece4','#faf6ef','#a8663f','#6c4b3d','#2d1f19']),
'g4':('waves',7734,['#1c1a1f','#c98560','#f2dfca','#765344','#4e3a31','#28201c'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Granada Centro · Hotel en el centro de Granada',see_rooms='Ver las habitaciones',hero_k='Granada · Calle Navarrete, 7',hero_t='En pleno centro de Granada, a cincuenta metros de Gran Vía',hero_s='Habitaciones cómodas, recepción 24 horas y vado privado frente a la puerta para descargar el equipaje.',
 intro_t='Tu hogar en Granada',intro_p1='Hotel Granada Centro está en pleno centro, a pocos minutos andando de los principales lugares de interés y a un paso de las principales líneas de autobús.',
 intro_p2='Ideal para descubrir la ciudad a pie y para ir de tapeo. En recepción te desvelan los secretos mejor guardados de la ciudad. Hotel pet friendly.',
 stats=['Recepción 24 horas','A 50 m de Gran Vía','Hotel pet friendly','Wifi gratis'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Todas con baño privado, calefacción y/o aire acondicionado, TV de pantalla plana, wifi gratis, secador y amenities ecológicos.',
 svcs=['Recepción 24 horas','Vado privado frente al hotel','Parking cercano','Hotel pet friendly','Consigna para equipajes','Cuna gratuita bajo petición'],
 loc_p='Calle Navarrete, 7 · 18001 Granada. Teléfono: 958 278 824. Recepción abierta las 24 horas.',
 chips=['¿Qué habitaciones tenéis?','¿Hay parking?','¿Admitís mascotas?','¿Cómo reservo?']),
'en':dict(title='Hotel Granada Centro · Hotel in central Granada',see_rooms='See the rooms',hero_k='Granada · Calle Navarrete, 7',hero_t='Right in the centre of Granada, fifty metres from Gran Vía',hero_s='Comfortable rooms, 24-hour reception and a private loading bay in front of the door for your luggage.',
 intro_t='Your home in Granada',intro_p1='Hotel Granada Centro is right in the centre, a few minutes’ walk from the main sights and close to the main bus lines.',
 intro_p2='Ideal for exploring the city on foot and going out for tapas. At reception they will share the city’s best-kept secrets. Pet-friendly hotel.',
 stats=['24-hour reception','50 m from Gran Vía','Pet-friendly hotel','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='All with private bathroom, heating and/or air conditioning, flat-screen TV, free wifi, hairdryer and eco-friendly amenities.',
 svcs=['24-hour reception','Private loading bay in front of the hotel','Nearby car park','Pet-friendly hotel','Luggage storage','Free cot on request'],
 loc_p='Calle Navarrete, 7 · 18001 Granada. Phone: +34 958 278 824. Reception open 24 hours.',
 chips=['Which rooms do you have?','Is there parking?','Do you allow pets?','How do I book?']),
'fr':dict(title='Hôtel Granada Centro · Hôtel au centre de Grenade',see_rooms='Voir les chambres',hero_k='Grenade · Calle Navarrete, 7',hero_t='En plein centre de Grenade, à cinquante mètres de Gran Vía',hero_s='Chambres confortables, réception 24 h/24 et emplacement privé devant la porte pour décharger les bagages.',
 intro_t='Votre maison à Grenade',intro_p1='L’Hôtel Granada Centro est en plein centre, à quelques minutes à pied des principaux sites et tout près des principales lignes de bus.',
 intro_p2='Idéal pour découvrir la ville à pied et faire la tournée des tapas. À la réception, on vous révèle les secrets les mieux gardés de la ville. Hôtel acceptant les animaux.',
 stats=['Réception 24 h/24','À 50 m de Gran Vía','Animaux acceptés','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Toutes avec salle de bains privée, chauffage et/ou climatisation, TV écran plat, wifi gratuit, sèche-cheveux et produits d’accueil écologiques.',
 svcs=['Réception 24 h/24','Emplacement privé devant l’hôtel','Parking à proximité','Animaux acceptés','Bagagerie','Lit bébé gratuit sur demande'],
 loc_p='Calle Navarrete, 7 · 18001 Grenade. Téléphone : +34 958 278 824. Réception ouverte 24 h/24.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il un parking ?','Acceptez-vous les animaux ?','Comment réserver ?']),
'de':dict(title='Hotel Granada Centro · Hotel im Zentrum von Granada',see_rooms='Zimmer ansehen',hero_k='Granada · Calle Navarrete, 7',hero_t='Mitten im Zentrum von Granada, fünfzig Meter von der Gran Vía',hero_s='Komfortable Zimmer, Rezeption rund um die Uhr und eine private Haltezone vor der Tür zum Ausladen des Gepäcks.',
 intro_t='Ihr Zuhause in Granada',intro_p1='Das Hotel Granada Centro liegt mitten im Zentrum, wenige Gehminuten von den wichtigsten Sehenswürdigkeiten und nahe den Hauptbuslinien.',
 intro_p2='Ideal, um die Stadt zu Fuß zu entdecken und Tapas zu probieren. An der Rezeption verrät man Ihnen die bestgehüteten Geheimnisse der Stadt. Haustierfreundliches Hotel.',
 stats=['Rezeption rund um die Uhr','50 m von der Gran Vía','Haustierfreundlich','Kostenloses WLAN'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Alle mit eigenem Bad, Heizung und/oder Klimaanlage, Flachbild-TV, kostenlosem WLAN, Haartrockner und ökologischen Pflegeprodukten.',
 svcs=['Rezeption rund um die Uhr','Private Haltezone vor dem Hotel','Parkhaus in der Nähe','Haustierfreundlich','Gepäckaufbewahrung','Kostenloses Kinderbett auf Anfrage'],
 loc_p='Calle Navarrete, 7 · 18001 Granada. Telefon: +34 958 278 824. Rezeption rund um die Uhr geöffnet.',
 chips=['Welche Zimmer gibt es?','Gibt es Parkplätze?','Sind Haustiere erlaubt?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://us2.cloudbeds.com/{}/reservation/W6kTGJ/?currency=eur'
BOOK=dict(mode='engine',url=dict(es=R.format('es-es'),en=R.format('en'),fr=R.format('fr'),de=R.format('de')))
D=dict(name='Hotel Granada Centro',ac='#211c1f',ac2='#9c5b3c',ac2_a11y='#7a4429',book=BOOK,around=[],foot=FOOT,
 address='Calle Navarrete, 7 · 18001 Granada',phones=['+34 958 278 824','+34 679 550 000'],emails=['info@hotelgranadacentro.com'],maps='Hotel Granada Centro, Calle Navarrete 7, 18001 Granada',t=T)
META=dict(repo='demo-hotel-granada-centro',name='Hotel Granada Centro',legal_name='Alhambra Hoteles 2001, S.L., CIF B18595959 (aviso legal de su web)',registry_ids=['B18595959'],
 url='https://hotelgranadacentro.com/',domain='hotelgranadacentro.com',municipality='Granada',province='Granada',sector='hotel en el centro de Granada junto a Gran Via',
 read_at='2026-11-02T07:27:00+01:00',created_at='2026-11-02T07:26:00+01:00',built_at='2026-11-02T07:36:00+01:00',audit_date='2026-11-02T07:26:00+01:00',
 rating=dict(value=4.3,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Hotel+Granada+Centro/@37.1810901,-3.6008146,17z'),
 book=dict(mode='engine',url=R.format('es-es'),note='motor Cloudbeds de su web (pagina /reserva/ carga el motor W6kTGJ): https://us2.cloudbeds.com/{es-es,en,fr,de}/reservation/W6kTGJ/?currency=eur, HTTP 200 en los 4 (02/11/2026 07:27).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Tenéis habitación familiar?','K02'),('¿Hay wifi?','K03'),('¿Hay parking?','K04'),('¿Puedo parar en la puerta a descargar?','K05'),('¿Admitís mascotas?','K06'),('¿Dónde estáis?','K07'),('¿Hay recepción 24 horas?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Tenéis cuna?','K10'),('¿Puedo dejar las maletas?','K11'),('¿Cuál es vuestro teléfono?','K12'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Do you have a family room?','K02'),('Is there wifi?','K03'),('Is there parking?','K04'),('Can I stop at the door to unload?','K05'),('Do you allow pets?','K06'),('Where are you?','K07'),('Is reception open 24 hours?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('Do you have a cot?','K10'),('Can I leave my luggage?','K11'),('What is your phone number?','K12'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Avez-vous une chambre familiale ?','K02'),('Y a-t-il le wifi ?','K03'),('Y a-t-il un parking ?','K04'),('Puis-je m’arrêter devant la porte pour décharger ?','K05'),('Acceptez-vous les animaux ?','K06'),('Où êtes-vous ?','K07'),('La réception est-elle ouverte 24 h/24 ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Avez-vous un lit bébé ?','K10'),('Puis-je laisser mes bagages ?','K11'),('Quel est votre numéro de téléphone ?','K12'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Haben Sie ein Familienzimmer?','K02'),('Gibt es WLAN?','K03'),('Gibt es Parkplätze?','K04'),('Kann ich vor der Tür zum Ausladen halten?','K05'),('Sind Haustiere erlaubt?','K06'),('Wo liegt das Hotel?','K07'),('Ist die Rezeption rund um die Uhr besetzt?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Haben Sie ein Kinderbett?','K10'),('Kann ich mein Gepäck lassen?','K11'),('Wie ist Ihre Telefonnummer?','K12'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
