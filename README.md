# ZORA MCP Service 🛰

_MCP Service – Standalone API Service for ZORA AI_  
Cung cấp các API tiện ích cho ZORA AI:

- 🌤 Weather – Thời tiết theo thành phố (Việt Nam)
- 🕒 Time – Thời gian hiện tại theo quốc gia
- 👤 Owner Info – Thông tin người tạo ZORA
- 🧰 Tools – Danh sách tool để LLM/Agent có thể gọi

Service được xây dựng bằng **FastAPI**, dùng như một **MCP-like tool backend** cho hệ thống AI Agent (ví dụ: ZORA AI).

---

## 🚀 Tính năng chính

### 1. Weather API – `/api/weather`
- Lấy **thời tiết hiện tại** theo **tên thành phố ở Việt Nam**
- Dùng **Open-Meteo API** (không cần API key)
- Trả về:
  - Nhiệt độ
  - Độ ẩm
  - Tốc độ gió
  - Mã thời tiết (WMO)
  - Mô tả tiếng Việt
  - Emoji 🌧️☀️⛈️…

### 2. Time API – `/api/time`
- Lấy **thời gian hiện tại** theo **quốc gia**
- Mapping sẵn một số nước phổ biến: `Vietnam, USA, Japan, China, Singapore, Thailand, South Korea, Australia, France, Germany, ...`
- Trả về:
  - Giờ hiện tại
  - Ngày
  - Timezone
  - Timestamp ISO

### 3. Owner Info API – `/api/owner`
- Trả về thông tin về **người tạo ZORA AI**:
  - Tên
  - Số điện thoại
  - Email
  - Vai trò
  - Bio
  - Danh sách kỹ năng

### 4. Tools API – `/api/tools`
- Trả về danh sách các **tool** mà LLM/Agent có thể gọi:
  - `get_weather`
  - `get_time`
  - `get_owner_info`
- Kèm đầy đủ:
  - endpoint
  - method
  - parameters
  - keywords
  - example

---

## 🧱 Cấu trúc code chính

File chính: `main.py` (hoặc tên bạn đang dùng)

- Khởi tạo app:
  ```python
  app = FastAPI(
      title="ZORA MCP Service",
      description="Model Context Protocol Service for ZORA AI - Weather, Time & Owner Info",
      version="1.0.0"
  )
