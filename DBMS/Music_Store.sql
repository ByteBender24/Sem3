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

DROP TABLE Musician;
DROP TABLE Album;
DROP TABLE Song;
DROP TABLE Artist;
DROP TABLE SungBy;
DROP TABLE Studio;

REM -------------CREATING TABLES--------------

SET ECHO ON

CREATE TABLE Musician (
	Musician_ID int,
	Name varchar(255),
	Birthplace varchar(255),
	CONSTRAINT PK_Musician PRIMARY KEY (Musician_ID)
);

CREATE TABLE Studio (
	Studio_name varchar(255),
	Address varchar(255),
	Phone int,
	CONSTRAINT PK_Studio PRIMARY KEY (Studio_name)
);

CREATE TABLE Album (
	Album_name varchar(255),
	Album_ID int,
	Year_of_release int,
	No_of_tracks int,
	Studio_recorded varchar(255),
	Album_genre varchar(255),
	Musicians int,
	CONSTRAINT PK_Album PRIMARY KEY (Album_ID),
	CONSTRAINT FK_Musicians FOREIGN KEY (Musicians) REFERENCES Musician(Musician_ID),
	CONSTRAINT FK_Studio FOREIGN KEY (Studio_recorded) REFERENCES Studio(Studio_name)
);

CREATE TABLE Song (
    Album_ID int,
    Track_no int,
    Song_name varchar(255),
    Song_length int,
    Song_genre varchar(255),
    CONSTRAINT PK_Song PRIMARY KEY (Album_ID, Track_no),
    CONSTRAINT FK_Album_ID_Song FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID)
);

CREATE TABLE Artist (
	Artist_ID int,
	Artist_name varchar(255),
	Album_ID int,	-- Created this query for 5)
	CONSTRAINT PK_Artist PRIMARY KEY (Artist_ID),
	CONSTRAINT FK_Album_ID FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID)
);

--CREATE TABLE SungBy (
--	Album_ID int,
--	Artist_ID int,
--	Track_no int,
--	Recording_date DATE,
--	CONSTRAINT PK_SungBy PRIMARY KEY (Album_ID, Artist_ID, Track_no),
--	CONSTRAINT FK_Album_ID_SungBy FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID),
--	CONSTRAINT FK_Artist_ID FOREIGN KEY (Artist_ID) REFERENCES Artist(Artist_ID),
--	CONSTRAINT FK_Track_no FOREIGN KEY (Track_no) REFERENCES Song(Track_no)
--);

CREATE TABLE SungBy (
    Album_ID int,
    Artist_ID int,
    Track_no int,
    Recording_date DATE,
    CONSTRAINT PK_SungBy PRIMARY KEY (Album_ID, Artist_ID, Track_no),
    CONSTRAINT FK_Album_ID_SungBy FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID),
    CONSTRAINT FK_Artist_ID FOREIGN KEY (Artist_ID) REFERENCES Artist(Artist_ID),
    CONSTRAINT FK_Track_no FOREIGN KEY (Album_ID, Track_no) REFERENCES Song(Album_ID, Track_no)
);

REM ---------CREATED BASIC SKELETON TABLES WITH PRIMARY KEYS---------------

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
