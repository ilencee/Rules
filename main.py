from config import EXCEL_PATH, OUTPUT_DIR
from core.service import RuleService


def main():
    service = RuleService()

    platform = "clash"   # 修改这里测试不同平台

    output, errors = service.process(EXCEL_PATH, platform)

    if errors:
        print("发现错误:")
        for e in errors:
            print(e)
        return

    OUTPUT_DIR.mkdir(exist_ok=True)
    output_path = OUTPUT_DIR / f"{platform}_rules.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output))

    print(f"生成完成: {output_path}")


if __name__ == "__main__":
    main()