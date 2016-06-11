(function () {


    angular.module('lingvo').controller('NewMeetingCtrl', function (NgMap, $scope, $http, $location, $rootScope) {

        $scope.zoom = 5;
        $scope.lat = null;
        $scope.lng = null;

        var vm = this;
        var marker = null;
        var meeting_url = 'api/1.0/meetings/';
        

        $scope.createMeeting = function () {
            var position = "POINT(" + $scope.lat + " " + $scope.lng +")";
            var data = {
                title: $scope.name,
                position: position,
                time: $scope.dateValue
            };
            $http.post(meeting_url, data).success(function (data) {
                marker.setMap(null);
                $location.path("/meetings/" + data.id);
            }).error(function (data) {
                if (data.time) {
                    $scope.error = data.time[0];
                }
            });
        };


        NgMap.getMap().then(function (map) {
            vm.map = map;
        });
        $scope.placeMarker = function (e) {
            if (marker != null) {
                marker.setMap(null);
            }

            marker = new google.maps.Marker({position: e.latLng, map: vm.map});

            $scope.lat = marker.getPosition().lat();
            $scope.lng = marker.getPosition().lng();
            $rootScope.markers.push(marker);
            vm.map.panTo(e.latLng);
        }
    });


})
();