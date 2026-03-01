class Rule:
    def __init__(self, rule_type: str, value: str, policy: str, line_no: int = None):
        self.type = rule_type.upper().strip()
        self.value = value.strip()
        self.policy = policy.strip()
        self.line_no = line_no

    def key(self):
        return (self.type, self.value, self.policy)

    def __repr__(self):
        return f"{self.type},{self.value},{self.policy}"  