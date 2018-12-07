var hist_vm = new Vue({
    el: "#hist-app",
    data: {
        votes: {},
    },

    methods: {
        get_votes: function () {
            var self = this;
            $.getJSON({
                url:'/users/0/votes',
            }).then(function (response) {
                self.votes = response;
            });
        },
    }
});

 hist_vm.get_votes();
