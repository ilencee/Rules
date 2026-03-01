'''
Author: ilencee 862491025@qq.com
Date: 2026-02-28 22:56:11
LastEditors: ilencee 862491025@qq.com
LastEditTime: 2026-02-28 23:49:19
FilePath: \Proxy-Rules\scripts\rule_loader.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
'''
Author: ilencee 862491025@qq.com
Date: 2026-02-28 22:56:11
LastEditors: ilencee 862491025@qq.com
LastEditTime: 2026-02-28 23:22:33
FilePath: \Proxy-Rules\scripts\rule_loader.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
'''
import pandas as pd
from pathlib import Path
VALID_TYPES = {
    "精确域名",
    "域名后缀",
    "域名关键字",
    "IPv4段",
    "IPv6段",
    "国家IP",
    "进程名",
    "端口",
    "最终匹配"
}
def validate_rules(rules):
    """
    校验规则：
    1. type不能为空
    2. value不能为空
    3. 重复规则检测
    """

    seen = {}
    errors = []

    for rule in rules:
        row_id = rule["id"]

        # ========================
        # 1️⃣ type 不能为空
        # ========================
        if not rule["type"] or rule["type"] == "None":
            errors.append(f"第 {row_id} 行错误：type 不能为空")

        # ========================
        # 2️⃣ value 不能为空
        # ========================
        if not rule["value"]:
            errors.append(f"第 {row_id} 行错误：value 不能为空")

        # ========================
        # 3️⃣ 重复规则检测
        # ========================
        key = (rule["type"], rule["value"])

        if key in seen:
            first_row = seen[key]
            errors.append(
                f"重复规则：第 {first_row} 行 与 第 {row_id} 行 type={rule['type']} value={rule['value']}"
            )
        else:
            seen[key] = row_id

    return errors

# Excel路径
BASE_DIR = Path(__file__).resolve().parent.parent
EXCEL_PATH = BASE_DIR / "data" / "rules.xlsx"


def load_rules():
    """
    读取Excel规则数据库
    返回：统一结构的规则列表（list of dict）
    """

    # 读取Excel
    df = pd.read_excel(EXCEL_PATH)

    # 去除列名空格
    df.columns = df.columns.str.strip()

    # 只保留启用规则
    df = df[df["启用"] == 1]

    # 如果有优先级列，按优先级排序
    if "优先级" in df.columns:
        df = df.sort_values(by="优先级", ascending=True)

    rules = []

    for _, row in df.iterrows():
        rule = {
            "id": row.get("ID"),
            "type": str(row.get("类型")).strip(),
            "value": str(row.get("内容")).strip(),
            "policy": str(row.get("策略组")).strip(),
            "port": row.get("端口"),
            "tag1": row.get("一级标签"),
            "tag2": row.get("二级标签"),
            "priority": row.get("优先级"),
            "note": row.get("备注"),
        }

        rules.append(rule)

    return rules

if __name__ == "__main__":
    rules = load_rules()

    print(f"共读取 {len(rules)} 条启用规则\n")

    errors = validate_rules(rules)
    for r in rules:
        print(r)

    if errors:
        print("发现以下问题：")
        for e in errors:
            print(" -", e)
    else:
        print("规则校验通过")
'''
import pandas as pd
from .rule_model import Rule
from .rule_normalizer import normalize_type, clean


def load_rules_from_excel(path):
    df = pd.read_excel(path)

    rules = []

    for index, row in df.iterrows():
        row_id = index + 1

        rule = Rule(
            id=row_id,
            type=normalize_type(row.get("类型"), row_id),
            value=clean(row.get("内容")),
            policy=clean(row.get("策略组")),
            port=row.get("端口"),
            priority=row.get("优先级") or 0,
            note=clean(row.get("备注")),
        )

        rules.append(rule)

    return rules