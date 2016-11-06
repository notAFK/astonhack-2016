<?php

require 'vendor/autoload.php';
use Crate\PDO\PDO;

function printMap()
{
    echo '<script>function initMap() {
        var england = {lat: 52.5, lng: -1.8};
        var map = new google.maps.Map(document.getElementById("map"), {
          zoom: 4,
          center: england
        });';
    printMarkers();
    echo 'var marker = new google.maps.Marker({
          position: england,
          map: map
        });
      }</script>';
}

function printMarkers() 
{
    $dsn = 'crate:10.0.2.15:4200';
    $connection = new PDO($dsn, null, null, null);
    $results = $connection->query('SELECT LOCATION_X, LOCATION_Y FROM geese');
    $id = 0;
    while ($row = $results->fetch())
    {
	echo 'var position' . $id . ' = { lat: ' . $row[1] . ', lng: ' . $row[0] . '};';
        echo 'var marker' . $id . ' = new google.maps.Marker({';
	echo 'position: position'. $id;
        echo ', map: map }); ';
        $id++;
    }
    
} 
?>
<!DOCTYPE html>
<html>
  <head>
    <style>
       #map {
        height: 400px;
        width: 100%;
       }
    </style>
  </head>
  <body>
    <h3>Fragile swarming geese</h3>
    <div id="map"></div>
    <?php printMap() ?>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCyT8A7_o7yXpZB7AI6uc4QwYR0bco2wTc&callback=initMap">
    </script>
  </body>

</html>
