create database sagefemme;
use sagefemme;

create table enemytype(
enemytypeID int not null auto_increment primary key,
name varchar(40),
description varchar(600),
attackstat int,
defencestat int,
startinghp int
);
create table tiletype(
tiletypeID int not null auto_increment primary key,
name varchar(40),
description varchar(600)
);
create table enemy(
enemyID int not null auto_increment primary key,
enemytypeID int,
tiletypeID int,
foreign key (enemytypeID) references enemytype (enemytypeID),
foreign key (tiletypeID) references tiletype (tiletypeID),
hpbar int,
locationID int
);
create table tile(
locationID int,
tiletypeID int,
locked int,
roominfo varchar(600),
primary key (locationID),
foreign key (tiletypeID) references tiletype (tiletypeID)
);
create table player(
playerID int not null auto_increment primary key,
name varchar(40),
description varchar(600),
level int,
hitpoints int,
locationID int,
tiletypeID int,
foreign key (tiletypeID) references tiletype (tiletypeID)
);
create table objecttype(
objecttypeID int not null auto_increment primary key,
name varchar(40),
description varchar(600)
);
create table otherobject(
objecttypeID int,
foreign key (objecttypeID) references objecttype (objecttypeID)
);
create table weaponobject(
attack int,
defence int,
objecttypeID int,
foreign key (objecttypeID) references objecttype (objecttypeID)
);
create table object(
locationID int,
playerID int,
foreign key (playerID) references player (playerID),
objecttypeID int,
foreign key (objecttypeID) references objecttype (objecttypeID)
);

#lisää nää arvot yllä tehtyihin tauluihin
insert into enemytype(name, description, attackstat, defencestat, startinghp)
values ("Boss",
"Once your best friend, she has come a long way since 4th grade. Wearing a skirt,  a jacket and high heels – all black – she is a clear contrast to the bland pastel colours of her employees. As a female branch manager, she has to uphold a certain reputation in order to command respect and authority. She looks angry. Better stay out of her way.",
 50, 35, 25),
 ("Giant Rat",
 "A giant frenzied killer rat? The sight makes you doubt your senses, but your brain trusts its eyes more than it trusts you. As your body begins surging your veins with adrenaline as its fight-or-flight response, you scan the room and realise that the latter is not an option. You prepare to equip whichever item at hand you judge to be best suited for fighting off a giant killer rat, but judging by the mangled corpses of your collegues at its feet, you doubt it will be enough.",
 15, 40, 50);

insert into enemy(enemytypeID, hpbar, locationID)
values (1, 25, 1), (2, 50, 2);

insert into tiletype (name, description)
values 
("Patient room",          #1
"'Whenever a hospital has funding issues, the patient rooms are the first ones to reveal it; the flower pattern tapestry that was once a rejuvenating decor for patients is starting to fall off and cracks are visible in the corners of the wall,  You try not to enter them unless absolutely necessary, but to your surprise, it’s mostly quiet; morphine induced snoring patients sleeping soundly in their beds. God bless morphine. It seems to make all your problems go away.'"),
("Corridor",              #2
"'A typical hospital corridor; rooms spanning both sides filled over their capacity with sick patients, some of them coughing, others screaming in pain. Sometimes you swear that you catch a glimpse of death itself creeping over the most terminal cases, his scythe gently caressing their cheeks before taking them into his cold embrace. You get the feeling that the now beige walls were originally white.'"),
("Cleaning room",         #3
"'A tiny room cramped from floor to roof with dust covered boxes and shelves full of cleaning materials. It would certainly benefit from a Spring cleaning itself. You spot a rolled up MAP of the hospital sitting on one of the shelves. You find it peculiar that someone would leave it there, but you doubt they would miss it much. A door with a malnourished African child sign on it that urges you to to lock the door and close the lights upon leaving lies to the West. The irony would humour you were it not so depressing.'"),
("Staircase",             #4
"'The smell of vomit impregnates your nose as you enter. Why do the elevators have to be out of order?'"),
("Elevator",              #5
"'wip'"),
("Toilet",                #6
"'The toilet is in surpriringly good shape considering the long lasting budget cuts, although you suspect it is more so because of a hospital policy to give patients bowls instead of wasting resources on accompanying them to the toilets'"), 
("Boss's Office",         #7
"'The throne room for her tyrannical rule'"), 
("Labor room",            #8
"'Where babies are made'"), 
("Medicine Supply Room",  #9
"'Your personal drug store'"),
("Dark patient room",     #10
"'There are no patients and the lights are out, just like in the corridors. Something is awry. You can feel it.'"),
("Dark corridor",         #11
"'The power is out, which makes no sense as the hospital has two backup generators capable of supporting the building running full steam for two days.'");

insert into tile (locationID, tiletypeID, locked, roominfo)
values (101,1,1,"The door to the hallway lies to your East."), (102,1,0,"The door to the hallway lies to your East."), (103,4,0,"The hallway lies to your North."), (104,2,0,"The hallway continues to the North, while the cleaning room is to your East and a patient room to your West. A staircase sits South of you."), (105,2,0,"The hallway continues to the North, East and South. The main door of the hospital sits west of you."), (106,2,0,"The hallway continues to the south, while the cleaning room is to your east and a patient room to you west. A staircase sits North of you."), (107,4,0,"The hallway lies to your South."), (108,3,0,"The hallway lies to your West."), (109,2,0,"The hallway continues to the East and West."), (110,1,0,"The hallway lies to your West."), (111,1,0,"The hallway lies to your North."), (112,2,0,"The hallway continues to the West. Patient rooms are to your North and South."), (113,1,0,"The hallway lies to the South."), 
(201,1,0,"The hallway lies to your East."), (202,1,0,"The hallway lies to your East."), (203,4,0,"The hallway lies to your North."), (204,2,0,"The hallway continues to the North, while the cleaning room is to your East and a patient room to your West. A stairscase sits South of you."), (205,2,0,"The hallway continues to the North, East, and South."), (206,2,0,"The hallway continues to your South, while the toilet is to your East and Patient room to your west. A staircase sits North of you."), (207,4,0,"The hallway lies to your South."), (208,9,0,"The hallway lies to your West."), (209,2,0,"The hallway continues to the East and West."), (210,6,0,"The hallway lies to your West."), (211,9,0,"The hallway lies to your North."), (212,2,0,"The hallway continues to the West, while the labour room is to your North and the medicine supply room is to your South. "), (213,8,0,"The hallway lies to your South."), 
(301,1,0,"The hallway lies to your East."), (302,1,0,"The hallway lies to your East."), (303,4,0,"The hallway lies to your North."), (304,2,0,"The hallway continues to North, while the cleaning room is East and patient room West."), (305,2,0,"The hallway continues to the North, East and West."), (306,2,0,"The hallway continues South, while the patient room is West and the stairs North."), (307,4,0,"The hallway lies to your South."), (308,3,0,"The hallway lies to your West."), (309,2,0,"The hallway continues to East and West."), (310,9,0,"The hallway lies to your North."), (311,2,0,"The hallway continues to West, while the Boss room is North and medicine room west."), (312,7,0,"The hallway lies to your South.");

insert into player (name, description, level, hitpoints, locationID)
values ("Charlotte", 
"You’re wearing a white hospital gown over a light pink outfit which differs from the nurses’ ones by a seemingly not different enough tone, as patients constantly call out to you for soothe and care. You’ve tied your hair in a bun and applied some dark eyeliner, more so in attempt to keep yourself sane and feeling like an ordinary working person than to impress anyone.",
1, 70, 108);

insert into objecttype (name, description)
values ("Scissors", "Made in America to withstand decades of use in a medical environment; you would trust them with your life. The iron has started showing some small signs of rusting, but not only the blades, but the tips as well are extremely sharp. They could easily hurt someone if not handled carefully."),
("Fists","wip"),  #maybe leave these out?
("Morphine bottle","A white pill of pure ecstacy- or morphine, rather. Your life's nectar."),
("Map","Scrolled up like an ancientscrooll - dusty like one too - you are almost too afraid to touch it in fear of it disintegrates into thin air."), 
("Stairs key","wip"), 
("Boss office key","No one really knew what this key looked like, until now."), 
("Masterkey","A fittingly named gigantic key that opens the main door of the hospital.");

insert into otherobject (objecttypeID)
values (3), (4);

insert into weaponobject (objecttypeID, attack, defence)
values (1, 15, 5), (2, 5, 10);

insert into object (locationID, objecttypeID, playerID)
values (null, 1, 1), (null, 2, 1), (208, 3, null), (108, 4, null); 