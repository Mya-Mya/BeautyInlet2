/**
 * @param {string} dateISOString
 * @returns {string}
 */
function getDetectionsByDate(dateISOString) {
  const s = getSheet()
  const range = s.getRange(1, 1, s.getLastRow(), 2)
  const values = range.getValues()

  const date = new Date(dateISOString)
  const start = new Date(date)
  start.setHours(0, 0, 0)
  const end = new Date(date)
  end.setHours(23, 59, 59)

  const satisfyingValues = values.filter(row =>
    start <= row[0] && row[0] <= end
  )

  /**@type {Detection[]} */
  const detections = satisfyingValues.map(row => ({
    dateISOString: toLocalISOString(row[0]),
    statusLabel: row[1]
  }))
  return JSON.stringify(detections)
}