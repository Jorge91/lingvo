(function () {
    angular.module('lingvo').controller('ChatListCtrl', function ($scope, $http, $routeParams, $rootScope, $location) {

        var chats_url = 'api/1.0/chats/';

        $http.get(chats_url).success(function (data) {
            $scope.chats = data;
        }).error(function (data) {

        });

    });

})
();