var kitchenLightSwitch = document.getElementById('kitchenLightSwitch');
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


var kitchenCounterLightSwitch = document.getElementById('kitchenCounterLightSwitch');
kitchenCounterLightSwitch.addEventListener('click', function() {
    if (kitchenCounterLightSwitch.checked) {
        fetch('/kitchencounterlight/on', {method: 'POST'});
    } else {
        fetch('/kitchencounterlight/off', {method: 'POST'});
    }
});
function updateKitchenCounterLightStatus() {
  fetch('/kitchencounterlight', {
      method: 'GET'
    })
    .then((response) => response.text()
      .then((text) => kitchenCounterLightSwitch.checked = text == 'ON')
    );
}
updateKitchenCounterLightStatus();
setInterval(updateKitchenCounterLightStatus, 2000);


var garageLightSwitch = document.getElementById('garageLightSwitch');
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


var energymonitor = document.getElementById('energymonitorSwitch');
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