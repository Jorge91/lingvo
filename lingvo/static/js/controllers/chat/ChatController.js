(function () {
    angular.module('lingvo').controller('ChatCtrl', function ($scope, $http, $routeParams, $rootScope, $location) {

        var socket = new WebSocket('ws://' + window.location.host + "/chat/" + $routeParams.id + "/");
        $scope.messages = [];

        socket.onmessage = function (message) {
            console.log(message.data);
            var args = message.data.split(":");
            var style = args[0] == $routeParams.id;
            var item = {"text": args[1], "style": style};
            $scope.messages.push(item);
            $scope.$apply();
        };

        $scope.sendMessage = function () {
            console.log('sending...');
            socket.send(JSON.stringify({message: $scope.message}));
            $scope.message = "";
        };

    });


})
();