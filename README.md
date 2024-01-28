<div align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" target="_blank">
    <img src="https://www.uit.edu.vn/sites/vi/files/banner_uit_15.png">
  </a>
</div>

#
![Language](https://img.shields.io/badge/python%203.11-%23FFF.svg?style=for-the-badge&logo=python)
=======
</p>
<h1 align="center"><b>Đồ án cuối kỳ môn Máy học - CS114.O11</b></h1>
<h2 align="center"><b>BÀI TOÁN NHẬN DẠNG CẢM XÚC
 </br></h2>

# Thông tin Môn học
<table>
  <tr><th>Môn Học     </th><td>Máy học (Machine Learning)</td></tr>
  <tr><th>Lớp         </th><td>CS114.O11                 </td></tr>
  <tr><th>GV Lý Thuyết</th><td>PGS.TS Lê Đình Duy        </td></tr>
  <tr><th>GV Lý Thuyết</th><td>ThS. Phạm Nguyễn Trường An</td></tr>
</table>

# Thông tin Thành viên
| MSSV       | Họ và Tên          | Email                   | Github                                                                                                                      |
| ---------- | ------------------ | ----------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `22521145` | Trương Lê Vĩnh Phúc| 222521145@gm.uit.edu.vn | [![](https://img.shields.io/badge/sloweyyy-%2324292f.svg?style=flat-square&logo=github      )](https://github.com/sloweyyy) |
| `22521467` | Lê Thành Tiến| 22521467@gm.uit.edu.vn | [![](https://img.shields.io/badge/ostic71-%2324292f.svg?style=flat-square&logo=github      )](https://github.com/ostic71) |


</p>



# **BẢNG MỤC LỤC**
1. [Tổng Quan Về Đồ Án](#1-mô-tả-bài-toán)
2. [Mô Tả Bộ Dữ Liệu](#2-mô-tả-bộ-dữ-liệu)
3. [Mô Tả Về Đặc Trưng](#3-mô-tả-về-đặc-trưng)
4. [Mô Tả Thuật Toán Máy Học](#4-mô-tả-thuật-toán-máy-học)
5. [Cài Đặt, Tinh Chỉnh Thông Số](#5-cài-đặt-tinh-chỉnh-thông-số)
6. [Kết Quả và Kết Luận](#6-đánh-giá-kết-quả-kết-luận)

# 1. Mô tả bài toán

## 1.1. Ngữ cảnh ứng dụng
  * Nếu trở lại 10 năm trước, thì một tấm ảnh chỉ có nhiệm vụ đơn thuần là lưu giữ lại một khoảnh khắc. Trong thời đại 4.0 ngày nay, mọi thứ dần trở nên số hóa (từ quản lý thông tin, bán háng, thu thập dữ liệu,...). Ảnh đã trở thành một trong những phương tiện giao tiếp, thu thập dữ liệu quan trọng và ngày càng phổ biến. Nhóm quyết định dùng ảnh chân dung con người để xây dựng một mô hình máy học phân loại thành nhiều cảm xúc khác nhau. Ý tưởng trên có thể ứng dụng vào việc phân tích cảm xúc của người mua hàng, phân tích cảm xúc của bệnh nhân tâm thần.
  
  * Dữ liệu được thu thập từ các nguồn: google, bing, unsplash.com, freepik.com
  * Đối tượng sử dụng là những cơ sở bán hàng thông qua các ứng dụng họp trực tuyến (zoom, google meet,....), bệnh viện tâm thần.

## 1.2. INPUT và OUTPUT Bài toán
 -	Input: Ảnh chứa mặt của 01 người
-	Output: Ảnh cắt mặt và mô tả cảm xúc

# 2. Mô tả Bộ Dữ Liệu
## 2.1. Thu thập dữ liệu
### 2.1.1. Cách thức thu thập dữ liệu


  - Tìm kiếm các keywords của cảm xúc liên quan (angry face humman, happy face,....) trên các trang web google, bing, unsplash.com, freepik.com,...
  - Sử dụng extension của trình duyệt google Chrome (Download All Images) để tải về tất cả các ảnh có trong trang.
  ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/main/material/1.png?raw=true)
  * Giải nén folder vừa tải về và xóa bớt các bức ảnh sai chủ đề.
  ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/main/material/2.png?raw=true)
### 2.1.2. Khó khăn trong việc thu thập dữ liệu
-	Khi sử dụng nhiều trang để tìm kiếm cùng một loại cảm xúc, nhiều trang có các tấm ảnh giống nhau.
-	Một tấm ảnh có thể tìm thấy ở 2 cảm xúc khác nhau (VD: fear và neutral).
-	Nhiều tấm ảnh không liên quan xuất hiện chung trang, gây mất thời gian phân loại.

## 2.2. Số lượng, độ đa dạng
Sau 10 lần thu thập data đầu tiên, có tất cả 5000 ảnh, thuộc vào 5 class. Mỗi class có 1000 ảnh. 
ID | Tên cảm xúc | Số lượng |   Hình ảnh | 
--- | --- | -- | -- |
0 | Angry | 1000 | ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/main/images/angry/angry%20(1).jpg?raw=true "") | 
1 | Fear | 1000 |  ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/main/images/fear/fear%20(128).jpg?raw=true "") | 
2 | Happy | 1000 |  ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/main/images/happy/happy%20(1).png?raw=true "") | 
3 | Neutral | 1000 | ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/main/images/neutral/neutral%20(8).jpg?raw=true "") | 
4 | Sad | 1000 | ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/main/images/sad/sad%20(1).jpg?raw=true "") | 

## 2.3. Các thao tác tiền xử lý dữ liệu
-	Lọc ảnh trùng
-	Xoá các ảnh không phải ảnh người thật
-	Xoá các ảnh khó phân biệt với cảm xúc khác
## 2.4. Phân chia dữ liệu
-	Sau khi label và lọc ảnh, còn lại 5000 ảnh. Tiến hành chia train/val với tỉ lệ 8/2:
    - Train: 4000 ảnh.
    - Validate: 1000 ảnh.
# 3.	Mô tả về đặc trưng
## 3.1.	Feature Engineering
-	Sử dụng Dlib để phát hiện khuôn mặt
-	Cắt ảnh chỉ giữ lại vùng xung quanh khuôn mặt
-	Resize ảnh về 48x48 pixel.
## 3.2.	Data Processing Pipeline
-	Chuyển ảnh thành ma trận pixel kích thước 48x48 pixel
-	Ghi ma trận vào file csv cùng với ID của label

# 4.	Mô tả thuật toán máy học
## 4.1.	Tổng quan thuật toán SVM (Support vector machine)
-	Support Vector Machines (có tài liệu dịch là Máy véctơ hỗ trợ) là một trong số những thuật toán phổ biến và được sử dụng nhiều nhất trong học máy trước khi mạng nơ ron nhân tạo trở lại với các mô hình deep learning. Nó được biết đến rộng rãi ngay từ khi mới được phát triển vào những năm 1990.

-	Mục tiêu của SVM là tìm ra một siêu phẳng trong không gian N chiều (ứng với N đặc trưng) chia dữ liệu thành hai phần tương ứng với lớp của chúng. Nói theo ngôn ngữ của đại số tuyển tính, siêu phẳng này phải có lề cực đại và phân chia hai bao lồi và cách đều chúng.
<p align ="middle">
<img src = "https://github.com/sloweyyy/CS114.O11-FinalProject/blob/main/material/3.webp?raw=true" height='400' width='400' />
</p>

## 4.2.	Nguyên lý hoạt động
-	Trong không gian N chiều, một siêu phẳng là một không gian con có kích thước N-1 chiều. Một cách trực quan, trong một mặt phẳng (2 chiều) thì siêu phẳng là một đường thẳng, trong một không gian 3 chiều thì siêu phẳng là một mặt phẳng. Để phân chia hai lớp dữ liệu, rõ ràng là có rất nhiều siêu phẳng có thể làm được điều này. Mặc dù vậy, mục tiêu của chúng ta là tìm ra siêu phẳng có lề rộng nhất tức là có khoảng cách tới các điểm của hai lớp là lớn nhất. Hình dưới đây là một ví dụ trực quan về điều đó.

<p align ="middle">
<img src = "https://github.com/sloweyyy/CS114.O11-FinalProject/blob/main/material/5.gif?raw=true" height='600' width='800' />
</p>

- Để phân chia hai lớp dữ liệu, rõ ràng là có rất nhiều siêu phẳng có thể làm được điều này. Mặc dù vậy, mục tiêu của chúng ta là tìm ra siêu phẳng có lề rộng nhất tức là có khoảng cách tới các điểm của hai lớp là lớn nhất. Hình dưới đây là một ví dụ trực quan về điều đó.

<p align ="middle">
<img src = "https://github.com/sloweyyy/CS114.O11-FinalProject/blob/main/material/6.jpeg?raw=true" height='400' width='800' />
</p>

# 5.	Cài đặt, tinh chỉnh thông số
## 5.1.	Tham số C
-	C là tham số đối với biên mềm trong mô hình SVM. Nó kiểm soát sự đồng nhất của biên quyết định.
-	Giá trị C lớn sẽ tạo ra một biên quyết định chặt chẽ, có thể dẫn đến việc mô hình không tổng quát hoá tốt (overfitting).
-	Giá trị C nhỏ hơn sẽ tạo ra một biên mềm, cho phép mô hình tổng quát hoá tốt hơn nhưng có thể không xác định các điểm nhiễu. 
## 5.2.	Tham số Gamma
-	Gamma đặc trưng mức độ ảnh hưởng của một điểm dữ liệu đến việc tạo ra biên quyết định. Giá trị gamma càng cao, mức độ ảnh hưởng càng giảm.
-	Đối với kernel “rbf”, “poly”, và “sigmoid”, gamma quyết định hình dạng của siêu phẳng quyết định.
## 5.3. Tham số kernel
-	Kernel quyết định loại hàm nhân được sử dụng trong SVM để biến đổi không gian dữ liệu. Các giá trị phổ biến cho kernel là “linear”, “rbf” (Radial Basis Function), “poly” (Polynomial), và “sigmoid”.

# 6. Đánh giá kết quả, kết luận
## 6.1. Đánh giá kết quả
Sau khi thực hiện train model, để xác định model của chúng ta có đủ tốt hay chưa cũng như đảm bảo khả năng nhận diện trong tương lai ta cần có một phương pháp đánh giá với tiêu chí cụ thể. Đối với bài toán Classification, model thường được đánh giá dựa trên Precission, Recall,  F1-score.

| Class | Tên cảm xúc | Precision | Recall | F1-Score |
| ----- | ------------ | --------- | ------ | -------- |
| 0     | Angry        | 0.5561    | 0.5278 | 0.5416   |
| 1     | Fear         | 0.5251    | 0.4947 | 0.5095   |
| 2     | Happy        | 0.7767    | 0.8333 | 0.8040   |
| 3     | Neutral      | 0.8191    | 0.7762 | 0.7971   |
| 4     | Sad          | 0.4692    | 0.5156 | 0.4913   |

## 6.2 Kết luận
-	Mô hình có hiệu suất khá tốt trong việc nhận diện cảm xúc “Happpy” và “Neutral”, với các độ đo hiệu suất đều ở mức cao.
-	Cần cải thiện thêm hiệu suất cho các cảm xúc “Angry”, “Sad” và “Fear” để đảm bảo hiệu suất giữa các lớp.

## 7. Hướng phát triển trong tương lai

*	Hệ thống sẽ trả về thông tin phân loại trực tiếp trên video, không chỉ ảnh.
*	Việc phân loại cần yếu tố thời gian, do đó yêu cầu thiết bị có cấu hình mạnh. Nhưng đa phần các loại điện thoại di động bây giờ không được thiết kế để thực hiện tác vụ này. Chúng em sẽ triển khai model lên web, người dùng sẽ giao tiếp với hệ thống thông qua web. Khi đó ta chỉ cần quan tâm tới tốc độ mạng (Vấn đề về mạng thì dễ giải quyết hơn).
*	Hướng phát triển tiếp theo là kết hợp model này với Zoom, Google Meet, vì được sử dụng rộng rãi hiện nay ở Việt Nam cho nhiều mục đích.


