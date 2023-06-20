//-----------------ИНИЦИАЛИЗАЦИЯ_КАРТЫ-------------------//
//-----------------ИНИЦИАЛИЗАЦИЯ_КАРТЫ-------------------//
//-----------------ИНИЦИАЛИЗАЦИЯ_КАРТЫ-------------------//
//-----------------ИНИЦИАЛИЗАЦИЯ_КАРТЫ-------------------//
var mbUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
//-----------------обьявление_интерактивной_и_современной_карты-------------------//
var interactive = L.tileLayer(mbUrl);
var real = L.tileLayer(mbUrl);
const map = L.map('map', {
    center: [53.967619, 58.410038],
    zoom: 8,
    layers: [interactive],
    defaultExtentControl: true,
    zoomControl: true,
});
var imageUrl = 'static/images/photos/Granica_1.png';
var imageUrl1 = 'static/images/photos/Granicagr.png';
var errorOverlayUrl = 'https://cdn-icons-png.flaticon.com/512/110/110686.png';
var altText = 'Историческая карта Уфимской и Орегбургской губернии';
var latLngBounds = L.latLngBounds([[56.46855975598276,65.78613281250001], [50.467994531475696,51.08642578125001]]);
var imageOverlay = L.imageOverlay(imageUrl, latLngBounds, {
    opacity: 1,
    errorOverlayUrl: errorOverlayUrl,
    alt: altText,
    interactive: true,
}).addTo(map);

var imageOverlay1 = L.imageOverlay(imageUrl1, latLngBounds, {
    opacity: 1,
    errorOverlayUrl: errorOverlayUrl,
    alt: altText,
    interactive: true,
}).addTo(map);

L.rectangle(latLngBounds, {
    opacity: 0,
    color: '#ffffff00'
}).addTo(map);
//-----------------ИКОНКИ_И_ПОЛЯ-------------------//
//-----------------ИКОНКИ_И_ПОЛЯ-------------------//
//-----------------ИКОНКИ_И_ПОЛЯ-------------------//
//-----------------ИКОНКИ_И_ПОЛЯ-------------------//
const Icon = L.Icon.extend({
    options: {
        iconSize: [38, 38],
    }
});

const memorialIcon = new Icon({iconUrl: 'static/images/icon/ToponymIcon.svg'}),
    monumentIcon = new Icon({iconUrl: 'static/images/icon/MonumentIcon.svg'}),
    cityIcon = new Icon({iconUrl: 'static/images/icon/CityIcon.svg'}),
    fortIcon = new Icon({iconUrl: 'static/images/icon/FortIcon.svg'}),
    RegimentIcon = new Icon({iconUrl: 'static/images/icon/RegimentIcon.svg'}),
    UezdIcon = new Icon({iconUrl: 'static/images/icon/UezdIcon.svg'}),
    memorialClick=new Icon({iconUrl: 'static/images/icon/ToponymIconClick.svg'}),
    monumentClick = new Icon({iconUrl: 'static/images/icon/MonumentIconClick.svg'});
    cityClick = new Icon({iconUrl: 'static/images/icon/CityIconClick.svg'}),
    fortClick = new Icon({iconUrl: 'static/images/icon/FortIconClick.svg'}),
    RegimentClick = new Icon({iconUrl: 'static/images/icon/RegimentIconClick.svg'}),
    UezdClick = new Icon({iconUrl: 'static/images/icon/UezdIconClick.svg'})

var Gidronimy = L.layerGroup();
var Toponimy = L.layerGroup();
var Pamyatniki = L.layerGroup();

var kahim = [" "];
var kahim1 = [" "];
//-----------------СОЗДАНИЕ_ЭКСТЕНТА_КАРТЫ-------------------//
//-----------------СОЗДАНИЕ_ЭКСТЕНТА_КАРТЫ-------------------//
//-----------------СОЗДАНИЕ_ЭКСТЕНТА_КАРТЫ-------------------//
//-----------------СОЗДАНИЕ_ЭКСТЕНТА_КАРТЫ-------------------//
var northWest = L.latLng(60.710713, 28.749180),
southEast = L.latLng(48.685720, 71.635020);
var bounds = L.latLngBounds(northWest, southEast);
map.setMaxBounds(bounds);
map.on('drag', function() {
  map.panInsideBounds(bounds, { animate: false });
});
map.options.minZoom = 6;
//-----------------ЗАГРУЗКА_С_JSON-------------------//
//-----------------ЗАГРУЗКА_С_JSON-------------------//
//-----------------ЗАГРУЗКА_С_JSON-------------------//
//-----------------ЗАГРУЗКА_С_JSON-------------------//
async function load_toponyms() {
    const response = await fetch('/api/toponyms/')
    const geojson = await response.json()
    return geojson
}
async function load_monuments() {
    const response = await fetch('/api/monuments/')
    const geojson = await response.json()
    return geojson
}
async function load_regiment() {
    const response = await fetch('/api/regiments/')
    const geojson = await response.json()
    return geojson
}
async function load_route() {
    const response = await fetch('/api/routes/')
    const geojson = await response.json()
    return geojson
}
async function load_fort() {
    const response = await fetch('/api/forts/')
    const geojson = await response.json()
    return geojson
}
async function load_cities() {
    const response = await fetch('/api/city/')
    const geojson = await response.json()
    return geojson
}
async function load_municipal() {
    const response = await fetch('/api/municipals/')
    const geojson = await response.json()
    return geojson
}
async function load_uezd() {
    const response = await fetch('/api/uezds/')
    const geojson = await response.json()
    return geojson
}
//ждем окончания пред функции
async function render_markers() {

    //-----------------ИКОНКА ЗКАГРУЗКИ САЙТА-------------------//
    const toponym = await load_toponyms();
	const monument = await load_monuments();
    const regiment = await load_regiment();
    const route = await load_route();
    const fort = await load_fort();
    const cities = await load_cities();
    const municipal = await load_municipal();
    const uezd = await load_uezd();
	var arr = [toponym, monument, regiment, route, fort, cities, municipal, uezd];

    //-----------------УБРАТЬ ИКОНКУ-------------------//
	return arr
}

//-----------------РАБОТА_С_JSON-------------------//
//-----------------РАБОТА_С_JSON-------------------//
//-----------------РАБОТА_С_JSON-------------------//
//-----------------РАБОТА_С_JSON-------------------//
render_markers().then(arr => {
	toponym=arr[0];
	monument=arr[1];
    regiment=arr[2];
    route=arr[3];
    fort=arr[4];
    cities=arr[5];
    municipal=arr[6];
    uezd=arr[7];
	//-----------------ДАННЫЕ_ДЛЯ_ПОИСКА-------------------//
    //-----------------ДАННЫЕ_ДЛЯ_ПОИСКА-------------------//
    //-----------------ДАННЫЕ_ДЛЯ_ПОИСКА-------------------//
    //-----------------ДАННЫЕ_ДЛЯ_ПОИСКА-------------------//
	ToponymOpts = {
        onEachFeature: function(feature) {
			var p = feature.properties;
			p.index = p.name + " | " + p.amenity; //создаем поле index через которое будем искать по параметрам
            
        },
        //собственные маркеры, которые можно сделать прозрачными
        pointToLayer: function(feature, latlng) {
            return L.marker(latlng, {
                icon: L.divIcon({
                    className: feature.properties.amenity,
                    iconSize: L.point(1, 1),
                    html: feature.properties.amenity[0].toUpperCase(),
                })
            }).bindPopup(feature.properties.amenity+'<br><b>'+feature.properties.name+'</b>');
        }
    };
    MonumentOpts = {
        onEachFeature: function(feature) {
			var p = feature.properties;
			p.index = p.name + " | " + p.architect + " | " + p.amenity; //создаем поле index через которое будем искать по параметрам
            
        },
        //собственные маркеры, которые можно сделать прозрачными
        pointToLayer: function(feature, latlng) {
            return L.marker(latlng, {
                icon: L.divIcon({
                    className: feature.properties.amenity,
                    iconSize: L.point(1, 1),
                    html: feature.properties.amenity[0].toUpperCase(),
                })
            }).bindPopup(feature.properties.amenity+'<br><b>'+feature.properties.name+'</b>');
        }
    };
    RegimentOpts = {
        onEachFeature: function(feature) {
			var p = feature.properties;
			p.index = p.name + " | " + p.place; //создаем поле index через которое будем искать по параметрам
            
        },
        //собственные маркеры, которые можно сделать прозрачными
        pointToLayer: function(feature, latlng) {
            return L.marker(latlng, {
                icon: L.divIcon({
                    className: feature.properties.amenity,
                    iconSize: L.point(1, 1),
                    html: feature.properties.amenity[0].toUpperCase(),
                })
            }).bindPopup(feature.properties.amenity+'<br><b>'+feature.properties.name+'</b>');
        }
    };
    FortOpts = {
        onEachFeature: function(feature) {
			var p = feature.properties;
			p.index = p.name; //создаем поле index через которое будем искать по параметрам
            
        },
        //собственные маркеры, которые можно сделать прозрачными
        pointToLayer: function(feature, latlng) {
            return L.marker(latlng, {
                icon: L.divIcon({
                    className: feature.properties.amenity,
                    iconSize: L.point(1, 1),
                    html: feature.properties.amenity[0].toUpperCase(),
                })
            }).bindPopup(feature.properties.amenity+'<br><b>'+feature.properties.name+'</b>');
        }
    };
    citiesOpts = {
        onEachFeature: function(feature) {
			var p = feature.properties;
			p.index = p.name + " | " + p.amenity; //создаем поле index через которое будем искать по параметрам
            
        },
        //собственные маркеры, которые можно сделать прозрачными
        pointToLayer: function(feature, latlng) {
            return L.marker(latlng, {
                icon: L.divIcon({
                    className: feature.properties.amenity,
                    iconSize: L.point(1, 1),
                    html: feature.properties.amenity[0].toUpperCase(),
                })
            }).bindPopup(feature.properties.amenity+'<br><b>'+feature.properties.name+'</b>');
        }
    };
    UezdOpts = {
        onEachFeature: function(feature) {
			var p = feature.properties;
			p.index = p.name + " | " + p.amenity; //создаем поле index через которое будем искать по параметрам
            
        },
        //собственные маркеры, которые можно сделать прозрачными
        pointToLayer: function(feature, latlng) {
            return L.marker(latlng, {
                icon: L.divIcon({
                    className: feature.properties.amenity,
                    iconSize: L.point(1, 1),
                    html: feature.properties.amenity[0].toUpperCase(),
                })
            }).bindPopup(feature.properties.amenity+'<br><b>'+feature.properties.name+'</b>');
        }
    };
    featurelayer = L.layerGroup([ 
		L.geoJson(toponym, ToponymOpts), //так можно добавлять еще слои в поиск
		L.geoJson(monument, MonumentOpts),
        L.geoJson(regiment, RegimentOpts),
        L.geoJson(fort, FortOpts),
        L.geoJson(cities, citiesOpts),
        L.geoJson(uezd, UezdOpts),
    ]);
    //-----------------СТАНДАРТНЫЕ_ДАННЫЕ-------------------//
    //-----------------СТАНДАРТНЫЕ_ДАННЫЕ-------------------//
    //-----------------СТАНДАРТНЫЕ_ДАННЫЕ-------------------//
    //-----------------СТАНДАРТНЫЕ_ДАННЫЕ-------------------//

    var citiesjson = L.geoJSON(json_Cities_6, {
        style: {
            color: '#b7484b',
            opacity: 1
        }
    });

    var gidronimyjson = L.geoJSON(json_Gidronimy_5, {
        style: {
            color: '#1f78b4',

        }
    }).addTo(map);

    var toponimyjson = L.geoJSON(json_Toponimy_2, {
        style: {
            color: '#85b66f',
        }
    }).addTo(map);



    var admRB = L.geoJSON(municipal, {
        style: {
            color: '#ff8100',
            opacity: 0.5
        },
        onEachFeature: LabelEachFeature
    });
    var routest = L.geoJSON(route, {
        style: {
            weight: 3,
                color: 'orange',
                opacity: 0.8
        },
        onEachFeature: LabelEachFeatureRoute
    }).addTo(map);
    routest.setText('\u25BA', {repeat: true,
        offset: 4,
        attributes: {fill: 'red'}});
    
    var or = L.geoJSON(or_json, {
        style: {
            color: '#dc570c',
            opacity: 0.1
        },
        onEachFeature: LabelEachFeatureOREN
    });
    var chel = L.geoJSON(chel_json, {
        style: {
            color: '#ffc507',
            opacity: 0.1
        },
        onEachFeature: LabelEachFeatureCHEL
    });
    //-----------------ДОБАВЛЕНИЕ_СЛОЕВ-------------------//
    //-----------------ДОБАВЛЕНИЕ_СЛОЕВ-------------------//
    //-----------------ДОБАВЛЕНИЕ_СЛОЕВ-------------------//
    //-----------------ДОБАВЛЕНИЕ_СЛОЕВ-------------------//
    var layersg = L.layerGroup([gidronimyjson, toponimyjson])
    
    var ToponimyInfo = L.geoJSON(toponym,{
        onEachFeature: onEachFeatureToponimy,
        pointToLayer: ptl1
    });

	var PamyatnikiInfo = L.geoJSON(monument,{
        onEachFeature: onEachFeaturePamyatniki,
        pointToLayer: ptl
    });

    var RegimentInfo = L.geoJSON(regiment,{
        onEachFeature: onEachFeatureRegiment,
        pointToLayer: ptlRegiment
    }).addTo(map);

    var FortInfo = L.geoJSON(fort,{
        onEachFeature: onEachFeatureFort,
        pointToLayer: ptlFort
    }).addTo(map);

    var citiesInfo = L.geoJSON(cities,{
        onEachFeature: onEachFeaturecities,
        pointToLayer: ptlcities
    }).addTo(map);
    var UezdInfo = L.geoJSON(uezd,{
        onEachFeature: onEachFeatureUezd,
        pointToLayer: ptlUezd
    }).addTo(map);

    //-----------------ИЗМЕНЕНИЕ_ИКОНКИ-------------------//
    //-----------------ИЗМЕНЕНИЕ_ИКОНКИ-------------------//
    //-----------------ИЗМЕНЕНИЕ_ИКОНКИ-------------------//
    //-----------------ИЗМЕНЕНИЕ_ИКОНКИ-------------------//
	function ptl(feature,latlng){
        return L.marker(latlng,{icon: monumentIcon});
    }
    function ptl1(feature,latlng){
        return L.marker(latlng,{icon: memorialIcon});
    }
    function ptlRegiment(feature,latlng){
        return L.marker(latlng,{icon: RegimentIcon}); 
    }
    function ptlFort(feature,latlng){
        return L.marker(latlng,{icon: fortIcon});
    }
    function ptlcities(feature,latlng){
        return L.marker(latlng,{icon: cityIcon});
    }
    function ptlUezd(feature,latlng){
        return L.marker(latlng,{icon: UezdIcon}); 
    }
    //-----------------ОТКРЫТИЕ_ПАНЕЛИ-------------------//
    //-----------------ОТКРЫТИЕ_ПАНЕЛИ-------------------//
    //-----------------ОТКРЫТИЕ_ПАНЕЛИ-------------------//
    //-----------------ОТКРЫТИЕ_ПАНЕЛИ-------------------//
    function onEachFeaturePamyatniki(feature, layer) {
        layer.on('click',function(e){
            layer.setIcon(monumentClick);
            map.setView(e.latlng, 13);
            openSidebarPamyatniki(e);
        });
    }
    function onEachFeatureToponimy(feature, layer) {
        layer.on('click',function(e){
            layer.setIcon(memorialClick);
            map.setView(e.latlng, 13);
            openSidebarToponimy(e);
        });
    }
    function onEachFeatureRegiment(feature, layer) {
        layer.on('click',function(e){
            layer.setIcon(RegimentClick); 
            map.setView(e.latlng, 13);
            openSidebarRegiment(e);
        });
    }
    function onEachFeatureFort(feature, layer) {
        layer.on('click',function(e){
            layer.setIcon(fortClick); 
            map.setView(e.latlng, 13);
            openSidebarFort(e);
        });
    }
    function onEachFeaturecities(feature, layer) {
        layer.on('click',function(e){
            layer.setIcon(cityClick); 
            map.setView(e.latlng, 13);
            openSidebarcities(e);
        });
    }
    function onEachFeatureUezd(feature, layer) {
        layer.on('click',function(e){
            layer.setIcon(UezdClick); 
            map.setView(e.latlng, 13);
            openSidebarUezd(e);
        });
    }
    function LabelEachFeature(feature, layer) {
        layer.on('click',function(e){
            map.setView(e.latlng, 10);
            openSidebarMunicipal(e);
        }),
        map.on('zoomend', function () {
            if (map.getZoom() > 8 && feature.id!="4") {
                layer.bindTooltip(feature.properties.name, {permanent: true, direction: "center", setZIndex: 5})
            }
            else if(feature.id=="4" && map.getZoom() <= 8){
                layer.bindTooltip(feature.properties.name,{permanent: true, direction: "center", setZIndex: 5})
            }
            else {
                layer.unbindTooltip();
            }


        }),
        map.zoomOut(1);
    }
    function LabelEachFeatureRoute(feature, layer) {
        map.on('zoomend', function () {
            if (map.getZoom() > 7) {
                layer.bindTooltip(feature.properties.name, {permanent: true, direction: "center", setZIndex: 5})
            }
            else {
                layer.unbindTooltip();
            }


        }),
        map.zoomOut(1);
    }
    function LabelEachFeatureOREN(feature, layer) {
        map.on('zoomend', function () {
            if (map.getZoom() <= 8) {
                layer.bindTooltip(feature.properties.name, {permanent: true, direction: "center", setZIndex: 5})
            } else {
                layer.unbindTooltip();
            }
        });
    }
    function LabelEachFeatureCHEL(feature, layer) {
        map.on('zoomend', function () {
            if (map.getZoom() <= 8) {
                layer.bindTooltip(feature.properties.name, {permanent: true, direction: "center", setZIndex: 5})
            } else {
                layer.unbindTooltip();
            }
        });
    }  
    var scale = L.control.scale();
    scale.addTo(map);
    //------------------БОКОВАЯ_ПАНЕЛЬ------------------//
    //------------------БОКОВАЯ_ПАНЕЛЬ------------------//
    //------------------БОКОВАЯ_ПАНЕЛЬ------------------//
    //------------------БОКОВАЯ_ПАНЕЛЬ------------------//
    function openSidebarPamyatniki(e) {
        sidebar.toggle();
        var popupContent=' ';
        
        kahim1=e.target.feature.properties.photo.split(' ');
        kahimVideoP=e.target.feature.properties.video.split(' ');  
        kahimAudio1=e.target.feature.properties.audio.split(' '); 

        if(kahimAudio1!="") {
            for (var d = 0; d < kahimAudio1.length; d++) {
                popupContent += '<h3>Аудио-файлы</h3><audio controls><source src="' + kahimAudio1[d] + '" type="audio/mpeg"></audio>';
            }
        }
        if(kahim1!=""||kahimVideoP!="")
        {popupContent+='<h3>Галерея фотографий и видео</h3><div>';
        for(var i=0;i<kahim1.length;i++) {
            popupContent+= '<div class="mySlides fade">\
        <img src="'+kahim1[i] +'" id="theImage"'+i+'" onClick="makeFullScreen()" class="Image"> </div>';
        }
        for(var i=0;i<kahimVideoP.length;i++) {
            popupContent+= '<div class="mySlides fade">\
            <video src="'+kahimVideoP[i]+'" controls class="Video"></video></div>';
        }
        popupContent+='<a class="prev" onclick="plusSlides(-1)">&#10094;</a>\
                        <a class="next" onclick="plusSlides(1)">&#10095;</a>';

        popupContent+='</div><br>' +
            '<div style="text-align:center">';

        for(var ii=0;ii<kahim1.length+kahimVideoP.length;ii++)
        {
            popupContent+= '<span class="dot" onclick="currentSlide('+(ii+1)+')"></span>';
        }
        popupContent+='</div>';
        }
        else{
        popupContent='';
        }
        sidebar.setContent('<h1>'+ e.target.feature.properties.name + '</h1>' +
            '<p>Скульптор: ' + e.target.feature.properties.architect + '<br>' +
            'Год: ' + e.target.feature.properties.year + '<br>' +
            'Описание ' + e.target.feature.properties.description + '<br>' + popupContent);
        showSlides();
    }

    function openSidebarToponimy(e) {
        sidebar.toggle();
        var popupContent1=' ';
        kahim1=e.target.feature.properties.photo.split(' ');
        kahimVideo1=e.target.feature.properties.video.split(' '); //.split(' ')
        kahimAudio1=e.target.feature.properties.audio.split(' '); //.split(' ')
    

    
        if(kahim1!=""||kahimVideo1!="")
        {
            popupContent1+='<h3>Галерея фотографий и видео</h3><div>';
            for(var i=0;i<kahim1.length;i++) {
                popupContent1+= '<div class="mySlides fade">\
            <img src="'+kahim1[i] +'" id="theImage"'+i+'" onClick="makeFullScreen()" class="Image"> </div>';
            }
            for(var i=0;i<kahimVideo1.length;i++) { //.length
                popupContent1+= '<div class="mySlides fade">\
                <video src="'+kahimVideo1[i]+'" controls class="Video"></video></div>';
            }
            popupContent1+='<a class="prev" onclick="plusSlides(-1)">&#10094;</a>\
                            <a class="next" onclick="plusSlides(1)">&#10095;</a>';
    
            popupContent1+='</div><br>' +
                '<div style="text-align:center">';
    
            for(var ii=0;ii<kahim1.length+kahimVideo1.length;ii++) 
            {
                popupContent1+= '<span class="dot" onclick="currentSlide('+(ii+1)+')"></span>';
            }
            popupContent1+='</div>';
        }
        else{
            popupContent1='';
        }
        sidebar.setContent('<h1>'+ e.target.feature.properties.name + '</h1>' +
            '<p>Место: ' + e.target.feature.properties.place + '<br>' +
            'Описание: ' + e.target.feature.properties.description + '<br>'+popupContent1);
        showSlides();
    }

    function openSidebarRegiment(e) {
        sidebar.toggle();
        var popupContentReg=' ';
        
        kahim1=e.target.feature.properties.photo.split(' ');
        kahimVideo1=e.target.feature.properties.video.split(' ');  
        kahimAudio1=e.target.feature.properties.audio.split(' '); 
       
        if(kahim1!=""||kahimVideo1!="")
        {popupContentReg+='<h3>Галерея фотографий и видео</h3><div>';
        for(var i=0;i<kahim1.length;i++) {
            popupContentReg+= '<div class="mySlides fade">\
        <img src="'+kahim1[i] +'" id="theImage"'+i+'" onClick="makeFullScreen()" class="Image"> </div>';
        }
        for(var i=0;i<kahimVideo1.length;i++) {
            popupContentReg+= '<div class="mySlides fade">\
            <video src="'+kahimVideo1[i]+'" controls class="Video"></video></div>';
        }
        popupContentReg+='<a class="prev" onclick="plusSlides(-1)">&#10094;</a>\
                        <a class="next" onclick="plusSlides(1)">&#10095;</a>';

                        popupContentReg+='</div><br>' +
            '<div style="text-align:center">';

        for(var ii=0;ii<kahim1.length+kahimVideo1.length;ii++)
        {
            popupContentReg+= '<span class="dot" onclick="currentSlide('+(ii+1)+')"></span>';
        }
        popupContentReg+='</div>';
        }
        else{
            popupContentReg='';
        }
        sidebar.setContent('<h1>'+ e.target.feature.properties.name + '</h1>' +
            '<p>Период существования: ' + e.target.feature.properties.period + '<br>' +
            'Место: ' + e.target.feature.properties.place + '<br>' +
            'Численность: ' + e.target.feature.properties.size + '<br>' +
            'Командир: ' + e.target.feature.properties.commander + '<br>' +
            '<b>Сражения:</b> ' + e.target.feature.properties.battle_set + '<br>' 
            + popupContentReg);
        showSlides();
    }
    function openSidebarFort(e) {
        sidebar.toggle();
        var popupContentReg=' ';
        
        kahim1=e.target.feature.properties.photo.split(' ');
        kahimVideo1=e.target.feature.properties.video.split(' ');  
        kahimAudio1=e.target.feature.properties.audio.split(' '); 
       
        if(kahim1!=""||kahimVideo1!="")
        {popupContentReg+='<h3>Галерея фотографий и видео</h3><div>';
        for(var i=0;i<kahim1.length;i++) {
            popupContentReg+= '<div class="mySlides fade">\
        <img src="'+kahim1[i] +'" id="theImage"'+i+'" onClick="makeFullScreen()" class="Image"> </div>';
        }
        for(var i=0;i<kahimVideo1.length;i++) {
            popupContentReg+= '<div class="mySlides fade">\
            <video src="'+kahimVideo1[i]+'" controls class="Video"></video></div>';
        }
        popupContentReg+='<a class="prev" onclick="plusSlides(-1)">&#10094;</a>\
                        <a class="next" onclick="plusSlides(1)">&#10095;</a>';

                        popupContentReg+='</div><br>' +
            '<div style="text-align:center">';

        for(var ii=0;ii<kahim1.length+kahimVideo1.length;ii++)
        {
            popupContentReg+= '<span class="dot" onclick="currentSlide('+(ii+1)+')"></span>';
        }
        popupContentReg+='</div>';
        }
        else{
            popupContentReg='';
        }
        sidebar.setContent('<h1>'+ e.target.feature.properties.name + '</h1>' +
            '<p>Описание: ' + e.target.feature.properties.description + popupContentReg);
        showSlides();
    }
    function openSidebarcities(e) {
        sidebar.toggle();
        var popupContentReg=' ';
        //-----------------ДОБАВИТЬ_МЕДИА?-------------------//
        sidebar.setContent('<h1>'+ e.target.feature.properties.name + '</h1>' +
        '<p>Описание: ' + e.target.feature.properties.amenity + popupContentReg);
        showSlides();
    }
    function openSidebarMunicipal(e) {
        sidebar.toggle();
        var popupContentReg=' ';
        //-----------------ДОБАВИТЬ_МЕДИА?-------------------//
        sidebar.setContent('<h1>'+ e.target.feature.properties.name + '</h1>' +
        '<p>Памятники (' + e.target.feature.properties.monument_set.length + '): ' + e.target.feature.properties.monument_set +
        '<p>Топонимы (' + e.target.feature.properties.toponym_set.length + '): ' + e.target.feature.properties.toponym_set + popupContentReg);
        showSlides();
    }
    function openSidebarUezd(e) {
        sidebar.toggle();
        var popupContentReg=' ';
        kahim1=e.target.feature.properties.photo.split(' ');
        kahimVideo1=e.target.feature.properties.video.split(' ');  
        kahimAudio1=e.target.feature.properties.audio.split(' '); 
       
        if(kahim1!=""||kahimVideo1!="")
        {popupContentReg+='<h3>Галерея фотографий и видео</h3><div>';
        for(var i=0;i<kahim1.length;i++) {
            popupContentReg+= '<div class="mySlides fade">\
        <img src="'+kahim1[i] +'" id="theImage"'+i+'" onClick="makeFullScreen()" class="Image"> </div>';
        }
        for(var i=0;i<kahimVideo1.length;i++) {
            popupContentReg+= '<div class="mySlides fade">\
            <video src="'+kahimVideo1[i]+'" controls class="Video"></video></div>';
        }
        popupContentReg+='<a class="prev" onclick="plusSlides(-1)">&#10094;</a>\
                        <a class="next" onclick="plusSlides(1)">&#10095;</a>';

                        popupContentReg+='</div><br>' +
            '<div style="text-align:center">';

        for(var ii=0;ii<kahim1.length+kahimVideo1.length;ii++)
        {
            popupContentReg+= '<span class="dot" onclick="currentSlide('+(ii+1)+')"></span>';
        }
        popupContentReg+='</div>';
        }
        else{
            popupContentReg='';
        }
        sidebar.setContent('<h1>'+ e.target.feature.properties.name + '</h1>' +
        '<p>Описание: ' + e.target.feature.properties.description + popupContentReg);
        showSlides();
    }
    //-----------------ФИЛЬТР-------------------//
    //-----------------ФИЛЬТР-------------------//
    //-----------------ФИЛЬТР-------------------//
    //-----------------ФИЛЬТР-------------------//
	var baseTree = {
        label: 'Слои',

        children: [
            {label: 'Историческая ', layer: interactive},
            {label: 'Современная ', layer: real},
        ]
    };
    
    var overlaysTree = {
        label: 'Объекты',
        selectAllCheckbox: true,
        children: [
            {
                label: '<img src="static/images/icon/FortIcon.svg" class="imgtree"> Крепости', layer: FortInfo,
            },
            {
                label: '<class="imgtree"> Маршруты', layer: routest,
            },
            
            {
                label: '<img src="static/images/icon/RegimentIcon.svg" class="imgtree"> Полки', layer: RegimentInfo, //-----ИКОНКА-----//
            },
            {
                label: '<img src="static/images/icon/CityIcon.svg" class="imgtree"> Населенные пункты', layer: citiesInfo,
            },
            {
                label: '<img src="static/images/icon/UezdIcon.svg" class="imgtree"> Уезды', layer: UezdInfo, //-----ИКОНКА-----//
            },
        ]
    };
    var overlaysTree1 = {
        label: 'Объекты',
        selectAllCheckbox: 'Un/select all',
        children: [{
                label: 'Маркеры',
                selectAllCheckbox: true,
                children: [
                    {
                        label: '<img src="static/images/icon/MonumentIcon.svg" class="imgtree"> Монументы/памятники', layer: PamyatnikiInfo,
                    },
                    {
                        label: '<img src="static/images/icon/ToponymIcon.svg" class="imgtree"> Топонимы', layer: ToponimyInfo,
                    },
                ]
            },
            {
                label: 'Области',
                selectAllCheckbox: true,
                children: [
                    {
                        label: 'Республика Башкортостан', layer: admRB,
                    },
                    {
                        label: 'Оренбургская область', layer: or,
                    },
                    {
                        label: 'Челябинская область', layer: chel,
                    },
                ]
            }
        ]
    };
    var lay = L.control.layers.tree(baseTree, overlaysTree,
        {
            namedToggle: false,
            selectorBack: false,
            collapseAll: 'Свернуть все',
            expandAll: 'Раскрыть все',
            collapsed: true,
        });
        lay.addTo(map)

    var lay1 = L.control.layers.tree(baseTree, overlaysTree1,
        {
            namedToggle: false,
            selectorBack: false,
            collapseAll: 'Свернуть все',
            expandAll: 'Раскрыть все',
            collapsed: true,
        });

  
    
    //-----------------ЛЕГЕНДА-------------------//
    //-----------------ЛЕГЕНДА-------------------//
    //-----------------ЛЕГЕНДА-------------------//
    //-----------------ЛЕГЕНДА-------------------//
        L.control.Legend({
            position: "bottomright",
            title: "Легенда",
            legends: [
            {
                label: "Монумент",
                type: "image",
                url: "static/images/icon/MonumentIcon.svg",
            },
            {
                label: "Топоним",
                type: "image",
                url: "static/images/icon/ToponymIcon.svg",
            },
            {
                label: "Крепость",
                type: "image",
                url: "static/images/icon/FortIcon.svg",
            }
            ,
            {
                label: "Полк",
                type: "image",
                url: "static/images/icon/RegimentIcon.svg",
            }
            ,
            {
                label: "Населенный пункт",
                type: "image",
                url: "static/images/icon/CityIcon.svg",
            }
            ,
            {
                label: "Уезд",
                type: "image",
                url: "static/images/icon/UezdIcon.svg",
            }
            ]
        }).addTo(map);
    //-----------------ПРИВЯЗКА_К_СЛОЮ-------------------//
    //-----------------ПРИВЯЗКА_К_СЛОЮ-------------------//
    //-----------------ПРИВЯЗКА_К_СЛОЮ-------------------//
    //-----------------ПРИВЯЗКА_К_СЛОЮ-------------------//
    map.on('baselayerchange',function(e){
        console.log(e.name);
        if(e.name==='1')
        {
            if(map.hasLayer(imageOverlay)){
                imageOverlay.removeFrom(map);
            }
            if(map.hasLayer(imageOverlay1)){
                imageOverlay1.removeFrom(map);
            }
            if(!map.hasLayer(admRB)){
                admRB.addTo(map);
            }
            if(!map.hasLayer(or)){
                or.addTo(map);
            }
            if(!map.hasLayer(chel)){
                chel.addTo(map);
            }
            if(!map.hasLayer(citiesjson)){
                citiesjson.addTo(map);
            }
            if(!map.hasLayer(gidronimyjson)){
                gidronimyjson.addTo(map);
            }
            if(!map.hasLayer(toponimyjson)){
                toponimyjson.addTo(map);
            }

            if(!map.hasLayer(PamyatnikiInfo)){
                PamyatnikiInfo.addTo(map);
            }
            if(!map.hasLayer(ToponimyInfo)){
                ToponimyInfo.addTo(map);
            }
            if(map.hasLayer(RegimentInfo)){
                RegimentInfo.removeFrom(map);
            }
            if(map.hasLayer(routest)){
                routest.removeFrom(map);
            }
            if(map.hasLayer(FortInfo)){
                FortInfo.removeFrom(map);
            }
            if(map.hasLayer(citiesInfo)){
                citiesInfo.removeFrom(map);
            }
            if(map.hasLayer(UezdInfo)){
                UezdInfo.removeFrom(map);
            }
            map.removeControl(lay);
            map.zoomIn(0.1);
            lay1.addTo(map).collapseTree(true).expandSelected();
        }
        else if(e.name==='0') {
            if(map.hasLayer(citiesjson)){
                citiesjson.removeFrom(map);
            }
            if(!map.hasLayer(imageOverlay)){
                imageOverlay.addTo(map);
            }
            if(!map.hasLayer(imageOverlay1)){
                imageOverlay1.addTo(map);
            }
            if(map.hasLayer(admRB)){
                admRB.removeFrom(map);
            }
            if(map.hasLayer(chel)){
                chel.removeFrom(map);
            }
            if(map.hasLayer(or)){
                or.removeFrom(map);
            }

            if(map.hasLayer(gidronimyjson)){
                gidronimyjson.removeFrom(map);
            }
            if(map.hasLayer(toponimyjson)){
                toponimyjson.removeFrom(map);
            }

            if(map.hasLayer(PamyatnikiInfo)){
                PamyatnikiInfo.removeFrom(map);
            }
            if(map.hasLayer(ToponimyInfo)){
                ToponimyInfo.removeFrom(map);
            }
            
            if(!map.hasLayer(RegimentInfo)){
                RegimentInfo.addTo(map);
            }
            if(!map.hasLayer(FortInfo)){
                FortInfo.addTo(map);
            }
            if(!map.hasLayer(routest)){
                routest.addTo(map);
            }
            if(!map.hasLayer(citiesInfo)){
                citiesInfo.addTo(map);
            }
            if(!map.hasLayer(UezdInfo)){
                UezdInfo.addTo(map);
            }
            
            lay.addTo(map).collapseTree(true).expandSelected();
            map.removeControl(lay1);
            chic();
            
        }
    });
    //-----------------ПОИСК-------------------//
    //-----------------ПОИСК-------------------//
    //-----------------ПОИСК-------------------//
    //-----------------ПОИСК-------------------//
    var controlSearch = new L.Control.Search({	
		layer: featurelayer,
		initial: false, // не обязательно вводить слово в слово при false
		propertyName: 'index',
		zoom: 13,
		marker: false,
		buildTip: function(text, val) {
			var type = val.layer.feature.properties.amenity; // будет указываться что за тип ищется
            var engltype = val.layer.feature.properties.amenity1; // будет настройка стиля для искомого типа
			return '<a href="#" class="'+engltype+'">'+text+'<b>'+type+'</b></a>';
		}
	});
	// открываем балун, если нашли
	controlSearch.on('search:locationfound', function(e) {  
        //-----------------ПЕРЕКЛЮЧЕНИЕ СЛОЯ-------------------//
        if ((e.layer.feature.properties.amenity == "Топоним") || (e.layer.feature.properties.amenity == "Монумент"))
        {
            var layerControlElement = document.getElementsByClassName('leaflet-control-layers')[0];
            layerControlElement.getElementsByTagName('input')[1].click();
        }
        else 
        {
            var layerControlElement = document.getElementsByClassName('leaflet-control-layers')[0];
            layerControlElement.getElementsByTagName('input')[0].click();
        }
        //-----------------ОТКРЫТИЕ БАЛУНА ПРИ НАХОЖДЕНИИ-------------------//
		e.layer.openPopup();
	})
	map.addControl( controlSearch );
    
  });
