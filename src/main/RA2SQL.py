from lark import Lark, Transformer, v_args

LARK_TREE = "<class 'lark.tree.Tree'>"
LARK_TOKEN = "<class 'lark.lexer.Token'>"
START = "start"
QUERY = "query"
RELATION = "relation"
SELECTION = "selection"
CONDITION = "condition"
WILDCARD = "*"

dbg = []
dbg.append(START)
dbg.append(QUERY)
dbg.append(SELECTION)
dbg.append(CONDITION)

'''
Relational Algebra to SQL Converter

Supported Operations:
1. selection (σ)
2. projection (π)
3. union (∪)
4. difference (−)
5. cartesian product (×)
'''

ra_grammar = """
start: query -> start
query: relation | selection -> query
relation: KEY -> relation
selection: "SELECTION" "(" condition ")" "(" query ")" -> selection
condition: WILDCARD | STRING [ (STRING)*] -> condition
WILDCARD: "*"
KEY: /[a-zA-Z0-9]+/
STRING: /[a-zA-Z0-9>=<]+/
%import common.WS
%ignore WS

"""


parser = Lark(ra_grammar, start=START)

def parse_ra_to_sql(ra_expr):
    return parser.parse(ra_expr)

def resolve_tree(node):
    expression = ""
    nodetype = str(type(node))
    if nodetype == LARK_TREE:
        if node.data == START:
            if START in dbg:
                print(node.data)
                print(node.children)
                print()
            expression = resolve_tree(node.children[0])
            return expression + ";"
        elif node.data == QUERY:
            if QUERY in dbg:
                print(node.data)
                print(node.children)
                print()
            expression = "(" + resolve_tree(node.children[0]) + ")"
        elif node.data == RELATION:
            if RELATION in dbg:
                print(node.data)
                print(node.children)
                print()
            expression = resolve_tree(node.children[0])
        elif node.data == SELECTION:
            if SELECTION in dbg:
                print(node.data)
                print(node.children)
                print()
            table = resolve_tree(node.children[1])
            expression = f"SELECT {WILDCARD} FROM {table}"
            conditions = resolve_tree(node.children[0])
            if conditions != WILDCARD:
                expression += f" WHERE {conditions}"
            
        elif node.data == "condition":
            if CONDITION in dbg:
                print(node.data)
                print(node.children)
                print()
            conditions = [resolve_tree(child) for child in node.children]
            return " ".join(conditions)
        else:
            raise SyntaxError('Invalid expression: %s' % node.data)
        
    elif nodetype == LARK_TOKEN:
        expression = node
    else:
        raise SyntaxError('Invalid expression: %s' % node)
    return expression

def cleanup(sqlquery):
    sqlquery = sqlquery[1:-2] + sqlquery[-1:]
    return sqlquery


expr = input()
sqlquery = resolve_tree(parse_ra_to_sql(expr))
sqlquery = cleanup(sqlquery)
print(sqlquery)