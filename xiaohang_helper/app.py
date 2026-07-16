import streamlit as st

# 会话状态初始化
if "answer" not in st.session_state:
    st.session_state["answer"] = ""

from api import call_api
from config import API_KEY, DATA_UPDATE_DATE
from prompts import RECOMMENDED_QUESTIONS, load_knowledge, show_phone_directory


st.set_page_config(page_title="小航校园信息助手", page_icon="🎓", layout="wide")

if "question" not in st.session_state:
    st.session_state["question"] = ""
if "answer" not in st.session_state:
    st.session_state["answer"] = ""

st.title("小航 · 郑州航院校园信息助手")
st.caption(f"数据更新：{DATA_UPDATE_DATE}")

if not API_KEY:
    st.warning("当前未配置 SILICONFLOW_API_KEY，先可测试页面交互和电话黄页展示。")

role = st.selectbox("你是?", ["新生", "在校生", "教师"])

st.markdown("**试试这些问题：**")
questions = RECOMMENDED_QUESTIONS.get(role, [])
cols = st.columns(4)
for i, q in enumerate(questions):
    with cols[i % 4]:
        if st.button(q, key=f"q_{role}_{i}", use_container_width=True):
            st.session_state["question"] = q

question = st.text_input("有啥想问的?", key="question")

action_col1, action_col2 = st.columns([1, 1])
with action_col1:
    ask_clicked = st.button("提问", use_container_width=True)
with action_col2:
    phone_clicked = st.button("查看电话黄页", use_container_width=True)

if phone_clicked:
    st.subheader("电话黄页")
    st.text(show_phone_directory())

if ask_clicked:
    # 双重校验：非空 + 去除空格后不为空字符串
    if question is not None and question.strip() != "":
        with st.spinner("正在整理答案..."):
            knowledge = load_knowledge()
            st.session_state["answer"] = call_api(question.strip(), role, knowledge)
    else:
        st.warning("请先输入问题。")

if st.session_state["answer"]:
    st.subheader("回答")
    st.write(st.session_state["answer"])
phone_content = show_phone_directory()
st.text(phone_content if phone_content is not None else "暂无电话黄页数据")