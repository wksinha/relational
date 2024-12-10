# Relational
A DSL for using Relational Algebra on top of SurrealDB.

## Motivation
- SurrealDB is a multi-model database.
- It supports both relational and graph queries.
- This support makes it suitable for learning to transition from relational to graph queries.
- This makes it suitable for a learning environment such as academia.
- We design and run a Relational Algebra -> SQL converter on top of SurrealDB.
- The Domain Specific Language for students aims to be the first step in learning DBMS.
- Combined with SurrealDB's multi-model architecture, it builds the right support for learning the transition.

## Technology
- Language: Python
- Modules: Lark
- Database: SurrealDB

## Methodology
- The application runs in a pipelined manner.
- The RA2SQL module takes in relational algebra (examples given) and outputs SQL queries.
    - The RA2SQL module, written in Python, uses Lark to create a parser from a grammar.
    - The grammar for the DSL is described using EBNF.
    - A custom interpreter then traverses the parsed AST to create the desired SQL query.
        - An alternative here could be to use Lark's inbuilt transformer module, but that has separate challenges.
- This output is then passed on to SurrealDB and the output is given to the user.

## Results
- Created a DSL that takes Relational Algebra and converts it into SQL queries.
- These queries are then run on SurrealDB.
- Handles SELECTION, PROJECTION, UNION, DIFFERENCE, CARTESIAN PRODUCT operations alongside NESTED queries.

## Challenges
- Familiarization with SurrealDB syntax. SurrealDB does not follow typical DML syntax. We can see an example in the `init.surql` file.
- Deciding on the right tool (PLY vs Lark vs PyParsing) - testing them and familiarization with Lark finally.
- Lark contains the Transformer module that helps write an Interpreter for a DSL.
    - It was challenging to set up and a custom interpreter was written instead.
- Debugging. Debugging specific issues on the tree was challenging due to feast-or-famine of logging information.
    - Added custom logs for specific operations which helped, but intermediate output was not exactly human readable.
    - Example:
    ```
    start
    [Tree('query', [Tree('selection', [Tree('condition', [Token('STRING', 'year'), Token('STRING', '='), Token('STRING', '2')]), Tree('query', [Tree('selection', [Tree('condition', [Token('STRING', 'sid'), Token('STRING', '>'), Token('STRING', '10')]), Tree(Token('RULE', 'query'), [Tree('relation', [Token('KEY', 'student')])])])])])])]

    query
    [Tree('selection', [Tree('condition', [Token('STRING', 'year'), Token('STRING', '='), Token('STRING', '2')]), Tree('query', [Tree('selection', [Tree('condition', [Token('STRING', 'sid'), Token('STRING', '>'), Token('STRING', '10')]), Tree(Token('RULE', 'query'), [Tree('relation', [Token('KEY', 'student')])])])])])]

    selection
    [Tree('condition', [Token('STRING', 'year'), Token('STRING', '='), Token('STRING', '2')]), Tree('query', [Tree('selection', [Tree('condition', [Token('STRING', 'sid'), Token('STRING', '>'), Token('STRING', '10')]), Tree(Token('RULE', 'query'), [Tree('relation', [Token('KEY', 'student')])])])])]

    query
    [Tree('selection', [Tree('condition', [Token('STRING', 'sid'), Token('STRING', '>'), Token('STRING', '10')]), Tree(Token('RULE', 'query'), [Tree('relation', [Token('KEY', 'student')])])])]

    selection
    [Tree('condition', [Token('STRING', 'sid'), Token('STRING', '>'), Token('STRING', '10')]), Tree(Token('RULE', 'query'), [Tree('relation', [Token('KEY', 'student')])])]

    query
    [Tree('relation', [Token('KEY', 'student')])]

    condition
    [Token('STRING', 'sid'), Token('STRING', '>'), Token('STRING', '10')]

    condition
    [Token('STRING', 'year'), Token('STRING', '='), Token('STRING', '2')]

    SELECT * FROM (SELECT * FROM (student) WHERE sid > 10) WHERE year = 2;
    ```

## References
- https://www.doc.ic.ac.uk/~pjm/teaching/student_projects/gc106_report.pdf
- https://lark-parser.readthedocs.io/en/latest/examples/index.html
- https://blog.erezsh.com/how-to-write-a-dsl-in-python-with-lark/
- https://gist.github.com/PH111P/7c8b529c0293d8c35adc#file-relalgsql-hs
- https://surrealdb.com/docs/surrealdb/introduction