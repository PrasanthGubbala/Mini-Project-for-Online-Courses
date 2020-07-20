
function ajaxcall(elm_id,url,spn_id) {
    var val = document.getElementById(elm_id).value;
    var param = 'key='+val;
    var req = new XMLHttpRequest();
    req.onreadystatechange = show;
    req.open('POST',url,true);
    req.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
    req.send(param);

    function show() {
        if(req.readyState==4){
            var json_data = JSON.parse(req.responseText);
            var sp = document.getElementById(spn_id);
            var bt = document.getElementById('button');

            if(json_data.error=='INVALID INPUT'){
                 sp.innerText = json_data.error+' '+elm_id+' '+val;
                 sp.style.color='red';
                 bt.disabled=true;
            }
            else {
                sp.innerText = val+' is '+json_data.message;
                sp.style.color='green';
                bt.disabled=false;
            }
        }
    }
}