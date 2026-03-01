'''
Author: ilencee 862491025@qq.com
Date: 2026-03-01 13:58:41
LastEditors: ilencee 862491025@qq.com
LastEditTime: 2026-03-01 14:00:51
FilePath: \Proxy-Rules\core\service.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
import pandas as pd
from rule_model import Rule
from rule_validator import RuleValidator
from rule_normalizer import RuleNormalizer
from rule_adapter import RuleAdapter


class RuleService:

    def __init__(self):
        self.validator = RuleValidator()
        self.normalizer = RuleNormalizer()

    def load_from_excel(self, path):
        df = pd.read_excel(path)

        rules = []
        for idx, row in df.iterrows():
            rules.append(
                Rule(
                    rule_type=str(row["type"]),
                    value=str(row["value"]),
                    policy=str(row["policy"]),
                    line_no=idx + 2
                )
            )

        return rules

    def process(self, path, platform):
        rules = self.load_from_excel(path)

        errors = self.validator.validate(rules)
        if errors:
            return None, errors

        rules = self.normalizer.normalize(rules)

        if platform == "clash":
            output = RuleAdapter.to_clash(rules)
        elif platform == "qx":
            output = RuleAdapter.to_qx(rules)
        elif platform == "shadowrocket":
            output = RuleAdapter.to_shadowrocket(rules)
        else:
            return None, ["不支持的平台"]

        return output, []