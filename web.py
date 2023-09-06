import streamlit as st
import base64

# Định nghĩa giao diện người dùng
st.title("Get link Redbubble")
uploaded_file = st.file_uploader("Chọn tệp txt chứa danh sách link Redbubble", type=["txt"])

if uploaded_file:
    st.markdown("### Kết quả sau khi chuyển đổi:")
    links = uploaded_file.read().decode("utf-8").split("\n")
    converted_links = []
    for link in links:
        converted_link = link.strip().replace('507x507', '2000x2000').replace('600x600', '2000x2000')
        converted_links.append(converted_link)

    # Hiển thị các link đã chuyển đổi
    # st.text("\n".join(converted_links))

    # Tạo tệp txt chứa các link đã chuyển đổi
    txt_data = "\n".join(converted_links)

    # Tạo nút "Tải xuống" để tải xuống tệp txt
    download_link = f'<a href="data:file/txt;base64,{base64.b64encode(txt_data.encode()).decode()}" download="links.txt"><button>Tải xuống</button></a>'
    st.markdown(download_link, unsafe_allow_html=True)
