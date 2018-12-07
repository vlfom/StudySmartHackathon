console.log('yey');
var vm = new Vue({
    el: "#userrecommend",
    data: {
        recommendations: []
    },
});

$.getJSON('/users/0/recommendations').then(function (response) {
    vm.recommendations = response;
});
