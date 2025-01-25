import yaml
import streamlit as st
import streamlit_authenticator as stauth

# YAML 파일 로드 함수
def load_users():
    with open("hash.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)["users"]

# 사용자 인증 함수
def authenticate(username, password, users):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

# Form 생성
st.title("🛴Kick Bird")
st.info("헬멧 착용 완료")

# YAML에서 사용자 로드
users = load_users()

# 로그인 성공 상태
login_success = False
username = ""

# 폼 시작
with st.form("form"):
    st.subheader("본인인증")
    username = st.text_input("이름", placeholder="이름을 입력하세요.")
    password = st.text_input("비밀번호", type="password")

    # 로그인 버튼 추가
    login_button = st.form_submit_button("로그인", type="primary")

    # 로그인 버튼 클릭 시
    if login_button:
        if authenticate(username, password, users):
            st.success(f"사용자 인증되었습니다.")
            login_success = True
        else:
            st.error("사용자 이름 또는 비밀번호가 잘못되었습니다.")

# 텍스트 파일 다운로드 버튼
if login_success:
    text_contents = "0"  # 내용 "0"인 파일
    st.download_button(
        label="Download txt",
        data=text_contents,
        file_name="streamlit_download.txt",
        mime="text/plain"
    )

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