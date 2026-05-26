import streamlit as st
from datetime import datetime

# 앱 제목
st.title("📅 디데이 계산기")

# 날짜 입력
target_date = st.date_input("목표 날짜를 선택하세요")

# 오늘 날짜
today = datetime.today().date()

# 디데이 계산
diff = (target_date - today).days

# 결과 출력
st.subheader("결과")

if diff > 0:
    st.success(f"🎉 D-{diff}")
elif diff == 0:
    st.info("🔥 D-DAY!")
else:
    st.error(f"📌 D+{abs(diff)}")
