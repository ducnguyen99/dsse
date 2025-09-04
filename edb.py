class EDB:
    def __init__(self, n: int, p: float, k: int) -> None:
        """
        n: (w,id) pair num
        p: False positive rate of BF
        k: Expansion factor of TSet
        """
        self.tset = TSet(n, k)
        self.xset = BF(n, p)

    def EDBSetup(self, fpath_wid: str, keys: PARAMS):
        T = dict()

        # read the inverted index
        dct_wid = read_index(fpath_wid)

        # every keyword - ids
        for w, ids in dct_wid.items():
            ke = prf(keys.ks, w)
            xtrap = pbc.prfToZr(keys.kx, w)
            # every id in ids
            t = []
            for i in range(len(ids)):
                # TSet
                ind = ids[i]
                xind = pbc.prfToZr(keys.ki, ind)
                z = pbc.prfToZr(keys.kz, w + str(i))
                y = pbc.mul2Zr(xind, ~z)
                y = pbc.Zr2Bytes(y)
                e = AES_enc(ke, ind)
                element = struct.pack("H", len(y)) + y + e
                t.append(element)
                # XSet
                xtag = pbc.gToPower2(xind, xtrap)
                self.xset.add(str(xtag))
            T[w] = t

        keys.kt = self.tset.setup(T)