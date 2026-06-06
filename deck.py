from flashcard import FlashCard
import json

class Deck:
    def __init__(self):
        self.cards = []
        self.filepath = "./data/cards.json"

    def add_card(self, question, answer):
        # creates a new FlashCard and adds to list
        self.cards.append(FlashCard(question, answer))
        return "Card added successfully!"

    def delete_card(self, index):
        # removes a card by its index
        if index < 0 or index <= len(self.cards):
            return "Error: Invalid Index!"
        self.cards.pop(index)
        return "Card removed successully!"

    def get_all_cards(self):
            # returns the list of all cards
            return self.cards

    def save(self):
        # saves all cards to cards.json
        try:
            with open(self.filepath, 'w') as file:
                data = {"cards": [card.todict() for card in self.cards]}
                json.dump(data, file, indent=4)
                return "Card saved to storage"
        
        except FileNotFoundError:
            print("File not found!")
        
        except json.JSONDecodeError:
            print("Error: Invalid JSON file format!") 

    def load(self):
        # loads cards from cards.json
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)

                for card in data["cards"]:
                    self.cards.append(
                        FlashCard(
                            question=card["question"],
                            answer=card["answer"],
                            correct=card["correct"],
                            attempted=card["attempted"]
                            )
                    )
                return "Cards loaded successfully"
        
        except FileNotFoundError:
            print("Error: File not found!")
            
        except json.JSONDecodeError:
            print("Error: Invalid JSON file format!")
