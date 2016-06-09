(function () {

    angular.module('lingvo').controller('ProfileDetailCtrl', ['$scope', '$http', '$routeParams', function ($scope, $http, $routeParams) {

        var profile_url = 'api/1.0/profiles/';
        $scope.id = $routeParams.id;


        $http.get(profile_url + $scope.id).success(function (data) {
            $scope.profile = data;
        }).error(function (data) {

        });

        $scope.calculateAge = function (birthday) {
            var ageDifMs = Date.now() - new Date(birthday);
            var ageDate = new Date(ageDifMs);
            return Math.abs(ageDate.getUTCFullYear() - 1970);
        }


    }]);

})
();