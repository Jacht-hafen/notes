def parse_csv_line(line: str) -> list[str]:
    fields = []
    current_field = ""
    in_quotes = False
    i = 0
    while i < len(line):
        char = line[i]

        if in_quotes:
            if char == '"':
                # Check for escaped quote ""
                if i + 1 < len(line) and line[i+1] == '"':
                    current_field += '"'
                    i += 1  # Skip the second quote of the pair
                else:
                    in_quotes = False
            else:
                current_field += char
        else:
            if char == '"':
                in_quotes = True
            elif char == ',':
                fields.append(current_field)
                current_field = ""
            else:
                current_field += char
        i += 1

    fields.append(current_field)
    return fields


assert parse_csv_line("a,b,c") == ["a", "b", "c"]
assert parse_csv_line('a,"b,c",d') == ["a", "b,c", "d"]
assert parse_csv_line('"a ""b"" c",d') == ['a "b" c', 'd']
assert parse_csv_line('"""",""""') == ['"', '"']
assert parse_csv_line(' a , b ') == [' a ', ' b ']
assert parse_csv_line('a,,b') == ['a', '', 'b']
