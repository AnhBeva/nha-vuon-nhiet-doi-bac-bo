from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent

PHASES = [
    ("01", "Tư duy tổng dự án", "Từ mong muốn sống đến hệ quyết định, brief, vai trò và tiêu chí thành công."),
    ("02", "Bối cảnh Bắc Bộ", "Khí hậu, văn hóa, đất, nước, gió, nắng và các điều kiện nền của một khu đất thật."),
    ("03", "Ý tưởng kiến trúc", "Tổ chức không gian nhà - sân - hiên - vườn theo lối sống và khí hậu."),
    ("04", "Thiết kế kỹ thuật nhà ở", "Móng, kết cấu, mái, tường, chống thấm, MEP, an toàn và vật liệu vòng đời dài."),
    ("05", "Thiết kế vườn nhiệt đới Bắc Bộ", "Tầng cây, nước, đất, tưới, vi khí hậu và sự trưởng thành của khu vườn."),
    ("06", "Quản lý thiết kế, ngân sách và thi công", "Hồ sơ, dự toán, nhà thầu, hợp đồng, tiến độ, nghiệm thu và kiểm soát lỗi."),
    ("07", "Hoàn thiện, bàn giao và vận hành", "Nội thất, thiết bị, hồ sơ bàn giao, nhật ký vận hành và bảo trì theo mùa."),
    ("08", "Tư duy vòng đời 30-50 năm", "Lão hóa vật liệu, cây trưởng thành, cải tạo, chi phí vòng đời và di sản sống."),
]

MODULES = [
    ("01", "Tư duy tổng dự án", "Vai trò chủ nhà trong một dự án nhà vườn", "Biến chủ nhà từ người mua dịch vụ thành người giữ chuẩn sống, chuẩn quyết định và chuẩn vận hành."),
    ("02", "Tư duy tổng dự án", "Từ giấc mơ sống đến brief thiết kế", "Chuyển mong muốn mơ hồ thành brief có thứ tự ưu tiên, ràng buộc và tiêu chí đo được."),
    ("03", "Tư duy tổng dự án", "Bản đồ quyết định sớm và muộn", "Biết quyết định nào khóa chi phí vòng đời, quyết định nào có thể để mở."),
    ("04", "Tư duy tổng dự án", "Đội dự án và cách làm việc với chuyên gia", "Phân vai kiến trúc sư, kỹ sư, cảnh quan, nhà thầu và chủ nhà để giảm hiểu nhầm."),
    ("05", "Tư duy tổng dự án", "Tiêu chí thành công của một ngôi nhà sống tốt", "Định nghĩa thành công bằng trải nghiệm, an toàn, chi phí vòng đời và khả năng thích nghi."),
    ("06", "Tư duy tổng dự án", "Ngân sách vòng đời thay vì chỉ chi phí xây", "Nhìn tổng chi phí sở hữu trong 30-50 năm để không tiết kiệm sai chỗ."),
    ("07", "Tư duy tổng dự án", "Rủi ro lớn nhất của nhà vườn khí hậu ẩm", "Nhận diện sớm thấm, nồm, nóng, bí gió, úng vườn và lỗi phối hợp."),
    ("08", "Tư duy tổng dự án", "Cách ghi nhật ký quyết định thiết kế", "Lưu lý do, phương án bị loại, giả định và trách nhiệm để kiểm soát thay đổi."),
    ("09", "Bối cảnh Bắc Bộ", "Đọc khí hậu nóng ẩm gió mùa", "Hiểu nắng, gió, mưa, nồm, rét, bão như đầu vào thiết kế chứ không phải phiền toái."),
    ("10", "Bối cảnh Bắc Bộ", "Đọc khu đất trước khi vẽ nhà", "Quan sát hướng, cao độ, nước, tiếng ồn, hàng xóm, riêng tư và tuyến tiếp cận."),
    ("11", "Bối cảnh Bắc Bộ", "Nắng tây, bóng đổ và chiến lược che nắng", "Dùng mái, hiên, cây và mặt đứng để giảm tải nhiệt mà không làm tối nhà."),
    ("12", "Bối cảnh Bắc Bộ", "Gió, thông thoáng và bẫy bí khí", "Tổ chức đường gió, cửa, giếng trời và khoảng rỗng để nhà thở được."),
    ("13", "Bối cảnh Bắc Bộ", "Mưa lớn, thoát nước và cao độ nền", "Thiết kế cao độ, sân, rãnh, mái và vườn để nước đi đúng đường."),
    ("14", "Bối cảnh Bắc Bộ", "Nồm ẩm và cân bằng hơi nước", "Hiểu cơ chế đọng sương để chọn vật liệu, thông gió và vận hành đúng."),
    ("15", "Bối cảnh Bắc Bộ", "Tinh thần sân, hiên, vườn trong nhà Bắc Bộ", "Học di sản không bằng hình thức, mà bằng quan hệ khí hậu, nếp sống và ngưỡng chuyển tiếp."),
    ("16", "Bối cảnh Bắc Bộ", "Pháp lý, quy hoạch và giới hạn cần kiểm tra", "Biết những câu hỏi pháp lý bắt buộc trước khi mua đất, thiết kế hoặc thi công."),
    ("17", "Ý tưởng kiến trúc", "Ngôn ngữ nhiệt đới Bắc Bộ đương đại", "Tạo phong cách từ cơ chế khí hậu và văn hóa sống, tránh sao chép biểu tượng."),
    ("18", "Ý tưởng kiến trúc", "Tổ chức mặt bằng theo nhịp sống gia đình", "Xếp không gian theo thói quen, riêng tư, tiếp khách, chăm sóc, tuổi già và trẻ nhỏ."),
    ("19", "Ý tưởng kiến trúc", "Hiên, mái và khoảng đệm", "Dùng khoảng chuyển tiếp để che mưa nắng, giảm sốc nhiệt và tạo nơi sống ngoài trời."),
    ("20", "Ý tưởng kiến trúc", "Sân trong, giếng trời và lõi thông gió", "Tạo ánh sáng, gió, cây và cảm giác sâu cho nhà mà vẫn kiểm soát nóng ẩm."),
    ("21", "Ý tưởng kiến trúc", "Quan hệ nhà - vườn - nước", "Đặt nước và cây như hạ tầng vi khí hậu, không chỉ là trang trí."),
    ("22", "Ý tưởng kiến trúc", "Riêng tư, an ninh và mở về thiên nhiên", "Cân bằng tầm nhìn, hàng rào, lớp cây, cửa và thói quen sử dụng."),
    ("23", "Ý tưởng kiến trúc", "Ánh sáng tự nhiên và bóng tối hữu ích", "Thiết kế ánh sáng để đọc, nghỉ, làm việc và cảm nhận mùa mà không gây chói nóng."),
    ("24", "Ý tưởng kiến trúc", "Mặt đứng, tỷ lệ và vật liệu địa phương", "Tạo vẻ đẹp bền bằng tỷ lệ, bóng đổ, vật liệu thật và chi tiết dễ bảo trì."),
    ("25", "Thiết kế kỹ thuật nhà ở", "Khảo sát địa chất và quyết định móng", "Biết vì sao móng cần dữ kiện đất thật và không thể chọn bằng kinh nghiệm truyền miệng."),
    ("26", "Thiết kế kỹ thuật nhà ở", "Kết cấu, nhịp và khả năng cải tạo", "Tổ chức cột, dầm, sàn để vừa an toàn vừa linh hoạt cho 30-50 năm."),
    ("27", "Thiết kế kỹ thuật nhà ở", "Mái trong khí hậu mưa nắng lớn", "Thiết kế mái như hệ che, thoát nước, cách nhiệt, chống dột và bảo trì."),
    ("28", "Thiết kế kỹ thuật nhà ở", "Tường, vỏ bao che và quán tính nhiệt", "Hiểu tường như lớp lọc nắng, ẩm, âm, gió và cảm giác chạm."),
    ("29", "Thiết kế kỹ thuật nhà ở", "Chống thấm từ nguyên lý", "Chặn nước bằng thiết kế đường nước, chi tiết cấu tạo, vật liệu và kiểm tra thi công."),
    ("30", "Thiết kế kỹ thuật nhà ở", "Chống nóng không chỉ bằng điều hòa", "Giảm nhiệt từ nguồn bằng hướng, che nắng, thông gió, mái, cây và vận hành."),
    ("31", "Thiết kế kỹ thuật nhà ở", "Điện, chiếu sáng và an toàn sử dụng", "Thiết kế hệ điện có dự phòng, dễ kiểm tra, đủ tải và phù hợp thói quen sống."),
    ("32", "Thiết kế kỹ thuật nhà ở", "Cấp thoát nước, bể, bơm và vệ sinh", "Tổ chức nước sạch, nước mưa, nước thải, thoát sàn và điểm kiểm tra."),
    ("33", "Thiết kế kỹ thuật nhà ở", "Thông gió, điều hòa và chất lượng không khí", "Phối hợp thông gió tự nhiên, cơ khí và điều hòa để tránh ẩm mốc và bí khí."),
    ("34", "Thiết kế kỹ thuật nhà ở", "Chống sét, cháy nổ và an toàn kỹ thuật", "Đưa an toàn thành yêu cầu thiết kế, không phải hạng mục thêm cuối dự án."),
    ("35", "Thiết kế kỹ thuật nhà ở", "Vật liệu cho khí hậu nóng ẩm", "Chọn vật liệu theo nước, nhiệt, bảo trì, tuổi thọ, cảm giác và khả năng sửa chữa."),
    ("36", "Thiết kế kỹ thuật nhà ở", "Chi tiết cấu tạo quyết định tuổi thọ", "Nhìn chân tường, mép mái, khe co giãn, cổ ống và tiếp giáp như điểm rủi ro chính."),
    ("37", "Thiết kế vườn nhiệt đới Bắc Bộ", "Bản đồ vườn như một hệ sinh thái sống", "Thiết kế vườn bằng tầng, chu trình nước, đất, ánh sáng, chăm sóc và thời gian."),
    ("38", "Thiết kế vườn nhiệt đới Bắc Bộ", "Tầng cây và cấu trúc bóng mát", "Xếp cây cao, cây trung, bụi, thảm, leo và mặt nước để tạo vi khí hậu."),
    ("39", "Thiết kế vườn nhiệt đới Bắc Bộ", "Chọn cây theo đất, nước, nắng và chăm sóc", "Chọn cây không theo ảnh đẹp mà theo điều kiện sống và năng lực bảo trì."),
    ("40", "Thiết kế vườn nhiệt đới Bắc Bộ", "Cây bản địa, cây ăn quả và cây hương", "Phối hợp giá trị sinh thái, ký ức, mùa vụ, mùi hương và an toàn sử dụng."),
    ("41", "Thiết kế vườn nhiệt đới Bắc Bộ", "Đất trồng, phân hữu cơ và sức khỏe rễ", "Xem đất là nền sống của vườn, không phải vật liệu lấp chỗ trống."),
    ("42", "Thiết kế vườn nhiệt đới Bắc Bộ", "Tưới, thu nước mưa và tiết kiệm nước", "Thiết kế tưới theo vùng, mùa, loại cây và khả năng kiểm soát."),
    ("43", "Thiết kế vườn nhiệt đới Bắc Bộ", "Thoát nước vườn và chống úng", "Tạo đường nước mặt, nước ngầm và điểm tràn an toàn trong mưa lớn."),
    ("44", "Thiết kế vườn nhiệt đới Bắc Bộ", "Lối đi, sân, bậc và vật liệu ngoài trời", "Chọn bề mặt không trơn, thoát nước, già đi đẹp và dễ sửa."),
    ("45", "Thiết kế vườn nhiệt đới Bắc Bộ", "Hồ, ao nhỏ và mặt nước có trách nhiệm", "Dùng nước để làm mát, phản chiếu và nuôi sinh thái nhưng kiểm soát muỗi, rò rỉ, an toàn."),
    ("46", "Thiết kế vườn nhiệt đới Bắc Bộ", "Vườn theo mùa và lịch chăm sóc", "Lập kịch bản hoa, lá, quả, cắt tỉa, sâu bệnh và nghỉ dưỡng theo mùa Bắc Bộ."),
    ("47", "Thiết kế vườn nhiệt đới Bắc Bộ", "Vườn trưởng thành qua 5-10-30 năm", "Thiết kế không gian cho cây lớn lên, thay bóng, rễ, tán và quan hệ với nhà."),
    ("48", "Thiết kế vườn nhiệt đới Bắc Bộ", "Động vật nhỏ, côn trùng và cân bằng sinh thái", "Tăng đa dạng sinh học vừa đủ mà vẫn giữ vệ sinh, an toàn và tiện nghi."),
    ("49", "Quản lý thiết kế, ngân sách và thi công", "Hồ sơ thiết kế cần có trước khi thi công", "Biết bộ bản vẽ, thuyết minh, dự toán và thông số nào cần khóa."),
    ("50", "Quản lý thiết kế, ngân sách và thi công", "Dự toán, báo giá và bẫy chi phí ẩn", "Đọc báo giá theo phạm vi, đơn giá, chủng loại, khối lượng, điều kiện và rủi ro phát sinh."),
    ("51", "Quản lý thiết kế, ngân sách và thi công", "Chọn nhà thầu và thiết lập hợp đồng", "Đánh giá năng lực, quy trình, trách nhiệm, bảo hành, thanh toán và thay đổi."),
    ("52", "Quản lý thiết kế, ngân sách và thi công", "Tiến độ thi công và điểm chờ nghiệm thu", "Biết lúc nào phải dừng để kiểm tra trước khi che khuất lỗi."),
    ("53", "Quản lý thiết kế, ngân sách và thi công", "Nghiệm thu móng, kết cấu và mái", "Kiểm tra các hạng mục khó sửa, ảnh hưởng an toàn và tuổi thọ."),
    ("54", "Quản lý thiết kế, ngân sách và thi công", "Nghiệm thu chống thấm, điện nước và thoát nước", "Kiểm tra bằng thử nước, thử áp, quan sát đường ống và hồ sơ hoàn công."),
    ("55", "Quản lý thiết kế, ngân sách và thi công", "Quản trị thay đổi trong lúc xây", "Phân biệt thay đổi cần thiết, thay đổi cảm tính và thay đổi phá hệ thống."),
    ("56", "Quản lý thiết kế, ngân sách và thi công", "Kiểm soát chất lượng hoàn thiện", "Nhìn hoàn thiện như lớp sử dụng lâu dài, không chỉ là bề mặt đẹp lúc bàn giao."),
    ("57", "Hoàn thiện, bàn giao và vận hành", "Nội thất gắn với khí hậu và lối sống", "Chọn đồ, bề mặt, lưu trữ và bố trí theo độ ẩm, vệ sinh, tuổi già và trẻ nhỏ."),
    ("58", "Hoàn thiện, bàn giao và vận hành", "Ánh sáng nhân tạo trong nhà vườn", "Tạo lớp sáng cho sinh hoạt, an ninh, cảnh quan đêm và tiết kiệm năng lượng."),
    ("59", "Hoàn thiện, bàn giao và vận hành", "Thiết bị, phụ kiện và khả năng thay thế", "Chọn thiết bị theo khả năng bảo hành, linh kiện, sửa chữa và thói quen dùng."),
    ("60", "Hoàn thiện, bàn giao và vận hành", "Hồ sơ bàn giao và nhật ký vận hành", "Giữ bản vẽ hoàn công, catalogue, bảo hành, ảnh đường ống và nhật ký lỗi."),
    ("61", "Hoàn thiện, bàn giao và vận hành", "Lịch bảo trì tuần, tháng, mùa, năm", "Biến bảo trì thành hệ thống nhẹ nhàng thay vì chữa cháy khi hỏng."),
    ("62", "Hoàn thiện, bàn giao và vận hành", "Quản lý ẩm mốc, côn trùng và vệ sinh", "Duy trì nhà vườn sạch, thoáng, khô đúng mức mà không triệt tiêu thiên nhiên."),
    ("63", "Hoàn thiện, bàn giao và vận hành", "Vận hành nhà khi đi xa, mưa bão và mất điện", "Chuẩn bị kịch bản bất thường để giảm thiệt hại và lo lắng."),
    ("64", "Hoàn thiện, bàn giao và vận hành", "Đo trải nghiệm sống sau khi vào ở", "Dùng phản hồi thực tế để tinh chỉnh ánh sáng, gió, cây, thói quen và bảo trì."),
    ("65", "Tư duy vòng đời 30-50 năm", "Nhà thay đổi theo gia đình", "Dự phòng cho trẻ lớn, người già, làm việc tại nhà, chăm sóc và chuyển giao thế hệ."),
    ("66", "Tư duy vòng đời 30-50 năm", "Lão hóa vật liệu và kế hoạch thay thế", "Biết vật liệu nào già đẹp, vật liệu nào cần thay và chu kỳ bảo trì hợp lý."),
    ("67", "Tư duy vòng đời 30-50 năm", "Cây lớn, rễ, bóng và rủi ro dài hạn", "Quản lý cây trưởng thành để giữ bóng mát mà không phá nền, tường, mái, ống."),
    ("68", "Tư duy vòng đời 30-50 năm", "Cải tạo theo giai đoạn không phá tổng thể", "Lập nguyên tắc nâng cấp để mỗi lần sửa làm nhà tốt hơn, không chắp vá."),
    ("69", "Tư duy vòng đời 30-50 năm", "Năng lượng, nước và khả năng tự chủ", "Xem xét thu nước mưa, điện mặt trời, dự phòng và tiết kiệm theo điều kiện thật."),
    ("70", "Tư duy vòng đời 30-50 năm", "Chi phí vòng đời và quỹ bảo trì", "Tạo ngân sách bảo trì, thay thế, cây xanh và sửa chữa định kỳ."),
    ("71", "Tư duy vòng đời 30-50 năm", "Tiêu chí đánh giá nhà sau 1-5-10 năm", "Đo nhà bằng sức khỏe, tiện nghi, chi phí, khả năng sửa, cây và niềm vui sống."),
    ("72", "Tư duy vòng đời 30-50 năm", "Di sản sống: giữ tinh thần nhà vườn qua thế hệ", "Biến ngôi nhà thành hệ thống ký ức, chăm sóc và thích nghi lâu dài."),
]

SLUGS = {
    "Tư duy tổng dự án": "tu-duy-tong-du-an",
    "Bối cảnh Bắc Bộ": "boi-canh-bac-bo",
    "Ý tưởng kiến trúc": "y-tuong-kien-truc",
    "Thiết kế kỹ thuật nhà ở": "thiet-ke-ky-thuat-nha-o",
    "Thiết kế vườn nhiệt đới Bắc Bộ": "thiet-ke-vuon-nhiet-doi-bac-bo",
    "Quản lý thiết kế, ngân sách và thi công": "quan-ly-thiet-ke-ngan-sach-thi-cong",
    "Hoàn thiện, bàn giao và vận hành": "hoan-thien-ban-giao-van-hanh",
    "Tư duy vòng đời 30-50 năm": "tu-duy-vong-doi-30-50-nam",
}


def slugify(text):
    mapping = {
        "à": "a", "á": "a", "ạ": "a", "ả": "a", "ã": "a", "â": "a", "ầ": "a", "ấ": "a", "ậ": "a", "ẩ": "a", "ẫ": "a", "ă": "a", "ằ": "a", "ắ": "a", "ặ": "a", "ẳ": "a", "ẵ": "a",
        "è": "e", "é": "e", "ẹ": "e", "ẻ": "e", "ẽ": "e", "ê": "e", "ề": "e", "ế": "e", "ệ": "e", "ể": "e", "ễ": "e",
        "ì": "i", "í": "i", "ị": "i", "ỉ": "i", "ĩ": "i",
        "ò": "o", "ó": "o", "ọ": "o", "ỏ": "o", "õ": "o", "ô": "o", "ồ": "o", "ố": "o", "ộ": "o", "ổ": "o", "ỗ": "o", "ơ": "o", "ờ": "o", "ớ": "o", "ợ": "o", "ở": "o", "ỡ": "o",
        "ù": "u", "ú": "u", "ụ": "u", "ủ": "u", "ũ": "u", "ư": "u", "ừ": "u", "ứ": "u", "ự": "u", "ử": "u", "ữ": "u",
        "ỳ": "y", "ý": "y", "ỵ": "y", "ỷ": "y", "ỹ": "y", "đ": "d",
    }
    raw = text.lower()
    raw = "".join(mapping.get(ch, ch) for ch in raw)
    out = []
    for ch in raw:
        if ch.isalnum():
            out.append(ch)
        elif out and out[-1] != "-":
            out.append("-")
    return "".join(out).strip("-")


def module_filename(num, title):
    return f"Module-{num}-{slugify(title)[:64]}.md"


def write(path, content):
    (ROOT / path).write_text(content.strip() + "\n", encoding="utf-8")


def phase_overview():
    rows = ["| Phần | Chủ đề | Vai trò trong dự án |", "|---|---|---|"]
    for code, title, desc in PHASES:
        rows.append(f"| {code} | {title} | {desc} |")
    return "\n".join(rows)


def module_table():
    rows = ["| Module | Phần | Bài học | Năng lực chính |", "|---|---|---|---|"]
    for num, phase, title, purpose in MODULES:
        rows.append(f"| {num} | {phase} | {title} | {purpose} |")
    return "\n".join(rows)


def public_warning():
    return (
        "Nội dung này là nền tảng học tập và chuẩn bị ra quyết định cho chủ nhà. "
        "Nó không thay thế khảo sát địa chất, hồ sơ thiết kế có pháp nhân, tính toán kết cấu, "
        "thiết kế MEP, tư vấn pháp lý, tư vấn cây xanh chuyên nghiệp hoặc nghiệm thu của người có năng lực. "
        "Với các quyết định liên quan an toàn, pháp lý, kết cấu, điện, chống sét, phòng cháy, nước thải và cây lớn, "
        "hãy làm việc với chuyên gia đủ điều kiện."
    )


def make_readme():
    return f"""
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

{phase_overview()}

## Ranh giới trách nhiệm

{public_warning()}

## Dựng website

Chạy:

```bash
python3 build_platform_html.py
```

Sau đó mở `index.html` trong trình duyệt. Website là bản học tĩnh, không cần backend.
"""


def make_map():
    layers = [
        ("Mục đích sống", "Gia đình muốn sống thế nào trong 30-50 năm?", "Brief, ưu tiên, ngân sách, vòng đời", "Tránh xây một căn nhà đẹp ảnh nhưng không hợp đời sống."),
        ("Khu đất", "Đất đang nói gì qua nắng, gió, nước, cao độ, hàng xóm?", "Site reading, cao độ, thoát nước, vi khí hậu", "Không áp ý tưởng lên đất khi chưa đọc điều kiện thật."),
        ("Khí hậu Bắc Bộ", "Nóng ẩm, nồm, mưa bão, rét tác động ra sao?", "Che nắng, thông gió, chống ẩm, mái, vỏ bao che", "Thiết kế từ cơ chế khí hậu thay vì chỉ dùng điều hòa."),
        ("Kiến trúc", "Nhà tổ chức đời sống, gió, sáng, riêng tư và chuyển tiếp thế nào?", "Mặt bằng, hiên, sân, mái, giếng trời, vật liệu", "Tạo khung sống bền, dễ dùng, dễ chăm."),
        ("Kỹ thuật", "Hệ nào nếu sai sẽ khó sửa và tốn chi phí nhất?", "Móng, kết cấu, MEP, chống thấm, an toàn", "Khóa rủi ro trước khi hoàn thiện che phủ lỗi."),
        ("Vườn", "Cây, đất, nước và thời gian cùng tạo môi trường sống thế nào?", "Tầng cây, đất, tưới, thoát nước, lịch chăm", "Thiết kế vườn như hệ sống trưởng thành."),
        ("Thi công", "Làm sao chuyển bản vẽ thành công trình không méo ý đồ?", "Hồ sơ, dự toán, hợp đồng, tiến độ, nghiệm thu", "Kiểm soát chất lượng bằng điểm chờ và bằng chứng."),
        ("Vận hành", "Sau khi vào ở, nhà vườn cần được chăm thế nào?", "Bảo trì, nhật ký lỗi, lịch mùa, ngân sách vòng đời", "Giữ nhà tốt dần thay vì xuống cấp âm thầm."),
    ]
    rows = ["| Tầng | Câu hỏi cốt lõi | Nhánh/mô hình tiêu biểu | Ý nghĩa thực tiễn |", "|---|---|---|---|"]
    for row in layers:
        rows.append("| " + " | ".join(row) + " |")
    principles = [
        ("Thiết kế từ nước", "Nước mưa, nước ngầm, hơi ẩm và nước sinh hoạt quyết định tuổi thọ nhà vườn.", "Sai đường nước thường tạo thấm, mốc, úng, hỏng vật liệu."),
        ("Tạo lớp đệm", "Hiên, mái, sân, cây, rèm, lam, hàng hiên làm giảm xung đột giữa trong và ngoài.", "Không gian đệm giúp nhà mát, khô, riêng tư và dễ sống."),
        ("Vòng đời dài", "Quyết định hôm nay tạo chi phí, bảo trì và khả năng sửa trong nhiều thập kỷ.", "Ưu tiên hệ khó sửa: móng, mái, thoát nước, kết cấu, MEP."),
        ("Vườn là hệ sống", "Cây lớn lên, rễ phát triển, bóng thay đổi, đất mệt hoặc khỏe theo chăm sóc.", "Thiết kế phải có kịch bản 5-10-30 năm."),
        ("Đẹp phải vận hành được", "Cái đẹp bền đến từ tỷ lệ, vật liệu thật, chi tiết đúng và chăm sóc vừa sức.", "Tránh hình ảnh ấn tượng nhưng khó vệ sinh, khó sửa, khó sống."),
    ]
    prows = ["| Nguyên lý | Bản chất | Nếu hiểu sai |", "|---|---|---|"]
    for row in principles:
        prows.append("| " + " | ".join(row) + " |")
    return f"""
# Bản đồ nhà và vườn nhiệt đới Bắc Bộ

## 1. Lĩnh vực này thực sự là gì?

Thiết kế nhà và vườn nhiệt đới Bắc Bộ là nghệ thuật tổ chức một hệ sống gồm con người, nhà, cây, nước, đất, khí hậu, kỹ thuật và bảo trì. Trọng tâm không phải là tạo hình ảnh “nhiệt đới”, mà là làm cho ngôi nhà sống tốt trong nóng ẩm, mưa nhiều, nồm, bão, rét và sự thay đổi của gia đình qua nhiều thập kỷ.

## 2. Bản đồ các tầng

{chr(10).join(rows)}

## 3. Nguyên lý nền tảng

{chr(10).join(prows)}

## 4. Câu hỏi kiểm tra trước mọi quyết định

| Câu hỏi | Vì sao quan trọng | Bằng chứng cần có |
|---|---|---|
| Quyết định này ảnh hưởng bao lâu? | Ưu tiên đúng hạng mục khó sửa. | Tuổi thọ, chi phí thay thế, khả năng tiếp cận. |
| Nước sẽ đi đâu? | Giảm thấm, úng, mốc và hỏng vật liệu. | Cao độ, dốc, rãnh, phễu thu, điểm tràn. |
| Ai sẽ chăm phần này? | Tránh thiết kế vượt quá năng lực vận hành. | Lịch bảo trì, người phụ trách, chi phí. |
| Nếu gia đình thay đổi thì sao? | Nhà cần thích nghi với tuổi tác và lối sống. | Phương án cải tạo, kết cấu, đường kỹ thuật. |
| Khi hỏng có sửa được không? | Thiết kế bền là thiết kế tiếp cận được. | Cửa thăm, bản vẽ hoàn công, vật tư thay thế. |
"""


def make_syllabus():
    return f"""
# Giáo trình nhà và vườn nhiệt đới Bắc Bộ

## Cấu trúc tổng thể

{phase_overview()}

## Danh mục 72 module

{module_table()}

## Lộ trình theo mục tiêu

| Mục tiêu | Nên học module | Kết quả mong đợi |
|---|---|---|
| Chuẩn bị làm việc với kiến trúc sư | 01-08, 17-24 | Có brief, tiêu chí thành công, bản đồ quyết định và ngôn ngữ thiết kế. |
| Đọc khu đất và khí hậu | 09-16 | Biết đặt câu hỏi đúng về nắng, gió, nước, nồm, cao độ và pháp lý. |
| Kiểm soát kỹ thuật khó sửa | 25-36, 49-56 | Biết điểm cần chuyên gia, điểm chờ nghiệm thu và rủi ro bị che khuất. |
| Xây vườn sống lâu | 37-48, 61-63, 67 | Có chiến lược cây, đất, nước, chăm sóc và kịch bản vườn trưởng thành. |
| Vận hành 30-50 năm | 57-72 | Có lịch bảo trì, quỹ vòng đời, nhật ký vận hành và tiêu chí đánh giá sau khi ở. |

## Cách dùng với dự án thật

Mỗi module nên kết thúc bằng một tài sản cụ thể: một quyết định, một checklist, một bản ghi quan sát, một câu hỏi gửi chuyên gia, một tiêu chí nghiệm thu hoặc một thay đổi trong kế hoạch vận hành. Không học module chỉ để biết thêm thuật ngữ.
"""


def make_glossary():
    terms = [
        ("Brief thiết kế", "Tổng dự án", "Tài liệu mô tả mục tiêu sống, ràng buộc, ưu tiên, ngân sách và tiêu chí thành công.", "Giúp đội thiết kế hiểu đúng vấn đề trước khi tạo hình.", "Nếu brief chỉ là ảnh tham khảo, dự án dễ chạy theo hình thức."),
        ("Vi khí hậu", "Khí hậu", "Điều kiện nắng, gió, ẩm, nhiệt trong phạm vi khu đất và từng khoảng sân.", "Quyết định cảm giác sống thật.", "Góc sân mát buổi chiều có thể tốt hơn phòng khách đẹp nhưng nóng."),
        ("Nồm", "Khí hậu", "Hiện tượng hơi nước đọng trên bề mặt khi không khí ẩm gặp bề mặt lạnh.", "Ảnh hưởng sàn, tường, đồ gỗ, thiết bị và sức khỏe.", "Mở cửa sai thời điểm có thể làm nhà ẩm hơn."),
        ("Khoảng đệm", "Kiến trúc", "Không gian chuyển tiếp giữa trong và ngoài như hiên, sảnh, sân, mái đua.", "Giảm mưa nắng, tạo riêng tư và nơi sống ngoài trời.", "Nhà không có khoảng đệm thường phụ thuộc mạnh vào điều hòa."),
        ("Đường nước", "Kỹ thuật", "Lộ trình nước mưa, nước mặt, nước ngầm, nước thải và nước rò đi qua công trình.", "Là trục kiểm soát thấm, úng và tuổi thọ.", "Mỗi điểm tiếp giáp mái, tường, sàn đều cần nghĩ đến nước."),
        ("Điểm chờ nghiệm thu", "Thi công", "Mốc phải kiểm tra trước khi che khuất bằng lớp hoàn thiện.", "Ngăn lỗi âm tường, âm sàn, âm mái.", "Chống thấm cần thử nước trước khi lát."),
        ("Tầng cây", "Cảnh quan", "Cấu trúc cây cao, cây trung, bụi, thảm, leo, mặt nước.", "Tạo bóng, độ sâu, đa dạng sinh học và ổn định vườn.", "Vườn chỉ có cây trang trí thấp thường nóng và nhanh cũ."),
        ("Quỹ bảo trì", "Vòng đời", "Khoản tiền định kỳ dành cho sửa chữa, thay thế, chăm cây và nâng cấp.", "Biến bảo trì thành kế hoạch thay vì khủng hoảng.", "Nhà vườn không có quỹ bảo trì dễ xuống cấp sau vài mùa mưa."),
        ("Hồ sơ hoàn công", "Vận hành", "Bộ bản vẽ và thông tin phản ánh công trình đã xây thực tế.", "Giúp sửa chữa, khoan đục, thay thiết bị và cải tạo an toàn.", "Ảnh chụp đường ống trước khi che phủ rất có giá trị."),
        ("Chi phí vòng đời", "Tài chính", "Tổng chi phí xây, vận hành, năng lượng, bảo trì, sửa chữa, thay thế.", "Giúp tránh chọn giải pháp rẻ lúc đầu nhưng đắt về sau.", "Một mái tốt có thể tiết kiệm tiền thấm và làm mát nhiều năm."),
    ]
    rows = ["| Thuật ngữ | Nhóm | Định nghĩa ngắn | Bản chất | Câu hỏi ứng dụng |", "|---|---|---|---|---|"]
    for t in terms:
        rows.append("| " + " | ".join(t) + " |")
    extra = []
    for _, phase, title, purpose in MODULES:
        extra.append(f"| {title} | {phase} | Chủ đề học về {title.lower()}. | {purpose} | Tôi cần bằng chứng gì trong dự án thật? |")
    return f"""
# Thuật ngữ nhà và vườn nhiệt đới Bắc Bộ

Glossary này dùng thuật ngữ như công cụ quan sát và hành động. Không dùng thuật ngữ để tạo cảm giác chuyên môn giả; mỗi từ phải giúp bạn hỏi câu hỏi tốt hơn trong dự án thật.

{chr(10).join(rows + extra)}
"""


def make_tools():
    return """
# Công cụ thực hành cho dự án nhà vườn Bắc Bộ

## 1. Worksheet brief thiết kế

| Mục | Câu hỏi cần trả lời | Bằng chứng hoặc ví dụ |
|---|---|---|
| Gia đình | Ai sống trong nhà hôm nay và 10 năm nữa? | Tuổi, thói quen, sức khỏe, khách, người chăm sóc. |
| Một ngày sống tốt | Buổi sáng, trưa, tối diễn ra thế nào? | Hành trình đi lại, ăn, nghỉ, làm việc, chăm vườn. |
| Ưu tiên | Ba điều không được hy sinh là gì? | Mát, riêng tư, ít bảo trì, sân rộng, ngân sách. |
| Giới hạn | Điều gì không thể vượt? | Pháp lý, tiền, thời gian, nhân lực chăm sóc. |
| Thành công | Sau 1 năm ở, biết nhà đúng bằng dấu hiệu nào? | Ít nóng, ít mốc, sân dùng thường xuyên, chi phí kiểm soát. |

## 2. Checklist đọc khu đất

| Lớp quan sát | Việc cần làm | Dấu hiệu cần ghi |
|---|---|---|
| Nắng | Quan sát sáng, trưa, chiều, đặc biệt nắng tây. | Vùng nóng, vùng bóng, bề mặt hấp nhiệt. |
| Gió | Ghi hướng gió mát, gió bụi, gió bão. | Đường gió bị chặn, góc bí, cửa có thể mở. |
| Nước | Quan sát mưa, cao độ, điểm đọng, đường thoát. | Vũng, mép tường ẩm, cống, điểm tràn. |
| Hàng xóm | Nhìn tầm nhìn, tiếng ồn, mùi, ranh giới. | Cần che, cần mở, cần cách âm. |
| Cây hiện hữu | Đánh giá tán, rễ, bóng, sức khỏe cây. | Giữ, di dời, thay thế, bảo vệ khi thi công. |

## 3. Ma trận quyết định vật liệu

| Vật liệu/hạng mục | Chịu nước | Chịu nắng | Dễ sửa | Già đi đẹp | Chi phí vòng đời | Ghi chú |
|---|---|---|---|---|---|---|
| Mái |  |  |  |  |  |  |
| Sàn ngoài trời |  |  |  |  |  |  |
| Tường ngoài |  |  |  |  |  |  |
| Đồ gỗ |  |  |  |  |  |  |

## 4. Điểm chờ nghiệm thu

| Giai đoạn | Không được bỏ qua | Cách kiểm tra |
|---|---|---|
| Móng/kết cấu | Kích thước, thép, bê tông, nhật ký đổ. | Kỹ sư kiểm tra, ảnh, biên bản. |
| Mái | Dốc, thoát nước, chống dột, cách nhiệt. | Phun/thử nước, kiểm tra máng, cổ ống. |
| Chống thấm | Nhà vệ sinh, ban công, mái, bồn cây. | Ngâm thử đủ thời gian, ghi ảnh, ký nghiệm thu. |
| Điện nước | Ống, dây, áp lực, vị trí thiết bị. | Test áp, đo điện, ảnh trước khi che. |
| Vườn | Đất, thoát nước, cây, tưới. | Kiểm tra sau mưa, tưới thử, cây không lấp cổ rễ. |

## 5. Lịch bảo trì 30-50 năm

| Chu kỳ | Việc cần làm |
|---|---|
| Hàng tuần | Quan sát cây, tưới, lá rụng, thoát sàn, dấu hiệu ẩm mốc. |
| Hàng tháng | Kiểm tra bơm, đèn, máng nước, côn trùng, điểm nứt mới. |
| Theo mùa mưa | Dọn máng, kiểm tra mái, rãnh, điểm tràn, chống úng vườn. |
| Theo mùa nồm | Quản lý mở cửa, hút ẩm, lau khô bề mặt, kiểm tra tủ kín. |
| Hàng năm | Rà soát chống thấm, sơn, thiết bị, cây lớn, quỹ bảo trì. |
| 5 năm | Đánh giá thay thiết bị, sửa bề mặt, cải tạo cây, cập nhật hồ sơ. |
| 10 năm trở lên | Rà soát nhu cầu gia đình, năng lượng, nước, an toàn, cải tạo lớn. |
"""


def module_specific_principles(title, phase):
    base = [
        ("Đi từ điều kiện thật", "Mọi quyết định phải bám vào khu đất, khí hậu, ngân sách, con người và năng lực chăm sóc.", "Dễ sai khi chỉ nhìn ảnh tham khảo hoặc lời khuyên rời rạc."),
        ("Ưu tiên hệ khó sửa", "Những gì nằm dưới đất, trong tường, trên mái và sau lớp hoàn thiện cần được quyết định cẩn trọng.", "Dễ sai khi dồn tiền vào bề mặt thấy ngay."),
        ("Thiết kế cho vận hành", "Một giải pháp tốt là giải pháp gia đình có thể dùng, chăm, sửa và trả chi phí trong nhiều năm.", "Dễ sai khi thiết kế vượt quá năng lực chăm sóc."),
    ]
    if "vườn" in phase.lower() or "cây" in title.lower():
        base[1] = ("Thiết kế theo thời gian", "Cây và đất thay đổi từng mùa, từng năm; bản vẽ phải dự đoán sự trưởng thành.", "Dễ sai khi trồng dày để đẹp ngay lúc bàn giao.")
    if "kỹ thuật" in phase.lower() or any(k in title.lower() for k in ["thấm", "mái", "điện", "nước", "móng", "kết cấu"]):
        base[0] = ("Bằng chứng trước cảm tính", "Hạng mục kỹ thuật cần khảo sát, bản vẽ, thông số, thử nghiệm và nghiệm thu.", "Dễ sai khi dùng kinh nghiệm truyền miệng cho quyết định an toàn.")
    if "thi công" in phase.lower() or "nghiệm thu" in title.lower():
        base[2] = ("Không che khuất lỗi", "Phải kiểm tra các lớp âm trước khi lát, sơn, đóng trần hoặc trồng phủ.", "Dễ sai khi chạy tiến độ mà bỏ điểm chờ nghiệm thu.")
    return base


def make_module(num, phase, title, purpose):
    principles = module_specific_principles(title, phase)
    principle_rows = ["| Nguyên lý | Giải thích | Khi nào dễ sai |", "|---|---|---|"]
    for row in principles:
        principle_rows.append("| " + " | ".join(row) + " |")
    file_ref = f"Module-{num}"
    return f"""
# Module {num}: {title}

**{purpose}**

**Định dạng:** Bài học ứng dụng cho chủ nhà và người quản lý dự án, đi từ vấn đề thật → bản chất → nguyên lý → mô hình → quy trình → case → thực hành → phản hồi → công cụ → kết quả đo được.

---

## 0. Vấn đề thật trong dự án

### Tình huống mở đầu

Gia đình chuẩn bị xây hoặc cải tạo một ngôi nhà vườn ở miền Bắc. Mọi người đều muốn nhà mát, đẹp, nhiều cây, ít thấm, dễ chăm và đủ bền trong nhiều thập kỷ. Nhưng khi vào việc, mỗi bên nói một ngôn ngữ: chủ nhà nói về cảm giác sống, kiến trúc sư nói về không gian, kỹ sư nói về an toàn, nhà thầu nói về tiến độ, người làm vườn nói về cây và nước. Nếu không hiểu **{title.lower()}**, dự án dễ chọn giải pháp đẹp trên giấy nhưng yếu trong vận hành.

| Khía cạnh | Mô tả |
|---|---|
| Quyền hạn | Chủ nhà quyết định mục tiêu, ngân sách, ưu tiên và tiêu chí nghiệm thu; chuyên gia chịu trách nhiệm chuyên môn. |
| Áp lực | Muốn đẹp, muốn nhanh, muốn tiết kiệm, nhưng vẫn cần bền, an toàn và dễ bảo trì. |
| Giới hạn | Thiếu dữ kiện khu đất, thiếu ngôn ngữ kỹ thuật, dễ bị ảnh tham khảo hoặc báo giá rẻ dẫn dắt. |
| Hậu quả | Sai quyết định có thể tạo thấm, nóng, bí gió, úng cây, đội chi phí hoặc khó sửa sau khi hoàn thiện. |

**Một câu cần nhớ:** {purpose}

**Mục tiêu năng lực sau bài này:**

- Gọi đúng tên vấn đề liên quan đến {title.lower()}.
- Phân biệt điều quan sát được, diễn giải, giả thuyết và kết luận.
- Đặt được câu hỏi đúng cho chuyên gia hoặc nhà thầu.
- Chuyển hiểu biết thành checklist, quyết định hoặc yêu cầu nghiệm thu.
- Biết giới hạn của mình và thời điểm cần người có chuyên môn.

## 1. Bóc tách bản chất

| Lớp phân tích | Câu hỏi kiểm tra | Nhận định cho chủ nhà |
|---|---|---|
| Triệu chứng | Điều gì làm mình lo hoặc thích ngay lúc này? | Ảnh đẹp, cảm giác nóng, vết ẩm, báo giá, cây xanh, mặt bằng. |
| Nguyên nhân gần | Điều gì trực tiếp tạo ra triệu chứng? | Hướng nắng, đường nước, vật liệu, chi tiết, cách thi công, cách chăm. |
| Nguyên nhân gốc | Cơ chế nào lặp lại phía sau? | Khí hậu nóng ẩm, nước đi sai đường, thiếu khoảng đệm, thiếu hồ sơ, thiếu bảo trì. |
| Hệ thống | Ai quyết định, ai thi công, ai kiểm tra, ai vận hành? | Nếu không rõ trách nhiệm, lỗi sẽ bị đẩy qua lại. |
| Đánh đổi | Được cái này thì mất gì? | Mở nhiều có thể mát nhưng giảm riêng tư; trồng nhiều có thể đẹp nhưng tăng chăm sóc. |

**Bản chất:** {title} là một phần của hệ nhà - vườn - khí hậu - con người - kỹ thuật. Nó không nên được xử lý như một hạng mục cô lập.

**Cơ chế:** Một ngôi nhà vườn Bắc Bộ vận hành tốt khi nước được dẫn đúng đường, nhiệt được giảm từ nguồn, gió đi qua nơi cần đi, vật liệu chịu được ẩm, cây có điều kiện sống, và gia đình có khả năng chăm sóc thực tế.

## 2. Nguyên lý cốt lõi

{chr(10).join(principle_rows)}

## 3. Mô hình tư duy

| Thành phần mô hình | Câu hỏi người học cần tự hỏi | Dấu hiệu cần quan sát |
|---|---|---|
| Điều kiện thật | Khu đất, khí hậu, gia đình và ngân sách đang đặt giới hạn gì? | Nắng, gió, nước, cao độ, thói quen, người chăm. |
| Hệ khó sửa | Quyết định này có bị che khuất sau khi thi công không? | Móng, kết cấu, mái, ống, dây, chống thấm, đất trồng. |
| Tác động vòng đời | Sau 1, 5, 10, 30 năm điều gì thay đổi? | Vật liệu lão hóa, cây lớn, gia đình đổi nhu cầu, thiết bị hết tuổi. |
| Người chịu trách nhiệm | Ai thiết kế, ai kiểm tra, ai vận hành, ai trả chi phí? | Hợp đồng, hồ sơ, biên bản, lịch bảo trì. |
| Bằng chứng | Quyết định dựa trên dữ kiện nào? | Bản vẽ, khảo sát, thử nước, ảnh, mẫu vật liệu, báo giá rõ phạm vi. |

### Điều thường bị hiểu sai

| Hiểu sai | Vì sao dễ mắc | Cách hiểu đúng hơn |
|---|---|---|
| Chỉ cần xem mẫu đẹp là làm được | Ảnh không cho thấy khí hậu, chi tiết, chi phí và bảo trì. | Dùng ảnh để nói cảm giác, nhưng quyết định bằng điều kiện thật. |
| Nhà vườn là trồng nhiều cây | Cây xanh tạo cảm giác nhiệt đới nhanh. | Vườn là hệ đất, nước, tầng cây, ánh sáng, chăm sóc và thời gian. |
| Có thể sửa sau | Một số lỗi bị che khuất và sửa rất tốn kém. | Xác định sớm hạng mục phải đúng ngay từ đầu. |

## 4. Quy trình hành động

| Bước | Việc cần làm | Câu hỏi cần hỏi | Đầu ra | Lỗi thường gặp |
|---|---|---|---|---|
| 1 | Ghi điều quan sát được trong dự án thật. | Tôi thấy gì, đo gì, chụp gì, nghe gì? | Nhật ký quan sát có ảnh và ngày giờ. | Nhảy ngay sang kết luận. |
| 2 | Xác định cơ chế liên quan. | Vấn đề thuộc nước, nhiệt, gió, vật liệu, cây, người hay quy trình? | Một giả thuyết có thể kiểm chứng. | Gộp mọi thứ thành cảm giác chung. |
| 3 | Hỏi chuyên gia đúng vai trò. | Ai đủ năng lực trả lời phần này? | Câu hỏi gửi kiến trúc sư/kỹ sư/nhà thầu/cảnh quan. | Hỏi sai người rồi lấy làm kết luận. |
| 4 | Chọn phương án theo tiêu chí. | Phương án nào bền, sửa được, vừa ngân sách, hợp vận hành? | Quyết định có lý do và đánh đổi. | Chọn theo giá rẻ hoặc hình ảnh. |
| 5 | Gắn vào nghiệm thu hoặc bảo trì. | Làm sao biết đã đúng sau khi thi công hoặc sau khi ở? | Checklist kiểm tra và lịch theo dõi. | Không có bằng chứng hoàn thành. |

## 5. Case thực chiến

| Thành phần | Nội dung |
|---|---|
| Bối cảnh | Khu đất ngoại thành miền Bắc, gia đình muốn nhà mở ra vườn, dùng lâu dài cho ba thế hệ. |
| Nhân vật/vai trò | Chủ nhà giữ ngân sách; kiến trúc sư đề xuất không gian; kỹ sư lo an toàn; nhà thầu muốn tiến độ; người chăm vườn chỉ có mặt vài buổi mỗi tuần. |
| Dữ kiện đang có | Ảnh tham khảo, kích thước đất, hướng nắng, mong muốn nhiều cây và hiên rộng. |
| Dữ kiện còn thiếu | Cao độ thoát nước, khảo sát đất, năng lực bảo trì, chi phí vòng đời, chi tiết vật liệu. |
| Mâu thuẫn lợi ích | Muốn mở nhiều ra vườn nhưng cần riêng tư, chống mưa tạt, chống nồm và an ninh. |
| Áp lực thời gian | Muốn khởi công sớm trước mùa mưa. |
| Quyết định phải đưa ra | Có khóa phương án liên quan đến {title.lower()} ngay bây giờ hay cần thêm kiểm chứng? |
| Rủi ro nếu chọn sai | Phát sinh sửa chữa, giảm tiện nghi, tăng bảo trì hoặc tạo lỗi khó sửa. |

### Phân tích case

| Câu hỏi | Trả lời gợi ý |
|---|---|
| Vấn đề thật là gì? | Chưa chuyển mong muốn sống thành quyết định có bằng chứng. |
| Triệu chứng là gì? | Nhiều ý tưởng hấp dẫn nhưng chưa rõ cái nào hợp khu đất và vòng đời. |
| Nguyên nhân gốc là gì? | Thiếu mô hình kiểm tra giữa khí hậu, kỹ thuật, cảnh quan và vận hành. |
| Mô hình nào giúp nhìn rõ hơn? | Điều kiện thật → hệ khó sửa → vòng đời → trách nhiệm → bằng chứng. |
| Có những phương án nào? | Khóa quyết định; trì hoãn để khảo sát; làm thử mẫu; chia giai đoạn. |
| Đánh đổi của từng phương án là gì? | Nhanh hơn nhưng rủi ro hơn; chậm hơn nhưng có bằng chứng tốt hơn. |

## 6. Thực hành có phản hồi

```text
Tình huống dự án thật:
Dữ kiện quan sát:
Diễn giải có thể:
Giả thuyết cần kiểm chứng:
Chuyên gia cần hỏi:
Phương án quyết định:
Lý do chọn:
Rủi ro nếu dùng sai:
Hành động tiếp theo:
Khi nào cần dừng để kiểm tra:
```

### Rubric phản hồi

| Tiêu chí | Chưa đạt | Đạt | Xuất sắc |
|---|---|---|---|
| Gọi tên vấn đề | Nói chung chung là “chưa đẹp/chưa ổn”. | Nêu đúng hạng mục và rủi ro. | Gắn hạng mục với cơ chế khí hậu, kỹ thuật, vận hành. |
| Phân biệt dữ kiện và suy đoán | Lẫn cảm giác với kết luận. | Tách quan sát và giả thuyết. | Nêu cách kiểm chứng từng giả thuyết. |
| Dùng mô hình | Chọn theo cảm tính. | Dùng vài tiêu chí rõ. | So sánh phương án theo vòng đời và trách nhiệm. |
| Ra quyết định | Không có tiêu chí. | Có quyết định và lý do. | Có cả đánh đổi, điều kiện dừng và bằng chứng nghiệm thu. |
| Quản trị rủi ro | Bỏ qua lỗi khó sửa. | Nhận ra rủi ro chính. | Gắn rủi ro với chuyên gia, hồ sơ, thử nghiệm hoặc bảo trì. |

## 7. Công cụ mang về dùng ngay

### Checklist {file_ref}

| Việc cần làm | Đã có chưa | Ghi chú |
|---|---|---|
| Có ảnh, số đo hoặc quan sát thực tế liên quan đến {title.lower()} |  |  |
| Có câu hỏi gửi đúng chuyên gia |  |  |
| Có ít nhất hai phương án và đánh đổi |  |  |
| Có tiêu chí nghiệm thu hoặc theo dõi sau khi ở |  |  |
| Có ghi vào nhật ký quyết định dự án |  |  |

## 8. Giới hạn và khi cần chuyên gia

{public_warning()}

Riêng với bài này, cần ưu tiên hỏi chuyên gia khi quyết định ảnh hưởng đến an toàn, kết cấu, chống thấm, điện nước, pháp lý, cây lớn, thoát nước hoặc chi phí lớn khó đảo ngược.

## 9. Kết quả đo được

Sau module này, bạn nên tạo được một trang ghi chú dự án gồm: vấn đề liên quan đến **{title}**, dữ kiện đã có, câu hỏi cần hỏi, phương án đang cân nhắc, rủi ro chính, tiêu chí nghiệm thu và hành động tiếp theo.
"""


def make_build_script():
    current_build_script = ROOT / "build_platform_html.py"
    if current_build_script.exists():
        return current_build_script.read_text(encoding="utf-8")
    return r'''
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parent

ORDER = [
    "README.md",
    "ban-do-nha-vuon-bac-bo.md",
    "giao-trinh-nha-vuon-bac-bo.md",
    "thuat-ngu-nha-vuon-bac-bo.md",
    "cong-cu-thuc-hanh.md",
]
ORDER.extend(sorted(p.name for p in ROOT.glob("Module-*.md")))


def anchor(text):
    text = text.lower()
    repl = {
        "à":"a","á":"a","ạ":"a","ả":"a","ã":"a","â":"a","ầ":"a","ấ":"a","ậ":"a","ẩ":"a","ẫ":"a","ă":"a","ằ":"a","ắ":"a","ặ":"a","ẳ":"a","ẵ":"a",
        "è":"e","é":"e","ẹ":"e","ẻ":"e","ẽ":"e","ê":"e","ề":"e","ế":"e","ệ":"e","ể":"e","ễ":"e",
        "ì":"i","í":"i","ị":"i","ỉ":"i","ĩ":"i",
        "ò":"o","ó":"o","ọ":"o","ỏ":"o","õ":"o","ô":"o","ồ":"o","ố":"o","ộ":"o","ổ":"o","ỗ":"o","ơ":"o","ờ":"o","ớ":"o","ợ":"o","ở":"o","ỡ":"o",
        "ù":"u","ú":"u","ụ":"u","ủ":"u","ũ":"u","ư":"u","ừ":"u","ứ":"u","ự":"u","ử":"u","ữ":"u",
        "ỳ":"y","ý":"y","ỵ":"y","ỷ":"y","ỹ":"y","đ":"d",
    }
    text = "".join(repl.get(ch, ch) for ch in text)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "section"


def inline_md(text):
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def parse_table(lines):
    rows = []
    for line in lines:
        cells = [inline_md(c.strip()) for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return ""
    head = rows[0]
    body = rows[2:] if len(rows) > 1 and all(set(c.strip()) <= {"-", ":"} for c in rows[1]) else rows[1:]
    html = ["<div class='table-wrap'><table><thead><tr>"]
    html.extend(f"<th>{c}</th>" for c in head)
    html.append("</tr></thead><tbody>")
    for row in body:
        html.append("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>")
    html.append("</tbody></table></div>")
    return "".join(html)


def md_to_html(markdown, section_id):
    out = []
    lines = markdown.splitlines()
    i = 0
    in_ul = False
    in_ol = False
    in_code = False
    code_lines = []
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                out.append("<pre><code>" + escape("\n".join(code_lines)) + "</code></pre>")
                in_code = False
            i += 1
            continue
        if in_code:
            code_lines.append(line)
            i += 1
            continue
        if stripped.startswith("|") and i + 1 < len(lines) and lines[i + 1].strip().startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            out.append(parse_table(table_lines))
            continue
        if not stripped:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_ol:
                out.append("</ol>")
                in_ol = False
            i += 1
            continue
        if stripped.startswith("#"):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_ol:
                out.append("</ol>")
                in_ol = False
            level = len(stripped) - len(stripped.lstrip("#"))
            text = stripped[level:].strip()
            hid = f"{section_id}-{anchor(text)}"
            out.append(f"<h{min(level, 4)} id='{hid}'>{inline_md(text)}</h{min(level, 4)}>")
        elif stripped.startswith("- "):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_md(stripped[2:])}</li>")
        elif re.match(r"^\d+\.\s+", stripped):
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_md(re.sub(r'^\d+\.\s+', '', stripped))}</li>")
        elif stripped == "---":
            out.append("<hr>")
        else:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if in_ol:
                out.append("</ol>")
                in_ol = False
            out.append(f"<p>{inline_md(stripped)}</p>")
        i += 1
    if in_ul:
        out.append("</ul>")
    if in_ol:
        out.append("</ol>")
    return "\n".join(out)


def first_heading(text):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Tài liệu"


def build():
    docs = []
    for name in ORDER:
        path = ROOT / name
        if path.exists():
            text = path.read_text(encoding="utf-8")
            title = first_heading(text)
            sid = anchor(name.replace(".md", ""))
            docs.append((name, title, sid, md_to_html(text, sid)))

    nav = "\n".join(f"<a href='#{sid}'>{escape(title)}</a>" for _, title, sid, _ in docs)
    articles = "\n".join(f"<article id='{sid}' class='doc'>{html}</article>" for _, _, sid, html in docs)
    module_count = len([d for d in docs if d[0].startswith("Module-")])
    html = f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Nền Tảng Học Thiết Kế Nhà Và Vườn Nhiệt Đới Bắc Bộ</title>
  <style>
    :root {{
      --bg: #f4f6f5;
      --paper: #ffffff;
      --text: #1f2423;
      --muted: #63706c;
      --line: #d8dfdc;
      --accent: #276749;
      --accent-2: #9a5b3d;
      --soft: #e8f0ec;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.65;
      letter-spacing: 0;
    }}
    header {{
      border-bottom: 1px solid var(--line);
      background: rgba(255,255,255,.96);
      position: sticky;
      top: 0;
      z-index: 5;
      backdrop-filter: blur(16px);
    }}
    .top {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 18px 28px;
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 20px;
      align-items: center;
    }}
    h1, h2, h3, h4 {{ line-height: 1.2; letter-spacing: 0; }}
    .brand h1 {{ font-size: clamp(22px, 3vw, 38px); margin: 0 0 6px; }}
    .brand p {{ margin: 0; color: var(--muted); max-width: 860px; }}
    .stats {{ display: flex; gap: 10px; flex-wrap: wrap; justify-content: flex-end; }}
    .stat {{ border: 1px solid var(--line); border-radius: 8px; padding: 8px 12px; background: var(--soft); min-width: 100px; }}
    .stat strong {{ display: block; font-size: 20px; }}
    .layout {{
      max-width: 1400px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 310px minmax(0, 1fr);
      gap: 34px;
      padding: 26px 28px 80px;
    }}
    nav {{
      position: sticky;
      top: 96px;
      align-self: start;
      max-height: calc(100vh - 120px);
      overflow: auto;
      border-right: 1px solid var(--line);
      padding-right: 18px;
    }}
    nav a {{
      display: block;
      color: var(--text);
      text-decoration: none;
      padding: 7px 8px;
      border-radius: 6px;
      font-size: 14px;
    }}
    nav a:hover {{ background: var(--soft); color: var(--accent); }}
    main {{ min-width: 0; }}
    .doc {{
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: clamp(22px, 4vw, 54px);
      margin-bottom: 24px;
      box-shadow: 0 18px 50px rgba(29, 43, 38, .06);
    }}
    .doc h1 {{ margin-top: 0; font-size: clamp(30px, 5vw, 58px); }}
    .doc h2 {{ margin-top: 44px; padding-top: 16px; border-top: 1px solid var(--line); font-size: 28px; }}
    .doc h3 {{ margin-top: 28px; color: var(--accent); }}
    p, li {{ font-size: 16px; }}
    code, pre {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
    pre {{ overflow: auto; background: #1f261f; color: #f7f1e7; padding: 16px; border-radius: 8px; }}
    .table-wrap {{ overflow-x: auto; margin: 18px 0; border: 1px solid var(--line); border-radius: 8px; }}
    table {{ width: 100%; border-collapse: collapse; min-width: 720px; background: #fff; }}
    th, td {{ padding: 11px 12px; border-bottom: 1px solid var(--line); vertical-align: top; text-align: left; }}
    th {{ background: var(--soft); color: #173d2a; font-weight: 700; }}
    tr:last-child td {{ border-bottom: 0; }}
    hr {{ border: 0; border-top: 1px solid var(--line); margin: 28px 0; }}
    @media (max-width: 900px) {{
      .top {{ grid-template-columns: 1fr; }}
      .stats {{ justify-content: flex-start; }}
      .layout {{ grid-template-columns: 1fr; padding: 18px 14px 50px; }}
      nav {{ position: static; max-height: 260px; border: 1px solid var(--line); border-radius: 8px; padding: 10px; background: var(--paper); }}
      .doc {{ padding: 22px 16px; }}
      table {{ min-width: 640px; }}
    }}
    @media print {{
      header, nav {{ display: none; }}
      .layout {{ display: block; padding: 0; }}
      .doc {{ box-shadow: none; border: 0; page-break-after: always; }}
      body {{ background: white; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="top">
      <div class="brand">
        <h1>Nền Tảng Học Thiết Kế Nhà Và Vườn Nhiệt Đới Bắc Bộ</h1>
        <p>Học toàn dự án từ ý tưởng, thiết kế, thi công, vận hành đến bảo trì 30-50 năm.</p>
      </div>
      <div class="stats">
        <div class="stat"><strong>{module_count}</strong>module</div>
        <div class="stat"><strong>8</strong>phần học</div>
        <div class="stat"><strong>30-50</strong>năm vòng đời</div>
      </div>
    </div>
  </header>
  <div class="layout">
    <nav aria-label="Mục lục">{nav}</nav>
    <main>{articles}</main>
  </div>
</body>
</html>"""
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"Đã dựng index.html với {len(docs)} tài liệu, gồm {module_count} module.")


if __name__ == "__main__":
    build()
'''


def main():
    write("README.md", make_readme())
    write("ban-do-nha-vuon-bac-bo.md", make_map())
    write("giao-trinh-nha-vuon-bac-bo.md", make_syllabus())
    write("thuat-ngu-nha-vuon-bac-bo.md", make_glossary())
    write("cong-cu-thuc-hanh.md", make_tools())
    for mod in MODULES:
        num, phase, title, purpose = mod
        write(module_filename(num, title), make_module(num, phase, title, purpose))
    write("build_platform_html.py", make_build_script())


if __name__ == "__main__":
    main()
