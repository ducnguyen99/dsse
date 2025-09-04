import unittest
from Utils.TSet import TSet, cal_size, genStag
from Utils.XSet import XSet
from Utils.AUHME import AUHME


class TestXSetSearch(unittest.TestCase):
    def test_xset_search(self):
        # Given data
        xset_dict = {
            "kw1||f1": 1, "kw1||f2": 1, "kw1||f3": 0,
            "kw2||f1": 1, "kw2||f2": 1, "kw2||f3": 1,
            "kw3||f1": 1, "kw3||f2": 1, "kw3||f3": 1,
        }

        # Setup XSet and AUHME
        xset = XSet()
        xset.setup()
        auhme = AUHME()
        auhme.setup()

        cnt = 1
        local_addr = []
        params = (cnt, local_addr)

        # Populate xset
        for k, v in xset_dict.items():
            utok, params = auhme.gen_upd("add", k, v, params)
            xset.update(utok, auhme)

        # Prepare keys
        key_dict = [
            {"kw2||f1": 1, "kw3||f1": 1},
            {"kw2||f2": 1, "kw3||f2": 1}
        ]
        dk = [auhme.key_gen(keys, params) for keys in key_dict]

        # Perform search
        res = xset.search(dk, auhme)

        # Assert expected result
        self.assertEqual(res, [0, 1])

if __name__ == "__main__":
    unittest.main()
