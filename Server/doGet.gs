function doGet(){
  const out = HtmlService.createHtmlOutputFromFile("monitor")
  out.addMetaTag("viewport","width=device-width, initial-scale=1")
  out.setTitle("BeautyInlet2 Web")
  return out
}