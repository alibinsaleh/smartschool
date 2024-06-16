      >>SOURCE FORMAT FREE
       IDENTIFICATION DIVISION.
       PROGRAM-ID. print_students.
       AUTHOR. ALI ALMOHAMMED SALEH.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT STUDENT-FILE ASSIGN TO 
               'students_data_cobol_structure.dat' 
               ORGANIZATION IS LINE SEQUENTIAL.
           SELECT REPORT-FILE  ASSIGN TO 'students_report.txt'
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD   STUDENT-FILE.
       01   INREC.
            05   STUDENT-NUMBER         PIC X(10).
            05   FILLER                 PIC X.
            05   STUDENT-NAME           PIC X(30).
            05   FILLER                 PIC X.
            05   CLASSROOM              PIC X(3).
            05   FILLER                 PIC X.
            05   STUDENT-ADDRESS        PIC X(30).
            05   FILLER                 PIC X.
            05   MOBILE-NUMBER          PIC X(15).
            05   FILLER                 PIC X.
            05   CREATED-AT             PIC X(10).
       
       FD   REPORT-FILE.
       01   REPORT-LINE                 PIC X(105).

       WORKING-STORAGE SECTION.
       01   WS-EOF           PIC X VALUE 'N'.
       
       PROCEDURE DIVISION.
           OPEN INPUT STUDENT-FILE OUTPUT REPORT-FILE.
           
           PERFORM PRINT-REPORT.
           CLOSE STUDENT-FILE.
           CLOSE REPORT-FILE.
           STOP RUN.

       PRINT-REPORT.
           MOVE 
           "******** S T U D E N T S    L I S T    R E P O R T ********"
           TO REPORT-LINE 
           WRITE REPORT-LINE
           MOVE SPACES TO REPORT-LINE 
           WRITE REPORT-LINE
           PERFORM UNTIL WS-EOF = 'Y'
                READ STUDENT-FILE 
                    AT END
                        MOVE 'Y' TO WS-EOF
                    NOT AT END
                        MOVE INREC TO REPORT-LINE
                        WRITE REPORT-LINE
                END-READ
           END-PERFORM
           MOVE SPACES TO REPORT-LINE 
           WRITE REPORT-LINE
           MOVE "********* E N D   O F   R E P O R T ***********" TO
           REPORT-LINE
           WRITE REPORT-LINE. 
