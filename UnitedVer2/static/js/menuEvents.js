// window.onload = function () {
//
// }

function checkboxClicked(obj) {
    console.log("yes");
    if(obj.checked){
        obj.setAttribute("data-hidden","false");
        dataHidden = false;
    }else{
        obj.setAttribute("data-hidden","true");
        dataHidden = true;
    }
}