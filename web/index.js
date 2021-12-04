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

async function update_hydrometer() {
    // Get the value from the input field
    pg = document.getElementById("progress1");
    // Update the progress bar with eel function get_hydrometer_value() by setting v with the value returned from eel
    let v = await eel.get_hydrometer_value()();
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

var t = '';
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

var show_video_feed_bool = false;

function show_video_feed() {
    if (!show_video_feed_bool) {
        $("#video-container").load("include/video.html");
    } else {
        document.getElementById("video-container").innerHTML = "";
    }
    show_video_feed_bool = !show_video_feed_bool;
}


function inject_hydrometer_for_plant(plant_name = plant_counts + 1) {
    plant_counts += 1;
    var plant = ''
    plant += '<div class="row">'
    plant += '<div class="col-md-6 col-12">'
    plant += '    <h2>Plant ' + String(plant_name) + '</h2>'
    plant += '<div class="row"><div class="col-md-8 col-12" id="plant1container"><span class="badge badge-warning"id="plant1warning" style="display:none;">Warning</span></div><br /></div>'
    plant += '    <div class="progress" style="height: 50px;">'
    plant += '   <div class="progress-bar" id="progress' + '_' + String(plant_counts) + '" role="progressbar" style="width: 50%" aria-valuenow="50"'
    plant += '  aria-valuemin="0" aria-valuemax="100">50%</div>'
    plant += '    </div>'
    plant += '</div>'
    plant += '<div class="col-md-6 col-12">'
    plant += '    <h2>&nbsp;</h2><br />'
    plant += '    <button class="btn btn-primary" onclick="waters25' + '_' + String(plant_counts) + '()">Waters 25ml</button>'
    plant += '    <button class="btn btn-primary" onclick="waters50' + '_' + String(plant_counts) + '()">Waters 50ml</button>'
    plant += '  <div class="custom-control custom-switch">'
    plant += '<input type="checkbox" class="custom-control-input" id="customSwitch1">'
    plant += '<label class="custom-control-label" for="customSwitch1">Toggle this switch element</label></div>'
    plant += '     </div>'
    plant += ' </div>'
    document.getElementById("plant_container").innerHTML += plant;
}