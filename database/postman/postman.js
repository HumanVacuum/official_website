var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function() {
  if(this.readyState === 4) {
    console.log(this.responseText);
    /*
    * responseText:
    *   value: The concentration of PM2.5
    *   Id: The identification of PM2,5 detector
    *   FlashTime: The time when detector collect the data
    * */
    var responseText = JSON.parse(this.responseText);

    //alert(responseText.Node.Value);
  }
});

xhr.open("POST", "http://ltwyiot.com/api/devicelist?token=7aa03e6bc795a560dea8b918882fdd64");

xhr.send();