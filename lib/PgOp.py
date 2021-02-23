from lib import PgCon
import logging
import psycopg2


class PgOp(PgCon):
  
    def display(self,var1):
        """
        Display the message in the variable var1
        :param var1: string
        :return: None
        """
        self.logger.info (var1)
        self.cursor.execute("Select 'In PgCon display module'")
        self.logger.info(self.cursor.fetchall())

    def runpsql(self,sqlString,param):
        """
        Execute the sqlString with in the database connection session
        :param sqlString: string
        :return: psycopg2 object
        """
        try:

            self.logger.debug(' Executing the select  ' + sqlString)
            self.cursor.execute(sqlString,param)
            return(self.cursor)
        except psycopg2.Error as e:
            error, = e.args
            self.logger.debug('Database connection error: %s',format(e))
            raise

    def runssql(self,sqlString,vardict=None):
        """
        Execute the sqlString with in the database connection session
        :param sqlString: string
        :return: psycopg2 object
        """

        try:
            if vardict is None:
                self.logger.debug(' Executing the statement  ' + sqlString)
                self.cursor.execute(sqlString)
            else:
                self.logger.debug(' Executing the statement  ')
                self.logger.debug(sqlString)
                self.logger.debug(vardict.values())
                self.cursor.execute(sqlString,vardict)
            return self.cursor
        except psycopg2.Error as e:
            error, = e.args
            self.logger.debug('Database connection error: %s',format(e))
            #raise

    def getState(self,query):
        self.logger.debug(' Check the existance of hashvalue in the table  ' + query)
        if self.cursor.execute(query).fetchone()[0] > 0:
            state='update'
        else:
            state='insert'
        self.logger.debug(' StateResult: State ' + state)
        return state

    def runusql(self,sqlString):
        """
        Execute the update statement with in the database connection session
        :param sqlString: string
        :return: cx_Oracle object
        """
        try:
            self.logger.debug(' Executing the statement  ' + sqlString)
            self.cursor.execute(sqlString)
        except psycopg2.Error as e:
            error, = e.args
            self.logger.debug('Database connection error: %s',format(e))
            raise

    def runmsql(self,query,rows):
        self.logger.debug(' Inserting the database  ' + query )
        self.logger.debug('Inserting records are ')
        self.logger.debug(rows)
        #self.cursor.prepare(query)
        nRet=0
        try:
            self.cursor.executemany(query, rows)
            nRet=self.cursor.rowcount
            self.logger.info('Successfully inserted the data')
            self.dbcon.commit()
        except psycopg2.Error as e:
            self.dbcon.rollback()
            error, = e.args
            self.logger.warning('Failed inserting the data: %s',format(e))
        return nRet
                        

    def runddl(self,query):
        self.logger.debug('Executing the DDL Commands...')
        self.logger.info('Running the DDL ' + '\n                  DDL :   '+ query )
        start=time.time()
        self.cursor.execute(query)
        self.logger.info('Elapsed time'+str(time.time()-start))


    def commit(self):
        """
        Doing explicit Commit in the database connection session
        :return:
        """
        self.logger.info("Performing the commit")
        self.dbcon.commit()


    def rollback(self):
        """
        Doing explicit Commit in the database connection session
        :return:
        """
        self.logger.info("Performing the commit")
        self.dbcon.rollback()



if __name__ == '__main__':
    #obj=Connection('cdlmasdevops1.es.ad.adp.com',1521,'wfc09d')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s:%(message)s',
                    filename='sample.log', datefmt='%m/%d/%Y %I:%M:%S %p',
                    filemode='w')
    obj=PgOp('test.xxxx',5432,'test')
    obj.entry('test','admin123')
    obj.display('Test Successful')
    print ("Version 2.0")    


