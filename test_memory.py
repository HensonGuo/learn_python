# coding=utf-8
__author__ = 'g7842'

# import gc
# import memory_profiler
# from memory_profiler import profile
#
# @profile
# def test():
#     for i in range(999999,0,-1):
#       s =  str(i) * i
#       s = None
#       gc.collect()
#
# if __name__ == "__main__":
#     test()

import sys
print (sys.getsizeof(1))
print (sys.getsizeof(2))
print (sys.getsizeof(1000000))
print(sys.getsizeof('a'))
print(sys.getsizeof('ab'))
print(sys.getsizeof('abc'))
print (sys.getsizeof({}))
print(sys.getsizeof({'1':123, '2':11}))
print(sys.getsizeof({u'toNick': u'', u'auth_anchor': u'', u'uid': 20092192, u'toUid': 0, u'camp': u'', u'private': 0, u'bubbleLevel': 0, u'bubbleType': 0, u'nick': u'\u5c3e\u706f\u5c3e\u706f\u5c3e\u706f\u5c3e\u706f\u5c3e\u706f\u5c3e\u706f\u5c3e\u706f\u5c3e\u706f\u5c3e\u706f\u5c3e\u706f\u5c3e\u706f\u5c3e\u706f', 'uidAdmin': True, 'role': 800, u'gameType': 0, u'time': u'2017-09-13 12:08:48', u'msg': u'444444444444444444444444444444444444444444444444444444444', 'uidVip': False, 'sex': 0, u'type': u'', u'gamelive_chat_json_data': u'{"wushentan": {"team_name": "c\\u67e5", "team": 2}, "badgeInfo": {"badgename": "ca3", "anchor_uid": 20051152, "level": 2}, "ccid": 7996874, "rideInfo": {"body": 0, "saleid": 0, "has_flag": 0}}', u'nameBoardId': 0}))