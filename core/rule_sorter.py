def sort_rules(rules):
    return sorted(rules, key=lambda r: r.priority, reverse=True)