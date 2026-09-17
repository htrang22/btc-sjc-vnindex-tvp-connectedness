# BTC–SJC–VN-Index TVP-VAR Connectedness

Nghiên cứu này phát triển phân tích **mức độ kết nối dựa trên TVP-VAR** từ nghiên cứu
[`btc-sjc-vnindex-risk-analysis`](https://github.com/htrang22/btc-sjc-vnindex-risk-analysis).
Repository gốc được giữ nguyên như phiên bản nghiên cứu đã hoàn thành; repository
hiện tại mở rộng mô hình, so sánh các đặc tả và thực hiện kiểm định độ vững.

## Câu hỏi nghiên cứu

Mô hình VAR–GFEVD/Diebold–Yılmaz với tham số cố định trong nghiên cứu gốc mô tả
cấu trúc lan truyền đại diện cho toàn bộ mẫu. Phần mở rộng này sử dụng TVP-VAR(1)
để nghiên cứu:

- mức độ kết nối thay đổi như thế nào theo thời gian;
- thời điểm BTC, vàng SJC và VN-Index chuyển đổi vai trò transmitter/receiver;
- mức độ bền vững của kết luận trước lựa chọn hệ số quên của phương trình hệ số
  và ma trận hiệp phương sai.

TVP-VAR là **phần mở rộng động theo thời gian** của phân tích gốc, không phủ định
hoặc thay thế các kết quả từ mô hình VAR với tham số cố định.

## Quan hệ với nghiên cứu gốc: VAR và TVP-VAR

Hai nghiên cứu trả lời các câu hỏi bổ sung cho nhau trên cùng ba chuỗi biến động
có điều kiện được ước lượng từ ARMA-EGARCH. Nghiên cứu ban đầu sử dụng VAR(9) với hệ
số cố định, sau đó tính GFEVD và các chỉ số Diebold-Yılmaz tại từng kỳ dự báo.
Kết quả vì vậy phản ánh một cấu trúc lan truyền duy nhất, đại diện cho toàn bộ
giai đoạn thời gian của mẫu. Nghiên cứu hiện tại sử dụng TVP-VAR(1), cho phép hệ số và ma trận hiệp
phương sai thay đổi theo thời gian; GFEVD, TCI, FROM, TO và NET do đó được tính
tại từng thời điểm. Giá trị trung bình của các chỉ số TVP-VAR tóm tắt quỹ đạo
động, còn giá trị cuối mẫu chỉ mô tả trạng thái tại quan sát cuối cùng. Hai đại
lượng này không tương đương với ước lượng VAR cố định trên toàn mẫu.

| Khía cạnh | VAR–GFEVD/Diebold–Yılmaz trong nghiên cứu gốc | TVP-VAR–GFEVD trong nghiên cứu này |
|---|---|---|
| Cấu trúc tham số | VAR(9), hệ số cố định trong toàn mẫu | TVP-VAR(1), hệ số và hiệp phương sai thay đổi theo thời gian |
| Nội dung nhận diện | Mức độ và hướng lan truyền đại diện cho toàn mẫu tại mỗi horizon | Quỹ đạo theo thời gian của mức độ và hướng lan truyền; đồng thời báo cáo trung bình toàn mẫu |
| TCI tại `H=5, 10, 20` | `1,4520%`; `4,1672%`; `7,6270%` | TCI trung bình: `5,0289%`; `7,9241%`; `13,2622%` |
| Vai trò NET tại `H=5` | SJC là transmitter; BTC và VN-Index là receiver | Trung bình toàn mẫu: BTC và SJC là transmitter; VN-Index là receiver |
| Vai trò NET tại `H=10` | VN-Index là transmitter; BTC và SJC là receiver | Trung bình toàn mẫu: BTC và SJC là transmitter; VN-Index là receiver |
| Vai trò NET tại `H=20` | VN-Index là transmitter; BTC và SJC là receiver | Trung bình toàn mẫu: BTC và SJC là transmitter; VN-Index là receiver |

Sự khác biệt về dấu của NET không phải là bằng chứng cho thấy kết quả cũ sai.
Mô hình VAR cố định gộp toàn bộ giai đoạn thành một hệ tham số, trong khi TVP-VAR cho phép vai trò truyền–nhận thay đổi giữa các thời điểm rồi mới lấy trung bình.
Ở mô hình TVP-VAR cơ sở (`H=10`), NET trung bình của BTC, SJC và VN-Index lần lượt là `2,8759`, `2,2210` và `-5,0969`; nhưng tại cuối mẫu, các giá trị tương ứng là `-1,5648`, `1,9368` và `-0,3720`. 

Điều này cho thấy BTC chuyển từ transmitter trung bình toàn mẫu sang receiver tại cuối mẫu, còn SJC duy trì vai trò transmitter và VN-Index vẫn là receiver. Đối chiếu này làm rõ đóng góp của TVP-VAR: bổ sung chiều thời gian và nhận diện sự chuyển đổi vai trò mà ước lượng VAR cố định không được thiết kế để thể hiện.

BTC: từ transmitter → receiver
Trong phần lớn giai đoạn mẫu, BTC là kênh phát tán biến động ra các tài sản khác về mặt thống kê. Có thể diễn giải do tính chất giao dịch liên tục 24/7 và phản ứng nhanh với các yếu tố vĩ mô toàn cầu (thanh khoản USD, kỳ vọng lãi suất, tâm lý risk-on/risk-off toàn cầu) mà BCT đóng vai trò như một chỉ báo sớm của biến động vĩ mô, các yếu tố này sau đó cũng ảnh hưởng đến tỷ giá, giá vàng trong nước, dòng vốn ngoại vào VN-Index với độ trễ khác nhau. 

Tuy nhiên BTC chuyển sang receiver ở cuối mẫu chứng tỏ mối liên kết giữa BTC và các tài sản khác không cố định.

SJC (vàng): duy trì vai trò transmitter
Vàng trong nước tiếp tục là nguồn phát tán biến động ổn định xuyên suốt - phù hợp với vai trò truyền thống của vàng như một "tài sản neo" phản ứng với các cú sốc vĩ mô (tỷ giá, lạm phát, bất ổn địa chính trị) rồi truyền ảnh hưởng sang các tài sản khác qua kỳ vọng của nhà đầu tư trong nước. Việc vai trò này không đổi theo thời gian cho thấy vàng có vị trí tương đối bền vững, ít nhạy với các chu kỳ ngắn hạn của thị trường crypto hay chứng khoán.

VN-Index: duy trì vai trò receiver
Chứng khoán Việt Nam liên tục là bên tiếp nhận biến động - hàm ý thị trường chứng khoán trong nước dễ bị ảnh hưởng bởi các cú sốc từ bên ngoài (vàng, crypto, hoặc gián tiếp là dòng vốn/tâm lý toàn cầu) hơn là chủ động lan tỏa rủi ro ra các thị trường khác. Điều này phù hợp với đặc điểm một thị trường mới nổi, quy mô vốn hóa còn nhỏ so với dòng vốn toàn cầu, nên thường ở vị thế "hấp thụ" cú sốc.

## Các đặc tả được xem xét

| Tên | λβ | κσ | p | H | Vai trò |
|---|---:|---:|---:|---:|---|
| `baseline_0999` | 0.999 | 0.96 | 1 | 10 | Đặc tả cơ sở |
| `robustness_0997` | 0.997 | 0.96 | 1 | 10 | Kiểm định độ vững |
| `kappa_094` | 0.999 | 0.94 | 1 | 10 | Độ nhạy theo κσ |
| `kappa_098` | 0.999 | 0.98 | 1 | 10 | Độ nhạy theo κσ |
| `horizon_05` | 0.999 | 0.96 | 1 | 5 | Độ nhạy theo kỳ dự báo |
| `horizon_20` | 0.999 | 0.96 | 1 | 20 | Độ nhạy theo kỳ dự báo |

Trong mỗi kiểm định độ nhạy, chỉ tham số được xem xét thay đổi; các tham số còn lại được giữ cố định.

## Phương pháp kiểm định độ vững được sử dụng
Phuơng pháp kiểm định độ vững của mô hình là phân tích độ nhạy tham số (parameter sensitivity analysis). Cơ chế: giữ nguyên mô hình, chỉ thay đổi một siêu tham số kỹ thuật tại một thời điểm, sau đó so sánh kết luận có thay đổi hay không. Nếu kết quả về dấu của NET, transmitter/receiver vẫn giữ nguyên qua các lựa chọn tham số khác nhau, thì kết luận được xem là vững.
Cụ thể có ba trục kiểm định:

1. Kiểm định theo λβ (forgetting factor của hệ số VAR)
So sánh kết quả giữa các giá trị λβ khác nhau (ví dụ 0,999 vs. một giá trị khác nhỏ hơn) — xem vai trò trung bình toàn mẫu và vai trò tại cuối mẫu có đổi dấu/đổi thứ hạng không.

2. Kiểm định theo κσ (forgetting factor của ma trận hiệp phương sai)
So sánh TCI và vai trò trung bình giữa κσ = 0,94 / 0,96 / 0,98 — xem độ lớn và dấu có ổn định không.

3. Kiểm định theo horizon dự báo H
So sánh TCI tại H = 5, 10, 20 — xem xu hướng kết luận có nhất quán không khi thay đổi độ dài horizon dùng trong GFEVD (generalized forecast error variance decomposition).

## Kết quả kiểm định độ vững và độ nhạy
Hai đặc tả theo `λβ` cho cùng kết luận về trung bình toàn mẫu: BTC và SJC là net transmitters, còn VN-Index là net receiver. Tuy nhiên, vai trò tại cuối mẫu nhạy hơn với `λβ`, đặc biệt đối với VN-Index. Đặc tả cơ sở `0.999` cũng có tỷ lệ ổn định cục bộ cao hơn nên tiếp tục được sử dụng làm đặc tả chính.

Phân tích độ nhạy theo `κσ` cho thấy vai trò trung bình không thay đổi, nhưng TCI nhạy với tốc độ cập nhật ma trận hiệp phương sai. TCI trung bình lần lượt là 9,4555%, 7,9241% và 5,9812% với `κσ=0.94, 0.96, 0.98`.

Phân tích độ nhạy theo kỳ dự báo cho thấy mức độ kết nối tích lũy tăng theo horizon: TCI trung bình là 5,0289%, 7,9241% và 13,2622% tại `H=5, 10, 20`.

## Ổn định cục bộ

Đặc tả cơ sở có 14/747 quan sát với bán kính phổ (max radius) ≥ 1, tập trung thành ba giai đoạn:

| Bắt đầu | Kết thúc | Số quan sát | Max radius |
|---|---|---:|---:|
| 29/11/2023 | 29/11/2023 | 1 | 1,0134 |
| 26/12/2023 | 10/01/2024 | 11 | 1,0269 |
| 15/01/2024 | 16/01/2024 | 2 | 1,0030 |

Trong tổng số 747 quan sát, chỉ có 14 quan sát (khoảng 1,9%) có bán kính phổ ≥ 1, tức là phần lớn thời gian mô hình ổn định cục bộ, chỉ một số ít thời điểm bị vượt ngưỡng.

TCI trung bình trong các ngày không ổn định cục bộ là 14,7108%, so với 7,7945% trong các ngày ổn định. Các điểm có bán kính phổ > 1 không phân bố ngẫu nhiên mà tập trung thành 3 cụm liên tiếp (cuối tháng 11/2023, cuối tháng 12/2023 - đầu tháng 1/2024, và giữa tháng 1/2024), hàm ý đây là một giai đoạn thị trường có biến động bất thường, không phải nhiễu thống kê rời rạc, mức độ kết nối cao.

Do GFEVD được tính tại horizon hữu hạn, các giai đoạn này được giữ lại và báo cáo như một kết quả chẩn đoán; chúng không được diễn giải như bằng chứng rằng mô hình ổn định vô điều kiện.

## Cấu trúc

```text
btc-sjc-vnindex-tvp-connectedness/
├── data/
│   └── model2_conditional_volatility.csv
├── src/tvp_connectedness/
│   ├── model.py           # TVP-VAR(1), forgetting-factor Kalman filter
│   ├── diagnostics.py     # Bán kính phổ và các giai đoạn không ổn định
│   ├── gfevd.py           # Time-varying generalized FEVD
│   ├── connectedness.py   # TCI, FROM, TO và NET
│   ├── pipeline.py        # Chạy và so sánh các đặc tả
│   └── io.py              # Đọc dữ liệu và lưu kết quả
├── notebooks/
│   └── model_comparison.ipynb
├── outputs/
│   ├── baseline_0999/
│   ├── robustness_0997/
│   ├── kappa_094/
│   ├── kappa_098/
│   ├── horizon_05/
│   ├── horizon_20/
│   └── specification_comparison.csv
├── scripts/
│   └── rebuild_model2_input.py
├── tests/
├── run_analysis.py
├── pyproject.toml
└── requirements.txt
```

## Cài đặt

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Chạy toàn bộ phân tích so sánh

```bash
python run_analysis.py
```

Lệnh này chạy độc lập sáu đặc tả, hiển thị bảng so sánh và lưu TCI, FROM, TO,
NET, chẩn đoán ổn định cục bộ, từng quan sát không ổn định và các giai đoạn
không ổn định vào `outputs/`.

## Chạy notebook từ kernel sạch

Trong Jupyter chọn **Kernel → Restart Kernel and Run All Cells**, hoặc chạy:

```bash
python -m jupyter nbconvert \
  --to notebook --execute --inplace \
  notebooks/model_comparison.ipynb
```

Notebook trong repository đã được khởi động lại kernel và chạy toàn bộ từ đầu
sau khi bổ sung các kiểm định độ vững.

## Chạy tests

```bash
python -m unittest discover -s tests
```

Các kiểm định hồi quy phần mềm xác nhận module mới tái tạo đúng kết quả đã có trong notebook đối với đặc tả cơ sở `λβ=0.999` và đặc tả kiểm định độ vững `λβ=0.997`.

## Cách dùng trong notebook

```python
from tvp_connectedness import (
    compare_specifications,
    load_volatility_data,
    run_specification,
)

data = load_volatility_data("../data/model2_conditional_volatility.csv")

baseline = run_specification(
    data,
    name="baseline_0999",
    lambda_beta=0.999,
)

robustness = run_specification(
    data,
    name="robustness_0997",
    lambda_beta=0.997,
)

compare_specifications([baseline, robustness])
```
## Dữ liệu

`data/model2_conditional_volatility.csv` chứa các chuỗi biến động có điều kiện của BTC, SJC và VN-Index được ước lượng bằng ARMA–EGARCH trong nghiên cứu gốc.
Tệp được đưa sang repository này để mô hình TVP-VAR có thể chạy độc lập.

Để tái tạo tệp CSV từ notebook nguồn mà không sửa đổi repository gốc:

```bash
python scripts/rebuild_model2_input.py /path/to/btc-sjc-vnindex-risk-analysis
```

Script chạy notebook nguồn trong kernel mới và chuyển kết quả từ cell xuất dữ liệu sang `data/model2_conditional_volatility.csv` của repository này. Lần kiểm tra hiện tại cho mã kiểm tra trùng khớp với tệp CSV đã lưu; xem `DATA_PROVENANCE.md`.
