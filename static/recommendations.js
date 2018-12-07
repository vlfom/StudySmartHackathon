console.log('yey');
var vm = new Vue({
    el: "#main-app",
    data: {
        votes: {},
        recommendations: [],
        avail_courses: ['BWLI', 'BWLII', 'VWLI'],
        crt_course : '',
        crt_grade : '',
        outlist: [],
    },

    methods: {
        get_recs: function () {
            var self = this;
            $.getJSON({
                url:'/users/0/recommendations',
            }).then(function (response) {
                self.outlist = response;
            });
        },

        get_votes: function () {
            var self = this;
            $.getJSON({
                url:'/users/0/votes',
            }).then(function (response) {
                self.votes = response;
            });
        },

        add_vote: function () {
            if (!this.crt_course || !this.crt_grade) return;
            this.votes[this.crt_course] = this.crt_grade;
            // this.avail_courses = this.avail_courses.filter(
                // function (el) { return el !== this.crt_course; }
            // );
            var jdata = {};
            jdata[this.crt_course] = this.crt_grade;
            console.log(jdata);
            $.post({
                url: '/users/0/vote',
                data: jdata,
                dataType: 'json'
            });
            this.crt_course = '';
            this.crt_grade = '';
        }
    }
});

 vm.get_votes();
