(function () {


    angular.module('lingvo')
        .controller('MainCtrl', function ($scope, $timeout, $mdSidenav, $rootScope, $http, $cookies, $mdToast) {

            var me_url = 'api/1.0/users/me/';
            var chats_url = 'api/1.0/chats/';
            var numberOfChats = null;

            $scope.toggleLeft = buildDelayedToggler('left');
            $rootScope.markers = [];


            $scope.logout = function () {
                $http.post("/rest-auth/logout/").success(function (data) {
                    delete $http.defaults.headers.common.Authorization;
                    delete $cookies.token;
                    $cookies.remove("csrftoken");
                    window.location = "/";
                }).error(function (data) {

                });


            };

            /**
             * Supplies a function that will continue to operate until the
             * time is up.
             */
            function debounce(func, wait, context) {
                var timer;

                return function debounced() {
                    var context = $scope,
                        args = Array.prototype.slice.call(arguments);
                    $timeout.cancel(timer);
                    timer = $timeout(function () {
                        timer = undefined;
                        func.apply(context, args);
                    }, wait || 10);
                };
            }

            /**
             * Build handler to open/close a SideNav; when animation finishes
             * report completion in console
             */
            function buildDelayedToggler(navID) {
                return debounce(function () {
                    // Component lookup should always be available since we are not using `ng-if`
                    $mdSidenav(navID)
                        .toggle()
                        .then(function () {

                        });
                }, 200);
            }

            function buildToggler(navID) {
                return function () {
                    $mdSidenav(navID)
                        .toggle()
                        .then(function () {

                        });
                }
            }

            $rootScope.$on('$routeChangeStart', function (event, next) {
                for (var i = 0; i < $rootScope.markers.length; i++) {
                    $rootScope.markers[i].setMap(null);
                }
                $rootScope.markers = [];
            });


            $http.get(me_url).success(function (data) {
                $rootScope.user_id = data.user.id;
            }).error(function (data) {

            });


            // Chat updates
            setInterval(function () {
                chatUpdate();
            }, 60000);


            function chatUpdate() {
                $http.get(chats_url).success(function (data) {
                    var number = data.length;
                    if (numberOfChats == null) {
                        numberOfChats = number;
                    } else if (number > numberOfChats) {
                        var diff = number - numberOfChats;
                        numberOfChats = number;
                        showToast(diff);
                    }
                }).error(function (data) {
                });
            }

            var last = {
                bottom: false,
                top: true,
                left: false,
                right: true
            };

            function showToast(number) {
                var pinTo = $scope.getToastPosition();
                $mdToast.show(
                    $mdToast.simple()
                        .textContent('You have (' + number + ') new chats!')
                        .position(pinTo)
                        .hideDelay(3000)
                );
            }

            $scope.toastPosition = angular.extend({}, last);
            $scope.getToastPosition = function () {
                sanitizePosition();
                return Object.keys($scope.toastPosition)
                    .filter(function (pos) {
                        return $scope.toastPosition[pos];
                    })
                    .join(' ');
            };
            function sanitizePosition() {
                var current = $scope.toastPosition;
                if (current.bottom && last.top) current.top = false;
                if (current.top && last.bottom) current.bottom = false;
                if (current.right && last.left) current.left = false;
                if (current.left && last.right) current.right = false;
                last = angular.extend({}, current);
            }


            //end chat updates


        })
        .controller('ToastCtrl', function ($scope, $mdToast) {
            $scope.closeToast = function () {
                $mdToast.hide();
            };
        })
        .controller('LeftCtrl', function ($scope, $timeout, $mdSidenav) {
            $scope.close = function () {
                // Component lookup should always be available since we are not using `ng-if`
                $mdSidenav('left').close()
                    .then(function () {

                    });

            };
        });

})
();
/**
 Copyright 2016 Google Inc. All Rights Reserved.
 Use of this source code is governed by an MIT-style license that can be in foundin the LICENSE file at http://material.angularjs.org/license.
 **/