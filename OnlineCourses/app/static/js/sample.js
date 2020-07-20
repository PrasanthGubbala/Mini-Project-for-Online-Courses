function checkContact() {
    var contact = document.getElementById('contact').value;
    var param = 'contact='+contact;
    var req = new XMLHttpRequest();
    req.onreadystatechange = show;
    req.open('POST','http://127.0.0.1:8000/checkContact/',true);
    req.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
    req.send(param);

    function show() {
        if(req.readyState==4){
            var json_data = JSON.parse(req.responseText);
            var sp = document.getElementById('cs');
            var bt = document.getElementById('button');

            if(json_data.error=='contact no has already exist'){
                 sp.innerText = json_data.error;
                 sp.style.color='red';
                 bt.disabled=true;
            }
            else {
                sp.innerText = json_data.message;
                sp.style.color='green';
                bt.disabled=false;
            }
        }
    }
}