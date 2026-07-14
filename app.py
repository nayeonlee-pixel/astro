import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="도플러 효과 시뮬레이터", page_icon="🌌")

st.title("🌌 도플러 효과 시뮬레이터")
st.write("### 물리학Ⅱ - 고전적 도플러 효과와 상대론적 도플러 효과 비교")

# -----------------------------
# 속도 입력
# -----------------------------
beta = st.slider(
    "속도 (v/c)를 선택하세요",
    0.0,
    0.99,
    0.20,
    0.01
)

# -----------------------------
# 계산
# -----------------------------
classical = 1 - beta
relativity = np.sqrt((1-beta)/(1+beta))
error = abs(classical-relativity)/relativity*100

# -----------------------------
# 결과
# -----------------------------
col1,col2,col3 = st.columns(3)

col1.metric("고전식", f"{classical:.4f}")
col2.metric("상대론", f"{relativity:.4f}")
col3.metric("오차", f"{error:.2f}%")

# -----------------------------
# 그래프
# -----------------------------
x=np.linspace(0,0.99,100)

y1=1-x
y2=np.sqrt((1-x)/(1+x))

fig,ax=plt.subplots(figsize=(8,5))

ax.plot(x,y1,label="Classical")

ax.plot(x,y2,label="Relativistic")

ax.scatter(beta,classical,s=80)

ax.scatter(beta,relativity,s=80)

ax.set_xlabel("v/c")

ax.set_ylabel("f'/f")

ax.grid()

ax.legend()

st.pyplot(fig)

# -----------------------------
# 적색편이
# -----------------------------
st.write("## 🌈 적색편이")

if beta<0.2:
    st.info("🔵 거의 변화가 없습니다.")
elif beta<0.5:
    st.warning("🟡 약한 적색편이가 나타납니다.")
elif beta<0.8:
    st.error("🟠 적색편이가 뚜렷합니다.")
else:
    st.error("🔴 매우 강한 적색편이입니다.")

# -----------------------------
# 수학적 모델
# -----------------------------
st.write("## 📚 수학적 모델")

st.latex(r"f_c=1-\beta")

st.latex(r"f_r=\sqrt{\frac{1-\beta}{1+\beta}}")

st.write("""
- β=v/c
- 속도가 증가할수록 두 함수의 차이가 커진다.
- 저속에서는 두 함수가 거의 일치한다.
""")

# -----------------------------
# 탐구 결과
# -----------------------------
st.write("## 👨‍🔬 탐구 결론")

st.success("""
고전적 도플러 공식은 저속에서는 충분히 정확하지만,
빛의 속도에 가까워질수록 상대론적 도플러 공식을 사용해야 한다.
이를 통해 하나의 물리 현상도 상황에 따라
다른 수학적 모델을 사용한다는 점을 확인하였다.
""")
