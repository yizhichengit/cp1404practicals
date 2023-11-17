class Band:
    """Band class for storing details of a band."""

    def __init__(self, name=""):
        """Initialise a Band."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"Band {self.name} with members: {', '.join(member.name for member in self.members)}"

    def add(self, musician):
        """Add a musician to the band's member list."""
        self.members.append(musician)

    def play(self):
        """Simulate playing music by printing each musician's play action."""
        for member in self.members:
            print(member.play())

# Assuming the rest of your `my_band.py` code remains unchanged.