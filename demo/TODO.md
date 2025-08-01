# 開發任務清單 (TODO) - v2

此清單根據 `prd.md` (v2) 文件產生，用於追蹤專案開發進度。

## 階段一：介面改造

- [ ] 修改 `main.py` 的主視窗佈局，改為左右分欄 (PanedWindow)。
- [ ] **左側**：將原有的下拉選單 (Combobox) 替換為支援複選的 `Listbox`。
- [ ] **右側**：建立一個 `Treeview` 元件，用於以表格形式顯示股票資訊。
- [ ] 設定 `Treeview` 的欄位標題，對應 `prd.md` 中指定的資訊欄位。

## 階段二：股票列表與選擇邏輯

- [ ] 維持現有的 `get_stocks_with_twstock()` 載入機制，但將結果填入新的 `Listbox` 中。
- [ ] 綁定 `Listbox` 的選擇事件 (`<<ListboxSelect>>`)，當使用者變更選擇時觸發一個函式。
- [ ] 該函式需要能獲取 `Listbox` 中所有被選取的項目。

## 階段三：多股資訊獲取與顯示

- [ ] 修改 `update_stock_data` 函式，使其能夠接收一個股票代碼**列表**。
- [ ] 修改背景工作函式 `_fetch_stock_data_worker`，使其可以非同步地處理多個 URL。
- [ ] **(重要)** 確保 `get_stock_data` 能夠並行處理多個請求，以提高效率。
- [ ] 當資料獲取成功後，更新 `Treeview` 的內容。先清除舊資料，再逐行插入新資料。

## 階段四：自動更新與錯誤處理

- [ ] 修改 `schedule_next_update` 函式，將更新間隔從 60 秒改為 **20 秒**。
- [ ] 更新函式現在需要更新所有在 `Listbox` 中被選取的股票。
- [ ] 維持現有的錯誤處理機制，當部分或全部股票資料獲取失敗時，能提供適當的反馈 (例如在表格中顯示錯誤狀態或彈出訊息框)。

## 階段五：完成與測試

- [ ] 程式碼整理與註解。
- [ ] 完整測試所有新功能：
    - [ ] 是否能正確載入股票列表到 `Listbox`？
    - [ ] 是否能用 Ctrl/Shift 鍵進行多選？
    - [ ] `Treeview` 是否能正確顯示所有選定股票的資訊？
    - [ ] 資訊是否每 20 秒自動更新？
    - [ ] 當選擇大量股票時，介面是否依然流暢？