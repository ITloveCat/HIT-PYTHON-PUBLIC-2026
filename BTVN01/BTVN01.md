## Bài 1: Python là ngôn ngữ thông dịch hay biên dịch?

Python thường được gọi là **ngôn ngữ thông dịch**, nhưng thực chất quy trình hoạt động của nó là sự kết hợp của cả hai quá trình: **biên dịch (compilation)** và **thông dịch (interpretation)**.

**Tại sao lại như vậy?**

* **Bước 1 (Biên dịch ngầm):** Khi bạn chạy một file code Python (đuôi `.py`), mã nguồn không chạy trực tiếp ngay lập tức. Cốt lõi của Python (thường là CPython) sẽ tự động biên dịch mã nguồn của bạn thành một dạng mã trung gian gọi là **Bytecode** (các file đuôi `.pyc`).
* **Bước 2 (Thông dịch):** Mã Bytecode này sau đó sẽ được đưa vào Máy ảo Python (Python Virtual Machine - PVM). Lúc này, PVM đóng vai trò là một trình thông dịch, đọc hiểu Bytecode và dịch nó thành mã máy (machine code) để máy tính chạy từng dòng một.

Vì quá trình biên dịch diễn ra hoàn toàn ngầm đằng sau, lập trình viên không cần gõ lệnh build/compile thủ công như các ngôn ngữ C++ hay Java, nên về mặt ứng dụng thực tế, Python được xếp vào nhóm ngôn ngữ thông dịch.

---

## Bài 2: Liệt kê các thành phần cơ bản trong Python

### Các kiểu dữ liệu cơ bản

* **Số nguyên (Integer):** `int` (Ví dụ: 10, -5, 0).
* **Số thực (Float):** `float` (Ví dụ: 3.14, -2.5).
* **Số phức (Complex):** `complex` (Ví dụ: 2+3j).
* **Chuỗi ký tự (String):** `str` (Ví dụ: "Hello", 'Python').
* **Logic (Boolean):** `bool` (Chứa hai giá trị `True` hoặc `False`).
* **Danh sách (List):** `list` (Tập hợp các phần tử có thứ tự, có thể thay đổi dữ liệu).
* **Danh sách cố định (Tuple):** `tuple` (Tập hợp các phần tử có thứ tự, không thể thay đổi dữ liệu).
* **Tập hợp (Set):** `set` (Tập hợp các phần tử duy nhất, không có thứ tự).
* **Từ điển (Dictionary):** `dict` (Lưu trữ dữ liệu theo cặp Khóa - Giá trị / Key - Value).
* **Kiểu rỗng:** `NoneType` (Đại diện cho giá trị rỗng `None`).

### Các toán tử trong Python

| Nhóm Toán Tử | Các ký hiệu | Chức năng |
| --- | --- | --- |
| **Toán học** | `+`, `-`, `*`, `/`, `//` (chia lấy phần nguyên), `%` (chia lấy phần dư), `**` (lũy thừa) | Thực hiện các phép tính số học cơ bản |
| **So sánh** | `==`, `!=`, `>`, `<`, `>=`, `<=` | So sánh hai giá trị và trả về True/False |
| **Logic** | `and`, `or`, `not` | Kết nối các biểu thức điều kiện với nhau |
| **Gán** | `=`, `+=`, `-=`, `*=`, `/=`... | Gán hoặc cập nhật giá trị cho biến |
| **Thành viên** | `in`, `not in` | Kiểm tra một phần tử có nằm trong một tập hợp hay không |
| **Định danh** | `is`, `is not` | Kiểm tra hai biến có trỏ về cùng một vùng nhớ gốc hay không |

### Mệnh đề điều kiện và Vòng lặp

* **Mệnh đề điều kiện:** Sử dụng các từ khóa **`if`**, **`elif`** (viết tắt của else if), và **`else`** để thiết lập các nhánh logic. Khối lệnh bên dưới sẽ chỉ chạy khi điều kiện là đúng.
* **Vòng lặp `for`:** Dùng để duyệt qua các phần tử của một tập hợp đã biết trước (như list, tuple, dictionary, chuỗi ký tự) hoặc dùng chung với hàm `range()` để lặp theo số lần cụ thể.
* **Vòng lặp `while`:** Vòng lặp sẽ chạy liên tục không ngừng nghỉ miễn là biểu thức điều kiện đi kèm vẫn còn đúng.
* **Lệnh điều khiển lặp:** **`break`** (thoát hoàn toàn vòng lặp), **`continue`** (bỏ qua vòng hiện tại để nhảy sang vòng tiếp theo), **`pass`** (lệnh giữ chỗ trống, không thực hiện hành động nào).

### Kiểu dữ liệu True, False

* Đây là kiểu dữ liệu logic có tên gọi chính thức là **Boolean** (`bool`).
* Khác với một số ngôn ngữ khác, trong Python, giá trị **`True`** (Đúng) và **`False`** (Sai) bắt buộc phải viết hoa chữ cái đầu tiên (`T` và `F`). Nếu viết `true` hay `false`, Python sẽ báo lỗi không nhận diện được biến.
* Khi tính toán toán học, Python ngầm quy ước `True` có giá trị tương đương với số `1`, và `False` có giá trị tương đương với số `0`.