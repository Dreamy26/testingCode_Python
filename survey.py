# Testing a class
"""Collect anonymous answers to a survey question."""

def __init__(self, question):
    """Store a question, and prepare to store responses."""
    self.question = question
    self.responses = [] # empty list, to store responses   

def show_question(self): # display survey question
    """Show the survey question"""
    print (self.question)

def store_response(self, new_response): # store a new response, and print all 
    """Store a single response to the survey."""
    self.responses.append()

def show_results(self): # show all 
    """Show all the responses that have been given."""
    print("Survey results:")
    for response in self.responses:
        print(f"- {response}")