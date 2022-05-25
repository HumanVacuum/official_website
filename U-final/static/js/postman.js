// judge html
var isPresent = 0;
var url = window.location.href;
var index = url.lastIndexOf("\/");
var str = url.substring(index + 1,url.length);
if(str === "present") isPresent = 1;

// tags to be changed
var tagLevel = document.getElementById("data-level");
var tagStrategy = document.getElementById("data-strategy");
if(isPresent) var tagValue = document.getElementById("data-value");

// xhr
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;
var a = 0;
xhr.addEventListener("readystatechange", function() {
    if(this.readyState === 4 && a === 0) {
        var responseText = JSON.parse(this.responseText);

        /*  responseText:
        *   Value: The concentration of PM2.5
        *       responseText.Device[0].Node[0].Value
        *   Id: The identification of PM2,5 detector
        *       responseText.Device[0].Node[0].Id
        *   FlashTime: The time when detector collect the data
        *       responseText.Device[0].Flashtime
        *   others:
        *       responseText.Device
        *       responseText.Device[0].Node
        *       responseText.Device[0].Node[0].Unit
        * */

        a = 1;
        console.log(responseText);
        // console.log(this.responseText);

        var value = responseText.Device[0].Node[0].Value;
        console.log(value);
        if(isPresent) tagValue.innerHTML = value;

        tagLevel.innerHTML = judge(value);
        console.log(judge(value));

        tagStrategy.innerHTML = judge_strategy(value);
        console.log(judge_strategy(value));

    }
});
xhr.open("POST", "http://ltwyiot.com/api/devicelist?token=7aa03e6bc795a560dea8b918882fdd64");
xhr.send();

function judge(x){
    if(x >= 0 && x < 35){
        return "Excellent";
    }
    if (x >= 35 && x < 75){
        return "Good";
    }
    if (x >= 75 && x < 115){
        return "Mild air pollution";
    }
    if (x >= 115 && x < 150){
        return "Moderate air pollution";
    }
    if (x >= 150 && x < 250){
        return "Severe air pollution";
    }
    else{
        return "Very severe air pollution";
    }
}

function judge_strategy(x){
    if(x >= 0 && x < 35){
        return "无污染";
    }
    if (x >= 35 && x < 75){
        return '请带上口罩,并开窗通风';
    }
    if (x >= 75 && x < 115){
        return '请带上口罩,并开窗通风';
    }
    if (x >= 115 && x < 150){
        return '请戴上口罩,开窗通风,打开空气净化器';
    }
    if (x >= 150 && x < 250){
        return  '请戴上口罩,开窗通风,打开空气净化器';
    }
    else{
        return '请戴上口罩,开窗通风,打开空气净化器';
    }
}