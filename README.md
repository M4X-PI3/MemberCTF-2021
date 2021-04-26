# MemberCTF-2021 RE
# 1> Meme
* ![image](https://user-images.githubusercontent.com/83124718/116029031-9b83d680-a682-11eb-9eb6-8549b13cd379.png)
* Meme.exe, Win32 EXE file
* Đưa chương trình vào IDA 32 xem có gì nào???
* ![image](https://user-images.githubusercontent.com/83124718/116029230-ffa69a80-a682-11eb-9996-5c70a850b2f6.png)
* Khá đơn giản cho flag đầu tiên của CTF này. hahaha
* **Flag: MemberCTF{W3lc0me-t0-rev3rse}**

# 2> ASM1
* asm.s, thử mở ra với text editor xem sao?
* ![image](https://user-images.githubusercontent.com/83124718/116029386-6d52c680-a683-11eb-8e63-94fc7d42497c.png)
* Một đoạn assembly code, push một đống data vào stack rồi in ra màn hình giá trị trên stack.
* Mình thử bỏ đống data này và chuyển sang dạng ascii để xem đống data này là gì?
* ![image](https://user-images.githubusercontent.com/83124718/116029582-d8040200-a683-11eb-8439-144d32c578b0.png)
* Vì data IO trên stack theo dạng FILO thông tin in ra màn hình khi chạy code sẽ là đảo ngược của đoạn text trên.
* Và đây là flag
* **Flag: MemberCTF{W3lc0me-t0-NASM}**
 
# 3> ASM2
* asm2.s tương tự với ASM1, là một đoạn code assembly.
* Để giải challenge này bạn cần hiểu một chút về cách ghi giá trị trên register.
* Trong đoạn code này có 2 flag là 'flag' và 'FakeFlag'.
* Mình sẽ bỏ qua phần in thông tin phụ ra màn hình và đoạn kiểm tra ký tự trong flag
* ![image](https://user-images.githubusercontent.com/83124718/116030091-00403080-a685-11eb-92ff-e63dde07e199.png)
* Đoạn này code sẽ skip các ký tự đầu và đọc flag từ ký tự 16 (là đoạn: 0x19923) và FakeFlag từ ký tự 12 (là đoạn: 0x41520)
* ![image](https://user-images.githubusercontent.com/83124718/116030256-5ca35000-a685-11eb-8640-898624869db1.png)
* Và đây là món chình của challenge này.
* move dl (với edx là byte[ebx]) vào eax. dl là một đoạn data 8 bit (1byte - 1 ký tự) sẽ được mov vào al của eax.
* Như vậy sau khi thực hiện xong loop edit, giá trị của flag sẽ là 'M0d1fY_t3xt_!!__0x41520'
* Và đây là flag của challenge này.
* **Flag: MemberCTF{M0d1fY_t3xt_!!__0x41520}**

# 4> ASM4
* asm4.s tương tự như 2 chal trên, đây cũng là 1 code assembly.
* Mình sẽ skip qua đoạn in text ra màn hình và lấy input.
* .atoi là đoạn chương trình phân tách số input (ascii) chuyển thành dạng số nguyên (int) để tính toán.
* .cal là đoạn tính toán cộng dồn eax (số nguyên đã được chuyển đổi) với ecx là giá trị giảm dần (index của loop).
* Sau .cal eax sẽ lưu giá trị cộng dồn 1+2+3+..+n với n là số user nhập.
* .cal2, đoạn tính toán và chuyển ngược kết quả từ int ra dạng ascii để in ra console.
* Như vậy kết quả của chương trình này là tổng 1+2+3+..+n với n là số user nhập
* Với input là 123 -> kết quả là (123+1)*123/2 = 7626
* Và đây là flag của challlenge này.
* Flag: MemberCTF{0xCA}

# 5> Pascal
* Xor_easy.pas
* Một đoạn chương trình pascal
* ![image](https://user-images.githubusercontent.com/83124718/116031947-f6b8c780-a688-11eb-9759-147e2f47ffc0.png)
* Trong chương trình này, các giá trị trong arr sẽ lần lượt được xor với key để lấy ra được giá trị cuối là flag.
* Với hàm Xor, a xor b = c --> a xor c = b --> b xor c = a
* Ở đây flag có format bắt đầu là MemberCTF{ với 10 ký tự, mình thử xor với 10 ký tự đầu trong array.
* M xor 86 = 27
* e xor 126 = 27
* m xor 118 = 27
* Như vậy key là 27.
* Thực hiện xor cho toàn bộ ký tự trong arr để ra được flag
* Để xor các bạn có thể dùng tool online, mình có viết 1 đoạn python để thực hiện giải phần xor này. (Xor_easy_solver.py)
* **Flag: MemberCTF{X0r_3s4y_VjpPr0_0x123}**

# 6> The flag on the cloud
* TheFlagOnTheCloud, một file ELF 64bit
* Mở bằng IDA 64bit để xem thử.
* ![image](https://user-images.githubusercontent.com/83124718/116060124-c46c9180-a6ab-11eb-8277-380e2c456798.png)
* Mình nhận ra ngay v7 là giá str giúp mình lấy ra password.
* Password sẽ là str gồm 16 ký tự lần lượt là ký tự của v7 với index +2 và sau đó +3 vào v5 trong mỗi vòng lặp hoàn thành.
* Mình viết một chương trình python để get password (TheFlagOnTheCloud_solver.py)
* Password: B@s1c_c0mpar3_!!
* chạy lệnh nc 45.119.86.116 27353 và submit với password trên là nhận được flag.
* Và flag của challenge này là
* **Flag: MemberCTF{B@s1c_c0mpar3_!!_0x1f5c86}**

# 7> ASM3
* Hello, file ELF 64bit
* Mở bằng IDA 64bit để kiểm tra nội dung file này.
* ![image](https://user-images.githubusercontent.com/83124718/116062378-07c7ff80-a6ae-11eb-904c-0dd1c1e04c0a.png)
* Chương trình trước tiên sẽ kiểm tra password, ở đây dễ dàng mình thấy được password được compare với s2 là "MOCQUACUTE".
* Sau khi pass được phần kiểm tra password, chương tình sẽ đọc file hello.txt, mở file hello.asm để ghi.
* Hàm xử lý việc ghi là 'abc' các bạn có thể mở hàm này và xem tác giả thay đổi như nào để ra được file hello.asm nha.
* Mình sẽ skip phần chuyển đổi này.
* Sau khi ghi xong, chương trình sẽ xóa file hello.asm này đi.
* Do đó mình sẽ đặt break point ở ngay chỗ remove("hello.asm") và tiến hành debug.
* Từ đó mình sẽ có thể đọc và ghi lại được nội dung của file hello.asm trước khi chương trình xóa
* Trong file hello.asm, lần lượt in ra màn hình từng ký tự riêng biệt, 
* ![image](https://user-images.githubusercontent.com/83124718/116082374-867c6700-a6c5-11eb-9796-8d2dada04186.png)
* Mình chuyển data hết thành dạng ascii và thu được flag
* **Flag: MemberCTF{eazy_asm}**

# 8> The last challenge
* LastChall, ELF 32bit
* Mở lên với IDA 32bit kiểm tra,
* Shift + f12 để mở bảng strings window, mình sẽ follow theo đoạn string "Please input %d random number\n" vì đây có thể là function chính của chương trình.
* Trong chương trình này có sử dụng ptrace để trace chính nó, một chương trình chỉ có thể attach 1 chương trình debug tại một thời điểm.
* Khi ta thực hiện debug trên IDA, ptrace trong chương trình sẽ không thể hoạt động được, nên ptrace thường được dùng để chống debug.
* Mình sẽ sử dụng patch để bypass kết quả trả về của ptrace để có thể để chương trình hoạt động đúng.
* ![image](https://user-images.githubusercontent.com/83124718/116092041-a87ae700-a6cf-11eb-8490-8c39dd6d7d43.png)
* Ở đây có 2 chuỗi data, aJHlagHkeFhphaH nhìn có vẻ là xáo trộn của FakeFlag nên mình sẽ pass và byte_565A3040 sẽ là đoạn data có chứa flag.
* Nhấn phím 'x' trên IDA để follow biến này.
* ![image](https://user-images.githubusercontent.com/83124718/116093760-27245400-a6d1-11eb-8996-89be3b48eccb.png)
* Sau khi kiểm tra có vẻ function sub_565A02ED sẽ trả về giá trị flag.
* Mình sẽ debug path program để có thể chạy được câu lệnh này trong sub_565A02ED
* ![image](https://user-images.githubusercontent.com/83124718/116094157-7ff3ec80-a6d1-11eb-9ce6-917c5c7d3232.png)
* Sau khi chỉnh sửa patch và chạy thành công, mình thu được flag của challenge này.
* **Flag: MemberCTF{Th3-l@st-Ch4ll3ng3_g00d-j0b}**

