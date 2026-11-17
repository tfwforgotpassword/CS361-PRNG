from Client import PRNGClient

# The main program supplies the user ID once.
Tongyin = PRNGClient("Luoton")
Alexander = PRNGClient("Alexander")
Robert = PRNGClient("Robert")


# Each client automatically includes its own user ID.
print(Tongyin.generate("meal"), 1)
print(Robert.generate("dashboard"), 2)
print(Alexander.generate("textadv"), 3)

# Update Tongyin's exercise result without changing other results.
print(Tongyin.generate("meal"), 1)
print(Alexander.retrieve("textadv"), 3)
print(Alexander.generate_range("jumpscare", 1, 10000))