from Singleton import Singleton
from enum import Enum

class ObjectIdentifier(Singleton):

    def __init__(self):
        Singleton.__init__(self)
            
