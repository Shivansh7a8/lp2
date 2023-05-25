# Define the knowledge base
knowledge_base = {
    "data_organization": {
        "question": "How should data be organized for efficient retrieval?",
        "answers": [
            "Data should be structured using a relational database model.",
            "Data can be organized in a hierarchical structure.",
            "Data can be stored in a distributed file system.",
            "Data can be organized using NoSQL databases."
        ]
    },
    "data_retrieval": {
        "question": "What are some techniques for efficient data retrieval?",
        "answers": [
            "Using indexing and search algorithms.",
            "Implementing caching mechanisms.",
            "Applying query optimization techniques.",
            "Utilizing data partitioning and sharding."
        ]
    },
    "data_security": {
        "question": "How can data security be ensured?",
        "answers": [
            "Implementing access control mechanisms.",
            "Encrypting sensitive data.",
            "Regularly updating security patches.",
            "Performing vulnerability assessments and penetration testing."
        ]
    }
}

# Define the inference engine
def process_input(user_input):
    if user_input.lower() in knowledge_base:
        knowledge = knowledge_base[user_input.lower()]
        return knowledge["question"], knowledge["answers"]
    else:
        return "I'm sorry, I don't have information about that topic.", []

# User interaction loop
print("Welcome to the Information Management Expert System!")
print("Please enter a topic (data_organization, data_retrieval, data_security) or 'exit' to quit.")

while True:
    user_input = input("User: ")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    question, answers = process_input(user_input)
    
    print("Expert System:")
    print(question)
    
    if answers:
        print("Possible answers:")
        for answer in answers:
            print("- " + answer)
    else:
        print("No information available on this topic.")
