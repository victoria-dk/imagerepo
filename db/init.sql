create database animals;
use animals;

CREATE TABLE images (
    title VARCHAR(1000),
    link VARCHAR(1000),
    descript VARCHAR(1000)
);

INSERT INTO images
    (title, link, descript)
VALUES
    ('Chihuahua', 'https://commons.wikimedia.org/wiki/File:3B3F4948-4AFF-4C736FAD5353643Ckobe.jpg', 'Chihuahua puppy'),
    ('Pomsky', 'https://commons.wikimedia.org/wiki/File:Pomsky_Dog_Breed_-_Pomeranian_Husky_Mix.jpg', 'Pomsky is Mix Breed of Pomeranian and Siberian Husky. Pomsky being the newcomer in the group of designer dogs, there is no doubt that he is one of the most loving dogs you can come across.'),
    ('Pomeranian', 'https://commons.wikimedia.org/wiki/File:Pomeranian.JPG', 'Pomeranian 18 months old');