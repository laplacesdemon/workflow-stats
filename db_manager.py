#!/usr/bin/env python
"""
Writes the app usage to db.

Author: Suleyman Melikoglu
suleyman [at] melikoglu.info
"""
import sqlite3 as lite
import datetime


class DatabaseManager(object):

    db_name = 'app_usage.db'
    db_table = "usage"

    def __init__(self):
        con = lite.connect(self.db_name)
        with con:
            cur = con.cursor()

            # try to create the table, if not already created
            try:
                cur.execute("CREATE TABLE %s (name TEXT, usage_time TIMESTAMP, session_start_time TIMESTAMP)" % self.db_table)
            except:
                # table is already created
                pass

    def enter_usage_to_db(self, app_name, usage_time):
        """Writes usage info to sqlite3 db"""
        con = lite.connect(self.db_name)
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO %s VALUES('%s', '%s', '%s')" % (self.db_table, app_name, usage_time, datetime.datetime.now()))

    def print_total_usage(self):
        """Print total usage to the screen"""
        con = lite.connect(self.db_name)
        with con:
            cur = con.cursor()
            cur.execute("SELECT name, SUM(usage_time) as total_time FROM %s GROUP BY name ORDER BY total_time desc" % self.db_table)
            rows = cur.fetchall()

            longest_name = max([len(row[0]) for row in rows] + [len('Application')]) + 2
            print ''
            print "%s | %s" % ('Application'.ljust(longest_name), 'Total Time')
            print "-" * (longest_name + 18)

            for row in rows:
                print "%s | %s" % (
                    row[0].ljust(longest_name),
                    str(datetime.timedelta(seconds=row[1])),
                )
