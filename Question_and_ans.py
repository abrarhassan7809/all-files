question_list = [
            {'text': "A slug's blood is green", 'ans': "True"},
            {'text': "The loudest animal is the african elephant", 'ans': "False"},
            {'text': "The google originally called", 'ans': "True"}
        ]


class Question:
    def __init__(self, q_1, q_2):
        self.text = q_1
        self.ans = q_2


class QuestionFunc:
    def __init__(self, que_list):
        self.question_no = 0
        self.score = 0
        self.question_l = que_list

    def still_have_ques(self):
        return self.question_no < len(self.question_l)

    def next_que(self):
        current_que = self.question_l[self.question_no]
        self.question_no += 1
        user_answer = input(f"{self.question_no} : {current_que.text} (True/False) : ")
        self.check_answer(user_answer, current_que.ans)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower:
            self.score += 1
            print("yes your right : ")
        else:
            print("that's wrong")
        print(f"the correct ans is : {correct_answer}")
        print(f"your score is {self.score}/{self.question_no}")


question_bank = []
for x in question_list:
    q1 = x["text"]
    q2 = x["ans"]
    new_question = Question(q1, q2)
    question_bank.append(new_question)

obj = QuestionFunc(question_bank)
while QuestionFunc.still_have_ques:
    obj.next_que()

hh = QuestionFunc
hh.next_que
