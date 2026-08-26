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
| `kappa_094` | 0.999 | 0.94 | 1 | 10 | κσ sensitivity |
| `kappa_098` | 0.999 | 0.98 | 1 | 10 | κσ sensitivity |
| `horizon_05` | 0.999 | 0.96 | 1 | 5 | Horizon sensitivity |
| `horizon_20` | 0.999 | 0.96 | 1 | 20 | Horizon sensitivity |

Trong từng sensitivity check, chỉ tham số đang được kiểm tra thay đổi; các tham
số còn lại được giữ cố định.

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

## Chạy toàn bộ comparison

```bash
python run_analysis.py
```

Lệnh này chạy sáu specifications độc lập, in bảng comparison và lưu TCI, FROM,
TO, NET, stability, từng unstable observation và unstable episodes vào
`outputs/`.

## Chạy notebook từ kernel sạch

Trong Jupyter chọn **Kernel → Restart Kernel and Run All Cells**, hoặc chạy:

```bash
python -m jupyter nbconvert \
  --to notebook --execute --inplace \
  notebooks/model_comparison.ipynb
```

Notebook trong repo đã được restart và chạy toàn bộ từ đầu sau khi thêm các
robustness checks.

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

Để tái tạo lại CSV từ notebook nguồn mà không sửa repo bài đã nộp:

```bash
python scripts/rebuild_model2_input.py /path/to/btc-sjc-vnindex-risk-analysis
```

Script chạy notebook nguồn trong kernel mới và chuyển cell export sang
`data/model2_conditional_volatility.csv` của repo này. Lần kiểm tra hiện tại cho
checksum trùng khớp với CSV đã lưu; xem `DATA_PROVENANCE.md`.

## Diễn giải robustness hiện tại

Hai specifications giữ nguyên kết luận trung bình toàn mẫu: BTC và SJC là net
transmitters, còn VN-Index là net receiver. Tuy nhiên, vai trò cuối mẫu nhạy hơn
với `λβ`, đặc biệt đối với VN-Index. Baseline `0.999` cũng có tỷ lệ local
stability cao hơn, nên tiếp tục được dùng làm specification chính.

Sensitivity của `κσ` cho thấy vai trò trung bình vẫn giữ nguyên, nhưng mức TCI
nhạy với tốc độ cập nhật covariance. Mean TCI lần lượt là 9,4555%, 7,9241% và
5,9812% với `κσ=0.94, 0.96, 0.98`.

Horizon sensitivity cho thấy connectedness tích lũy tăng theo kỳ dự báo: Mean
TCI là 5,0289%, 7,9241% và 13,2622% tại `H=5, 10, 20`.

## Local stability

Baseline có 14/747 quan sát với spectral radius ≥ 1, tập trung thành ba episode:

| Bắt đầu | Kết thúc | Số quan sát | Max radius |
|---|---|---:|---:|
| 29/11/2023 | 29/11/2023 | 1 | 1,0134 |
| 26/12/2023 | 10/01/2024 | 11 | 1,0269 |
| 15/01/2024 | 16/01/2024 | 2 | 1,0030 |

TCI trung bình trong các ngày local instability là 14,7108%, so với 7,7945%
trong các ngày stable. Các điểm vượt unit circle vì vậy không rải ngẫu nhiên mà
tập trung quanh một giai đoạn connectedness cao. Do GFEVD được tính tại horizon
hữu hạn, các episode này được giữ lại và báo cáo minh bạch như một diagnostic;
không được diễn giải như bằng chứng rằng mô hình ổn định vô điều kiện.
