# class => use to bundle data(attributes) & behaviour

class Dog:
    def __init__(self, name, breed="Not Assigned"):
        self.name = name
        self.breed = breed

# Create dog objects - using positional arguments
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Or with named arguments (clearer)
dog3 = Dog(name="Charlie", breed="Poodle")
dog4 = Dog("Rocky")

print(dog1.name)   # Buddy
print(dog2.breed)  # Beagle
print(dog3.breed)  # Poodle
print(dog3.name)   # Charlie
print(dog4.breed)  # Not Assigned
print(dog4.name)   # Rocky

# ------------------------------------------

# Without classes - data and functions separate
name = "OpenAI"
model = "gpt-4o-mini"

def generate_response(prompt):
    # Process prompt...
    response = "Response From OpenAI (Without Classes)"
    return response

print(generate_response("Hello"))

# -------------------------------------------

# With classes - everything bundled together
class OpenAIClient:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def generate_response(self, prompt):
        # Process prompt...
        response = "Response from OpenAI (With Classes)"
        return response


obj = OpenAIClient(name, model)
print(obj.generate_response("Hello"))


# --------------------------------------------
