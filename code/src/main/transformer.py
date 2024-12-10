"""
An attempt at writing an interpreter using the Lark Transformer
"""
# from lark import Lark, Transformer, v_args

# ra_grammar = """
#     start: select
#          | project
#          | rename
#          | union
#          | difference
#          | cartesian
#          | join

#     select: "SELECT" "(" expression ")"
#     project: "PROJECT" "(" expression ")"
#     rename: "RENAME" ID "(" expression ")"
#     union: expression "UNION" expression
#     difference: expression "DIFFERENCE" expression
#     cartesian: expression "CARTESIAN" expression
#     join: expression "JOIN" "(" expression ")" "ON" expression EQUALS expression

#     expression: ID
#               | expression DOT ID  -> dot_expression

#     ID: /[a-zA-Z_][a-zA-Z0-9_]*/
#     DOT: "."
#     EQUALS: "="
#     %ignore " "
# """

# class RAtoSQLTransformer(Transformer):
#     @v_args(inline=True)
#     def select(self, *args):
#         return f"SELECT {args[0]}"

#     @v_args(inline=True)
#     def project(self, *args):
#         return f"SELECT {args[0]}"

#     @v_args(inline=True)
#     def rename(self, *args):
#         return f"SELECT {args[1]} AS {args[0]}"

#     @v_args(inline=True)
#     def union(self, *args):
#         return f"({args[0]}) UNION ({args[1]})"

#     @v_args(inline=True)
#     def difference(self, *args):
#         return f"({args[0]}) EXCEPT ({args[1]})"

#     @v_args(inline=True)
#     def cartesian(self, *args):
#         return f"({args[0]}) CROSS JOIN ({args[1]})"

#     @v_args(inline=True)
#     def join(self, *args):
#         return f"({args[0]}) JOIN ({args[1]}) ON {args[2]} = {args[3]}"

#     @v_args(inline=True)
#     def dot_expression(self, *args):
#         return f"{args[0]}.{args[1]}"

#     @v_args(inline=True)
#     def id(self, *args):
#         return args[0]

# parser = Lark(ra_grammar, start='start', parser='lalr', transformer=RAtoSQLTransformer())

# def parse_ra_to_sql(ra_expr):
#     return parser.parse(ra_expr)

# expr1 = "SELECT (Employee)"
# print(parse_ra_to_sql(expr1))

# expr2 = "PROJECT (Employee)"
# print(parse_ra_to_sql(expr2))

# expr3 = "RENAME EmpName (Employee)"
# print(parse_ra_to_sql(expr3))

# expr4 = "Employee UNION Manager"
# print(parse_ra_to_sql(expr4))

# expr5 = "Employee DIFFERENCE Manager"
# print(parse_ra_to_sql(expr5))

# expr6 = "Employee CARTESIAN Department"
# print(parse_ra_to_sql(expr6))

# expr7 = "Employee JOIN (Department) ON Employee.dept_id = Department.id"
# print(parse_ra_to_sql(expr7))
