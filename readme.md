# Database Command Line tool 

This package can be installed using the below command and also can be used directly using the file  dbshipt.py

Installation of the package

```sh
python setup.py install
```

To use directly use the file  dbshipt.py

Currently, the script offers to user validation.
  
# Tools Used

    -   Python 3
    
Custom packages Needed

    - psycopg2
    

User Defined Packages and Libraries
  
    - lib
        - PgCon
        - PgOp
        - usercheck
    
    - sqlqueries
        - useractivity
        
## Scritp Execution  

Script Help documentation

```sh
$ python dbshipt.py -h
usage: dbshipt.py [-h] [-u USER] [-l LOGFILE] [-d DEBUGLEVEL] [-f CONFILE]
                  [-o OUTPUTFILE]

This program provides command line tool for the postgres activity

optional arguments:
  -h, --help     show this help message and exit
  -u USER        Store the username
  -l LOGFILE     Store the logfile
  -d DEBUGLEVEL  Debug Level
  -f CONFILE     Postgres Databases connection information file
  -o OUTPUTFILE  Output Status File

```

About input parameters

- The script default genreates an output file and logfile.
- The logfile is used for debugging purpose.  We can log more details by passing the parameter DEBUG
- The Script takes connection file as an input parameter.  The file consists of list of database connections in a required format.
- Another parameter user has to be passed to validate the user and turn the user to nologin

Sample Script execution

```sh
    python dbshipt.py -u test -f connections.txt -d DEBUG
```

###Reference
rameshgopisettyny@gmail.com