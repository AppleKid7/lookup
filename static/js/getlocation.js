$.ajax({
    url: "http://ipinfo.io/json",
    success: function(res){
        $("form").prepend(`input type='hidden' value='${res.city.toLowerCase()}' />`);
    }
});
