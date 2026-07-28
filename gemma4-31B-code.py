def parse_csv_line(line: str) -> list[str]:
    fields = []
    current_field = []
    in_quotes = False
    i = 0
    while i < len(line):
        char = line[i]
        if in_quotes:
            if char == '"':
                # Check for escaped double quote ""
                if i + 1 < len(line) and line[i+1] == '"':
                    current_field.append('"')
                    i += 1  # Skip the second quote
                else:
                    in_quotes = False
            else:
                current_field.append(char)
        else:
            if char == '"':
                in_quotes = True
            elif char == ',':
                fields.append("".join(current_field))
                current_field = []
            else:
                current_field.append(char)
        i += 1
    
    fields.append("".join(current_field))
    return fields

assert parse_csv_line('a,b,c') == ['a', 'b', 'c']
assert parse_csv_line('"a,b",c') == ['a,b', 'c']
assert parse_csv_line(',,') == ['', '', '']
assert parse_csv_line('  foo  ," bar "  ') == ['  foo  ', ' bar   ']
assert parse_csv_line('"a""b",c') == ['a"b', 'c']
assert parse_csv_line('"He said ""Hello""", "Hi"') == ['He said "Hello"', ' Hi']
