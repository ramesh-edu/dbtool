from lib import PgOp
import logging
from sqlqueries.useractivity import useractivity


def usercheck(pg,user,outfile=None,db=None):
    logging.info('You are in the usercheck module')

    file1 = open(outfile, "a") 

    login=0

    ###Validate the existance of the user

    sql=useractivity.userval+" where rolname='"+user+"'"
    res=pg.runssql(sql).fetchall()
    if res == []:
        logging.info('User Not exists')        
        file1.write(db+' : User Not Exists \n')
        return
    else:
        if res[0][1] :
            logging.info('Login is true. So, proceeding further...')
            login=1
        else :
            file1.write(db+' : Login is false \n')
        

    ####Validate any objects in the database

    sql=useractivity.userObjects+" and  rol.rolname='"+user+"'"
    res=pg.runssql(sql).fetchall()

    if res == []:
        logging.info('No Objects found for that user ')
    else:
        logging.info('list of objects ')
        logging.info(res.fetchall())

    if login == 1:
        ###Update the user to nologin settings
        sql="alter user "+user+"  nologin"
        pg.runssql(sql)
        logging.info('User modified to nologin')
        file1.write(db+' : Changed to NOLogin \n')

    file1.close()


