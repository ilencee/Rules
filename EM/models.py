class Rule:
    def __init__(self, rule_type, value, policy, line_no=None):
        self.type = rule_type.strip().upper()
        self.value = value.strip()
        self.policy = policy.strip()
        self.line_no = line_no

    def key(self):
        return (self.type, self.value, self.policy)