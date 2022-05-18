// tags to be changed
var level = document.getElementById("data-level");
var strategy = document.getElementById("data-strategy");

// xhr
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;
var a = 0;
xhr.addEventListener("readystatechange", function() {
    if(this.readyState === 4 && a === 0) {
        //console.log(this.responseText);
        /*
        * responseText:
        *   value: The concentration of PM2.5
        *   Id: The identification of PM2,5 detector
        *   FlashTime: The time when detector collect the data
        * */
        var responseText = JSON.parse(this.responseText);
        /*
        console.log(responseText);
        console.log(responseText.Device);
        console.log(responseText.Device[0].Node);
        console.log(responseText.Device[0].Node[0].Value);
        console.log(responseText.Device[0].Node[0].Id);
        console.log(responseText.Device[0].Flashtime);
        console.log(responseText.Device[0].Node[0].Unit);

         */
        //document.getElementById("Device");
        //document.getElementById("Value");
        console.log(responseText);
        console.log(this.responseText);
        //var url = " http://127.0.0.1:5000/";
        //xhr.open("POST", url);
        //xhr.send(this.responseText);
        a = 1;

        var value = responseText.Device[0].Node[0].Value;
        console.log(value);

        level.innerHTML = judge(value);
        console.log(judge(value));
        strategy.innerHTML = judge_strategy(value);
        console.log(judge_strategy(value));
    }
});
xhr.open("POST", "http://ltwyiot.com/api/devicelist?token=7aa03e6bc795a560dea8b918882fdd64");
xhr.send();
//xhr.open("POST", "http://127.0.0.1:5000/");

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