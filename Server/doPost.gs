function doPost(e) {
  /**@type {Detection} */
  const data = JSON.parse(e.postData.getDataAsString())
  const {dateISOString, statusLabel} = data
  const s = getSheet()
  const date = new Date(dateISOString)
  s.appendRow([date,statusLabel])
  return ContentService.createTextOutput(`Added record dateISOString=${dateISOString}, statusLabel=${statusLabel}`)
}
