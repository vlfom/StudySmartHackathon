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
            this.do_vote = false;
            var self = this;
            $.getJSON({
                url:'/users/0/recommendations',
                data: this.votes
            }).then(function (response) {
                self.outlist = response;
            });
        },

        add_vote: function () {
            if (!this.crt_course || !this.crt_grade) return;
            console.log('here');
            this.votes[this.crt_course] = this.crt_grade;
            this.avail_courses = this.avail_courses.filter(
                function (el) { return el !== this.crt_course; }
            );
            this.crt_course = '';
            this.crt_grade = '';
        }
    }
});

// vm.get_recs();
