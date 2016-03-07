var VirtualEntityModule = (function(){

    var loadEntities = function() {

        return $.ajax({
            type: 'GET',
            url: '/api/entity',
            success: function (data) {
                data.Data.forEach(function(entity){
                    console.log(entity.name)
                    $('#entities-table tbody').append(
                        "<tr><td>"+entity.id+"</td><td>"+entity.name+"</td><td>"+entity.description+"</td><td>"+entity.properties.length+"</td></tr>"

                        );

                });

            },
            error: function (jqXHR, textStatus, errorThrown) {
                Utils.alertShow('Error loading resources.');
            },
            complete: function (jqXHR, textStatus) {
            }
        });
    };

    return {

        /**
         * Initializes module.
         */
        initialize: function() {
            //$('[rel="spinner"]').spin();

            loadEntities();
        }
    };

})();


require(['jquery', 'bootstrap','utils'], VirtualEntityModule.initialize);