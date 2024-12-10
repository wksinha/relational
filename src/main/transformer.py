# class RAtoSQLTransformer(Transformer):
#     @v_args(inline=True)
#     def start(self, *args):
#         if "start" in dbg:
#             print("DEBUG START start")
#             print(*args, sep='\n')
#             print("DEBUG END start")
#         return f"SELECT {args[0]}"

#     @v_args(inline=True)
#     def query(self, *args):
#         if "query" in dbg:
#             print("DEBUG START query")
#             print(*args, sep='\n')
#             print("DEBUG END query")
#         return f"SELECT {args[0]}"

#     @v_args(inline=True)
#     def relation(self, *args):
#         if "relation" in dbg:
#             print("DEBUG START relation")
#             print(*args, sep='\n')
#             print("DEBUG END relation")
#         return f"SELECT {args[0]}"

#     @v_args(inline=True)
#     def selection(self, *args):
#         if "selection" in dbg:
#             print("DEBUG START selection")
#             print(*args, sep='\n')
#             print("DEBUG END selection")
#         return f"SELECT {args[0]}"

#     @v_args(inline=True)
#     def condition(self, *args):
#         if "condition" in dbg:
#             print("DEBUG START condition")
#             print(*args, sep='\n')
#             print("DEBUG END condition")
#         return f"SELECT {args[0]}"


# parser = Lark(ra_grammar, start='start', parser='lalr', transformer=RAtoSQLTransformer())
