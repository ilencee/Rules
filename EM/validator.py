'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2026-03-01 14:40:00
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2026-03-01 14:42:11
FilePath: \EM\validator.py
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


def validate_rules(rules):
    errors = []
    seen = {}

    for rule in rules:

        if rule.type not in ALLOWED_TYPES:
            errors.append(f"[Line {rule.line_no}] 非法类型: {rule.type}")

        if not rule.value:
            errors.append(f"[Line {rule.line_no}] value 为空")

        if rule.type == "IP-CIDR":
            try:
                ipaddress.ip_network(rule.value)
            except Exception:
                errors.append(f"[Line {rule.line_no}] 非法 IP-CIDR: {rule.value}")

        if rule.type in {"DOMAIN", "DOMAIN-SUFFIX"}:
            if not DOMAIN_PATTERN.match(rule.value):
                errors.append(f"[Line {rule.line_no}] 非法域名: {rule.value}")

        key = rule.key()
        if key in seen:
            errors.append(
                f"[Line {rule.line_no}] 与 Line {seen[key]} 重复: {rule.type},{rule.value},{rule.policy}"
            )
        else:
            seen[key] = rule.line_no

    return errors