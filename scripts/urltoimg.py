#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://shilingdao.beijing.gov.cn/library/191/10/738495/234111/108201_.jpg
# http://shilingdao.beijing.gov.cn/library/191/10/738495/234111/index.html
# 
# http://zhengwu.beijing.gov.cn/sy/yw/W020170602571030884347.png
# http://zhengwu.beijing.gov.cn/sy/yw/t1481885.htm

url = "http://shilingdao.beijing.gov.cn/library/191/10/738495/234111/index.html"
img_name = "108201_.jpg"

url_tuple = url.rpartition("/")

img_url = url_tuple[0] + url_tuple[1] + img_name

print(img_url)