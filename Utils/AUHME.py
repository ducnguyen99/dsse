from Crypto.Random import get_random_bytes
from .cryptoUtils import prf, hash_length, xor_bytes

class AUHME:
  k1: bytes
  k2: bytes
  k3: bytes

  def setup(self):
    self.k1 = get_random_bytes(32)
    self.k2 = get_random_bytes(32)
    self.k3 = get_random_bytes(32)

  def enc(self, dict: dict):
    enc_dict = {}
    for (k, v) in dict:
      addr = prf(self.k1, k)
      val = xor_bytes(prf(self.k2, addr + v), prf(self.k3, addr + 0))
      enc_dict[addr] = val

    return enc_dict
  
  def gen_upd(self, op: str, k, v, params):
    tok = {}
    cnt, local_addr = params
    utok = []
    if op == "add":
      addr = prf(self.k1, k)
      val = xor_bytes(prf(self.k2, addr + bytes(str(v), 'utf-8')), prf(self.k3, addr + bytes(str(cnt), 'utf-8')))
      tok[addr] = val
      local_addr.append(addr)
   
    # return (utok, params)
    else:
      for k in local_addr:
        upd_val_tok = xor_bytes(prf(self.k2, k + str(0)), prf(self.k2, k + str(1)))
        upd_cnt_tok = xor_bytes(prf(self.k3, k + str(cnt)), prf(self.k3, k + str(cnt + 1)))
        tok[k] = xor_bytes(upd_val_tok, upd_cnt_tok)
        cnt = cnt + 1
      
    params = (cnt, local_addr)
    utok = (op, tok)
    # print(utok)
    return (utok, params)
      
  def apply_upd(self, utok: list, enc_dict: tuple):
    # print(utok)
    op, tok = utok

    if op == "add":
      for (k, v) in tok.items():
        enc_dict[k] = v
    else:
      for (k, v) in tok:
        enc_dict[k] = xor_bytes(enc_dict[k], v)
  
  def key_gen(self, dict: dict, params):
    xors = b'\x00'
    cnt, _ = params
    loc = []

    for (k, v) in dict.items():
      addr = prf(self.k1, k)
      loc.append(addr)
      tmp = xor_bytes(prf(self.k2, addr + bytes(str(v), 'utf-8')), prf(self.k3, addr + bytes(str(cnt), 'utf-8')))
      xors = xor_bytes(xors, tmp)

    rand = get_random_bytes(32)
    hash_val = hash(rand + xors)

    return (loc, rand, hash_val)
  

  def query(self, dk, enc_dict):
    loc, r, h = dk
    xors = b'\x00'

    for k in loc:
      xors = xor_bytes(xors, enc_dict[k])

    hash_val = hash(r + xors)

    return hash_val == h
  
