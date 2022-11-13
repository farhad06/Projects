function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("sqft");
  var bhk = document.getElementById("bhk");
  var bathrooms = document.getElementById("bath");
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("showprice");
  //console.log(sqft.value," ",bhk.value," ",bathrooms.value," ",location.value)

  var url = "http://localhost:5000/predict_home_price";
  //var url = "/api/predict_home_price"; onwards

  $.post(
    url,
    {
      total_sqft: parseFloat(sqft.value),
      bhk: parseInt(bhk.value),
      bath: parseInt(bathrooms.value),
      location: location.value,
    },
    function (data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML =
        "<h4 style='color: #76448A;'>" +
        "Estimated Price is: " +
        data.estimated_price.toString() +
        " Lakh</h4>";
      console.log(status);
    }
  );
}

function onPageLoad() {
  console.log("document loaded");

  var url = "http://localhost:5000/get_location_names";
  //var url = "/api/get_location_names";
  $.get(url, function (data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $("#uiLocations").empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $("#uiLocations").append(opt);
      }
    }
  });
}

window.onload = onPageLoad();
