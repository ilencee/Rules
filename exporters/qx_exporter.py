'''
Author: ilencee 862491025@qq.com
Date: 2026-02-28 23:42:26
LastEditors: ilencee 862491025@qq.com
LastEditTime: 2026-03-01 00:12:32
FilePath: \Proxy-Rules\exporters\qx_exporter.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from .base_exporter import BaseExporter

QX_TYPE_MAP = {
    "DOMAIN": "host",
    "DOMAIN-SUFFIX": "host-suffix",
    "DOMAIN-KEYWORD": "host-keyword",
    "IP-CIDR": "ip-cidr",
    "IP-CIDR6": "ip6-cidr",
    "GEOIP": "geoip",
    "DST-PORT": "dst-port",
}


class QXExporter(BaseExporter):

    name = "qx"

    def export_rule(self, rule):
        qx_type = QX_TYPE_MAP.get(rule.type)

        if not qx_type:
            raise ValueError(f"QX 不支持类型 {rule.type}")

        return f"{qx_type}, {rule.value}, {rule.policy}"