#!/usr/bin/env python3
import unittest
from lib import load
import main


class Cmd(unittest.TestCase):
    def test_info(self):
        self.fail("Not implemented")

    def test_dead(self):
        self.fail("Not implemented")

    def test_list(self):
        #self.fail("Not implemented")
        #list_ = load.parse_mvp_list("test_files/test_mvps1.list")
        print("respond: ", main.get_mvps())

    def test_help(self):
        self.fail("Not implemented")


class Load(unittest.TestCase):
    def test_1_load_settings(self):
        ret = load.load_settings("test_files/test_config1.yml")
        token = ret['token']
        mvp_list = ret['mvp_list']
        time_diff = ret['time_diff']

        self.assertEqual(token, "abc1234ghj")
        self.assertEqual(time_diff, 9)
        self.assertEqual(mvp_list, "mvps.list")

    def test_2_load_settings(self):
        ret = load.load_settings("test_files/test_config2.yml")
        token = ret['token']
        mvp_list = ret['mvp_list']
        time_diff = ret['time_diff']

        self.assertEqual(token, "abc1234ghj0000")
        self.assertEqual(time_diff, -9)
        self.assertEqual(mvp_list, "mvps_test.list")

    def test_1_load_list_mvp_names(self):
        ret = load.parse_mvp_list("test_files/test_mvps1.list")
        if len(ret) != 3:
            self.assertFalse()
        self.assertNotEqual(ret['Ygnizem'], None)
        self.assertNotEqual(ret['Amon Ra'], None)
        self.assertNotEqual(ret['Assassin Cross Eremes'], None)

#    def test_1_load_list_mvp_info(self):
#        ret = load.parse_mvp_list("test_files/test_mvps1.list")
#        if len(ret) != 3:
#            self.assertFalse()
#        mvp1 = ret[0]
#        mvp2 = ret[1]
#        mvp3 = ret[2]
#
#        self.assertEqual(mvp1.info, [['moc_pryd06', 60, 70], ['test', 20, 20]])
#       self.assertEqual(mvp2.info, [['lhz_dun03', 100, 130]])
#         self.assertEqual(mvp3.info, [['lhz_dun02', 120, 130]])
#
#    def test_2_load_list_mvp_info(self):
#        names = ['moc_pryd06', 'test', 'lhz_dun03', 'lhz_dun02']
#        ret = load.parse_mvp_list("test_files/test_mvps1.list")
#        i = 0
#        for key in ret:
#            self.assertEqual(ret[key].info[0], names[i])
#            i += 1
#
#    def test_3_load_list_mvp_info(self):
#        ret = load.parse_mvp_list("test_files/test_mvps1.list")
#        if len(ret) != 3:
#            self.assertFalse()
#        mvp1 = ret[0]
#        mvp2 = ret[1]
#        mvp3 = ret[2]
#
#        self.assertEqual(mvp1.maps[0].time_min, 60)
#        self.assertEqual(mvp1.maps[0].time_max, 70)
#        self.assertEqual(mvp1.maps[1].time_min, 20)
#        self.assertEqual(mvp1.maps[1].time_max, 20)
#        self.assertEqual(mvp2.maps[0].time_min, 100)
#        self.assertEqual(mvp2.maps[0].time_max, 130)
#        self.assertEqual(mvp3.maps[0].time_min, 120)
#        self.assertEqual(mvp3.maps[0].time_max, 130)


if __name__ == '__main__':
    unittest.main()
