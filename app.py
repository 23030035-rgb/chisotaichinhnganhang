import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Ứng dụng tính chỉ số tài chính ngân hàng",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Ứng dụng tính các chỉ số tài chính ngân hàng - ĐỀ TÀI 4")

st.markdown("### Nhập dữ liệu")

LNST = st.number_input("Lợi nhuận sau thuế (triệu đồng)", min_value=0.0)

TTTDK = st.number_input("Tổng tài sản đầu kỳ (triệu đồng)", min_value=0.0)
TTTCK = st.number_input("Tổng tài sản cuối kỳ (triệu đồng)", min_value=0.0)

VCSHDK = st.number_input("Vốn CSH đầu kỳ (triệu đồng)", min_value=0.0)
VCSHCK = st.number_input("Vốn CSH cuối kỳ (triệu đồng)", min_value=0.0)

TNL = st.number_input("Thu nhập lãi (triệu đồng)", min_value=0.0)
CPL = st.number_input("Chi phí lãi (triệu đồng)", min_value=0.0)
TSSLBQ = st.number_input("Tài sản sinh lãi bình quân (triệu đồng)", min_value=0.0)

TDN = st.number_input("Tổng dư nợ (triệu đồng)", min_value=0.0)

DNN1 = st.number_input("Dư nợ nhóm 1 (triệu đồng)", min_value=0.0)
DNN2 = st.number_input("Dư nợ nhóm 2 (triệu đồng)", min_value=0.0)
DNN3 = st.number_input("Dư nợ nhóm 3 (triệu đồng)", min_value=0.0)
DNN4 = st.number_input("Dư nợ nhóm 4 (triệu đồng)", min_value=0.0)
DNN5 = st.number_input("Dư nợ nhóm 5 (triệu đồng)", min_value=0.0)

DPRRTD = st.number_input("Dự phòng rủi ro tín dụng (triệu đồng)", min_value=0.0)

TGKKH = st.number_input("Tiền gửi không kỳ hạn (triệu đồng)", min_value=0.0)
TTGKH = st.number_input("Tổng tiền gửi khách hàng (triệu đồng)", min_value=0.0)

if st.button("📊 Tính toán"):

    # ROA
    TTSBQ = (TTTDK + TTTCK) / 2

    if TTSBQ != 0:
        ROA = (LNST / TTSBQ) * 100
        st.write("### Kết quả")
        st.success(f"ROA = {ROA:.2f}%")
    else:
        st.error("Không thể tính ROA.")

    # ROE
    VCSHBQ = (VCSHDK + VCSHCK) / 2

    if VCSHBQ != 0:
        ROE = (LNST / VCSHBQ) * 100
        st.success(f"ROE = {ROE:.2f}%")
    else:
        st.error("Không thể tính ROE.")

    # NIM
    TNLT = TNL - CPL

    if TSSLBQ != 0:
        NIM = (TNLT / TSSLBQ) * 100
        st.success(f"NIM = {NIM:.2f}%")
    else:
        st.error("Không thể tính NIM.")

    # Nợ xấu
    NX = DNN3 + DNN4 + DNN5
    st.success(f"Nợ xấu = {NX:,.2f} triệu đồng")

    if TDN != 0:
        TLNX = (NX / TDN) * 100
        st.success(f"Tỷ lệ nợ xấu = {TLNX:.2f}%")
    else:
        st.error("Không thể tính tỷ lệ nợ xấu.")

    # Nợ quá hạn
    NQH = DNN2 + DNN3 + DNN4 + DNN5
    st.success(f"Nợ quá hạn = {NQH:,.2f} triệu đồng")

    if TDN != 0:
        TLNQH = (NQH / TDN) * 100
        st.success(f"Tỷ lệ nợ quá hạn = {TLNQH:.2f}%")
    else:
        st.error("Không thể tính tỷ lệ nợ quá hạn.")

    # Bao phủ nợ xấu
    if NX != 0:
        BPNX = (DPRRTD / NX) * 100
        st.success(f"Bao phủ nợ xấu = {BPNX:.2f}%")
    else:
        st.error("Không thể tính Bao phủ nợ xấu.")

    # CASA
    if TTGKH != 0:
        CASA = (TGKKH / TTGKH) * 100
        st.success(f"CASA = {CASA:.2f}%")
    else:
        st.error("Không thể tính CASA.")
