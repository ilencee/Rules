'''
Author: ilencee 862491025@qq.com
Date: 2026-02-28 23:42:05
LastEditors: ilencee 862491025@qq.com
LastEditTime: 2026-03-01 13:56:54
FilePath: \Proxy-Rules\core\rule_validator.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
import ipaddress
import re

ALLOWED_TYPES = {
    "DOMAIN",
    "DOMAIN-SUFFIX",
    "DOMAIN-KEYWORD",
    "IP-CIDR",
    "GEOIP",
    "MATCH"
}

DOMAIN_PATTERN = re.compile(r"^[a-zA-Z0-9.-]+$")


class RuleValidator:

    def validate(self, rules):
        errors = []
        seen = {}

        for rule in rules:

            # 类型校验
            if rule.type not in ALLOWED_TYPES:
                errors.append(f"[Line {rule.line_no}] 非法类型: {rule.type}")

            # 空值校验
            if not rule.value:
                errors.append(f"[Line {rule.line_no}] value 为空")

            # IP 校验
            if rule.type == "IP-CIDR":
                try:
                    ipaddress.ip_network(rule.value)
                except Exception:
                    errors.append(f"[Line {rule.line_no}] 非法 IP-CIDR: {rule.value}")

            # 域名校验
            if rule.type in {"DOMAIN", "DOMAIN-SUFFIX"}:
                if not DOMAIN_PATTERN.match(rule.value):
                    errors.append(f"[Line {rule.line_no}] 非法域名: {rule.value}")

            # 重复检测
            key = rule.key()
            if key in seen:
                errors.append(
                    f"[Line {rule.line_no}] 与 Line {seen[key]} 重复: {rule}"
                )
            else:
                seen[key] = rule.line_no

        return errors