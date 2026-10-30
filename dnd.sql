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
    description VARCHAR(50),
    castType VARCHAR(4)
);


-- Create characters table
CREATE TABLE characters (
    name VARCHAR(30) PRIMARY KEY,
    lvl NUMERIC(2, 0) CHECK (lvl BETWEEN 1 AND 20),
    class VARCHAR(10)
);


-- Create spell table
CREATE TABLE spell (
    name VARCHAR(35) PRIMARY KEY,
    lvl NUMERIC(1, 0) CHECK (lvl BETWEEN 0 AND 9),
    school VARCHAR(15),
    description VARCHAR(50)
);


-- Create slotProgression table
CREATE TABLE slotProgression (
    castType VARCHAR(10) PRIMARY KEY,
    playerLvl NUMERIC(2,0) CHECK (playerLvl BETWEEN 1 AND 20) PRIMARY KEY,
    lvl1 NUMERIC(1, 0),
    lvl2 NUMERIC(1, 0),
    lvl3 NUMERIC(1, 0),
    lvl4 NUMERIC(1, 0),
    lvl5 NUMERIC(1, 0),
    lvl6 NUMERIC(1, 0),
    lvl7 NUMERIC(1, 0),
    lvl8 NUMERIC(1, 0),
    lvl9 NUMERIC(1, 0)
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

-- Create Data For slotProgression
INSERT INTO slotProgression (castType, playerLvl, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lvl7, lvl8, lvl9) VALUES
('Full', 1, 2, 0, 0, 0, 0, 0, 0, 0, 0),
('Full', 2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
('Full', 3, 4, 2, 0, 0, 0, 0, 0, 0, 0),
('Full', 4, 4, 3, 0, 0, 0, 0, 0, 0, 0),
('Full', 5, 4, 3, 2, 0, 0, 0, 0, 0, 0),
('Full', 6, 4, 3, 3, 0, 0, 0, 0, 0, 0),
('Full', 7, 4, 3, 3, 1, 0, 0, 0, 0, 0),
('Full', 8, 4, 3, 3, 2, 0, 0, 0, 0, 0),
('Full', 9, 4, 3, 3, 3, 1, 0, 0, 0, 0),
('Full', 10, 4, 3, 3, 3, 2, 0, 0, 0, 0),
('Full', 11, 4, 3, 3, 3, 2, 1, 0, 0, 0),
('Full', 12, 4, 3, 3, 3, 2, 1, 0, 0, 0),
('Full', 13, 4, 3, 3, 3, 2, 1, 1, 0, 0),
('Full', 14, 4, 3, 3, 3, 2, 1, 1, 0, 0),
('Full', 15, 4, 3, 3, 3, 2, 1, 1, 1, 0),
('Full', 16, 4, 3, 3, 3, 2, 1, 1, 1, 0),
('Full', 17, 4, 3, 3, 3, 2, 1, 1, 1, 1),
('Full', 18, 4, 3, 3, 3, 2, 1, 1, 1, 1),
('Full', 19, 4, 3, 3, 3, 2, 2, 1, 1, 1),
('Full', 20, 4, 3, 3, 3, 2, 2, 2, 1, 1);

INSERT INTO slotProgression (castType, playerLvl, lvl1, lvl2, lvl3, lvl4, lvl5) VALUES
('Half', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
('Half', 2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
('Half', 3, 3, 0, 0, 0, 0, 0, 0, 0, 0),
('Half', 4, 3, 0, 0, 0, 0, 0, 0, 0, 0),
('Half', 5, 4, 2, 0, 0, 0, 0, 0, 0, 0),
('Half', 6, 4, 2, 0, 0, 0, 0, 0, 0, 0),
('Half', 7, 4, 3, 0, 0, 0, 0, 0, 0, 0),
('Half', 8, 4, 3, 0, 0, 0, 0, 0, 0, 0),
('Half', 9, 4, 3, 2, 0, 0, 0, 0, 0, 0),
('Half', 10, 4, 3, 2, 0, 0, 0, 0, 0, 0),
('Half', 11, 4, 3, 3, 0, 0, 0, 0, 0, 0),
('Half', 12, 4, 3, 3, 0, 0, 0, 0, 0, 0),
('Half', 13, 4, 3, 3, 1, 0, 0, 0, 0, 0),
('Half', 14, 4, 3, 3, 1, 0, 0, 0, 0, 0),
('Half', 15, 4, 3, 3, 2, 0, 0, 0, 0, 0),
('Half', 16, 4, 3, 3, 2, 0, 0, 0, 0, 0),
('Half', 17, 4, 3, 3, 3, 1, 0, 0, 0, 0),
('Half', 18, 4, 3, 3, 3, 1, 0, 0, 0, 0),
('Half', 19, 4, 3, 3, 3, 2, 0, 0, 0, 0),
('Half', 20, 4, 3, 3, 3, 2, 0, 0, 0, 0);

-- Insert sample classes
INSERT INTO class (name, description) VALUES
('Wizard', 'Arcane spellcaster', 'Full'),
('Cleric', 'Divine spellcaster' 'Full'),
('Bard', 'Magical performer', 'Full'),
('Paladin', 'Divine Halfcaster' 'Half');


-- Insert sample characters
INSERT INTO characters (name, lvl, class) VALUES
('Gandalf', 10, 'Wizard'),
('Jesus', 5, 'Cleric'),
('Joe Minstrel', 5, 'Bard'),
('Johnny B. Good', 5, 'Paladin');


-- Insert sample spells
INSERT INTO spell (name, lvl, school, description) VALUES
('Fireball', 3, 'Evocation', 'A burst of fire damage'),
('Magic Missile', 1, 'Evocation', 'Darts of magical force'),
('Shield', 1, 'Abjuration', 'Creates a magical barrier'),
('Cure Wounds', 1, 'Evocation', 'Restores hit points'),
('Healing Word', 1, 'Evocation', 'Heals at a distance'),
('Confusion', 4, 'Enchantment', 'Confuses a guy'),
('Misty Step', 2, 'Conjuration', 'Teleport a short distance');


-- Insert class-to-spell relationships
INSERT INTO learns (className, spellName, spellLvl) VALUES
('Wizard', 'Fireball', 3),
('Wizard', 'Magic Missile', 1),
('Wizard', 'Shield', 1),
('Wizard', 'Misty Step', 2),
('Cleric', 'Cure Wounds', 1),
('Cleric', 'Healing Word', 1),
('Bard', 'Confusion', 4),
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
