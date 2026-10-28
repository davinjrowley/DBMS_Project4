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

CREATE TABLE learns (
        className varchar(10) PRIMARY KEY,
        spellName varchar(35),
        spellLvl NUMERIC(1, 0),
        FOREIGN KEY (className) REFERENCES class(name),
        FOREIGN KEY (spellName) REFERENCES spell(name),
        FOREIGN KEY (spellLvl) REFERENCES spell(lvl)
        );

CREATE TABLE canUse (
        charName varchar(30) PRIMARY KEY,
        spellName varchar(35)
        );