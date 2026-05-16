# Nền Tảng Học Thiết Kế Nhà Và Vườn Nhiệt Đới Bắc Bộ

Nền tảng này giúp chủ nhà và người quản lý dự án học cách hình thành, thiết kế, thi công, vận hành và bảo trì một ngôi nhà vườn nhiệt đới miền Bắc Việt Nam trong vòng đời 30-50 năm.

## Lời hứa học tập

Sau khi học, bạn có thể:

- Viết được brief thiết kế rõ ràng cho một dự án nhà thật.
- Đọc khu đất theo nắng, gió, nước, cao độ, riêng tư, tiếng ồn và khả năng bảo trì.
- Hiểu bản chất của nhà vườn nhiệt đới Bắc Bộ: thích ứng khí hậu, tạo khoảng đệm, tổ chức bóng mát, kiểm soát nước, sống cùng cây và bảo trì dài hạn.
- Làm việc có cấu trúc với kiến trúc sư, kỹ sư, nhà thầu và đội cảnh quan.
- Biết các điểm cần chuyên gia kiểm tra thay vì quyết định bằng cảm tính.
- Lập được hệ thống vận hành và bảo trì nhà - vườn trong 30-50 năm.

## Cách học

1. Đọc `ban-do-nha-vuon-bac-bo.md` để thấy toàn bộ lĩnh vực.
2. Theo `giao-trinh-nha-vuon-bac-bo.md` để học theo thứ tự.
3. Dùng mỗi module như một buổi làm việc: đọc vấn đề, trả lời worksheet, áp dụng vào khu đất thật.
4. Tra `thuat-ngu-nha-vuon-bac-bo.md` khi gặp thuật ngữ.
5. Dùng `cong-cu-thuc-hanh.md` như sổ tay quản lý dự án.

## Cấu trúc nền tảng

| Phần | Chủ đề | Vai trò trong dự án |
|---|---|---|
| 01 | Tư duy tổng dự án | Từ mong muốn sống đến hệ quyết định, brief, vai trò và tiêu chí thành công. |
| 02 | Bối cảnh Bắc Bộ | Khí hậu, văn hóa, đất, nước, gió, nắng và các điều kiện nền của một khu đất thật. |
| 03 | Ý tưởng kiến trúc | Tổ chức không gian nhà - sân - hiên - vườn theo lối sống và khí hậu. |
| 04 | Thiết kế kỹ thuật nhà ở | Móng, kết cấu, mái, tường, chống thấm, MEP, an toàn và vật liệu vòng đời dài. |
| 05 | Thiết kế vườn nhiệt đới Bắc Bộ | Tầng cây, nước, đất, tưới, vi khí hậu và sự trưởng thành của khu vườn. |
| 06 | Quản lý thiết kế, ngân sách và thi công | Hồ sơ, dự toán, nhà thầu, hợp đồng, tiến độ, nghiệm thu và kiểm soát lỗi. |
| 07 | Hoàn thiện, bàn giao và vận hành | Nội thất, thiết bị, hồ sơ bàn giao, nhật ký vận hành và bảo trì theo mùa. |
| 08 | Tư duy vòng đời 30-50 năm | Lão hóa vật liệu, cây trưởng thành, cải tạo, chi phí vòng đời và di sản sống. |

## Website học tập

- Bản website tĩnh nằm ở `index.html`.
- Khi xuất bản qua GitHub Pages, truy cập: https://anhbeva.github.io/nha-vuon-nhiet-doi-bac-bo/
- Source học tập chính là các tệp Markdown; `index.html` được dựng lại từ source bằng `build_platform_html.py`.

## Cấu trúc repo

| Nhóm tệp | Vai trò |
|---|---|
| `README.md` | Giới thiệu nền tảng, cách học, cách dựng website. |
| `ban-do-nha-vuon-bac-bo.md` | Bản đồ lĩnh vực và nguyên lý nền tảng. |
| `giao-trinh-nha-vuon-bac-bo.md` | Lộ trình 72 module. |
| `thuat-ngu-nha-vuon-bac-bo.md` | Glossary thuật ngữ. |
| `cong-cu-thuc-hanh.md` | Checklist, worksheet, lịch bảo trì. |
| `Module-*.md` | 72 bài học chuyên sâu. |
| `build_platform_html.py` | Script dựng website từ Markdown. |
| `index.html` | Website tĩnh để học ngay. |

## Ranh giới trách nhiệm

Nội dung này là nền tảng học tập và chuẩn bị ra quyết định cho chủ nhà. Nó không thay thế khảo sát địa chất, hồ sơ thiết kế có pháp nhân, tính toán kết cấu, thiết kế MEP, tư vấn pháp lý, tư vấn cây xanh chuyên nghiệp hoặc nghiệm thu của người có năng lực. Với các quyết định liên quan an toàn, pháp lý, kết cấu, điện, chống sét, phòng cháy, nước thải và cây lớn, hãy làm việc với chuyên gia đủ điều kiện.

## Dựng website

Chạy:

```bash
python3 build_platform_html.py
```

Sau đó mở `index.html` trong trình duyệt. Website là bản học tĩnh, không cần backend.
