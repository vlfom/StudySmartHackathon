console.log('yey');
var rec_vm = new Vue({
    el: "#rec-app",
    data: {
        cscores: [],
    },

    methods: {
        get_recs: function () {
            var self = this;
            $.getJSON({
                url:'/users/0/recommendations',
            }).then(function (response) {
                self.cscores = response;
            });
        },
    }
});

 rec_vm.get_recs();
