'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2026-03-01 14:39:59
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2026-03-01 15:10:02
FilePath: \EM\config.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
'''
自动去重

自动排序（按优先级）

自动分组输出（按一级标签分块）

自动加注释

输出 Clash / Surge 多平台

检查规则合法性

'''
from pathlib import Path
class Config:
    """
    项目全局路径配置类
    """

    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent

        # Excel 数据源
        self.EXCEL_PATH = self.BASE_DIR / "rules.xlsx"

        # 输出目录
        self.OUTPUT_DIR = self.BASE_DIR / "Output_Rules"

        # 自动创建输出目录（不存在就创建）
        self.OUTPUT_DIR.mkdir(exist_ok=True)

        # 输出文件
        self.QX_OUTPUT_FILE = self.OUTPUT_DIR / "QX_Rules.conf"
        self.Clash_OUTPUT_FILE = self.OUTPUT_DIR / "Clash_Rules.conf"