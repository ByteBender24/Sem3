SET ECHO ON;

REM| Question 1

REM| Author : Harishraj S
REM| Date : 15-10-2023

REM| The relation Classes records the name of the class – ship class, the type of ships (bb
REM| for battleship or bc for battle cruiser), the country that built the ship, the number of
REM| main guns, the bore (diameter of the gun barrel, in inches) of the main guns, and
REM| the displacement (weight, in tons). 

REM| DROPPING Tables

DROP TABLE Shipclass;

REM| CREATING Tables;

CREATE TABLE Shipclass (
	class varchar(255),
	type varchar(10),
	country varchar(25),
	numguns int,
	bore int,
	displacement int,
	CONSTRAINT PK_Shipclass PRIMARY KEY (class)
);

REM| Some more commands

REM| 1. Populate the relation with the above(given in the question) set of tuples using INSERT clause

-- Inserting data for Bismark
INSERT INTO Shipclass (class, type, country, numGuns, bore, displacement)
VALUES ('Bismark', 'bb', 'Germany', 8, 14, 32000);

-- Inserting data for Iowa
INSERT INTO Shipclass (class, type, country, numGuns, bore, displacement)
VALUES ('Iowa', 'bb', 'USA', 9, 16, 46000);

-- Inserting data for Kongo
INSERT INTO Shipclass (class, type, country, numGuns, bore, displacement)
VALUES ('Kongo', 'bc', 'Japan', 8, 15, 42000);

-- Inserting data for North Carolina
INSERT INTO Shipclass (class, type, country, numGuns, bore, displacement)
VALUES ('North Carolina', 'bb', 'USA', 9, 16, 37000);

-- Inserting data for Revenge
INSERT INTO Shipclass (class, type, country, numGuns, bore, displacement)
VALUES ('Revenge', 'bb', 'Gt. Britain', 8, 15, 29000);

-- Inserting data for Renown
INSERT INTO Shipclass (class, type, country, numGuns, bore, displacement)
VALUES ('Renown', 'bc', 'Gt. Britain', 6, 15, 32000);


REM| 2.Display the populated relation

SELECT * FROM Shipclass;

REM| 3. Mark an intermediate point here in this transaction.

SAVEPOINT intermediate_point;

REM| 4. For the battleships having at least 9 number of guns or the ships with at least 15
REM| inch bore, increase the displacement by 10%.

UPDATE Shipclass
SET displacement = displacement * 1.10
WHERE type = 'bb' and (numguns >= 9 or bore >= 15);

SELECT * FROM Shipclass;

REM| 5. Delete Kongo class of ship from Classes table.

DELETE FROM Shipclass
WHERE class = 'Kongo';

REM| 6. Display your changes to the table.

SELECT * FROM Shipclass;

REM| 7. Discard the recent updates to the relation without discarding the earlier INSERT
REM| operation(s).

ROLLBACK TO intermediate_point;
SELECT * FROM Shipclass;

REM| 8.Commit the changes

COMMIT;
