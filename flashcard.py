# Flash Card Formatting
class FlashCard:
    def __init__(self, question, answer, correct=0, attempted=0):
        self.question = question
        self.answer = answer
        self.correct = correct
        self.attempted = attempted

    def mark_correct(self):
        # Updates total correct and attempted values
        self.correct += 1
        self.attempted += 1

    def mark_attempts(self):
        # Updates total attempts made   
        self.attempted += 1

    def get_stats(self):
        # Returns stats
        return f"You have {self.correct} correct answers out of {self.attempted} attempts."
    
    def to_dict(self):
        # Formatting the data to dictionary
        return {
            "question" : self.question,
            "answer" : self.answer,
            "correct" : self.correct,
            "attempted" : self.attempted
        }
