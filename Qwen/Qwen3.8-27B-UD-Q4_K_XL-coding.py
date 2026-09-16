def parse_csv_line(line: str) -> list[str]:
fields = []
field = []
in_quotes = False
i = 0
n = len(line)

while i < n:
    ch = line[i]

    if in_quotes:
        if ch == '"':
            if i + 1 < n and line[i + 1] == '"':
                field.append('"')
                i += 2
                continue
            in_quotes = False
        else:
            field.append(ch)
    else:
        if ch == '"':
            in_quotes = True
        elif ch == ',':
            fields.append(''.join(field))
            field = []
        else:
            field.append(ch)

    i += 1

fields.append(''.join(field))
return fields
assert parse_csv_line("a,b,c") == ["a", "b", "c"]
assert parse_csv_line('"hello, world",plain') == ["hello, world", "plain"]
assert parse_csv_line(",a,,b") == ["", "a", "", "b"]
assert parse_csv_line("  a , b ") == ["  a ", " b "]
assert parse_csv_line('"a"",b') == ['a"', 'b']
assert parse_csv_line('"a""b"') == ['a"b']
