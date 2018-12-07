console.log('yey');
var vm = new Vue({
    el: "#userrecommend",
    data: {
        recommendations: []
    },
    methods: {
        get_recs: function () {
            // this.recommendations = [{name: 'hui', prob: 'pizda'}];
            $.ajax({
                url: 'http://localhost:5000/users/0/recommendations',
                dataType: 'jsonp',
                contentType: 'application/json',
                success: function (response) {
                    this.recommendations =  response.data;
                }

            });
        }
    }
});

vm.get_recs();
