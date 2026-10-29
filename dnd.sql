drop table if exists class;
drop table if exists characters;
drop table if exists spell;
drop table if exists invests;
drop table if exists learns;
drop table if exists canUse;


CREATE TABLE class (
        name varchar(10) PRIMARY KEY,
        description varchar(50)
        );

CREATE TABLE characters (
        name varchar(30) PRIMARY KEY,
        lvl NUMERIC(2, 0) CHECK (lvl > 0)
        );

CREATE TABLE spell (
        name varchar(35) PRIMARY KEY,
        lvl NUMERIC(1, 0),
        school varchar(15),
        description varchar(50)
        );

CREATE TABLE invests (
        charName varchar(30) PRIMARY KEY,
        className varchar(10),
        subClass varchar(35),
        lvl1 NUMERIC(1, 0),
        lvl2 NUMERIC(1, 0),
	lvl3 NUMERIC(1, 0),
	lvl4 NUMERIC(1, 0),
	lvl5 NUMERIC(1, 0),
        lvl6 NUMERIC(1, 0),
	lvl7 NUMERIC(1, 0),
	lvl8 NUMERIC(1, 0),
	lvl9 NUMERIC(1, 0),
	FOREIGN KEY (charName) REFERENCES characters(name),
	FOREIGN KEY (className) REFERENCES class(name)
	);

CREATE TABLE learns (
        className varchar(10),
        spellName varchar(35),
        spellLvl NUMERIC(1, 0),
	PRIMARY KEY (className, spellName),
        FOREIGN KEY (className) REFERENCES class(name),
        FOREIGN KEY (spellName) REFERENCES spell(name)
        );

CREATE TABLE canUse (
    	charName varchar(30),
    	spellName varchar(35),
    	PRIMARY KEY (charName, spellName),
    	FOREIGN KEY (charName) REFERENCES characters(name),
    	FOREIGN KEY (spellName) REFERENCES spell(name)
	);