# coding: utf-8
# ------------------------------------
# 问题描述:
#
# 多个category之间相互存在影响, 比如: 只使用`楼栋号`作为category可以召回所有楼栋号
# POI, 而使用`住宅|楼栋号`作为category的情况下, 部分楼栋号POI无法被正常召回; 使用
# `楼栋号|学校`等作为category没有触发该BUG;
#
#
# EXAMPLE:
#
# http://restapi.amap.com/v3/place/around?
# location=121.3184590000,31.2422110000
# &extensions=all&page=1&offset=6&types=楼栋号&key=
# -----------------------------------------------
# | B0FFIKYNM0 | 金园一路1359弄10幢 - 金园一路1359弄10幢28-30号 : 37
# | B0FFILCXF1 | 金园一路1359弄14幢 - 金园一路1359弄14幢40-41号 : 55
# | B0FFILD0JH | 金园一路1359弄11幢 - 金园一路1359弄11幢31-33号 : 58
# | B0FFILD07T | 金园一路1359弄6幢 - 金园一路1359弄6幢16-18号 : 59
# | B0FFILFIMV | 金园一路1359弄15幢 - 金园一路1359弄15幢42-43号 : 59
# | B0FFIKGAG1 | 金园一路1359弄19幢 - 金园一路1359弄19幢51-53号 : 68
# -----------------------------------------------
# http://restapi.amap.com/v3/place/around?
# location=121.3184590000,31.2422110000
# &extensions=all&page=1&offset=6&types=楼栋号|住宅区&key=
# -----------------------------------------------
# | B00155QXUG | 金沙缘圆宝邸 - 金园一路1359弄1-69号 : 0
# | B0FFGLR7LQ | 缘圆宝坻小区 - 金园一路1359弄1-69号 : 115
# | B0FFH10FP3 | 金园社区 - 金园一路 : 174
# | B0FFG94W6Z | 金鹤新城 - 金园一路与金沙江西路交叉口北100米 : 235
# | B0FFINH7HJ | 鹤霞路111弄76号楼 - 嘉定区 : 277
# | B0FFILELLH | 鹤霞路111弄74号楼 - 嘉定区 : 278
# -----------------------------------------------
# http://restapi.amap.com/v3/place/around?
# location=121.3184590000,31.2422110000
# &extensions=all&page=1&offset=6&types=190403|120300&key=
# -----------------------------------------------
# | B00155QXUG | 金沙缘圆宝邸 - 金园一路1359弄1-69号 : 0
# | B0FFGLR7LQ | 缘圆宝坻小区 - 金园一路1359弄1-69号 : 115
# | B0FFH10FP3 | 金园社区 - 金园一路 : 174
# | B0FFG94W6Z | 金鹤新城 - 金园一路与金沙江西路交叉口北100米 : 235
# | B0FFINH7HJ | 鹤霞路111弄76号楼 - 嘉定区 : 277
# | B0FFILELLH | 鹤霞路111弄74号楼 - 嘉定区 : 278
# -----------------------------------------------
from __future__ import absolute_import

try:
    from urllib import unquote
except ImportError:
    from urllib.request import unquote
import copy

import requests


def request_to_amap(key, params):
    params.update({'key': key})

    r = requests.get('http://restapi.amap.com/v3/place/around', params=params)
    r.raise_for_status()

    return r


_DEMO_PARAMS = {'location': '121.3184590000,31.2422110000',
                'extensions': 'all',
                'page': 1,
                'offset': 6}

DEMO_DEFAULT_PARAMS = copy.deepcopy(_DEMO_PARAMS)
DEMO_DEFAULT_PARAMS.update({'types': u'楼栋号'})

DEMO_ERROR_PARAMS = copy.deepcopy(_DEMO_PARAMS)
DEMO_ERROR_PARAMS.update({'types': u'楼栋号|住宅区'})

DEMO_ERROR_2_PARAMS = copy.deepcopy(_DEMO_PARAMS)
DEMO_ERROR_2_PARAMS.update({'types': u'190403|120300'})


def demo(key):
    a = request_to_amap(key, DEMO_DEFAULT_PARAMS)
    b = request_to_amap(key, DEMO_ERROR_PARAMS)
    c = request_to_amap(key, DEMO_ERROR_2_PARAMS)

    for data in (a, b, c):
        pois = data.json()['pois']

        print('-----------------------------------------------')
        print(unquote(data.url))
        print('-----------------------------------------------')

        for poi in pois:
            print(u'| {id} | {name} - {address} : {distance}'.format(
                id=poi['id'], name=poi['name'], address=poi['address'],
                distance=poi['distance'],
            ))

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


