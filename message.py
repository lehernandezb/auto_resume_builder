from master_resume import start
message = """
Hello, welcome to the auto resume builder!
          
What would you like to do today?
    1. Add to master resume
    2. Create tailored resume
    3. Edit master resume
"""

def opening_screan():
    print(message)
    user_input = input()
    digits_only = ''.join(c for c in user_input if c.isdigit())
    key = ["1", "2", "3"]
    if digits_only not in key:
       opening_screan()
    if digits_only == 1:
        start()