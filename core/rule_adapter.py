'''
Author: ilencee 862491025@qq.com
Date: 2026-03-01 13:58:19
LastEditors: ilencee 862491025@qq.com
LastEditTime: 2026-03-01 13:58:25
FilePath: \Proxy-Rules\11.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
class RuleAdapter:

    @staticmethod
    def to_clash(rules):
        return [
            f"- {r.type},{r.value},{r.policy}"
            for r in rules
        ]

    @staticmethod
    def to_qx(rules):
        return [
            f"{r.type.lower()}, {r.value}, {r.policy.lower()}"
            for r in rules
        ]

    @staticmethod
    def to_shadowrocket(rules):
        return [
            f"{r.type},{r.value},{r.policy}"
            for r in rules
        ]