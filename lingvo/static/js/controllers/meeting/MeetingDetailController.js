(function () {
    angular.module('lingvo').controller('MeetingDetailCtrl', function (NgMap, $scope, $http, $routeParams, $rootScope, $location) {

        var meeting_url = 'api/1.0/meetings/';
        var attendance_url = 'api/1.0/attendances/';
        var vm2 = this;
        $scope.id = $routeParams.id;

        $http.get(meeting_url + $scope.id).success(function (data) {
            $scope.meeting = data;
        }).error(function (data) {

        });

        $scope.getIn = function () {
            var data = {
                meeting: $scope.id,
                user: $rootScope.user_id
            };
            $http.post(attendance_url, data).success(function (data) {
                $location.path("/meetings/");
            }).error(function (data) {
                $location.path("/meetings/");
            });

        };

        NgMap.getMap().then(function (map) {
            vm2.map = map;
        });

    });


})
();