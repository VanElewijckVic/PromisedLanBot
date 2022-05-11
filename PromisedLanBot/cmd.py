import discord

class Commands(object):
    prefix = '$'
    __instance = None
    
    def __new__(cls):
        if Commands.__instance == None:
            Commands.__instance = object.__new__(cls)
        return Commands.__instance

    

    
    


