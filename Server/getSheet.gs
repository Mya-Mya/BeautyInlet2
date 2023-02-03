function getSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet()
  const s = ss.getSheetByName("main")
  return s
}