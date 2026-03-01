class RuleNormalizer:

    def normalize(self, rules):
        normalized = []

        for rule in rules:
            rule.type = rule.type.upper()
            rule.value = rule.value.strip()
            rule.policy = rule.policy.strip()
            normalized.append(rule)

        return normalized