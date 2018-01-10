# coding: utf-8
# ----------------------------
# 问题描述:
#
# 已知case, 使用offset=20, 坐标点为(31.2422110000,121.3184590000)时会复现该问题,
# 表现为`offset=3`与`offset=1`召回的poi点有重复召回现象
# `offset`使用其他参数时复现该问题
#
# EXAMPLE:
#
# -----------------------------------------------
# http://restapi.amap.com/v3/place/around?
# location=121.3184590000,31.2422110000&extensions=all
# &page=1&offset=15&sortrule=distance&types=住宅区|学校|门牌信息&key=
# -----------------------------------------------
# | B00155QXUG | 金沙缘圆宝邸 - 金园一路1359弄1-69号 : 0
# | B0FFGLR7LQ | 缘圆宝坻小区 - 金园一路1359弄1-69号 : 115
# | B0FFH10FP3 | 金园社区 - 金园一路 : 174
# | B0FFG94W6Z | 金鹤新城 - 金园一路与金沙江西路交叉口北100米 : 235
# | B0FFINH7HJ | 鹤霞路111弄76号楼 - 嘉定区 : 277
# | B0FFILELLH | 鹤霞路111弄74号楼 - 嘉定区 : 278
# | B0FFILE68O | 鹤霞路111弄72号楼 - 嘉定区 : 281
# | B0FFIKZCYB | 鹤霞路111弄81号楼 - 嘉定区 : 317
# | B0FFILIO7B | 鹤霞路111弄83号楼 - 嘉定区 : 323
# | B0FFILEFUN | 鹤霞路111弄61号楼 - 嘉定区 : 326
# | B0FFIKZ8JZ | 鹤霞路111弄63号楼 - 嘉定区 : 339
# | B0FFINGK4Y | 鹤霞路111弄65号楼 - 嘉定区 : 344
# | B0FFINH7CW | 鹤霞路111弄62号楼 - 嘉定区 : 346
# | B0FFINGK55 | 鹤霞路111弄60号楼 - 嘉定区 : 347
# | B0FFILE6BP | 鹤霞路111弄58号楼 - 嘉定区 : 349
# -----------------------------------------------
# http://restapi.amap.com/v3/place/around?
# location=121.3184590000,31.2422110000&extensions=all
# &page=2&offset=15&sortrule=distance&types=住宅区|学校|门牌信息&key=
# -----------------------------------------------
# | B0FFILE9DA | 鹤霞路111弄69号楼 - 嘉定区 : 356
# | B0FFINH5HZ | 鹤霞路111弄53号楼 - 嘉定区 : 376
# | B0FFINMT8B | 鹤霞路555弄4幢 - 鹤霞路555弄4幢11-12号 : 379
# | B0FFINH84F | 鹤霞路111弄48号楼 - 嘉定区 : 381
# | B00156COV0 | 金霞苑 - 鹤霞路111弄18号 : 382
# | B0FFINMW7S | 鹤霞路555弄7幢 - 鹤霞路555弄7幢17-18号 : 384
# | B0FFILEAFC | 鹤霞路111弄31号楼 - 嘉定区 : 385
# | B0FFINGJUP | 鹤霞路111弄55号楼 - 嘉定区 : 386
# | B0FFINGJ7Z | 鹤霞路111弄44号楼 - 嘉定区 : 386
# | B0FFINGJ7A | 鹤霞路111弄50号楼 - 嘉定区 : 388
# | B0FFILEB2R | 鹤霞路111弄33号楼 - 嘉定区 : 390
# | B0FFING74Y | 鹤霞路555弄17幢 - 鹤霞路555弄17幢38-40号 : 403
# | B0FFIKZES3 | 鹤霞路111弄37号楼 - 嘉定区 : 405
# | B0FFIB3IBZ | 莱茵华庭 - 鹤旋路98号附近 : 411
# | B00156Z1JB | 澜茵华庭 - 嘉定金园一路1519弄 : 411
# -----------------------------------------------
# http://restapi.amap.com/v3/place/around?
# location=121.3184590000,31.2422110000&extensions=all&page=3
# &offset=15&sortrule=distance&types=住宅区|学校|门牌信息&key=
# -----------------------------------------------
# | B0FFIPGOS0 | 鹤霞路111弄39号楼 - 嘉定区 : 412
# | B0FFILJFUC | 鹤霞路555弄11幢 - 鹤霞路555弄11幢26-27号 : 412
# | B0FFIKZ8CL | 鹤霞路111弄41号楼 - 嘉定区 : 420
# | B0FFILFL0C | 鹤霞路555弄5幢 - 鹤霞路555弄5幢13-15号 : 425
# | B0FFILJGPD | 鹤霞路555弄18幢 - 鹤霞路555弄18幢41-42号 : 425
# | B0FFINGJNL | 鹤霞路111弄30号楼 - 嘉定区 : 433
# | B0FFILEARP | 鹤霞路111弄32号楼 - 嘉定区 : 433
# | B0FFINGJNY | 鹤霞路111弄28号楼 - 嘉定区 : 433
# | B0FFINH75R | 鹤霞路111弄22号楼 - 嘉定区 : 434
# | B0FFILEE86 | 鹤霞路111弄20号楼 - 嘉定区 : 436
# | B0FFILJGUY | 鹤霞路111弄17号楼 - 嘉定区 : 439
# | B0FFILE6KV | 鹤霞路111弄19号楼 - 嘉定区 : 442
# | B0FFILE972 | 鹤霞路111弄21号楼 - 嘉定区 : 443
# | B001571ESK | 上海市嘉定区金鹤幼儿园 - 江桥镇鹤霞路11号(金运路口) : 447
# | B0FFIPRNUY | 澜茵华庭二期3幢 - 金园一路1518弄3幢7-9号 : 447
# -----------------------------------------------
# http://restapi.amap.com/v3/place/around?
# location=121.3184590000,31.2422110000&extensions=all
# &page=4&offset=15&sortrule=distance&types=住宅区|学校|门牌信息&key=
# -----------------------------------------------
# *| B0FFILEFUN | 鹤霞路111弄61号楼 - 嘉定区 : 326
# *| B0FFIKZ8JZ | 鹤霞路111弄63号楼 - 嘉定区 : 339
# *| B0FFINGK4Y | 鹤霞路111弄65号楼 - 嘉定区 : 344
# *| B0FFINH7CW | 鹤霞路111弄62号楼 - 嘉定区 : 346
# *| B0FFINGK55 | 鹤霞路111弄60号楼 - 嘉定区 : 347
# | B0FFILIMWJ | 澜茵华庭15幢 - 金园一路1519弄15幢30号 : 349
# *| B0FFILE6BP | 鹤霞路111弄58号楼 - 嘉定区 : 349
# | B0FFIL1ERR | 澜茵华庭17幢 - 金园一路1519弄17幢48-51号 : 352
# *| B0FFILE9DA | 鹤霞路111弄69号楼 - 嘉定区 : 356
# | B0FFILD15R | 澜茵华庭14幢 - 金园一路1519弄14幢29号 : 357
# | B0FFINNF2Q | 澜茵华庭7幢 - 金园一路1519弄7幢31号 : 372
# *| B0FFINH5HZ | 鹤霞路111弄53号楼 - 嘉定区 : 376
# | B0FFIPEDWI | 澜茵华庭12幢 - 金园一路1519弄12幢36-39号 : 377
# *| B0FFINMT8B | 鹤霞路555弄4幢 - 鹤霞路555弄4幢11-12号 : 379
# *| B0FFINH84F | 鹤霞路111弄48号楼 - 嘉定区 : 381
# -----------------------------------------------
# ['B0FFILEFUN: 2', 'B0FFIKZ8JZ: 2', 'B0FFINGK4Y: 2', 'B0FFINH7CW: 2',
#  'B0FFINGK55: 2', 'B0FFILE6BP: 2', 'B0FFILE9DA: 2', 'B0FFINH5HZ: 2',
#  'B0FFINMT8B: 2', 'B0FFINH84F: 2']
# -----------------------------------------------
from __future__ import absolute_import, unicode_literals

try:
    from urllib import unquote
except ImportError:
    from urllib.request import unquote
from collections import Counter

import requests


def request_to_amap(key, params):
    params.update({'key': key})

    r = requests.get('http://restapi.amap.com/v3/place/around', params=params)
    r.raise_for_status()

    return r


DEMO_PARAMS = {'location': '121.3184590000,31.2422110000',
               'extensions': 'all',
               'page': 1,
               'offset': 15,
               'sortrule': 'distance',
               'types': '住宅区|学校|门牌信息'}


def demo(key):
    DEMO_PARAMS['page'] = 1
    a = request_to_amap(key, DEMO_PARAMS)
    DEMO_PARAMS['page'] = 2
    b = request_to_amap(key, DEMO_PARAMS)
    DEMO_PARAMS['page'] = 3
    c = request_to_amap(key, DEMO_PARAMS)
    DEMO_PARAMS['page'] = 4
    d = request_to_amap(key, DEMO_PARAMS)

    id_list = []

    for data in (a, b, c, d):
        pois = data.json()['pois']

        print('-----------------------------------------------')
        print(unquote(data.url))
        print('-----------------------------------------------')

        for poi in pois:
            if poi['id'] in id_list:
                print('*', end='')

            print(u'| {id} | {name} - {address} : {distance}'.format(
                id=poi['id'], name=poi['name'], address=poi['address'],
                distance=poi['distance'],
            ))

            id_list.append(poi['id'])

    print('-----------------------------------------------')

    cc = Counter(id_list)
    print(["{}: {}".format(i[0], i[1]) for i in cc.most_common() if i[1] > 1])

    print('-----------------------------------------------')


if __name__ == '__main__':
    import sys

    try:
        key = sys.argv[1]
    except IndexError:
        print('ERROR: require amap key')
        print('--- EXIT ---')
        exit(1)
    else:
        demo(key)
