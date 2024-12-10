# Example Relational Algebra
1. SELECTION (*) (student)
    - Wildcard selection
2. SELECTION (year = 2) (SELECTION  (sid > 10) (student))
    - Nested selection
3. PROJECTION (year, sid) (student)
    - Projection
4. PROJECTION (year) (SELECTION (year=1) (student))
    - Projection over Selection
5. UNION ( SELECTION (year=1) (student) ) ( SELECTION (year=2) (student) )
    - Union
6. DIFFERENCE (PROJECTION (sid) (SELECTION (*) (enrollment))) (PROJECTION (sid) (student))
    - Difference
7. PRODUCT (SELECTION (*) (student)) (SELECTION (*) (course))
    - Cross Product