(function () {

    angular.module('login').controller('LoginCtrl', ['$scope', '$http', function ($scope, $http) {

        $scope.mode = 'Login';
        $scope.errors = '';
        var url_login = '/rest-auth/login/';
        var url_registration = '/rest-auth/registration/';


        $scope.changeMode = function () {
            if ($scope.mode == 'Login') {
                $scope.mode = 'Register';
            } else {
                $scope.mode = 'Login';
            }
        };

        $scope.makeRequest = function () {
            if ($scope.mode == 'Login') {
                login();
            } else {
                register();
            }
        };

        function login() {
            var data = {
                "username": $scope.username,
                "email": $scope.email,
                "password": $scope.password
            };
            $http.post(url_login, data).success(function (data, status, headers, config) {
                window.location = "/";
            }).error(function (data, status, headers, config) {
                $scope.errors = 'Incorrect data';
            });
        }

        function register() {
            var data = {
                "username": $scope.username,
                "email": $scope.email,
                "password1": $scope.password,
                "password2": $scope.password2
            };
            $http.post(url_registration, data).success(function (data, status, headers, config) {
                $scope.username = '';
                $scope.email = '';
                $scope.password = '';
                $scope.password2 = '';
                $scope.mode = 'Login';
            }).error(function (data, status, headers, config) {

            });
        }

    }]);

})
();