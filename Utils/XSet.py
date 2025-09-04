from Crypto.Random import get_random_bytes
from .cryptoUtils import prf, hash_length, xor_bytes
from dataclasses import dataclass
from Crypto.Util.number import long_to_bytes
from .AUHME import AUHME
import random
import math




class XSet:
    kt: bytes
    FileCnt: dict
    DictW: dict


    def __init__(self):
      self.__init__


    def setup(self):
      self.DictW = {}

    def update(self, utok, auhme: AUHME):
      # print(utok)
      auhme.apply_upd(utok, self.DictW)
      
            
    # def print_txt(self):
    #    for k, v in self.DictW.items():
    #       print(k.decode('utf-8') + ": " + v.decode('utf-8'))

    def search(self, dk, auhme: AUHME):
      pos = []
      for i in range(0, len(dk)):
        if auhme.query(dk[i], self.DictW):
          pos.append(i)

        
      return pos

    def print_xset(self):
      print(self.DictW)

