import nltk
import random

class Chatbot:
    responses = {
        "안녕": "안녕하세요!",
        "반가워": "저도 반갑습니다!",
        "잘가": "다음에 또 뵈어요!"
    }

    def __init__(self):
        # 챗봇 초기화 작업 수행
        nltk.download('punkt') # NLTK 패키지의 punkt 모듈을 다운로드

    def get_response(self, message):
        # 사용자의 입력에 대한 적절한 응답 반환
        if message in self.responses:
            return self.responses[message]
        else:
            return "죄송해요, 잘 모르겠어요."