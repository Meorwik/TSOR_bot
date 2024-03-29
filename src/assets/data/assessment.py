from .assessment_data import assessment_data
from typing import Final, List, Dict


class Question:
    """
    Class 'Question' represents an instance of one single question
    It contains data about question itself, correct and incorrect answers
    """

    __name__: Final[str] = "Question"

    def __repr__(self):
        return f"({id(self)}) - {self.__name__}Object N#{self.number}"

    def __init__(self, question: Dict):
        self.__number: Final[int] = question.get("number")
        self.__text: Final[str] = question.get("question")
        self.__answers: Final[List[str]] = question.get("answers")
        self.__correct_answer: Final[str] = question.get("correct_answer")

    @property
    def number(self) -> int:
        return self.__number

    @property
    def text(self) -> str:
        return self.__text

    @property
    def correct_answer(self) -> str:
        return self.__correct_answer

    @property
    def answers(self) -> List[str]:
        return self.__answers


class Assessment:

    __name__: Final[str] = "Assessment"

    def __repr__(self):
        return f"({id(self)}) - {self.__name__}Object"

    def __init__(self, data: Dict):
        self.context: Final[str] = data.get("main_text")
        self.questions: Final[List[Question]] = [
            Question(data.get(f"question_{n}")) for n in range(1, len(data) - 1)
        ]

    def get_question(self, question_number: int) -> Question:
        for question in self.questions:
            if question.number == question_number:
                return question


main_assessment: Assessment = Assessment(assessment_data)
