def export_qx(rules):
    lines = []

    for r in rules:
        lines.append(
            f"{r.type.lower()}, {r.value}, {r.policy.lower()}"
        )

    return lines