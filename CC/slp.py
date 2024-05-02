def generate_s_t(assembly_code):
    loc_counter = 0
    symbol_table = {}
    literal_tables = []
    current_literal_table = []
    queue = []

    for line in assembly_code:
        tokens = line.strip().split()

        if tokens[1] == 'START':
            loc_counter = int(tokens[2])
        elif tokens[0] != '*':
            symbol_table[tokens[0]] = loc_counter
            loc_counter += 1
            if tokens[3][0] == '=':
                queue.append(tokens[3])
                
        elif tokens[1] == 'END':
            while queue :
                literal = queue.pop(0)
                loc_counter += 1
                current_literal_table.append((literal,loc_counter))
            literal_tables.append(current_literal_table)
            break
        elif tokens[1] == 'LTORG':
            for literal in queue:
                current_literal_table.append((literal,loc_counter))
                loc_counter += 1
            literal_tables.append(current_literal_table)
            current_literal_table = []
            queue = []
        else :
            if tokens[3][0] == '*':
                queue.append(tokens[3])
                loc_counter += 1
            else :
                loc_counter += 1
    return symbol_table, literal_tables

def create_pool_table(literal_tables):
    pool_table = []
    index = 0
    for i, literal_table in enumerate(literal_tables):
        pool_table.append("#" + str(index + 1))
        index += len(literal_tables)
    return pool_table

assembly_code = [
     "*  START 180 *",
    "*  READ M *",
    "*  READ N *",
    "LOOP MOVER AREG, M",
    "*  MOVER BREG, N",
    "*  COMP BREG, ='200'",
    "*  BC GT, LOOP",
    "BACK SUB AREG, M",
    "*  COMP AREG, ='500'",
    "*  BC LT, BACK",
    "*  STOP * *",
    "M DS 1 *",
    "N DS 1 *",
    "*  END * *"
]

symbol_table, literal_tables = generate_s_t(assembly_code)
print("Symbol Table: ")
print(symbol_table)
print("\nLiteral Table: ")
for i,literal_table in enumerate(literal_tables):
    print(f"Literal Table { i+1 }: ")
    for literal in literal_table:
        print(literal)
        
pool_table = create_pool_table(literal_tables)
print("\nPool Table: ")
for i in pool_table:
    print(i)