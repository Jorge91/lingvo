(function () {
    angular.module('lingvo').controller('MeetingListCtrl', function (NgMap, $scope, $http, $location) {

        var meeting_url = 'api/1.0/meetings/';
        $scope.meetings = null;

        $http.get(meeting_url).success(function (data) {
            $scope.meetings = data.features;
        }).error(function (data) {

        });
        
        $scope.goToMeetingDetail = function (id) {
            $location.path("/meetings/" + id);
        };

        
    });


})
();