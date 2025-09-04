from Crypto.Random import get_random_bytes
from .cryptoUtils import prf, hash_length, xor_bytes
from dataclasses import dataclass
from Crypto.Util.number import long_to_bytes
import random
import math

@dataclass
class HValue:
    b: int
    L: bytes
    K: bytes



class TSet:
    kt: bytes
    FileCnt: dict
    DictW: dict


    def __init__(self):
      self.__init__


    def setup(self):
      self.kt = get_random_bytes(32)
      self.FileCnt = {}
      self.DictW = {}

    def update(self, op: str, w: str, id: str):
        if w not in self.FileCnt:
          self.FileCnt[w] = -1

        self.FileCnt[w] = self.FileCnt[w] + 1

        addr = prf(self.kt, w + str(self.FileCnt[w]) + str(0))
        val = xor_bytes(bytes(id + op, 'utf-8'), prf(self.kt, w + str(self.FileCnt[w]) + str(1)))

        self.DictW[addr] = val
            


    def search(self, w: str):
      Tlist = []
      # print(self.DictW)
      for i in range(0, self.FileCnt[w] + 1):
        addr = prf(self.kt, w + str(i) + str(0))
        if addr in self.DictW:
          Tlist.append(self.DictW[addr])

      print(len(Tlist))
      res = [] 
      for i in range(0, len(Tlist)):
        tmp = xor_bytes(Tlist[i], prf(self.kt, w + str(i) + str(1)))
        tmp = tmp.decode('utf-8') # tmp has length 32 bytes, to remove opp, slice to -30
        res.append(tmp[:-30])
        

        
      return res


def genStag(kt: bytes, w: str) -> bytes:
    return prf(kt, w)


# Calculate the memory size of useful data in TSet
def cal_size(tset: TSet) -> int:
    size = 0
    for pair_lst in tset.t_set:
        for pair in pair_lst:
            if pair != b"":
                size += len(pair)
    return size
