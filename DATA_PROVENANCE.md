# Data provenance

`data/model2_conditional_volatility.csv` được sao chép từ:

- Repository: `htrang22/btc-sjc-vnindex-risk-analysis`
- Branch nguồn: `tvp-var`
- Commit nguồn: `ef9f974b950610656642cf496c04e8101474d47b`
- Đường dẫn nguồn: `outputs/model2_conditional_volatility.csv`

File gồm 747 quan sát conditional volatility của BTC, vàng SJC và VN-Index,
được tạo từ bước ARMA–EGARCH của nghiên cứu gốc. Dữ liệu này được giữ nguyên
trong repository mới để các TVP-VAR specifications có thể chạy độc lập và cho
kết quả có thể tái lập.

Ngày 26/08/2026, notebook nguồn đã được chạy lại từ kernel sạch bằng
`scripts/rebuild_model2_input.py`. Cell export được chuyển hướng sang repo mới
để không sửa repository bài đã nộp. File tái tạo có SHA-256:

```text
2a568ac70f1db0e34d9aa418e20bca899c04693a4071d6545e5e6086bd458a0c
```

Checksum này trùng với CSV đã được chuyển sang repo mới trước đó.
