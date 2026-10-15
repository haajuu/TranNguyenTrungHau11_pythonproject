import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Ho_ten": [
        "Nguyễn Văn An",
        "Trần Thị Bích",
        "Lê Hoàng Cường",
        "Phạm Thị Dung",
        "Hoàng Văn Em",
        "Đỗ Thị Phương",
        "Bùi Văn Giang",
        "Vũ Thị Hương",
        "Ngô Văn Khải",
        "Phan Thị Lan"
    ],
    "Chuyen_can": [9.0, 8.0, 7.5, 6.0, 8.5, 9.5, 4.0, 7.0, 8.0, 5.5],
    "Giua_ky": [8.0, 7.5, 6.5, 5.0, 7.0, 9.0, 4.5, 6.5, 8.5, 6.0],
    "Cuoi_ky": [8.5, 8.0, 7.0, 5.5, 7.5, 8.5, 3.5, 6.5, 9.0, 5.0]
}

df = pd.DataFrame(data)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("Bảng dữ liệu ban đầu")
st.dataframe(df, use_container_width=True)

df["Tong_ket"] = (
    0.2 * df["Chuyen_can"] + 0.3 * df["Giua_ky"] + 0.5 * df["Cuoi_ky"]
).round(2)

st.subheader("Bảng dữ liệu sau khi tính tổng kết")
st.dataframe(df, use_container_width=True)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

st.subheader("Bảng dữ liệu sau khi xếp loại")
st.dataframe(df, use_container_width=True)

dtb_lop = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_sinh_vien_dat = (df["Tong_ket"] >= 5.0).sum()

st.subheader("Thống kê kết quả học tập lớp học")
st.write(f"- Điểm tổng kết trung bình của lớp: {dtb_lop:.2f}")
st.write(f"- Sinh viên có điểm tổng kết cao nhất: {sv_max['Ho_ten']} ({sv_max['Tong_ket']} điểm)")
st.write(f"- Sinh viên có điểm tổng kết thấp nhất: {sv_min['Ho_ten']} ({sv_min['Tong_ket']} điểm)")
st.write(f"- Số sinh viên đạt (điểm tổng kết >= 5.0): {so_sinh_vien_dat}")

st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"], color="skyblue", edgecolor="black")
ax.set_xlabel("Họ và tên sinh viên", fontsize=12)
ax.set_ylabel("Điểm tổng kết", fontsize=12)
ax.set_title(
    "Biểu đồ cột thể hiện điểm tổng kết của 10 sinh viên",
    fontsize=14,
    fontweight="bold"
)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig)

st.markdown("---")
st.markdown("<p style='text-align: center;'>Người thực hiện: Trần Nguyễn Trung Hậu</p>", unsafe_allow_html=True)
