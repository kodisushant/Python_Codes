import random
import time

class DadJokeGenerator:
    def __init__(self):
        self.setups = [
            "Why don't scientists trust atoms?",
            "Why did the scarecrow win an award?",
            "What do you call a bear with no teeth?",
            "Why don't eggs tell jokes?",
            "What do you call a fake noodle?",
            "Why did the bicycle fall over?",
            "What do you call a can opener that doesn't work?",
            "Why don't skeletons fight each other?"
        ]
        
        self.punchlines = [
            "Because they make up everything! 😄",
            "Because he was outstanding in his field! 🌾",
            "A gummy bear! 🐻",
            "They'd crack each other up! 🥚",
            "An impasta! 🍝",
            "Because it was two-tired! 🚲",
            "A can't opener! 🥫",
            "They don't have the guts! 💀"
        ]
    
    def tell_joke(self):
        """Tells a joke with dramatic pause"""
        idx = random.randint(0, len(self.setups) - 1)
        
        print(f"\n🎤 Dad Joke #{random.randint(1, 999)}:")
        print(f"\n{self.setups[idx]}")
        
        # Dramatic pause with dots
        print("\n🤔 Thinking", end="")
        for _ in range(3):
            time.sleep(2)
            print(".", end="", flush=True)
        
        time.sleep(2)
        print(f"\n\n{self.punchlines[idx]}")
        print("\n" + "😂" * 5)
        
        # Rate your own joke (always thinks it's funny)
        self.rate_joke()
    
    def rate_joke(self):
        """Dad always thinks his jokes are 10/10"""
        time.sleep(2)
        print("\n📊 Dad's self-rating: 10/10 ⭐")
        print("👨 'I'm hilarious!' - Dad, probably")


# Run the dad joke generator
if __name__ == "__main__":
    print("🎭 Welcome to the Dad Joke Generator 3000! 🎭")
    print("=" * 50)
    
    dad = DadJokeGenerator()
    
    while True:
        dad.tell_joke()
        
        response = input("\n\nWant another joke? (y/n): ").lower()
        if response != 'y':
            print("\n👋 Thanks for laughing (or groaning)! Bye!")
            break