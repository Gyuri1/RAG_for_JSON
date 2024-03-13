RAG with JSON Data

How to install:
====

    pip install -r requirements.txt


How to run:
====

    python rag.py


This should be the result:
====
> python3 rag.py  
> Question: Who is the oldest and how old is he?  
Query: Who is the oldest and how old is he?  
SQL Query: SELECT name, age  
FROM items  
ORDER BY age DESC  
LIMIT 1;  
Table Schema: {'name': <class 'str'>, 'age': <class 'int'>, 'major': <class 'str'>, 'email': <class 'str'>, 'address': <class 'str'>, 'city': <class 'str'>, 'state': <class 'str'>, 'country': <class 'str'>, 'phone': <class 'str'>, 'occupation': <class 'str'>}  
SQL Response: [{'name': 'Michael Johnson', 'age': 35}]  
Response: The oldest person is Michael Johnson and he is 35 years old.
> Answer: The oldest person is Michael Johnson and he is 35 years old.  
>   
