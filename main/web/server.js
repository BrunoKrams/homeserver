var lightswitch = document.getElementById('flexSwitchLightswitch');
lightswitch.addEventListener('click', function() {
    if (lightswitch.checked) {
        fetch('/lightswitch/off', {method: 'POST'});
    } else {
        fetch('/lightswitch/on', {method: 'POST'});
    }
});
function updateLightswitchStatus() {
  fetch('/lightswitch', {
      method: 'GET'
    })
    .then((response) => response.text()
      .then((text) => lightswitch.checked = text == 'ON')
    );
}
updateLightswitchStatus();
setInterval(updateLightswitchStatus, 2000);


var energymonitor = document.getElementById('flexSwitchEnergymonitor');
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