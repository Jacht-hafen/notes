def parse_csv_line(line: str) -> list[str]:
fields = []
current = []
in_quotes = False
i = 0

while i < len(line):
    ch = line[i]

    if in_quotes:
        if ch == '"':
            if i + 1 < len(line) and line[i + 1] == '"':
                current.append('"')
                i += 2
                continue
            in_quotes = False
        else:
            current.append(ch)
    else:
        if ch == '"' and not current:
            in_quotes = True
        elif ch == ',':
            fields.append(''.join(current))
            current = []
        else:
            current.append(ch)

    i += 1

fields.append(''.join(current))
return fields
assert parse_csv_line("a,b,c") == ["a", "b", "c"]
assert parse_csv_line('"a,b",c') == ["a,b", "c"]
assert parse_csv_line('a,,b') == ["a", "", "b"]
assert parse_csv_line(' a , b ') == [" a ", " b "]
assert parse_csv_line('"a""b"') == ["a"b"]
assert parse_csv_line('x,"he said ""hello"""') == ['x', 'he said "hello"']
