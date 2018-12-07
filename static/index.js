console.log('yey');
var vm = new Vue({
    el: "#userrecommend",
    data: {
        outlist: []
    },
    methods: {
        get_recs: function () {
            var self = this;
            $.getJSON(
                '/users/0/recommendations'
            ).then(function (response) {
                self.outlist = response;
            });
        },
        get_votes: function () {
            var self = this;
            $.getJSON(
                '/users/0/votes'
            ).then(function (response) {
                self.outlist = response;
            });
        }
    }
});

// vm.get_recs();
