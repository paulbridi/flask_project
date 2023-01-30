
$("#map-form").on("submit", function(event) {
  event.preventDefault();
  let location = $("#map-input").val();

  $.ajax({
      type: "POST",
      // body: ADD IN BODY
      url: "/update_map",
      data: JSON.stringify({ location: location }),
      contentType: "application/json; charset=utf-8",
      dataType: "json",

      success: function(response) {
        console.log(response)
          // update the map with the new data
          let map = new google.maps.Map(document.getElementById("map"), {
              zoom: 15,
              center: { lat: 0.000, lng: 0.0 },
          });

          let marker = new google.maps.Marker({
              position: { lat: 0.000, lng: 0.0 },
              map: map
          });
      }
  });
});
