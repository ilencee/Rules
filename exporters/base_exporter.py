class BaseExporter:

    name = "base"

    def export_rule(self, rule):
        raise NotImplementedError

    def export(self, rules):
        lines = []
        for rule in rules:
            lines.append(self.export_rule(rule))
        return "\n".join(lines)