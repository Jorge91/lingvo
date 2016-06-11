(function () {

    angular.module('lingvo').controller('RelatedPeopleCtrl', ['$scope', '$http', '$location', function ($scope, $http, $location) {

        var related_url = 'api/1.0/related/';
        $scope.loading = true;

        $http.get(related_url).success(function (data) {
            $scope.related = data;
            $scope.loading = false;
        }).error(function (data) {

        });

        $scope.goToProfile = function (id) {
            $location.path("/profile/" + id);
        }


    }]);

})
();