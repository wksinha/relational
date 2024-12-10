#!/bin/bash

cat query.surql | surreal sql --endpoint http://localhost:8000 --username root --password root --namespace popl --database relational