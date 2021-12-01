// sleep time expects milliseconds
function sleep(time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}

function generate_image(base64) {
    document.getElementById("qr").src = base64;
}


function generate_qrcode() {
    // Get the value from the input field
    var data = document.getElementById("data").value;
    eel.generate_qrcode(data)(generate_image);
}

function update_hydrometer() {
    // Get the value from the input field
    pg = document.getElementById("progress1");
    v = Math.round(Math.random() * 100);
    pg.value = v;
    pg.style = "width: " + v + "%";
    pg.innerHTML = v + "%";
    if (v < 20) {
        document.getElementById("plant1warning").style = "";
        pg.style.backgroundColor = "red";
    }
    if (v > 20) {
        document.getElementById("plant1warning").style = "display:none;";
        pg.style.backgroundColor = "";
    }
}

var t = None;
var is_running = false;

function start_syncing() {
    if (is_running) {
        return;
    }
    is_running = true;
    t = setInterval(update_hydrometer, 1000);
}

function stop_syncing() {
    if (is_running) {
        clearInterval(t);
        is_running = false;
    }
}

var plant_counts = 2;

function inject_hydrometer_for_plant(plant_name = plant_counts + 1) {
    plant_counts += 1;
    var plant = ''
    plant += '<div class="row">'
    plant += '<div class="col-md-8 col-12">'
    plant += '    <h2>Plant ' + String(plant_name) + '</h2>'
    plant += '<div class="row"><div class="col-md-8 col-12" id="plant1container"><span class="badge badge-warning"id="plant1warning" style="display:none;">Warning</span></div><br /></div>'
    plant += '    <div class="progress" style="height: 50px;">'
    plant += '   <div class="progress-bar" id="progress' + '_' + String(plant_counts) + '" role="progressbar" style="width: 50%" aria-valuenow="50"'
    plant += '  aria-valuemin="0" aria-valuemax="100">50%</div>'
    plant += '    </div>'
    plant += '</div>'
    plant += '<div class="col-md-4 col-12">'
    plant += '    <h2>&nbsp;</h2>'
    plant += '    <button class="btn btn-primary" onclick="waters25' + '_' + String(plant_counts) + '()">Waters 25ml</button>'
    plant += '    <button class="btn btn-primary" onclick="waters50' + '_' + String(plant_counts) + '()">Waters 50ml</button>'
    plant += '     </div>'
    plant += ' </div>'
    document.getElementById("plant_container").innerHTML += plant;
}