# Chatbot


# introduction
-------------------------------
훈련된 질의에 대해서는 검색 기반 모델로 응답을 하고, <br>
훈련되지 않은 질의의 대해서도 적절한 대답을 할 수 있도록 생성모델을 챗봇 기능에 추가하여 하이브리드 챗봇을 개발한다.

# Process
-------------------------------
![ChatbotProcess](https://user-images.githubusercontent.com/35329247/64348087-8b436180-d02f-11e9-84a1-e54a922a1385.png)

1. Entity 추출 : 사용자의 질문에서 핵심 단어를 추출한다.
2. TF-IDF : 훈련 데이터로 얻은 TF-IDF를 적용하여 생성 모델에 대한 의도를 추출
3. Intent 추출 : 딥러닝 모델 Feed Forward Neural Network 형태의 모델로 Multi Classification 기능을 구현한다. 이를 통해 질문에서 사용자의 의도를 추출한다.
4. Slot Filling : 대답을 하기 위한 핵심단어와 의도가 준비되면 그 데이터를 토대로 적절한 답변을 Database에서 가져온다.
5. 생성 모델 : Recurrent Neural Network 중 하나인 Seq2Seq 모델을 이용하여 적절한 일상 대화를 학습 시켜 답변을 생성한다.
6. 코사인 유사도 : 코사인 유사도는 두 벡터 간의 코사인 각도를 이용하여 구할 수 있는 두 벡터의 유사도를 의미하며, 유사도 값에 따라서 유사도를 판단한다.


# Environment
--------------------------------
Chatbot : TensorFlow, MongoDB, Keras <br>
Web Server : Flask, Javascript <br>
NLP : Mecab <br>


