class MySQLc:
    import MySQLdb

    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                         user="root", # your username
                         passwd="", # your password
                         db="mydata") # name of the database

    # you must create a Cursor object. It will let
    #  you execute all the query you need
    cur = db.cursor() 
    
    #
    #database schema/structure:
    #
    #create table itemTable (ID numeric(3), item varchar(15), price numeric(5,2));
    #insert into itemTable values ('1', 'bananOne', '3');
    #insert into itemTable values ('2', 'bananTwo', '4');
    #insert into itemTable values ('3', 'bananThree', '4.55');
    #insert into itemTable values ('4', 'bananFour', '6.66');
