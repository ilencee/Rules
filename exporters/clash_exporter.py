from .base_exporter import BaseExporter


class ClashExporter(BaseExporter):

    name = "clash"

    def export_rule(self, rule):
        return f"{rule.type},{rule.value},{rule.policy}"