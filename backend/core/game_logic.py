class Node:
    def __init__(self, word):
        self.word = word
        self.next = None

class GameManager:
    def __init__(self):
        self.head = None
        self.words = set()
        self.score = 0

    def reset(self):
        self.head = None
        self.words.clear()
        self.score = 0

    def get_history(self):
        current = self.head
        history = []
        while current:
            history.append(current.word)
            current = current.next
        return history

    def get_score(self):
        return {"score": self.score}

    async def handle_guess(self, data):
        guess = data.get("guess")
        seed = data.get("seed", "Rock")
        strict_mode = data.get("strict_mode", False)

        if guess in self.words:
            return {"status": "Game Over", "message": f"{guess} was already guessed."}

        # Use strict logic or AI verdict
        if strict_mode:
            verdict = GameManager.strict_logic(guess, seed)
        else:
            # TODO: Replace with actual OpenAI call
            verdict = "YES"

        if verdict == "YES":
            new_node = Node(guess)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

            self.words.add(guess)
            self.score += 1
            return {"status": "Correct", "message": f"✅ Nice! '{guess}' beats '{seed}'."}

        elif verdict == "TIE":
            return {"status": "Tie", "message": f"⚖️ It's a tie between '{guess}' and '{seed}'."}
        else:
            return {"status": "Wrong", "message": f"❌ '{guess}' does not beat '{seed}'."}

    @staticmethod
    def strict_logic(guess: str, seed: str) -> str:
        rules = {
            "Rock": "Scissors",
            "Scissors": "Paper",
            "Paper": "Rock"
        }
        if guess == seed:
            return "TIE"
        elif rules.get(guess) == seed:
            return "YES"
        else:
            return "NO"
