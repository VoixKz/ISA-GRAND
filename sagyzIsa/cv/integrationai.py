from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

class Question:
    def __init__(self, beautyId: int, option, question: str):
        self.bid = beautyId
        self.option = option
        self.question = question
    
    def isComboBoxQuestion(self) -> bool:
        return type(self.option) is PossibleOptions
    
    def isChatGPTQuestion(self) -> bool:
        return type(self.option) is str
    
    def getFancyName(self) -> str:
        return f'interestq_{self.bid}'
    
    def getFancyLabelId(self) -> str:
        return f'interestql_{self.bid}'
    
    def getFriendlyQuestion(self) -> str:
        return self.question

class PossibleOptions:
    def __init__(self, responses: list[str]):
        self.responses = responses
    
    def getResponses(self) -> list[str]:
        return self.responses
    
class TextBox:
    def __init__(self, password: bool = False):
        self.password = password

    def isPassField(self) -> bool:
        return self.password

REQ_GEN_HASHTAG = 'Summarise the given output by user in hashtags ENGLISH lowercase, maximum 5. Separate hashtags with single space'

PROMPT_GPT_GENERAL = {
    "role": "system",
    "content": "На каждый запрос пользователя хештеги на английском языке lowercase. Между ответами на запросы перемещай на другой строку. Отвечай только один раз на каждый запрос"
}

question_asking = {
    0: Question(0, PossibleOptions(['14-18', '18-24']), 'В какую категорию возраста вы входите?'),
    1: Question(1, PossibleOptions(['Да', 'Нет']), 'Вы учитесь в ВУЗе? (Университет или колледж)'),
    2: Question(2, REQ_GEN_HASHTAG, "Какие есть у вас навыки, которые могут пригодится?"),
    3: Question(3, REQ_GEN_HASHTAG, "Есть ли у вас клалификация и образование? Если да, то какие?"),
    4: Question(4, REQ_GEN_HASHTAG, "Есть ли у вас опыт работы в данной сфере? Если да, то какие?"),
    5: Question(5, 'Summarise the given output by getting a time answers by {MONTH}M or {DAYS}D or {YEARS}Y', 'Через какое время вы хотите устроиться на работу?'),
}

def processPost(userResponses: dict):
    answer_sheet = dict()
    for item, data in userResponses.items():
        if item == 'csrfmiddlewaretoken':
            continue
        print(f"Processing item: {item}")  # Отладочный вывод
        try:
            id = int(item.split('_')[1])
        except:
            continue
        if question_asking[id].isChatGPTQuestion:
            answer_sheet[id] = processByChatGPT(data)
        else:
            answer_sheet[id] = data
    return answer_sheet

def generatePdfCV(userResponses: dict):
    answer_sheet = ''
    for item, data in userResponses.items():
        if item == 'csrfmiddlewaretoken':
            continue
        print(f"Processing item: {item}")  # Отладочный вывод
        try:
            id = int(item.split('_')[1])
        except:
            continue
        if question_asking[id].isChatGPTQuestion:
            answer_sheet += " " + str(data)
    answer_sheet = processChatGPTQuestion([
        {
            "role": "system",
            "content": "Используя всю информацию с ввода пользователя, составь резюме по нему. Строго по шаблону - первый абзац про профиль, второй про навыки, третий про образование и клалификацию. Третий абзац должен быть маленьким, пару предложении. Писать простым текстом без форматирования, но можно делать списки"
        },
        {
            "role": "user",
            "content": answer_sheet
        }
    ])
    return answer_sheet

def getQuestions() -> dict[int, Question]:
    return question_asking

def processByChatGPT(responseUser: str):
    return processChatGPTQuestion([PROMPT_GPT_GENERAL, {"role": "user", "content": f"{responseUser}"}])

def processChatGPTQuestion(prompts_user):
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=3200,
        temperature=0.2,
        messages=prompts_user,
    )
    return chat_completion.choices[0].message.content.strip()