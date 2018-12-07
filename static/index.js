console.log('yey');
var vm = new Vue({
    el: "#main-app",
    data: {
        outlist: [],
        do_vote: false,
        avail_courses: ['hui', 'govno']
    },
    methods: {
        get_recs: function () {
            this.do_vote = false;
            var self = this;
            $.getJSON(
                '/users/0/recommendations'
            ).then(function (response) {
                self.outlist = response;
            });
        },
        get_votes: function () {
            this.do_vote = false;
            var self = this;
            $.getJSON(
                '/users/0/votes'
            ).then(function (response) {
                self.outlist = response;
            });
        },
        display_vote: function () {
            this.do_vote = true;
        }
    }
});

// vm.get_recs();
