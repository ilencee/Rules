def normalize_rules(rules):
    for rule in rules:
        rule.type = rule.type.upper()
        rule.value = rule.value.strip()
        rule.policy = rule.policy.upper()
    return rules

