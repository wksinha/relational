# Relational
A DSL for using Relational Algebra on top of SurrealDB.

## Technology
- Language: Python
- Modules: Lark
    - Run the following in the `relational` directory:
    ```
    pip install -r requirements.txt
    ```
- Database: SurrealDB
    - Run the following to populate the DB data from the `relational/code/src/main` directory:
    ```
    bash init.sh
    ```
- Testing: Bash

## Testing
- Used bash scripts to run the application against custom testcases for the DSL.
    - Generated output was compared against expected output.
    - Examples:  
    
    RA:
    ```
    SELECTION (*) (student)
    SELECTION (year = 2) (SELECTION  (sid > 10) (student))
    PROJECTION (year, sid) (student)
    PROJECTION (year) (SELECTION (year=1) (student))
    UNION ( SELECTION (year=1) (student) ) ( SELECTION (year=2) (student) )
    DIFFERENCE (PROJECTION (sid) (SELECTION (*) (enrollment))) (PROJECTION (sid) (student))
    PRODUCT (SELECTION (*) (student)) (SELECTION (*) (course))
    ```

    SQL (Generated):
    ```
    SELECT * FROM (student);
    SELECT * FROM (SELECT * FROM (student) WHERE sid > 10) WHERE year = 2;
    SELECT year, sid FROM (student);
    SELECT year FROM (SELECT * FROM (student) WHERE year=1);
    (SELECT * FROM (student) WHERE year=1) UNION (SELECT * FROM (student) WHERE year=2);
    (SELECT sid FROM (SELECT * FROM (enrollment))) EXCEPT (SELECT sid FROM (student));
    (SELECT * FROM (student)) CROSS JOIN (SELECT * FROM (course));
    ```
    - From the `relational/code/src/tests` directory, run:
    ```
    bash test_dsl.sh
    ```
    Expected Output:
    ```
    Test passed: difference_test_1.in
    Test passed: product_test_1.in
    Test passed: projection_test_1.in
    Test passed: projection_test_2.in
    Test passed: selection_test_1.in
    Test passed: selection_test_2.in
    Test passed: union_test_1.in
    ```
- Checked error-free execution of the pipeline with SurrealDB for supported operations.
    - To check the pipeline, from the `relational/code/src/main` directory, run:
    ```
    bash check_pipeline.sh
    ```
    Expected Output:
    ```
    Pipeline passed for selection_test_1.in
    Pipeline passed for selection_test_2.in
    Pipeline passed for projection_test_1.in
    Pipeline passed for projection_test_2.in
    ```

## References
- https://www.doc.ic.ac.uk/~pjm/teaching/student_projects/gc106_report.pdf
- https://lark-parser.readthedocs.io/en/latest/examples/index.html
- https://blog.erezsh.com/how-to-write-a-dsl-in-python-with-lark/
- https://gist.github.com/PH111P/7c8b529c0293d8c35adc#file-relalgsql-hs
- https://surrealdb.com/docs/surrealdb/introduction