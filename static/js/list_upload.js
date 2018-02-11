window.onload = function(){
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:2016/graphs/',
        dataType: 'json',

        success: function(get_data){
            var items = []
            arr = get_data.graphs
            arr.forEach(function(item, i, arr){
                    function send_graph(uuid){
                        console.log(uuid)
                    };
                    items.push('<option value="' + item.uuid + '">' +  + item.name + '  ' + item.timestamp + '</option>');
            });
            console.log(items)
            $('<select/>', {
                name: 'graphs',
                html: items.join('')
                }).appendTo('#graphs_list');
            var button = $('<input type="submit" name="submit"/>')
            button.click(function(){
                $.ajax({
                    type: "POST",
                    url: 'http://127.0.0.1:2016/selected_graph/',
                    dataType: 'json',
                    data:{"data": $('select').val()}
                })

            })
            button.appendTo('#graphs_list');
        }
    })
}

