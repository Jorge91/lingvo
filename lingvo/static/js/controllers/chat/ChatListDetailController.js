(function () {
    angular.module('lingvo').controller('ChatListDetailCtrl', function ($scope, $http, $routeParams, $rootScope, $location) {

        var id = $rootScope.user_id;
        if ($scope.chat.user_from.id == id) {
            $scope.userChat = $scope.chat.user_to;
        } else {
            $scope.userChat = $scope.chat.user_from;
        }
        

    });

})
();