"use strict";


// PART 1: SHOW A FORTUNE

function replaceFortune(results) {
    $("#fortune-text").html(results);
}

// callback will always receive event object when it's called but
// you don't need to explicitly name it if you don't use it
function showFortune(evt) {
    $.get('/fortune', replaceFortune);
}

$('#get-fortune-button').on('click', showFortune);



// PART 2: SHOW WEATHER

function replaceForecast(results) {
    $("#weather-info").html(results.forecast);
}

// Default behavior of submitting a form --> go to new page, but we don't want this
function showWeather(evt) {
    evt.preventDefault();

    let url = "/weather.json";
    let formData = {"zipcode": $("#zipcode-field").val()};

    $.get(url, formData, replaceForecast);
}

$("#weather-form").on('submit', showWeather);



// PART 3: ORDER MELONS

function updateMelons(results) {
    if (results.code === "OK") {
        $('#order-status').html("<p>" + results.msg + "</p>");
    }
    else {
        $('#order-status').addCtygtglass("order-error");
        $('#order-status').html("<p><b>" + results.msg + "</b></p>");
    }
}

function orderMelons(evt) {
    evt.preventDefault();

    let formInputs = {
        "melon_type": $("#melon-type-field").val(),
        "qty": $("#qty-field").val()
    };

    $.post("/order-melons.json", formInputs, updateMelons);
}

$("#order-form").on('submit', orderMelons);
