import pandas as pd
from config import Config
# 中文类型 → QX 类型 映射
TYPE_MAP = {
    "域名后缀": "host-suffix",
    "域名": "host",
    "域名关键词": "host-keyword",
    "IP段": "ip-cidr"
}

config = Config()
def generate_qx():
    df = pd.read_excel(config.EXCEL_PATH)

    # 只保留启用的规则
    df = df[df["启用"] == 1]

    lines = []
    lines.append("# =======================")
    lines.append("# Quantumult X Rules")
    lines.append("# Generated Automatically")
    lines.append("# =======================")
    lines.append("")

    for _, row in df.iterrows():

        rule_type_cn = str(row["类型"]).strip()
        content = str(row["内容"]).strip()
        policy = str(row["策略组"]).strip()

        if rule_type_cn not in TYPE_MAP:
            print(f"未知类型跳过: {rule_type_cn}")
            continue

        rule_type = TYPE_MAP[rule_type_cn]

        line = f"{rule_type},{content},{policy}"
        lines.append(line)

    config.QX_OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print("✅ QX 规则生成成功：", config.QX_OUTPUT_FILE)


if __name__ == "__main__":
    generate_qx()