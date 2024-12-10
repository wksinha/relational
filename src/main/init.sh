#!/bin/bash

cat init.surql | surreal sql --endpoint http://localhost:8000 --username root --password root --namespace popl --database relational