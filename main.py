from Client import PRNGClient

# The main program supplies the user ID once.
Tongyin = PRNGClient("Luoton")
Alexander = PRNGClient("Alexander")
Robert = PRNGClient("Robert")


# Each client automatically includes its own user ID.
print(Tongyin.generate("meal"))
print(Robert.generate("dashboard"))
print(Alexander.generate("textadv"))

# Update Tongyin's exercise result without changing other results.
print(Tongyin.generate("meal"))