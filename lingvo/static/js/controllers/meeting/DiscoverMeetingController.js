(function () {
    angular.module('lingvo').controller('DiscoverMeetingCtrl', function (NgMap, $scope, $http, $rootScope, $location) {

        var meeting_url = 'api/1.0/meetings/';
        var vm3 = this;
        var changedRadiusFlag = false;



        $scope.locationEnabled = false;
        $scope.radius = 4000;

        $scope.activeLocation = function () {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (position) {
                    $scope.$apply(function () {
                        $scope.position = [position.coords.latitude, position.coords.longitude];
                        $scope.locationEnabled = true;
                        requestNearMeetings($scope.radius);
                    });
                });
            }
        };


        NgMap.getMap().then(function (map) {
            vm3.map = map;
        });


        function placeMarker(lat, lon) {
            var latLng = new google.maps.LatLng(lat, lon);
            marker = new google.maps.Marker({position: latLng, map: vm3.map});
            $rootScope.markers.push(marker);
        }

        $scope.$watch("radius", function (newValue, oldValue) {
            if (changedRadiusFlag == false) {
                changedRadiusFlag = true;
            } else {
                requestNearMeetings(newValue);
            }
        });


        function requestNearMeetings(radius) {
            var url = meeting_url + "?distance=" + radius + "&lat=" + $scope.position[0] + "&lon=" + $scope.position[1];
            $http.get(url).success(function (data) {
                for (var i = 0; i < $rootScope.markers.length; i++) {
                    $rootScope.markers[i].setMap(null);
                }
                $rootScope.markers = [];
                $scope.meetings = data.features;
                for (var j = 0; j<$scope.meetings.length; j++) {
                    placeMarker($scope.meetings[j].geometry.coordinates[0], $scope.meetings[j].geometry.coordinates[1]);
                }
            }).error(function (data) {

            });
        }

        $scope.goToMeetingDetail = function (id) {
            $location.path("/meetings/" + id);
        };

    });


})
();