(function () {
    angular.module('lingvo').controller('ChatCtrl', function ($scope, $http, $routeParams, $rootScope, $location) {

        var chats_url = 'api/1.0/chats/';
        $scope.messages = [];


            $http.get(chats_url + $routeParams.id).success(function (data) {
                var messages = data.messages;
                for (var i = messages.length - 1; i < messages.length; i--) {
                    var style = true;
                    if (messages[i].user != null) {
                        style = messages[i].user.id == $routeParams.id
                    }
                    $scope.messages.push({"text": messages[i].message, "style": style})
                }


            }).error(function (data) {

            });



        var socket = new WebSocket('ws://' + window.location.host + "/chat/" + $routeParams.id + "/");


        socket.onmessage = function (message) {
            var args = message.data.split(":");
            var style = args[0] == $routeParams.id;
            var item = {"text": args[1], "style": style};
            $scope.messages.push(item);
            var element = document.getElementById("chatListId");
            $(element).scrollTop(parseInt($(element)[0].scrollHeight) + 200);
            $scope.$apply();
        };

        $scope.sendMessage = function () {
            if ($scope.message) {
                socket.send(JSON.stringify({message: $scope.message}));
                $scope.message = "";
            }
        };

    });


})
();