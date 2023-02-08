/**
 * @param {Date} date
 */

const toLocalISOString = (date) => {
  const pad2 = (x) => ('0' + x).slice(-2);
  const year = (date.getFullYear()).toString();
  const month = pad2((date.getMonth() + 1).toString());
  const day = pad2(date.getDate().toString());
  const hour = pad2(date.getHours().toString());
  const min = pad2(date.getMinutes().toString());
  const sec = pad2(date.getSeconds().toString());
  return `${year}-${month}-${day}T${hour}:${min}:${sec}`;
}