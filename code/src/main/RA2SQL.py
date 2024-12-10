import sys
from lark import Lark, Transformer, v_args

LARK_TREE = "<class 'lark.tree.Tree'>"
LARK_TOKEN = "<class 'lark.lexer.Token'>"
START = "start"
QUERY = "query"
RELATION = "relation"
SELECTION = "selection"
PROJECTION = "projection"
ATTRIBUTES = "attributes"
UNION = "union"
DIFFERENCE = "difference"
PRODUCT = "product" # Cartesian Product
CONDITION = "condition"
WILDCARD = "*"

dbg = []
# dbg.append(START)
# dbg.append(QUERY)
# dbg.append(SELECTION)
# dbg.append(CONDITION)
# dbg.append(PROJECTION)
# dbg.append(UNION)
# dbg.append(DIFFERENCE)
# dbg.append(PRODUCT)

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
    query: relation | selection | projection | union | difference | product-> query
    relation: KEY -> relation
    selection: "SELECTION" "(" condition ")" "(" query ")" -> selection
    projection: "PROJECTION" "(" attributes ")" "(" query ")" -> projection
    union: "UNION" "(" query ")" "(" query")" -> union
    difference: "DIFFERENCE" "(" query ")" "(" query")" -> difference
    product: "PRODUCT" "(" query ")" "(" query ")" -> product
    condition: WILDCARD | STRING [ (STRING)*] -> condition
    attributes: STRING [("," STRING)*] -> attributes
    WILDCARD: "*"
    KEY: /[a-zA-Z0-9]+/
    STRING: /[a-zA-Z0-9>=<]+/
    %import common.WS
    %ignore WS
"""


def parse_ra_to_sql(ra_expr):
    '''
    Uses Lark to parse the Relational Algebra Expression
    Args:
        ra_expr (string): Relational Algebra Expression
    Returns:
        AST (lark Tree): Lark parsed AST
    '''
    parser = Lark(ra_grammar, start=START)
    return parser.parse(ra_expr)

def resolve_tree(node):
    '''
    Traverses and Interprets the Lark AST, conditionally processing different types of nodes.
    Args:
        node (lark Tree/Token): AST Parsed by Lark. (Subtree)
    Returns:
        SQL expression (string) for the subtree.
    '''
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
        elif node.data == CONDITION:
            if CONDITION in dbg:
                print(node.data)
                print(node.children)
                print()

            conditions = [resolve_tree(child) for child in node.children]
            expression = " ".join(conditions)
        elif node.data == PROJECTION:
            if PROJECTION in dbg:
                print(node.data)
                print(node.children)
                print()

            attributes = resolve_tree(node.children[0])
            table = resolve_tree(node.children[1])
            expression = f"SELECT {attributes} FROM {table}"
        elif node.data == ATTRIBUTES:
            if ATTRIBUTES in dbg:
                print(node.data)
                print(node.children)
                print()

            attributes = [resolve_tree(child) for child in node.children]
            expression = ", ".join(attributes)
        elif node.data == UNION:
            if UNION in dbg:
                print(node.data)
                print(node.children)
                print()

            left = resolve_tree(node.children[0])
            right = resolve_tree(node.children[1])
            expression = f"{left} UNION {right}"
        elif node.data == DIFFERENCE:
            if DIFFERENCE in dbg:
                print(node.data)
                print(node.children)
                print()
            
            left = resolve_tree(node.children[0])
            right = resolve_tree(node.children[1])
            expression = f"{left} EXCEPT {right}"
        elif node.data == PRODUCT:
            if PRODUCT in dbg:
                print(node.data)
                print(node.children)
                print()

            left = resolve_tree(node.children[0])
            right = resolve_tree(node.children[1])
            expression = f"{left} CROSS JOIN {right}"
        else:
            raise SyntaxError('Invalid expression: %s' % node.data)
        
    elif nodetype == LARK_TOKEN:
        expression = node
    else:
        raise SyntaxError('Invalid expression: %s' % node)
    return expression

def cleanup(sqlquery):
    '''
    Removes redundant "(" ")" from the sql query.
    Arguments:
        sqlquery (string): The query to be cleaned.
    Returns:
        sqlquery (string): The cleaned query
    '''
    sqlquery = sqlquery[1:-2] + sqlquery[-1:]
    return sqlquery


def main():
    try:
        expr = input()
    except IOError as e:
        print(e, file=sys.stderr)
        return

    try:
        sqlquery = resolve_tree(parse_ra_to_sql(expr))
        sqlquery = cleanup(sqlquery)
    except Exception as e:
        print("Failed to parse input for expression:", expr, ", error: ", e, file=sys.stderr)
        return

    print(sqlquery)

if __name__=="__main__":
    main()