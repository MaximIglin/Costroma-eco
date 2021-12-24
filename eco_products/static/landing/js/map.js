let center = [57.36990711383908,40.47317526113556];

function init() {
    let map = new ymaps.Map('map', {
        center: center,
        zoom: 16,
    });
    let placeMark = new ymaps.Placemark(center,{}, {

    });

    map.geoObjects.add(placeMark)
}



ymaps.ready(init)