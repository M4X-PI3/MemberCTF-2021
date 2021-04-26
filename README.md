# MemberCTF-2021 RE
# 1> Meme
* ![image](https://user-images.githubusercontent.com/83124718/116029031-9b83d680-a682-11eb-9eb6-8549b13cd379.png)
* Meme.exe, Win32 EXE file
* Đưa chương trình vào IDA 32 xem có gì nào???
* ![image](https://user-images.githubusercontent.com/83124718/116029230-ffa69a80-a682-11eb-9996-5c70a850b2f6.png)
* Khá đơn giản cho flag đầu tiên của CTF này. hahaha
 **Flag: MemberCTF{W3lc0me-t0-rev3rse}**

# 2> ASM1
* asm.s, thử mở ra với text editor xem sao?
* ![image](https://user-images.githubusercontent.com/83124718/116029386-6d52c680-a683-11eb-8e63-94fc7d42497c.png)
* Một đoạn assembly code, push một đống data vào stack rồi in ra màn hình giá trị trên stack.
* Mình thử bỏ đống data này và chuyển sang dạng ascii để xem đống data này là gì?
* ![image](https://user-images.githubusercontent.com/83124718/116029582-d8040200-a683-11eb-8439-144d32c578b0.png)
* Vì data IO trên stack theo dạng FILO thông tin in ra màn hình khi chạy code sẽ là đảo ngược của đoạn text trên.
* Và đây là flag
 **Flag: MemberCTF{W3lc0me-t0-NASM}**
 
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
 **Flag: MemberCTF{M0d1fY_t3xt_!!__0x41520}**
