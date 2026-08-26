# BTC–SJC–VN-Index TVP-VAR Connectedness

Repository này phát triển phần **TVP-VAR connectedness** từ nghiên cứu
[`btc-sjc-vnindex-risk-analysis`](https://github.com/htrang22/btc-sjc-vnindex-risk-analysis).
Repository gốc được giữ nguyên như phiên bản bài tập đã nộp; repository này dành
cho việc refactor mô hình, so sánh specifications và thực hiện robustness.

## Câu hỏi nghiên cứu

Mô hình static VAR–GFEVD/Diebold–Yılmaz trong nghiên cứu gốc mô tả cấu trúc lan
truyền trung bình trong toàn mẫu. Phần mở rộng này dùng TVP-VAR(1) để nghiên cứu:

- connectedness thay đổi như thế nào theo thời gian;
- BTC, vàng SJC và VN-Index chuyển đổi vai trò transmitter/receiver khi nào;
- kết luận có bền vững trước lựa chọn coefficient forgetting factor hay không.

TVP-VAR là **extension/alternative specification**, không thay thế static VAR-DY.

## Specifications hiện có

| Tên | λβ | κσ | p | H | Vai trò |
|---|---:|---:|---:|---:|---|
| `baseline_0999` | 0.999 | 0.96 | 1 | 10 | Baseline |
| `robustness_0997` | 0.997 | 0.96 | 1 | 10 | Robustness |

Mọi tham số ngoài `λβ` được giữ cố định để comparison có ý nghĩa.

## Cấu trúc

```text
btc-sjc-vnindex-tvp-connectedness/
├── data/
│   └── model2_conditional_volatility.csv
├── src/tvp_connectedness/
│   ├── model.py           # TVP-VAR(1), forgetting-factor Kalman filter
│   ├── diagnostics.py     # Spectral radius và unstable episodes
│   ├── gfevd.py           # Time-varying generalized FEVD
│   ├── connectedness.py   # TCI, FROM, TO và NET
│   ├── pipeline.py        # Chạy và so sánh specifications
│   └── io.py              # Đọc dữ liệu và lưu kết quả
├── notebooks/
│   └── model_comparison.ipynb
├── outputs/
│   ├── baseline_0999/
│   ├── robustness_0997/
│   └── specification_comparison.csv
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

## Chạy toàn bộ comparison

```bash
python run_analysis.py
```

Lệnh này chạy hai specifications độc lập, in bảng comparison và lưu TCI, FROM,
TO, NET, stability cùng unstable episodes vào `outputs/`.

## Chạy tests

```bash
python -m unittest discover -s tests
```

Regression tests kiểm tra module mới tái tạo đúng các kết quả đã có trong
notebook: baseline `λβ=0.999` và robustness `λβ=0.997`.

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

Mỗi specification trả về object riêng, nên kết quả không bị ghi đè bởi trạng
thái kernel như khi toàn bộ pipeline được viết nối tiếp bằng nhiều cell.

## Dữ liệu

`data/model2_conditional_volatility.csv` chứa conditional volatility của BTC,
SJC và VN-Index được tạo từ bước ARMA–EGARCH trong nghiên cứu gốc. File được
đưa sang repository này để mô hình TVP-VAR có thể chạy độc lập.

## Diễn giải robustness hiện tại

Hai specifications giữ nguyên kết luận trung bình toàn mẫu: BTC và SJC là net
transmitters, còn VN-Index là net receiver. Tuy nhiên, vai trò cuối mẫu nhạy hơn
với `λβ`, đặc biệt đối với VN-Index. Baseline `0.999` cũng có tỷ lệ local
stability cao hơn, nên tiếp tục được dùng làm specification chính.
