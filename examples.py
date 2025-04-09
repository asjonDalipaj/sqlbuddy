examples = [
    {
        "input": "Details of contract with the longest term of months?",
        "query": '''
You are an Oracle SQL expert. Given an input question, first create a syntactically correct Oracle SQL query to run.
Here is the relevant table info:
Table Name:sictrhead
Table Description: Contains contract header info.
Columns: contract (Primary Key) type VARCHAR2(20 CHAR), dtapproval type DATE, dtsign type DATE, dstart type DATE, dteot type DATE, cdproduct (Foreign Key to tabproducts) type VARCHAR2(10 CHAR),
cdstatus (Foreign Key to tabstatu) type VARCHAR2(1 CHAR), cdsubstatus (Foreign Key to tabproducts) type VARCHAR2(10 CHAR), cdcustomer (Foreign Key to sianagr) type NUMBER(9),
operator type VARCHAR2(320 CHAR), ctrgroupctr VARCHAR2(20 CHAR)
Columns description: contract is contract id, dtapproval is approval date, dtsign is signature date, dstart is start date, cdproduct is contract product code,
cdstatus is contract status code, cdsubstatus is contract substatus code, cdcustomer is contract's client id, operator is contract's creator name, ctrgroupctr is contract's financial arrangement

CREATE TABLE sictrhead(CONTRACT VARCHAR2(20 CHAR) NOT NULL,
                       DTAPPROVAL DATE,
                       DTSIGN DATE,
                       DTSTART  DATE,
                       DTEOT DATE,
                       CDPRODUCT VARCHAR2(10 CHAR) NOT NULL,
                       CDSTATUS VARCHAR2(1 CHAR) NOT NULL,
                       CDSUBSTATUS VARCHAR2(10 CHAR) NOT NULL,
                       CDCUSTOMER NUMBER(9),
                       OPERATOR  VARCHAR2(320 CHAR),
                       CTRGROUPCTR  VARCHAR2(20 CHAR));
ALTER TABLE sictrhead ADD (CONSTRAINT PK_SICTRHEAD PRIMARY KEY(CONTRACT),
                           FOREIGN KEY (CDPRODUCT)
                           REFERENCES tabproducts (CDPRODUCT),
                           FOREIGN KEY (CDSTATUS, CDSUBSTATUS)
                           REFERENCES tabstatu (COD_STAT, SUB_STAT),
                           FOREIGN KEY (CDCUSTOMER)
                           REFERENCES sianagr (ANACODANA));

Table Name: sictrfin
Table Description: Contains contract financial information
Columns: cdcontract (Primary Key) type  VARCHAR2(10 CHAR) , currtotam type NUMBER(18,4), flplanty ( Foreign Key to inttppia) type VARCHAR2(1 CHAR), nrterm type NUMBER(9),
instty (Foreign Key to intpmt) type VARCHAR2(1 CHAR)
Columns description: cdcontract is the contract id, currtotam is the contract's total amount, flplanty is contract's schedule plan type, nrterm is the contract's total number of months, instty is
the installment type of the contract

CREATE TABLE sictrfin (CDCONTRACT VARCHAR2(20 CHAR) NOT NULL,
                       CURRTOTAM NUMBER(18,4),
                       FLPLANTY VARCHAR2(1 CHAR),
                       NRTERM NUMBER(9),
                       INSTTY VARCHAR2(1 CHAR));
ALTER TABLE sictrfin ADD (CONSTRAINT PK_SICTRFIN PRIMARY KEY (CDCONTRACT),
                          FOREIGN KEY (FLPLANTY)
                          REFERENCES inttpia (CODICE),
                          FOREIGN KEY (INSTTY)
                          REFERENCES intpmt (CODICE));
'''
    },
    {
        "input": "Product description and start date of this contract id?",
        "query": '''
You are an Oracle SQL expert. Given an input question, first create a syntactically correct Oracle SQL query to run.
Here is the relevant table info:
Table Name:sictrhead
Table Description: Contains contract header info.
Columns: contract (Primary Key) type VARCHAR2(20 CHAR), dtapproval type DATE, dtsign type DATE, dtstart type DATE, dteot type DATE, cdproduct (Foreign Key to tabproducts) type VARCHAR2(10 CHAR),
cdstatus (Foreign Key to tabstatu) type VARCHAR2(1 CHAR), cdsubstatus (Foreign Key to tabproducts) type VARCHAR2(10 CHAR), cdcustomer (Foreign Key to sianagr) type NUMBER(9),
operator type VARCHAR2(320 CHAR), ctrgroupctr VARCHAR2(20 CHAR)
Columns description: contract is contract id, dtapproval is approval date, dtsign is signature date, dtstart is start date, cdproduct is contract product code,
cdstatus is contract status code, cdsubstatus is contract substatus code, cdcustomer is contract's client id, operator is contract's creator name, ctrgroupctr is contract's financial arrangement

CREATE TABLE sictrhead(CONTRACT VARCHAR2(20 CHAR) NOT NULL,
                       DTAPPROVAL DATE,
                       DTSIGN DATE,
                       DTSTART  DATE,
                       DTEOT DATE,
                       CDPRODUCT VARCHAR2(10 CHAR) NOT NULL,
                       CDSTATUS VARCHAR2(1 CHAR) NOT NULL,
                       CDSUBSTATUS VARCHAR2(10 CHAR) NOT NULL,
                       CDCUSTOMER NUMBER(9),
                       OPERATOR  VARCHAR2(320 CHAR),
                       CTRGROUPCTR  VARCHAR2(20 CHAR));
ALTER TABLE sictrhead ADD (CONSTRAINT PK_SICTRHEAD PRIMARY KEY(CONTRACT),
                           FOREIGN KEY (CDPRODUCT)
                           REFERENCES tabproducts (CDPRODUCT),
                           FOREIGN KEY (CDSTATUS, CDSUBSTATUS)
                           REFERENCES tabstatu (COD_STAT, SUB_STAT),
                           FOREIGN KEY (CDCUSTOMER)
                           REFERENCES sianagr (ANACODANA));

Table Name: sictrfin
Table Description: Contains contract financial information
Columns: cdcontract (Primary Key) type  VARCHAR2(10 CHAR) , currtotam type NUMBER(18,4), flplanty ( Foreign Key to inttppia) type VARCHAR2(1 CHAR), nrterm type NUMBER(9),
instty (Foreign Key to intpmt) type VARCHAR2(1 CHAR)
Columns description: cdcontract is the contract id, currtotam is the contract's total amount, flplanty is contract's schedule plan type, nrterm is the contract's total number of months, instty is
the installment type of the contract

CREATE TABLE sictrfin (CDCONTRACT VARCHAR2(20 CHAR) NOT NULL,
                       CURRTOTAM NUMBER(18,4),
                       FLPLANTY VARCHAR2(1 CHAR),
                       NRTERM NUMBER(9),
                       INSTTY VARCHAR2(1 CHAR));
ALTER TABLE sictrfin ADD (CONSTRAINT PK_SICTRFIN PRIMARY KEY (CDCONTRACT),
                          FOREIGN KEY (FLPLANTY)
                          REFERENCES inttpia (CODICE),
                          FOREIGN KEY (INSTTY)
                          REFERENCES intpmt (CODICE));

Table Name: tabproducts
Table Description: Contains contract product description
Columns: cdproduct (Primary Key) type VARCHAR2(10 CHAR), description type VARCHAR2(2000 CHAR)
Columns description: cdproduct is the product code, description is the description of the product code

CREATE TABLE tabproducts (CDPRODUCT VARCHAR2(10 CHAR) NOT NULL,
                          DESCRIPTION VARCHAR2(2000 CHAR) NOT NULL);
ALTER TABLE tabproducts ADD (CONSTRAINT PK_TABPRODUCTS PRIMARY KEY(CDPRODUCT));

Human Question: Details of contract with the longest term of months?

AI:
The contract with longest term of month is '311627575550000'

SQL Query:
SELECT
    h.contract,
    h.dtapproval,
    h.dtsign,
    h.dtstart,
    h.dteot,
    h.cdproduct,
    h.cdstatus,
    h.cdsubstatus,
    h.cdcustomer,
    h.operator,
    h.ctrgroupctr,
    f.currtotam,
    f.flplanty,
    f.nrterm,
    f.instty
FROM
    sictrhead h
JOIN
    sictrfin f ON h.contract = f.cdcontract
WHERE
    f.nrterm = (SELECT MAX(nrterm) FROM sictrfin)
'''},
    {
        "input": "Give the asset details of this contract id",
        "query": '''
You are an Oracle SQL expert. Given an input question, first create a syntactically correct Oracle SQL query to run.
Here is the relevant table info:
Table Name:sictrhead
Table Description: Contains contract header info.
Columns: contract (Primary Key) type VARCHAR2(20 CHAR), dtapproval type DATE, dtsign type DATE, dstart type DATE, dteot type DATE, cdproduct (Foreign Key to tabproducts) type VARCHAR2(10 CHAR),
cdstatus (Foreign Key to tabstatu) type VARCHAR2(1 CHAR), cdsubstatus (Foreign Key to tabproducts) type VARCHAR2(10 CHAR), cdcustomer (Foreign Key to sianagr) type NUMBER(9),
operator type VARCHAR2(320 CHAR), ctrgroupctr VARCHAR2(20 CHAR)
Columns description: contract is contract id, dtapproval is approval date, dtsign is signature date, dstart is start date, cdproduct is contract product code,
cdstatus is contract status code, cdsubstatus is contract substatus code, cdcustomer is contract's client id, operator is contract's creator name, ctrgroupctr is contract's financial arrangement

CREATE TABLE sictrhead(CONTRACT VARCHAR2(20 CHAR) NOT NULL,
                       DTAPPROVAL DATE,
                       DTSIGN DATE,
                       DTSTART  DATE,
                       DTEOT DATE,
                       CDPRODUCT VARCHAR2(10 CHAR) NOT NULL,
                       CDSTATUS VARCHAR2(1 CHAR) NOT NULL,
                       CDSUBSTATUS VARCHAR2(10 CHAR) NOT NULL,
                       CDCUSTOMER NUMBER(9),
                       OPERATOR  VARCHAR2(320 CHAR),
                       CTRGROUPCTR  VARCHAR2(20 CHAR));
ALTER TABLE sictrhead ADD (CONSTRAINT PK_SICTRHEAD PRIMARY KEY(CONTRACT),
                           FOREIGN KEY (CDPRODUCT)
                           REFERENCES tabproducts (CDPRODUCT),
                           FOREIGN KEY (CDSTATUS, CDSUBSTATUS)
                           REFERENCES tabstatu (COD_STAT, SUB_STAT),
                           FOREIGN KEY (CDCUSTOMER)
                           REFERENCES sianagr (ANACODANA));

Table Name: sicespit
Table Description: Contains contract object info
Columns: cescodces (Primary Key) type NUMBER(9), cescodctr (Foreign Key to sictrhead) type VARCHAR2(20 CHAR),
ces_a_s_i (Foreign key to intcateg) type VARCHAR2(1 CHAR), cestarga type VARCHAR2(15 CHAR),
autmodello type VARCHAR2(50 CHAR), cesvalval type NUMBER(18,4)
Columns description: cescodces is the object id from the contract, cescodctr is the contract id, ces_a_s_i is the object category,
cestarga is the object's licence plate number, autmodello is the object's car model, cesvalval is the object purchase value

CREATE TABLE sicespit (CESCODCES NUMBER(9) NOT NULL,
                       CESCODCTR VARCHAR2(20 CHAR),
                       CES_A_S_I VARCHAR2(1 CHAR),
                       CESTARGA VARCHAR2(15 CHAR),
                       AUTMODELLO VARCHAR2(50 CHAR),
                       CESVALVAL NUMBER(18,4));
ALTER TABLE sicespit ADD (CONSTRAINT PK_SICESPIT PRIMARY KEY (CESCODCES),
                          FOREIGN KEY (CESCODCTR)
                          REFERENCES sictrhead (CONTRACT),
                          FOREIGN KEY (CES_A_S_I)
                          REFERENCES intcateg (CODE));

Table Name: intcateg
Table Description: Contains object category code description
Columns: code (Primary Key) type VARCHAR2(1 CHAR) , description type VARCHAR2(25 CHAR)
Columns description: code is the category code, description is the category's code description

CREATE TABLE intcateg (CODE VARCHAR2(1 CHAR) NOT NULL,
                       DESCRIPTION  VARCHAR2(25 CHAR));
ALTER TABLE INTCATEG ADD (CONSTRAINT PK_INTCATEG PRIMARY KEY (CODE);

Table Name:tabstatu
Table Description: Contains contract status description.
Columns: cod_stat (Primary Key) type VARCHAR2(1 CHAR), sub_stat(Primary Key) type  VARCHAR2(10 CHAR) , des_stat type VARCHAR2(2000 CHAR)
Columns description: cod_stat is the status code, sub_stat is the substatus code, des_stat is the description of the status and substatus codes combinations

CREATE TABLE tabstatu (COD_STAT VARCHAR2(1 CHAR) NOT NULL,
                       SUB_STAT VARCHAR2(10 CHAR) NOT NULL,
                       DES_STAT VARCHAR2(2000 CHAR));
ALTER TABLE tabstatu ADD (CONSTRAINT PK_TABSTATU PRIMARY KEY (COD_STAT, SUB_STAT));

Table Name: tabproducts
Table Description: Contains contract product description
Columns: cdproduct (Primary Key) type VARCHAR2(10 CHAR), description type VARCHAR2(2000 CHAR)
Columns description: cdproduct is the product code, description is the description of the product code

CREATE TABLE tabproducts (CDPRODUCT VARCHAR2(10 CHAR) NOT NULL,
                          DESCRIPTION VARCHAR2(2000 CHAR) NOT NULL);
ALTER TABLE tabproducts ADD (CONSTRAINT PK_TABPRODUCTS PRIMARY KEY(CDPRODUCT));

Human Question: Details of contract with the longest term of months?

AI:
The contract with longest term of month is '311627575550000'

SQL Query:
SELECT
    h.contract,
    h.dtapproval,
    h.dtsign,
    h.dtstart,
    h.dteot,
    h.cdproduct,
    h.cdstatus,
    h.cdsubstatus,
    h.cdcustomer,
    h.operator,
    h.ctrgroupctr,
    f.currtotam,
    f.flplanty,
    f.nrterm,
    f.instty
FROM
    sictrhead h
JOIN
    sictrfin f ON h.contract = f.cdcontract
WHERE
    f.nrterm = (SELECT MAX(nrterm) FROM sictrfin)

Human Question: Product description and start date of this contract id?

AI:
The Product description is 'Huurovereenkomst' and start date is '31-JAN-12'

SQLQuery:
SELECT
    p.description,
    h.dtstart
FROM
    sictrhead h
JOIN
    tabproducts p ON h.cdproduct = p.cdproduct
WHERE
    h.contract = '311627575550000';
'''
    }
]