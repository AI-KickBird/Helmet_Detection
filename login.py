import datetime
import streamlit as st

# Form 생성
st.title("🛴Kick Bird")
st.info("헬멧 착용 완료")

# 폼 시작
with st.form("form"):
    
    # 사용자 정보 입력 
    st.subheader("이름")
    text_input = st.text_input(" ", placeholder="이름을 입력하세요.")

    st.subheader("생년월일")
    d = st.date_input("", value=None)

    # 로그인 버튼
    submitted = st.form_submit_button("로그인", type="primary")
    # st.link_button("확인", "https://naver.com")

    # 자바스크립트로 인증창 띄우기
    if submitted:
        js_code = """
        <script>
        alert('사용자 인증되었습니다.');
        </script>
        """
        st.components.v1.html(js_code)

# 텍스트 파일 다운로드 버튼
text_contents = "user"
st.download_button("Download text", text_contents)

# folium 지도 생성
import folium
from streamlit_folium import st_folium

# folium 마커 추가
m = folium.Map(location=[37.547621, 126.945588], zoom_start=16)
folium.Marker(
    [37.547621, 126.945588], 
    popup="CodingOn", 
    tooltip="CodingOn",
    icon=folium.Icon(color="red")
).add_to(m)

# map 출력
st.subheader("📍현재 위치")
st_data = st_folium(m, width=700)