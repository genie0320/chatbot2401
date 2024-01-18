import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
debug_mode = os.getenv("DEBUG")
# NOTE: 처음실행시, 여기에 각 값을 입력>저장해줘야 함(안그러면 계속 반복적으로 생성.)
ast_ID = ''
trd_ID = ''
msg_ID = []

OpenAI.api_key = api_key
client = OpenAI()

def create_assistant():
    my_assistant = client.beta.assistants.create(
            instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
            name="Math Tutor2",
            tools=[{"type": "code_interpreter"}],
            model="gpt-3.5-turbo-1106",
        )
    ast_ID = my_assistant.id
    # print(my_assistant)
    print(f'ast_ID : {ast_ID}')
    return ast_ID

def create_thred():
    thread = client.beta.threads.create()
    trd_ID = thread.id
    # print(thread)
    print(f'trd_ID : {trd_ID}')
    return trd_ID

def create_msg(user_msg):
    message = client.beta.threads.messages.create(
    thread_id=trd_ID,
    role="user",
    content=user_msg
    )
    msg_added = messages.data[0].content[0].text.value
    return msg_added

# Create Assistant
if ast_ID:
    print ('There is a assistant for you.')
else:
    ast_ID = create_assistant()

# Create thred
if trd_ID:
    print ('There is a thred.')
else:
    trd_ID = create_thred()

# Create message with user input
user_msg = input("뭐가 궁금? ")
# TODO:사용자가 자유롭게 입력할 수 있는 내용을 쌓을 수 있도록... 입력할지 넘어갈지 물어보기.
if user_msg:
    msg_added = create_msg(user_msg)
    print(msg_added)
else:
    # View list of msgs
    messages = client.beta.threads.messages.list(
        thread_id=trd_ID,
        order = 'asc'
        )
    # print(messages)
    print(len(messages.data))
    for msg in messages.data:
        print(msg.content[0].text.value)

user_inst = input("특별한 지시사항이 있나요? ")
send_or_not = int(input('요청을 보낼까요? (1/0)'))

# Run assistant.
run_ID='run_c2p22TrM56P6m729VCKPni9u'

# FIXME:결과를 어떻게 받아줄 것인가.... status가 complete 될 때까지 계속 불러줘야 한다는데...  
if send_or_not:
    run = client.beta.threads.runs.create(
        thread_id=trd_ID,
        assistant_id=ast_ID,
        instructions=user_inst
        )
    # print(f'cre : {run}')
else :
    print('bye')

# Assistant 는 매우 비싸다. gpt3.5-turbo의 30배정도?
# https://openai.com/pricing
# Tool	Input
# Code interpreter	$0.03 / session
# Retrieval	$0.20 / GB / assistant / day (free until 02/01/2024)