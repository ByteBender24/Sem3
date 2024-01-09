SET ECHO ON

REM ***** MUSIC STORE *****
REM ------------------------------------
REM Author: Harishraj S
REM Date: 24/09/2023
REM -----------------------------------

REM -----------For checking the table names created-----------
-- SELECT table_name
-- FROM user_tables;
REM ----------------------------------------------------------

REM --------------------DROPPING TABLES----------------------

ALTER TABLE Album
DROP CONSTRAINT FK_Musicians;

ALTER TABLE Album
DROP CONSTRAINT FK_Studio;

ALTER TABLE Song
DROP CONSTRAINT FK_Album_ID_Song;

ALTER TABLE SungBy
DROP CONSTRAINT FK_Album_ID_SungBy;

ALTER TABLE SungBy
DROP CONSTRAINT FK_Track_no;

ALTER TABLE SungBy
DROP CONSTRAINT FK_Artist_ID;

ALTER TABLE Artist
DROP CONSTRAINT FK_Album_ID;

DROP TABLE Musician CASCADE CONSTRAINTS;
DROP TABLE Album CASCADE CONSTRAINTS;
DROP TABLE Song CASCADE CONSTRAINTS;
DROP TABLE Artist CASCADE CONSTRAINTS;
DROP TABLE SungBy CASCADE CONSTRAINTS;
DROP TABLE Studio CASCADE CONSTRAINTS;

REM -------------CREATING TABLES--------------

-- Create tables
CREATE TABLE Musician (
    Musician_ID int,
    Name varchar(255),
    Birthplace varchar(255)
);

CREATE TABLE Studio (
    Studio_name varchar(255),
    Address varchar(255),
    Phone int
);

CREATE TABLE Album (
    Album_name varchar(255),
    Album_ID int,
    Year_of_release int,
    No_of_tracks int,
    Studio_recorded varchar(255),
    Album_genre varchar(255),
    Musicians int
);

CREATE TABLE Song (
    Album_ID int,
    Track_no int,
    Song_name varchar(255),
    Song_length int,
    Song_genre varchar(255)
);

CREATE TABLE Artist (
    Artist_ID int,
    Artist_name varchar(255),
    Album_ID int
);

CREATE TABLE SungBy (
    Album_ID int,
    Artist_ID int,
    Track_no int,
    Recording_date DATE
);

-- Add primary key constraints
ALTER TABLE Musician
ADD CONSTRAINT PK_Musician PRIMARY KEY (Musician_ID);

ALTER TABLE Studio
ADD CONSTRAINT PK_Studio PRIMARY KEY (Studio_name);

ALTER TABLE Album
ADD CONSTRAINT PK_Album PRIMARY KEY (Album_ID);

ALTER TABLE Song
ADD CONSTRAINT PK_Song PRIMARY KEY (Album_ID, Track_no);

ALTER TABLE Artist
ADD CONSTRAINT PK_Artist PRIMARY KEY (Artist_ID);

ALTER TABLE SungBy
ADD CONSTRAINT PK_SungBy PRIMARY KEY (Album_ID, Artist_ID, Track_no);

-- Add foreign key constraints
ALTER TABLE Album
ADD CONSTRAINT FK_Musicians FOREIGN KEY (Musicians) REFERENCES Musician(Musician_ID);

ALTER TABLE Album
ADD CONSTRAINT FK_Studio FOREIGN KEY (Studio_recorded) REFERENCES Studio(Studio_name);

ALTER TABLE Song
ADD CONSTRAINT FK_Album_ID_Song FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID);

ALTER TABLE Artist
ADD CONSTRAINT FK_Album_ID FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID);

ALTER TABLE SungBy
ADD CONSTRAINT FK_Album_ID_SungBy FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID);

ALTER TABLE SungBy
ADD CONSTRAINT FK_Artist_ID FOREIGN KEY (Artist_ID) REFERENCES Artist(Artist_ID);

ALTER TABLE SungBy
ADD CONSTRAINT FK_Track_no FOREIGN KEY (Album_ID, Track_no) REFERENCES Song(Album_ID, Track_no);


REM -----------------------------CREATING CONSTRAINTS--------------------------------------------

REM 1) The genre for Album can be generally categorized as CAR for
-- Carnatic, DIV for Divine, MOV for Movies, POP for Pop songs.

ALTER TABLE Album
ADD CONSTRAINT Check_Album_genre CHECK (Album_genre IN ('CAR', 'DIV', 'MOV', 'POP'));

REM ---------------------------------------------------------------------------------------------

REM 2) The genre for Song can be PHI for philosophical, REL for relationship,
-- LOV for duet, DEV for devotional, PAT for patriotic type of songs.

ALTER TABLE Song
ADD CONSTRAINT Check_Song_genre CHECK (Song_genre IN ('PHI', 'REL', 'LOV', 'DEV', 'PAT'));

REM ---------------------------------------------------------------------------------------------

REM 3) The artist ID, album ID, musician ID, and track number, studio name
-- are used to retrieve tuple(s) individually from respective relations.

--  --------The primary are defined correctly. So that it can be used to retrieve (tuples)Rows, 
-- individually from respective relations, and they are identified by a unique one for each row-----------

REM ---------------------------------------------------------------------------------------------

REM 4) Ensure that the artist, musician, song, sungby, and studio cannot be removed without deleting the album details.

-- This is done by ensuring every table mentioned has foreign key referencing to the album table
-- Please refer the table SungBy as two of them are mentioned as foreign key at last statement to avoid
-- ORA-02270: no matching unique or primary key for this column-list

REM ---------------------------------------------------------------------------------------------

REM 5) A song may be sung by more than one artist. The same artist may sing for more than 
-- one track in the same album. Similarly, an artist can sing for different albums.

-- created the SungBy table to handle the relationship between artists, albums, and tracks
-- Created composite primary keys for that table
-- Also refer SungBy and Artist table to handle *-* and 1-* relationships 

REM ---------------------------------------------------------------------------------------------

REM 6) It was learned that the artists do not have the same name

ALTER TABLE Artist
ADD CONSTRAINT Unique_Artist_name UNIQUE(Artist_name);

REM ---------------------------------------------------------------------------------------------

REM 7) The number of tracks in an album must always be recorded.

ALTER TABLE Album
MODIFY No_of_tracks int NOT NULL;

REM ---------------------------------------------------------------------------------------------

REM 8) The length of each song must be greater than 7 for PAT songs.

ALTER TABLE Song
ADD CONSTRAINT Check_PAT_song_len 
CHECK (Song_genre <> 'PAT' or (Song_genre = 'PAT' AND Song_length > 7));

REM ---------------------------------------------------------------------------------------------

REM 9) The year of release of an album cannot be earlier than 1945.

ALTER TABLE Album
ADD CONSTRAINT Check_year_of_release 
CHECK (year_of_release >= 1945);

REM ----------------------ADDITIONAL CHANGES-----------------------------

REM 10) It is necessary to represent the gender of an artist in the table

ALTER TABLE Artist
ADD Gender char(1);

ALTER TABLE Artist
ADD CONSTRAINT Check_Gender 
CHECK (Gender in ('M','F'));

REM ---------------------------------------------------------------------------------------------

REM 11) The first few words of the lyrics constitute the song name. The
-- song name has to accommodate some of the words (in lyrics).

ALTER TABLE Song
ADD First_lyrics varchar(255);

REM ---------------------------------------------------------------------------------------------

REM 12) The phone number of each studio should be different.

ALTER TABLE Studio
ADD CONSTRAINT Unique_Phone UNIQUE (Phone);

REM ---------------------------------------------------------------------------------------------

REM 13) An artist who sings a song for a particular track of an album can
-- not be recorded without the record_date.

ALTER TABLE SungBy
MODIFY Recording_date DATE NOT NULL;

REM ---------------------------------------------------------------------------------------------

REM 14) It was decided to include the genre NAT for nature songs.

ALTER TABLE Song
DROP CONSTRAINT Check_Song_genre ;

ALTER TABLE Song
ADD CONSTRAINT Check_Song_genre CHECK (Song_genre IN ('PHI', 'REL', 'LOV', 'DEV', 'PAT', 'NAT'));

REM ---------------------------------------------------------------------------------------------


REM 15) Due to typo-error, there may be a possibility of false information.
-- Hence while deleting the song information, make sure that all the
-- corresponding information is also deleted.

-- Drop the existing foreign key constraints
ALTER TABLE SungBy DROP CONSTRAINT FK_Album_ID_SungBy;
ALTER TABLE SungBy DROP CONSTRAINT FK_Artist_ID;
ALTER TABLE SungBy DROP CONSTRAINT FK_Track_no;

-- Re-add the foreign key constraints with ON DELETE CASCADE
ALTER TABLE SungBy
ADD CONSTRAINT FK_Album_ID_SungBy FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID) ON DELETE CASCADE;

ALTER TABLE SungBy
ADD CONSTRAINT FK_Artist_ID FOREIGN KEY (Artist_ID) REFERENCES Artist(Artist_ID) ON DELETE CASCADE;

ALTER TABLE SungBy
ADD CONSTRAINT FK_Track_no FOREIGN KEY (Track_no, Album_ID) REFERENCES Song(Track_no, Album_ID) ON DELETE CASCADE;

REM ---------------------------------------SCRIPT FILE END--------------------------------------------------


SET ECHO ON

REM: HARISHRAJ S
REM: 25/09/2023

REM ------------------INSERT INTO VALUES----------------

-- Inserting data into the Musician table
INSERT INTO Musician (Musician_ID, Name, Birthplace)
VALUES (1, 'John Doe', 'New York'); -- Inserting a musician

-- Inserting data into the Studio table
INSERT INTO Studio (Studio_name, Address, Phone)
VALUES ('Music Studio A', '123 Main St', 1234567890); -- Inserting a studio

-- Inserting data into the Album table
INSERT INTO Album (Album_name, Album_ID, Year_of_release, No_of_tracks, Studio_recorded, Album_genre, Musicians)
VALUES ('Greatest Hits', 1, 2000, 12, 'Music Studio A', 'POP', 1); -- Inserting an album

-- Inserting data into the Song table
INSERT INTO Song (Album_ID, Track_no, Song_name, Song_length, Song_genre)
VALUES (1, 1, 'Track 1', 240, 'POP'); -- Inserting a song

-- Inserting data into the Artist table
INSERT INTO Artist (Artist_ID, Artist_name, Album_ID, Gender)
VALUES (1, 'Singer A', 1, 'F'); -- Inserting an artist

-- Inserting data into the SungBy table
INSERT INTO SungBy (Album_ID, Artist_ID, Track_no, Recording_date)
VALUES (1, 1, 1, TO_DATE('2023-09-29', 'YYYY-MM-DD')); -- Linking an artist to a song

-- More data can be inserted in a similar way for testing.

-- Inserting more data into the Musician table
INSERT INTO Musician (Musician_ID, Name, Birthplace)
VALUES (2, 'Jane Smith', 'Los Angeles'); -- Another musician

-- Inserting more data into the Studio table
INSERT INTO Studio (Studio_name, Address, Phone)
VALUES ('Sound Waves Studio', '456 Elm St', 9876543210); -- Another studio

-- Inserting more data into the Album table
INSERT INTO Album (Album_name, Album_ID, Year_of_release, No_of_tracks, Studio_recorded, Album_genre, Musicians)
VALUES ('Rock Anthems', 2, 1995, 10, 'Sound Waves Studio', 'POP', 2); -- Another album

-- Inserting more data into the Song table
INSERT INTO Song (Album_ID, Track_no, Song_name, Song_length, Song_genre)
VALUES (2, 1, 'Rock Song 1', 320, 'POP'); -- Another song

-- Inserting more data into the Artist table
INSERT INTO Artist (Artist_ID, Artist_name, Album_ID, Gender)
VALUES (2, 'Singer B', 2, 'M'); -- Another artist

-- Inserting more data into the SungBy table
INSERT INTO SungBy (Album_ID, Artist_ID, Track_no, Recording_date)
VALUES (2, 2, 1, TO_DATE('2023-09-30', 'YYYY-MM-DD')); -- Linking another artist to a song

-- You can continue to add more data using similar INSERT INTO statements as needed.

-- Attempting to insert data into the SungBy table with a non-existing Artist_ID (violating FK_Artist_ID)
-- This should result in a foreign key constraint error.
INSERT INTO SungBy (Album_ID, Artist_ID, Track_no, Recording_date)
VALUES (1, 3, 1, TO_DATE('2023-09-30', 'YYYY-MM-DD'));

-- Attempting to insert data into the SungBy table with a non-existing Album_ID (violating FK_Album_ID_SungBy)
-- This should result in a foreign key constraint error.
INSERT INTO SungBy (Album_ID, Artist_ID, Track_no, Recording_date)
VALUES (3, 1, 1, TO_DATE('2023-09-30', 'YYYY-MM-DD'));

-- Attempting to insert data into the SungBy table with a non-existing Track_no (violating FK_Track_no)
-- This should result in a foreign key constraint error.
INSERT INTO SungBy (Album_ID, Artist_ID, Track_no, Recording_date)
VALUES (1, 1, 10, TO_DATE('2023-09-30', 'YYYY-MM-DD'));

-- Attempting to insert a song with a genre 'INVALID' (violating Check_Song_genre constraint)
-- This should result in a check constraint error.
INSERT INTO Song (Album_ID, Track_no, Song_name, Song_length, Song_genre)
VALUES (1, 2, 'Invalid Song', 180, 'INVALID');

-- Attempting to insert an album with less than 7 tracks (violating Check_PAT_song_len constraint)
-- This should result in a check constraint error.
INSERT INTO Album (Album_name, Album_ID, Year_of_release, No_of_tracks, Studio_recorded, Album_genre, Musicians)
VALUES ('Short Album', 3, 2020, 5, 'Music Studio A', 'POP', 1);

-- Attempting to insert an album with a release year earlier than 1945 (violating Check_year_of_release constraint)
-- This should result in a check constraint error.
INSERT INTO Album (Album_name, Album_ID, Year_of_release, No_of_tracks, Studio_recorded, Album_genre, Musicians)
VALUES ('Old Album', 4, 1930, 12, 'Sound Waves Studio', 'POP', 2);

-- Attempting to insert an artist with an invalid gender 'X' (violating Check_Gender constraint)
-- This should result in a check constraint error.
INSERT INTO Artist (Artist_ID, Artist_name, Album_ID, Gender)
VALUES (3, 'Singer C', 3, 'X');


REM -----------------------------------FORMAT COLUMN--------------------------------------------------------------

REM --------------------- Musician Table -------------------------

COLUMN Musician_ID FORMAT A20
COLUMN Name FORMAT A20
COLUMN Birthplace FORMAT A20

REM --------------------- Studio Table --------------------------

COLUMN Studio_name FORMAT A20
COLUMN Address FORMAT A20
COLUMN Phone FORMAT A20

REM ------------------------Album Table ------------------------------

COLUMN Album_name FORMAT A20
COLUMN Album_ID FORMAT A20
COLUMN Year_of_release FORMAT A20
COLUMN No_of_tracks FORMAT A20
COLUMN Studio_recorded FORMAT A20
COLUMN Album_genre FORMAT A20
COLUMN Musicians FORMAT A20

REM ----------------------- Song Table -----------------------------

COLUMN Album_ID FORMAT A20
COLUMN Track_no FORMAT A20
COLUMN Song_name FORMAT A20
COLUMN Song_length FORMAT A20
COLUMN Song_genre FORMAT A20

REM ------------------------- Artist Table ---------------------------

COLUMN Artist_ID FORMAT A20
COLUMN Artist_name FORMAT A20
COLUMN Album_ID FORMAT A20
COLUMN Gender FORMAT A20

REM ------------------------------ SungBy Table ---------------------------

COLUMN Album_ID FORMAT A20
COLUMN Artist_ID FORMAT A20
COLUMN Track_no FORMAT A20
COLUMN Recording_date FORMAT A20

REM -----------------------------------------SELECT QUERIES --------------------------------------------------

SELECT * FROM Musician;
SELECT * FROM Studio;
SELECT * FROM Album;
SELECT * FROM Song;
SELECT * FROM Artist;
SELECT * FROM SungBy;

REM --------------------------------------- END OF SCRIPT FILE ----------------------------------------------


