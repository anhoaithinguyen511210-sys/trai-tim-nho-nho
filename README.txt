TRÁI TIM VÀ THƠ CỦA TÔI — HƯỚNG DẪN ĐĂNG LÊN RENDER

CÁC FILE
- app.py: mã trang web
- requirements.txt: thư viện cần cài
- Procfile: lệnh khởi động trên Render

LƯU Ý
- Bài thơ hiện đang để trống theo yêu cầu.
- Khi bạn gửi bài thơ, hãy thêm nội dung vào biến POEM trong app.py.
- Trang này chỉ hiển thị bài thơ; khách truy cập không thể tự sửa nội dung.
- Khi cập nhật file app.py trên GitHub, Render sẽ triển khai lại nếu bật tự động deploy.

CÁCH ĐƯA LÊN GITHUB BẰNG TRÌNH DUYỆT
1. Đăng nhập https://github.com/
2. Tạo repository mới, ví dụ: trai-tim-tho
3. Chọn Add file > Upload files.
4. Tải lên cả app.py, requirements.txt và Procfile.
5. Nhấn Commit changes.

CÁCH ĐƯA LÊN RENDER
1. Mở https://render.com/ và đăng nhập.
2. Chọn New > Web Service.
3. Kết nối GitHub, chọn repository trai-tim-tho.
4. Đặt:
   - Runtime/Language: Python (nếu được hỏi)
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app
5. Chọn gói phù hợp, sau đó chọn Create Web Service.
6. Chờ trạng thái triển khai thành công.
7. Mở URL .onrender.com được Render cấp và gửi link đó cho người khác.

NẾU CẦN CẬP NHẬT THƠ
Sửa biến POEM trong app.py. Ví dụ:
POEM = """Dòng thơ thứ nhất
Dòng thơ thứ hai

Dòng thơ tiếp theo"""
Sau đó tải bản app.py mới lên GitHub và Commit changes. Render sẽ triển khai lại.
