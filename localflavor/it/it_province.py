#: An alphabetical list of provinces and regions
PROVINCES = (
    ('AG', 'Agrigento', 'SIC'),
    ('AL', 'Alessandria', 'PMN'),
    ('AN', 'Ancona', 'MAR'),
    ('AO', 'Aosta', 'VAO'),
    ('AR', 'Arezzo', 'TOS'),
    ('AP', 'Ascoli Piceno', 'MAR'),
    ('AT', 'Asti', 'PMN'),
    ('AV', 'Avellino', 'CAM'),
    ('BA', 'Bari', 'PUG'),
    ('BT', 'Barletta-Andria-Trani', 'PUG'),  # active starting from 2009
    ('BL', 'Belluno', 'VEN'),
    ('BN', 'Benevento', 'CAM'),
    ('BG', 'Bergamo', 'LOM'),
    ('BI', 'Biella', 'PMN'),
    ('BO', 'Bologna', 'EMR'),
    ('BZ', 'Bolzano/Bozen', 'TAA'),
    ('BS', 'Brescia', 'LOM'),
    ('BR', 'Brindisi', 'PUG'),
    ('CA', 'Cagliari', 'SAR'),
    ('CL', 'Caltanissetta', 'SIC'),
    ('CB', 'Campobasso', 'MOL'),
    ('CI', 'Carbonia-Iglesias', 'SAR'),
    ('CE', 'Caserta', 'CAM'),
    ('CT', 'Catania', 'SIC'),
    ('CZ', 'Catanzaro', 'CAL'),
    ('CH', 'Chieti', 'ABR'),
    ('CO', 'Como', 'LOM'),
    ('CS', 'Cosenza', 'CAL'),
    ('CR', 'Cremona', 'LOM'),
    ('KR', 'Crotone', 'CAL'),
    ('CN', 'Cuneo', 'PMN'),
    ('EN', 'Enna', 'SIC'),
    ('FM', 'Fermo', 'MAR'),  # active starting from 2009
    ('FE', 'Ferrara', 'EMR'),
    ('FI', 'Firenze', 'TOS'),
    ('FG', 'Foggia', 'PUG'),
    ('FC', 'Forlì-Cesena', 'EMR'),
    ('FR', 'Frosinone', 'LAZ'),
    ('GE', 'Genova', 'LIG'),
    ('GO', 'Gorizia', 'FVG'),
    ('GR', 'Grosseto', 'TOS'),
    ('IM', 'Imperia', 'LIG'),
    ('IS', 'Isernia', 'MOL'),
    ('SP', 'La Spezia', 'LIG'),
    ('AQ', 'L’Aquila', 'ABR'),
    ('LT', 'Latina', 'LAZ'),
    ('LE', 'Lecce', 'PUG'),
    ('LC', 'Lecco', 'LOM'),
    ('LI', 'Livorno', 'TOS'),
    ('LO', 'Lodi', 'LOM'),
    ('LU', 'Lucca', 'TOS'),
    ('MC', 'Macerata', 'MAR'),
    ('MN', 'Mantova', 'LOM'),
    ('MS', 'Massa-Carrara', 'TOS'),
    ('MT', 'Matera', 'BAS'),
    ('VS', 'Medio Campidano', 'SAR'),
    ('ME', 'Messina', 'SIC'),
    ('MI', 'Milano', 'LOM'),
    ('MO', 'Modena', 'EMR'),
    ('MB', 'Monza e Brianza', 'LOM'),  # active starting from 2009
    ('NA', 'Napoli', 'CAM'),
    ('NO', 'Novara', 'PMN'),
    ('NU', 'Nuoro', 'SAR'),
    ('OG', 'Ogliastra', 'SAR'),
    ('OT', 'Olbia-Tempio', 'SAR'),
    ('OR', 'Oristano', 'SAR'),
    ('PD', 'Padova', 'VEN'),
    ('PA', 'Palermo', 'SIC'),
    ('PR', 'Parma', 'EMR'),
    ('PV', 'Pavia', 'LOM'),
    ('PG', 'Perugia', 'UMB'),
    ('PU', 'Pesaro e Urbino', 'MAR'),
    ('PE', 'Pescara', 'ABR'),
    ('PC', 'Piacenza', 'EMR'),
    ('PI', 'Pisa', 'TOS'),
    ('PT', 'Pistoia', 'TOS'),
    ('PN', 'Pordenone', 'FVG'),
    ('PZ', 'Potenza', 'BAS'),
    ('PO', 'Prato', 'TOS'),
    ('RG', 'Ragusa', 'SIC'),
    ('RA', 'Ravenna', 'EMR'),
    ('RC', 'Reggio Calabria', 'CAL'),
    ('RE', 'Reggio Emilia', 'EMR'),
    ('RI', 'Rieti', 'LAZ'),
    ('RN', 'Rimini', 'EMR'),
    ('RM', 'Roma', 'LAZ'),
    ('RO', 'Rovigo', 'VEN'),
    ('SA', 'Salerno', 'CAM'),
    ('SS', 'Sassari', 'SAR'),
    ('SV', 'Savona', 'LIG'),
    ('SI', 'Siena', 'TOS'),
    ('SR', 'Siracusa', 'SIC'),
    ('SO', 'Sondrio', 'LOM'),
    ('TA', 'Taranto', 'PUG'),
    ('TE', 'Teramo', 'ABR'),
    ('TR', 'Terni', 'UMB'),
    ('TO', 'Torino', 'PMN'),
    ('TP', 'Trapani', 'SIC'),
    ('TN', 'Trento', 'TAA'),
    ('TV', 'Treviso', 'VEN'),
    ('TS', 'Trieste', 'FVG'),
    ('UD', 'Udine', 'FVG'),
    ('VA', 'Varese', 'LOM'),
    ('VE', 'Venezia', 'VEN'),
    ('VB', 'Verbano Cusio Ossola', 'PMN'),
    ('VC', 'Vercelli', 'PMN'),
    ('VR', 'Verona', 'VEN'),
    ('VV', 'Vibo Valentia', 'CAL'),
    ('VI', 'Vicenza', 'VEN'),
    ('VT', 'Viterbo', 'LAZ'),
)

#: An alphabetical list of provinces
PROVINCE_CHOICES = tuple((p[0], p[1]) for p in PROVINCES)

#: A dictionary of provinces mapped to regions
PROVINCE_REGIONS = dict([(p[0], p[2]) for p in PROVINCES])
