# Dit stuk code definieert een Python-klasse genaamd "Question". De klasse heeft twee attributen: "text" en "answer".
# De init methode wordt gebruikt om nieuwe objecten van de klasse te maken. Het heeft twee parameters: "question_text"
# en "question_answer". Deze worden gebruikt om de waarden van de attributen "text" en "answer" in te stellen wanneer
# er een nieuw object wordt gemaakt.

# De regels:
# new_question = Question("a piece of text", "False")
# print(new_question.text)
# maken een nieuw object van de klasse "Question" en slaan het op in de variabele "new_question". Het "question_text"
# argument "a piece of text" wordt gebruikt om de waarde van het attribuut "text" in te stellen en het "question_answer"
# argument "False" wordt gebruikt om de waarde van het attribuut "answer" in te stellen.
# Vervolgens wordt met de "print" functie de waarde van "new_question.text" afgedrukt, in dit geval "a piece of text".

class Question:
    def __init__(self, question_text, question_answer):
        self.text = question_text
        self.answer = question_answer


new_question = Question("A piece of text", "False")
print(new_question.text)
