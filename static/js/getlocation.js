$.ajax({
    url: "https://ipinfo.io/json",
    success: function(res){
        $("form").prepend(`<input type='hidden' name='city' value='${res.city.toLowerCase()}' />`);
    }
});
