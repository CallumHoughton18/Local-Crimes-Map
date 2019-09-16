var openStreetViewModule = (function(){
    
    function OpenStreetView(location){
        if (confirm("Open crime location in Google StreetView?")){
            let streetViewURL = "https://www.google.com/maps/@?api=1&map_action=pano&viewpoint="+location;
            window.open(streetViewURL);
        }
    }

    return {
        OpenStreetView: OpenStreetView,
      };
  }());