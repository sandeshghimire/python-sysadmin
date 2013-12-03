#!/usr/bin/env python 

import syslog

class PyBackup(object):
    def __init__ (self, server_name, username, password):
        syslog.syslog("starting backup process")
        self.server_name= server_name
        self.username = username
        self.password = password
        
        
        
if __name__ == '__main__':
    
        
    
    