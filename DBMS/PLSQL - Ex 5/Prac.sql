REM| Harishraj S
REM| PL/SQL queries

-- PRINT FIRST 5 NUMBERS SUM

SET SERVEROUTPUT ON;

DECLARE 
   n NUMBER := &n;
   sum_num NUMBER := 0;
BEGIN
   FOR num IN 1..n LOOP
      sum_num := sum_num + num;
      DBMS_OUTPUT.PUT_LINE('Loop num: ' || num || ', Sum: ' || sum_num);
   END LOOP;
END;
/


