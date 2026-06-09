import streamlit as st
from google import genai

# 페이지 설정
st.set_page_config(
    page_title="연애 상담 챗봇",
    page_icon="💖"
)

st.title("💖 연애 상담 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반")

# API 키 확인
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("GEMINI_API_KEY가 Secrets에 설정되지 않았습니다.")
    st.stop()

# Gemini 클라이언트 생성
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Gemini 초기화 오류: {e}")
    st.stop()

# 채팅 기록 저장
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요! 연애 고민이 있다면 편하게 이야기해 주세요 😊"
        }
    ]

# 기존 메시지 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력
prompt = st.chat_input("메시지를 입력하세요")

if prompt:
    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # 대화 기록 생성
    conversation = ""

    for msg in st.session_state.messages:
        role = "사용자" if msg["role"] == "user" else "상담사"
        conversation += f"{role}: {msg['content']}\n"

    system_prompt = """
너는 친절한 연애 상담 챗봇이다.

규칙:
- 공감하는 말투 사용
- 현실적인 조언 제공
- 지나치게 단정하지 않기
- 답변은 너무 길지 않게
- 한국어로 답변
"""

    try:
        with st.chat_message("assistant"):
            with st.spinner("생각 중..."):

                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=f"""
{system_prompt}

대화 내용:
{conversation}

상담사 답변:
"""
                )

                answer = response.text

                st.markdown(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

    except Exception as e:
        error_msg = f"오류가 발생했습니다: {e}"

        with st.chat_message("assistant"):
            st.error(error_msg)

        st.session_state.messages.append(
            {"role": "assistant", "content": error_msg}
        )
