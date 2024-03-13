
# imports 
import logging
import sys

import os
import openai


from llama_index.llms.openai import OpenAI
from llama_index.core.query_engine import JSONalyzeQueryEngine


# optional logging 
#logging.basicConfig(stream=sys.stdout, level=logging.INFO)
#logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


os.environ["OPENAI_API_KEY"] = "YOUR-API-KEY"
openai.api_key = "YOUR-API-KEY"


json_list = [
    {
        "name": "John Doe",
        "age": 25,
        "major": "Computer Science",
        "email": "john.doe@example.com",
        "address": "123 Main St",
        "city": "New York",
        "state": "NY",
        "country": "USA",
        "phone": "+1 123-456-7890",
        "occupation": "Software Engineer",
    },
    {
        "name": "Jane Smith",
        "age": 30,
        "major": "Business Administration",
        "email": "jane.smith@example.com",
        "address": "456 Elm St",
        "city": "San Francisco",
        "state": "CA",
        "country": "USA",
        "phone": "+1 234-567-8901",
        "occupation": "Marketing Manager",
    },
    {
        "name": "Michael Johnson",
        "age": 35,
        "major": "Finance",
        "email": "michael.johnson@example.com",
        "address": "789 Oak Ave",
        "city": "Chicago",
        "state": "IL",
        "country": "USA",
        "phone": "+1 345-678-9012",
        "occupation": "Financial Analyst",
    },
    {
        "name": "Emily Davis",
        "age": 28,
        "major": "Psychology",
        "email": "emily.davis@example.com",
        "address": "234 Pine St",
        "city": "Los Angeles",
        "state": "CA",
        "country": "USA",
        "phone": "+1 456-789-0123",
        "occupation": "Psychologist",
    },
    {
        "name": "Alex Johnson",
        "age": 27,
        "major": "Engineering",
        "email": "alex.johnson@example.com",
        "address": "567 Cedar Ln",
        "city": "Seattle",
        "state": "WA",
        "country": "USA",
        "phone": "+1 567-890-1234",
        "occupation": "Civil Engineer",
    },
    {
        "name": "Jessica Williams",
        "age": 32,
        "major": "Biology",
        "email": "jessica.williams@example.com",
        "address": "890 Walnut Ave",
        "city": "Boston",
        "state": "MA",
        "country": "USA",
        "phone": "+1 678-901-2345",
        "occupation": "Biologist",
    },
    {
        "name": "Matthew Brown",
        "age": 26,
        "major": "English Literature",
        "email": "matthew.brown@example.com",
        "address": "123 Peach St",
        "city": "Atlanta",
        "state": "GA",
        "country": "USA",
        "phone": "+1 789-012-3456",
        "occupation": "Writer",
    },
    {
        "name": "Olivia Wilson",
        "age": 29,
        "major": "Art",
        "email": "olivia.wilson@example.com",
        "address": "456 Plum Ave",
        "city": "Miami",
        "state": "FL",
        "country": "USA",
        "phone": "+1 890-123-4567",
        "occupation": "Artist",
    },
    {
        "name": "Daniel Thompson",
        "age": 31,
        "major": "Physics",
        "email": "daniel.thompson@example.com",
        "address": "789 Apple St",
        "city": "Denver",
        "state": "CO",
        "country": "USA",
        "phone": "+1 901-234-5678",
        "occupation": "Physicist",
    },
    {
        "name": "Sophia Clark",
        "age": 27,
        "major": "Sociology",
        "email": "sophia.clark@example.com",
        "address": "234 Orange Ln",
        "city": "Austin",
        "state": "TX",
        "country": "USA",
        "phone": "+1 012-345-6789",
        "occupation": "Social Worker",
    },
    {
        "name": "Christopher Lee",
        "age": 33,
        "major": "Chemistry",
        "email": "christopher.lee@example.com",
        "address": "567 Mango St",
        "city": "San Diego",
        "state": "CA",
        "country": "USA",
        "phone": "+1 123-456-7890",
        "occupation": "Chemist",
    },
    {
        "name": "Ava Green",
        "age": 28,
        "major": "History",
        "email": "ava.green@example.com",
        "address": "890 Cherry Ave",
        "city": "Philadelphia",
        "state": "PA",
        "country": "USA",
        "phone": "+1 234-567-8901",
        "occupation": "Historian",
    },
    {
        "name": "Ethan Anderson",
        "age": 30,
        "major": "Business",
        "email": "ethan.anderson@example.com",
        "address": "123 Lemon Ln",
        "city": "Houston",
        "state": "TX",
        "country": "USA",
        "phone": "+1 345-678-9012",
        "occupation": "Entrepreneur",
    },
    {
        "name": "Isabella Carter",
        "age": 28,
        "major": "Mathematics",
        "email": "isabella.carter@example.com",
        "address": "456 Grape St",
        "city": "Phoenix",
        "state": "AZ",
        "country": "USA",
        "phone": "+1 456-789-0123",
        "occupation": "Mathematician",
    },
    {
        "name": "Andrew Walker",
        "age": 32,
        "major": "Economics",
        "email": "andrew.walker@example.com",
        "address": "789 Berry Ave",
        "city": "Portland",
        "state": "OR",
        "country": "USA",
        "phone": "+1 567-890-1234",
        "occupation": "Economist",
    },
    {
        "name": "Mia Evans",
        "age": 29,
        "major": "Political Science",
        "email": "mia.evans@example.com",
        "address": "234 Lime St",
        "city": "Washington",
        "state": "DC",
        "country": "USA",
        "phone": "+1 678-901-2345",
        "occupation": "Political Analyst",
    },
]


llm = OpenAI(model="gpt-3.5-turbo")

json_stats_query_engine = JSONalyzeQueryEngine(
    list_of_dict=json_list,
    llm=llm,
    verbose=True,
)

q1="Who is the oldest and how old is he?"

print("> Question: {}".format(q1))
print("Answer: {}".format(json_stats_query_engine.query(q1)))
