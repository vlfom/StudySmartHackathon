course_names = ["Introduction to Informatics 1", "Fundamentals of Programming (Exercises & Laboratory)", "Introduction to Informatics 2", "Introduction to Computer Organization and Technology - Computer Architecture", "Laboratory: Computer Organization and Computer Architecture", "Introduction to Software Engineering", "Fundamentals of Algorithms and Data Structures", "Fundamentals of Databases", "Basic Principles: Operating Systems and System Software", "Introduction to Computer Networking and Distributed Systems", "Computer Systems Performance Analysis", "Cloud Computing", "Microprocessors", "Advanced Computer Architecture", "Foundations of program and system development", "IT-Consulting", "Algorithms and Data Structures", "User Modeling and Recommender Systems", "Networks for Monetary Transactions", "International Experience & Communication Skills", "Start-up financing", "Business Plan - Basic Course (Business Idea and Market)", "Patents and Trade Secrets", "Topics in Marketing, Strategy & Leadership (MSL) - (F&WM) I", "Introduction to Business Law", "Statistics for BWL", "Energy & Climate Policy", "High Performance Leadership", "Basic Principles and international Aspects of Corporate Management", "Project Management", "Law of Business Association 1", "Topics in General Management", "Investment and Financial Management", "Production and Logistics",]
course_ids = ["IN0001", "IN0002", "IN0003", "IN0004", "IN0005", "IN0006", "IN0007", "IN0008", "IN0009", "IN0010", "IN2072", "IN2073", "IN2075", "IN2076", "IN2078", "IN2079", "IN8009", "IN2119", "IN2161", "WI900004", "WI001163", "WI000159", "WI000810", "WIB21933", "WI001119", "MA9712", "WI001183", "WI000996", "WI001028", "WI000264", "WI100130", "WI001159", "WI000219", "WI001060",]

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
