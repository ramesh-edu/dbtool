import psycopg2
import datetime
import logging


class PgCon(object):
    hostname=''
    dbname=''
    port=''
    dbcon=''
    cursor=''

    def __init__(self, hostname, port, dbname):
        """
        Prepare for the Connection string information
        :param hostname: string  <<<Hostname>>>
        :param port: integer <<<Port Number>>>
        :param servicename: string <<<Service Name>>>
        """
        self.hostname = hostname
        self.dbname = dbname
        self.port = port
        self.connectionstring = hostname+":"+str(port)+"/"+dbname
        self.logger = logging.getLogger('Connection')
        self.logger.debug(self.connectionstring)

    def entry(self, username, pwd):
        """
        Connect to the database
        :param username:  string   <<<username>>>
        :param pwd: string <<<password>>>
        :return: None
        """
        try:
            self.dbcon = psycopg2.connect(host=self.hostname,dbname=self.dbname,port=self.port,user=username,password=pwd)
            self.cursor = self.dbcon.cursor()
        except psycopg2.Error as e:
            error, = e.args
            self.logger.info(str(e.args))
            self.logger.info('Database connection error: %s',format(e))
            raise

    def exit(self):
        """
        Disconnect from the database. If this fails, for instance
        if the connection instance doesn't exist we don't really care.
        """
        try:
            self.cursor.close()
            self.dbcon.close()
        except psycopg2.Error as e:
            pass

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s:%(message)s',
                    filename='sample.log', datefmt='%m/%d/%Y %I:%M:%S %p',
                    filemode='w')
    obj=PgCon('test.xxx',5432,'test')
    obj.entry('test','test123')

