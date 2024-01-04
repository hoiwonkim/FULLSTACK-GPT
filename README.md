env\Scripts\Activate.ps1 - env환경을 들어가기
streamlit run Home.py
PrivateGPT: 
1. WSL 활성화: Windows에서 WSL 기능을 활성화해야 합니다. 이를 위해 PowerShell을 관리자 권한으로 실행한 후 다음 명령어를 입력합니다:

wsl --install
이 명령은 WSL과 함께 Ubuntu Linux 배포판을 설치합니다.

WSL 업데이트: 최신 버전의 WSL을 사용하는 것이 좋습니다. WSL 업데이트는 Microsoft Store를 통해 할 수 있습니다.

리눅스 배포판 실행: 설치가 완료되면, 시작 메뉴에서 Ubuntu를 검색하여 실행합니다.

2. Ollama 설치: Ubuntu 터미널이 열리면, Ollama를 설치하기 위한 명령어를 입력합니다. 일반적으로 Ollama의 설치 스크립트를 사용하여 설치할 수 있습니다. 예를 들어:

curl https://ollama.ai/install.sh | sh
이 명령은 Ollama의 설치 스크립트를 다운로드하고 실행합니다.

3. Ollama 실행 확인: 설치가 완료되면, Ollama가 제대로 설치되었는지 확인하기 위해 다음 명령어를 입력할 수 있습니다:

ollama --version

Metting GPT
1. choco install ffmpeg-full 명령어를 실행할 때 관리자 권한이 필요합니다. 관리자 권한으로 PowerShell 또는 명령 프롬프트를 실행하여 설치 과정을 진행해야 합니다. 다음과 같이 진행해주세요:

2. 관리자 권한으로 PowerShell 또는 명령 프롬프트 실행:
Windows 검색 바에서 'PowerShell' 또는 '명령 프롬프트'를 검색합니다.
나타난 결과에서 마우스 오른쪽 버튼을 클릭하고 '관리자 권한으로 실행'을 선택합니다.

3. Chocolatey를 이용한 FFmpeg 설치:
관리자 권한으로 열린 PowerShell 또는 명령 프롬프트에서 choco install ffmpeg-full을 입력하고 실행합니다.
설치 동의를 물어보면 'Y'를 눌러 진행합니다.

4. ffmpeg using command in the terminal

5. ffmpeg -i files/podcast.mp4 -vn files/audio.mp3

SiteGPT: npm install playwright
jupter 사용 단축키
Windows 전용 단축키입니다.

- ESC: "셀 편집 모드"에서 "셀 선택 모드"로 전환
- ENTER: 선택된 셀 편집하기(커서 생성)
- CTRL+ENTER: 현재 셀 코드 실행하기
- SHIFT+ENTER: 셀 실행한 뒤 새로운 셀 생성하기
- D D: 선택된 셀 삭제하기
- A / B: 위로(A) 혹은 아래로(B) 새로운 셀 생성하기

# Fullstack GPT

랭체인으로 AI 웹 서비스 7개 만들기

## 무엇을 배우나요?

GPT-4, Langchain 을 활용하여 AI 웹 서비스를 구축하는 방법을 A 부터 Z 까지 배웁니다.

-   Langchain, Language Models 에 대한 기본 이해
-   자체 데이터에 GPT-4를 사용하는 방법
-   커스텀 자율 에이전트(Autonomous Agent)를 만드는 방법…등 다수!

이제 AI를 활용하고 제대로 다루는 것은 개발자의 덕목 중 하나라고 해도 과언이 아닙니다. Fullstack GPT 강의를 통해 생산성은 물론 개발자로서의 스펙트럼을 넓혀 보세요.

## 어떻게 배우나요?

지금 당장 활용 할 수 있는 실전형 AI 웹서비스 7개를 직접 구현하며 배웁니다.

- AI 웹 서비스 (6종) : DocumentGPT, PrivateGPT, QuizGPT, SiteGPT, MeetingGPT, InvestorGPT
- ChatGPT 플러그인 (1종) : ChefGPT
- 활용하는 패키지 : Langchain, GPT-4, Whisper, FastAPI, Streamlit, Pinecone, Hugging Face… and more!

직접 구현하면서 배우는 것 만큼 빠르고 효과적인 학습방법은 없습니다. 실전 경험 그리고 포트폴리오까지 얻어가세요!

### DocumentGPT

법률. 의학 등 어려운 용어로 가득한 각종 문서. AI로 빠르게 파악하고 싶다면?

AI로 신속하고 정확하게 문서 내용을 파악하고 정리한 뒤, 필요한 부분만 쏙쏙 골라내어 사용하세요. DocumentGPT 챗봇을 사용하면, AI가 문서(.txt, .pdf, .docx 등)를 꼼꼼하게 읽고, 해당 문서에 관한 질문에 척척 답변해 줍니다.

### 이 코드는 Streamlit을 사용하여 문서 기반 질의응답 챗봇을 구현하는 것과 관련된 것입니다. 주요 구성 요소와 기능은 다음과 같습니다:

LangChain 라이브러리 사용: LangChain 라이브러리는 문서 로딩, 임베딩, 벡터 저장소, 챗 모델 등 다양한 기능을 제공합니다. 이 코드에서는 여러 LangChain 모듈이 사용됩니다.

Streamlit 설정: st.set_page_config을 사용하여 Streamlit 앱의 페이지 제목과 아이콘을 설정합니다.

ChatCallbackHandler 클래스: BaseCallbackHandler를 상속받아 커스텀 콜백 핸들러를 정의합니다. 이 클래스는 모델이 토큰을 생성할 때마다 호출되며, 메시지를 저장하고 Streamlit 인터페이스에 표시하는 기능을 담당합니다.

문서 처리 및 임베딩: 사용자가 업로드한 문서 파일을 읽고 처리하여 임베딩을 생성합니다. 이 과정에서 FAISS 벡터 저장소가 사용됩니다.

메시지 저장 및 표시 함수: save_message, add_to_history, send_message, paint_history 함수들은 사용자와 AI 간의 대화 내역을 관리하고 Streamlit 인터페이스에 표시합니다.

질의응답 프롬프트: ChatPromptTemplate.from_messages를 사용하여 질문-응답 형식의 프롬프트를 정의합니다.

Streamlit 인터페이스 구성: Streamlit을 사용하여 웹 인터페이스를 구성합니다. 파일 업로더, 메시지 입력 창, 챗 메시지 표시 등의 요소가 포함됩니다.

질의응답 처리 로직: 사용자가 메시지를 입력하면, 이전 대화의 컨텍스트(history)와 함께 현재의 질문을 처리하여 응답을 생성합니다. 이 과정에서 ChatOpenAI 모델과 정의된 프롬프트가 사용됩니다.

코드의 핵심은 사용자가 업로드한 문서에 대한 질문을 받아, 해당 문서 내용과 이전 대화의 컨텍스트를 기반으로 AI 모델을 통해 답변을 생성하는 것입니다. Streamlit은 사용자 인터페이스를 제공하고, LangChain은 문서 처리 및 AI 모델과의 상호작용을 담당합니다.

### PrivateGPT

회사 기밀이 유출될까 걱정된다면? 이제 나만이 볼 수 있는 비공개 GPT를 만들어 활용하세요!

DocumentGPT와 비슷하지만 로컬 언어 모델을 사용해 비공개 데이터를 다루기에 적합한 챗봇입니다. 데이터는 컴퓨터에 보관되므로 오프라인에서도 사용할 수 있습니다. 유출 걱정 없이 필요한 데이터를 PrivateGPT에 맡기고 업무 생산성을 높일 수 있어요.

### QuizGPT

암기해야 할 내용을 효율적으로 학습하고 싶다면?

문서나 위키피디아 등 학습이 필요한 컨텐츠를 AI에게 학습시키면, 이를 기반으로 퀴즈를 생성해 주는 앱입니다. 번거로운 과정을 최소화하고 학습 효율을 극대화할 수 있어, 특히 시험이나 단기간 고효율 학습이 필요할 때 매우 유용하게 사용할 수 있어요.

### SiteGPT

자주 묻는 질문 때문에 CS 직원을 채용...? SiteGPT로 비용을 2배 절감해 봅시다.

웹사이트를 스크랩하여 콘텐츠를 수집하고, 해당 출처를 인용하여 관련 질문에 답변하는 챗봇입니다. 고객 응대의 대부분을 차지하는 단순 정보 안내에 들이는 시간을 획기적으로 줄일 수 있고, 고객 또한 CS직원의 근무 시간에 구애받지 않고 정확한 정보를 빠르게 전달받을 수 있습니다.

### MeetingGPT

이제 회의록 정리는 MeetingGPT에게 맡기세요!

회의 영상 내용을 토대로 오디오 추출, 콘텐츠를 수집하여 회의록을 요약 및 작성해 주는 앱입니다. 회의 내용을 기록하느라 회의에 제대로 참석하지 못하는 일을 방지할 수 있고, 관련 질의응답도 가능해 단순한 기록보다 훨씬 더 효율적으로 회의록을 관리하고 활용할 수 있습니다.

### InvestorGPT

AI가 자료 조사도 알아서 척척 해 줍니다.

인터넷을 검색하고 타사 API를 사용할 수 있는 자율 에이전트입니다. 회사, 주가 및 재무제표를 조사하여 재무에 대한 인사이트를 제공할 수 있습니다. 또한 알아서 데이터베이스를 수집하기 때문에 직접 SQL 쿼리를 작성할 필요가 없고, 해당 내용에 대한 질의응답도 얼마든지 가능합니다.

### ChefGPT

요즘 핫한 ChatGPT 플러그인? 직접 구현해 봐요!

유저가 ChatGPT 플러그인 스토어에서 설치할 수 있는 ChatGPT 플러그인입니다. 이 플러그인을 통해 유저는 ChatGPT 인터페이스에서 바로 레시피를 검색하고 조리법을 얻을 수 있습니다. 또한 ChatGPT 플러그인에서 OAuth 인증을 구현하는 방법에 대해서도 배웁니다.