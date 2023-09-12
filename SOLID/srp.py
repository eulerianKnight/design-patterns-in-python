# Consider a class Journal which has primary responsibility of maintaining entries.
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


# Below PersistenceManager Class should be a separate class
# The method to save the Journal should not be included in the Journal class itself.
# Including the method will violate SRP.

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file_ = open(filename, 'w')
        file_.write(str(journal))
        file_.close()


if __name__ == "__main__":
    j = Journal()
    j.add_entry("I am learning Design Patterns today.")
    j.add_entry("I will learn Microservices next week.")
    print(f'Journal entries: \n{j}')
    file = r'C:\Users\euler\temp\journal.txt'
    PersistenceManager.save_to_file(j, file)
    with open(file) as fh:
        print(fh.read())
