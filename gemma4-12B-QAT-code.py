def parse_csv_line(line: str) -> list[str]:
    fields = []
    current_field = []
    in_quotes = False
    i = 0
    while i < len(line):
        char = line[i]
        if char == '"':
            # Check for escaped double quote: "" inside a quoted field
            if in_quotes and i + 1 < len(line) and line[i+1] == '"':
                current_field.append('"')
                i += 2
                continue
            else:
                # Toggle the quoting state
                in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            fields.append("".join(current_field))
            current_field = []
        else:
            current_field.append(char)
        i += 1
    
    # Append the final field remaining after the loop
    fields.append("".join(current_field))
    return fields

assert parse_csv_line('a,b,c') == ['a', 'b', 'c']
assert parse_csv_line('"City, State",Country') == ['City, State', 'Country']
assert parse_csv_line('val1,,val3') == ['val1', '', 'val3']
assert parse_csv_line('  space , "quoted space" ') == ['  space ', 'quoted space ']
assert parse_csv_line('"He said ""Hello!"""') == ['He said "Hello!"']
assert parse_csv_line('"" , "A ""quote"" B"') == ['', 'A "quote" B']
