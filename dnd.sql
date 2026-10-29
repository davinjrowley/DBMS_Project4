-- Drop existing tables
DROP TABLE IF EXISTS canUse;
DROP TABLE IF EXISTS learns;
DROP TABLE IF EXISTS invests;
DROP TABLE IF EXISTS spell;
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS class;


-- Create class table
CREATE TABLE class (
    name VARCHAR(10) PRIMARY KEY,
    description VARCHAR(50)
);


-- Create characters table
CREATE TABLE characters (
    name VARCHAR(30) PRIMARY KEY,
    lvl NUMERIC(2, 0) CHECK (lvl BETWEEN 1 AND 20)
);


-- Create spell table
CREATE TABLE spell (
    name VARCHAR(35) PRIMARY KEY,
    lvl NUMERIC(1, 0) CHECK (lvl BETWEEN 0 AND 9),
    school VARCHAR(15),
    description VARCHAR(50)
);


-- Create invests table
CREATE TABLE invests (
    charName VARCHAR(30) PRIMARY KEY,
    className VARCHAR(10),
    subClass VARCHAR(35),
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


-- Create learns table
CREATE TABLE learns (
    className VARCHAR(10),
    spellName VARCHAR(35),
    spellLvl NUMERIC(1, 0),
    PRIMARY KEY (className, spellName),
    FOREIGN KEY (className) REFERENCES class(name),
    FOREIGN KEY (spellName) REFERENCES spell(name)
);


-- Create canUse table
CREATE TABLE canUse (
    charName VARCHAR(30),
    spellName VARCHAR(35),
    PRIMARY KEY (charName, spellName),
    FOREIGN KEY (charName) REFERENCES characters(name),
    FOREIGN KEY (spellName) REFERENCES spell(name)
);


-- Insert sample classes
INSERT INTO class (name, description) VALUES
('Wizard', 'Arcane spellcaster'),
('Cleric', 'Divine spellcaster'),
('Warlock', 'Pact magic user'),
('Bard', 'Magical performer'),
('Fighter', 'Master of weapons');


-- Insert sample characters
INSERT INTO characters (name, lvl) VALUES
('Gandalf', 10),
('Shadowheart', 5),
('Wyll', 5),
('Astarion', 5),
('Lae zel', 5);


-- Insert sample spells
INSERT INTO spell (name, lvl, school, description) VALUES
('Fireball', 3, 'Evocation', 'A burst of fire damage'),
('Magic Missile', 1, 'Evocation', 'Darts of magical force'),
('Shield', 1, 'Abjuration', 'Creates a magical barrier'),
('Cure Wounds', 1, 'Evocation', 'Restores hit points'),
('Eldritch Blast', 0, 'Evocation', 'A beam of magical force'),
('Healing Word', 1, 'Evocation', 'Heals at a distance'),
('Vicious Mockery', 0, 'Enchantment', 'Psychic damage and debuff'),
('Misty Step', 2, 'Conjuration', 'Teleport a short distance');


-- Insert sample class levels and subclasses
INSERT INTO invests
(charName, className, subClass,
 lvl1, lvl2, lvl3, lvl4, lvl5,
 lvl6, lvl7, lvl8, lvl9)
VALUES
('Gandalf', 'Wizard', 'School of Evocation',
 0, 0, 0, 0, 0, 0, 0, 0, 0),
('Shadowheart', 'Cleric', 'Trickery Domain',
 0, 0, 0, 0, 0, 0, 0, 0, 0),
('Wyll', 'Warlock', 'Fiend Patron',
 0, 0, 0, 0, 0, 0, 0, 0, 0),
('Astarion', 'Bard', 'College of Swords',
 0, 0, 0, 0, 0, 0, 0, 0, 0),
('Lae zel', 'Fighter', 'Battle Master',
 0, 0, 0, 0, 0, 0, 0, 0, 0);


-- Insert class-to-spell relationships
INSERT INTO learns (className, spellName, spellLvl) VALUES
('Wizard', 'Fireball', 3),
('Wizard', 'Magic Missile', 1),
('Wizard', 'Shield', 1),
('Wizard', 'Misty Step', 2),
('Cleric', 'Cure Wounds', 1),
('Cleric', 'Healing Word', 1),
('Warlock', 'Eldritch Blast', 0),
('Warlock', 'Misty Step', 2),
('Bard', 'Vicious Mockery', 0),
('Bard', 'Healing Word', 1);


-- Insert character-to-spell relationships
INSERT INTO canUse (charName, spellName) VALUES
('Gandalf', 'Fireball'),
('Gandalf', 'Magic Missile'),
('Gandalf', 'Shield'),
('Shadowheart', 'Cure Wounds'),
('Shadowheart', 'Healing Word'),
('Wyll', 'Eldritch Blast'),
('Wyll', 'Misty Step'),
('Astarion', 'Vicious Mockery'),
('Astarion', 'Healing Word');
