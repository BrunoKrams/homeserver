var garageLightSwitch = document.getElementById('flexGarageLightSwitch');
garageLightSwitch.addEventListener('click', function() {
    if (garageLightSwitch.checked) {
        fetch('/garagelight/on', {method: 'POST'});
    } else {
        fetch('/garagelight/off', {method: 'POST'});
    }
});
function updateGarageLightStatus() {
  fetch('/garagelight', {
      method: 'GET'
    })
    .then((response) => response.text()
      .then((text) => garageLightSwitch.checked = text == 'ON')
    );
}
updateGarageLightStatus();
setInterval(updateGarageLightStatus, 2000);


var kitchenLightSwitch = document.getElementById('flexKitchenLightSwitch');
kitchenLightSwitch.addEventListener('click', function() {
    if (kitchenLightSwitch.checked) {
        fetch('/kitchenlight/on', {method: 'POST'});
    } else {
        fetch('/kitchenlight/off', {method: 'POST'});
    }
});
function updateKitchenLightStatus() {
  fetch('/kitchenlight', {
      method: 'GET'
    })
    .then((response) => response.text()
      .then((text) => kitchenLightSwitch.checked = text == 'ON')
    );
}
updateKitchenLightStatus();
setInterval(updateKitchenLightStatus, 2000);


var energymonitor = document.getElementById('flexEnergymonitorSwitch');
energymonitor.addEventListener('click', function() {
    if (energymonitor.checked) {
        fetch('/energymonitor/start', {method: 'POST'});
    } else {
        fetch('/energymonitor/stop', {method: 'POST'});
    }
});
function updateEnergymonitorStatus() {
  fetch('/energymonitor', {
      method: 'GET'
    })
    .then((response) => response.text()
      .then((text) => energymonitor.checked = text == 'ON')
    );
}
updateEnergymonitorStatus();
setInterval(updateEnergymonitorStatus, 2000);