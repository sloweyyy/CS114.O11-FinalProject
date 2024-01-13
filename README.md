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
<h2 align="center"><b>BÀI TOÁN PHÂN LOẠI CẢM XÚC
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
1. [Tổng Quan Về Đồ Án](#tongquan)
2. [Xây Dựng Bộ Dữ Liệu](#dulieu)
3. [Training Và Đánh Giá Model](#training)
4. [Hướng Phát Triển Và Cải Tiến](#ungdung)

<a name="tongquan"></a>
# **2. Tổng Quan Về Đồ Án**

## **2.1. Ngữ cảnh ứng dụng**
  * Nếu trở lại 10 năm trước, thì một tấm ảnh chỉ có nhiệm vụ đơn thuần là lưu giữ lại một khoảnh khắc. Trong thời đại 4.0 ngày nay, mọi thứ dần trở nên số hóa (từ quản lý thông tin, bán háng, thu thập dữ liệu,...). Ảnh đã trở thành một trong những phương tiện giao tiếp, thu thập dữ liệu quan trọng và ngày càng phổ biến. Nhóm quyết định dùng ảnh chân dung con người để xây dựng một mô hình máy học phân loại thành nhiều cảm xúc khác nhau. Ý tưởng trên có thể ứng dụng vào việc phân tích cảm xúc của người mua hàng, phân tích cảm xúc của bệnh nhân tâm thần.
  
  * Dữ liệu được thu thập từ các nguồn: google, bing, unsplash.com, freepik.com
  * Đối tượng sử dụng là những cơ sở bán hàng thông qua các ứng dụng họp trực tuyến (zoom, google meet,....), bệnh viện tâm thần.

## **2.2. INPUT và OUTPUT Bài toán**
  * INPUT: 
    * Ảnh chân dung của một người.
    
  * OUTPUT: 
    * Ảnh và mô tả cảm xúc.

      
      


<a name="dulieu"></a>
# **3.Xây Dựng Bộ Dữ Liệu**
## **3.1. Thu thập dữ liệu**
### **3.1.1. Thông tin thu thập dữ liệu**


*	Cách thức thu thập: 
  * Tìm kiếm các keywords của cảm xúc liên quan (angry face humman, happy face,....) trên các trang web google, bing, unsplash.com, freepik.com,...
  * Sử dụng extension của trình duyệt google Chrome (Download All Images) để tải về tất cả các ảnh có trong trang.
  ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/ver112024/material/1.png?raw=true)
  * Giải nén folder vừa tải về và xóa bớt các bức ảnh sai chủ đề.
  ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/ver112024/material/2.png?raw=true)


### **3.1.2. Kết quả thu thập dữ liệu**
Sau 2 lần thu thập data đầu tiên, có tất cả 6500 ảnh, thuộc vào 5 class. Mỗi class có 1300 ảnh. 
ID | Tên cảm xúc | Số lượng |   Hình ảnh | 
--- | --- | -- | -- |
0 | Angry | 1300 | ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/ver112024/images/angry/image0001765.jpg?raw=true "") | 
1 | Fear | 1300 |  ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/ver112024/images/fear/image0000473.jpg?raw=true "") | 
2 | Happy | 1300 |  ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/ver112024/images/happy/ffhq_1003.png?raw=true "") | 
3 | Neutral | 1300 | ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/ver112024/images/neutral/ffhq_1003.png?raw=true "") | 
4 | Sad | 1300 | ![](https://github.com/sloweyyy/CS114.O11-FinalProject/blob/ver112024/images/sad/image0000073.jpg?raw=true "") | 

### **3.1.3. Khó khăn của việc thu thập dữ liệu**
* Khi sử dụng nhiều trang để tìm kiếm cùng một loại cảm xúc, nhiều trang có các tấm ảnh giống nhau.
* Một tấm ảnh có thể tìm thấy ở 2 cảm xúc khác nhau (VD: fear và neutral).
* Nhiều tấm ảnh không liên quan xuất hiện chung trang, gây mất thời gian phân loại.



## **3.2. Xử lý dữ liệu**

### **3.2.1. Chia tập train/val**

* Sau khi label và lọc ảnh, còn lại 6500 ảnh. Tiến hành chia train/val với tỉ lệ 8/2:
    * Train: 5200 ảnh. 
    * Val: 1300 ảnh.


# **4. Training Và Đánh Giá Model**
## **4.1. Tổng quan SVM (SUPORT VECTOR MACHINE)**
### **4.1.1. Tổng quát**
  * Support Vector Machines (có tài liệu dịch là Máy véctơ hỗ trợ) là một trong số những thuật toán phổ biến và được sử dụng nhiều nhất trong học máy trước khi mạng nơ ron nhân tạo trở lại với các mô hình deep learning. Nó được biết đến rộng rãi ngay từ khi mới được phát triển vào những năm 1990.

  * Mục tiêu của SVM là tìm ra một siêu phẳng trong không gian N chiều (ứng với N đặc trưng) chia dữ liệu thành hai phần tương ứng với lớp của chúng. Nói theo ngôn ngữ của đại số tuyển tính, siêu phẳng này phải có lề cực đại và phân chia hai bao lồi và cách đều chúng.
<p align ="middle">
<img src = "https://github.com/sloweyyy/CS114.O11-FinalProject/blob/ver112024/material/3.webp?raw=true" height='400' width='400' />
</p>

### **4.1.2. Nguyên lý hoạt động**
  * Trong không gian N chiều, một siêu phẳng là một không gian con có kích thước N-1 chiều. Một cách trực quan, trong một mặt phẳng (2 chiều) thì siêu phẳng là một đường thẳng, trong một không gian 3 chiều thì siêu phẳng là một mặt phẳng. Để phân chia hai lớp dữ liệu, rõ ràng là có rất nhiều siêu phẳng có thể làm được điều này. Mặc dù vậy, mục tiêu của chúng ta là tìm ra siêu phẳng có lề rộng nhất tức là có khoảng cách tới các điểm của hai lớp là lớn nhất. Hình dưới đây là một ví dụ trực quan về điều đó.

<p align ="middle">
<img src = "https://github.com/sloweyyy/CS114.O11-FinalProject/blob/ver112024/material/5.gif?raw=true" height='600' width='800' />
</p>

  * Để phân chia hai lớp dữ liệu, rõ ràng là có rất nhiều siêu phẳng có thể làm được điều này. Mặc dù vậy, mục tiêu của chúng ta là tìm ra siêu phẳng có lề rộng nhất tức là có khoảng cách tới các điểm của hai lớp là lớn nhất. Hình dưới đây là một ví dụ trực quan về điều đó.

<p align ="middle">
<img src = "https://github.com/sloweyyy/CS114.O11-FinalProject/blob/ver112024/material/6.jpeg?raw=true" height='400' width='800' />
</p>

## **4.1. Đánh giá mô hình**

Sau khi thực hiện train model, để xác định model của chúng ta có đủ tốt hay chưa cũng như đảm bảo khả năng nhận diện trong tương lai ta cần có một phương pháp đánh giá với tiêu chí cụ thể. Đối với bài toán Classification, model thường được đánh giá dựa trên Precission, Recall,  F1-score.

Class | Tên cảm xúc | Precission |   Recall |  F1-Score|
--- | --- | -- | -- |-- |
0 | angry | 0.4795 | 0.5474 | 0.5111 |
1 | fear | 0.4783 | 0.4074 | 0.4400 |
2 | sad | 0.4320 | 0.4635 | 0.4472 |
3 | neutral | 0.8090 | 0.8385 | 0.8235|
4 | happy | 0.8608 | 0.7952 | 0.8267 |


## **5.2. Hướng phát triển trong tương lai**

*	Hệ thống sẽ trả về thông tin phân loại trực tiếp trên video, không chỉ ảnh.
*	Việc phân loại cần yếu tố thời gian, do đó yêu cầu thiết bị có cấu hình mạnh. Nhưng đa phần các loại điện thoại di động bây giờ không được thiết kế để thực hiện tác vụ này. Chúng em sẽ triển khai model lên web, người dùng sẽ giao tiếp với hệ thống thông qua web. Khi đó ta chỉ cần quan tâm tới tốc độ mạng (Vấn đề về mạng thì dễ giải quyết hơn).
*	Hướng phát triển tiếp theo là kết hợp model này với Zoom, Google Meet, vì được sử dụng rộng rãi hiện nay ở Việt Nam cho nhiều mục đích.


